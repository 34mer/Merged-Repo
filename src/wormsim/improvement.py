from __future__ import annotations

import json
import shutil
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np

from .abstraction import PCARidgeModel, train_pca_ridge
from .checkpoint import file_hash
from .config import WormConfig
from .controls import train_over_stable_control, train_random_latent_control
from .curve import _score_model_run
from .repair import run_repair_test


@dataclass(frozen=True)
class ImprovedSubstrateConfig:
    method: str = "robust-regularized"
    equivalence_threshold: float = 0.90
    transition_shrink: float = 0.92
    motor_smoothing: float = 0.08
    alpha: float = 1e-3

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _write_json(path: Path, payload: dict[str, Any] | list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def train_improved_substrate(
    base_abstraction: str | Path | None,
    dataset: str | Path,
    out: str | Path,
    latent_dim: int = 8,
    config: ImprovedSubstrateConfig | None = None,
) -> dict[str, Any]:
    """Create a regularized PCA-Ridge substrate compatible with the live runtime.

    Minimal Round 3 v1: train or load a PCA-Ridge model, then apply conservative
    substrate-level regularization: transition shrinkage and motor smoothing.
    This preserves the process interface while improving stability/migratability
    properties such as smaller effective dynamics and smoother actions.
    """

    cfg = config or ImprovedSubstrateConfig()
    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)

    if base_abstraction is None:
        temp_base = out_path / "_base_fit"
        train_pca_ridge(dataset, temp_base, latent_dim=latent_dim, alpha=cfg.alpha)
        source_model_path = temp_base / "model.npz"
    else:
        source_model_path = Path(base_abstraction) / "model.npz" if Path(base_abstraction).is_dir() else Path(base_abstraction)

    with np.load(source_model_path, allow_pickle=False) as data:
        mean = data["mean"].astype(np.float64)
        components = data["components"].astype(np.float64)
        singular_values = data["singular_values"].astype(np.float64)
        transition_weights = data["transition_weights"].astype(np.float64)
        motor_weights = data["motor_weights"].astype(np.float64)
        latent_dim = int(data["latent_dim"][0])

    improved_transition = transition_weights.copy()
    improved_transition[:-1, :] *= cfg.transition_shrink
    improved_transition[:latent_dim, :] *= cfg.transition_shrink

    improved_motor = motor_weights.copy()
    improved_motor[:-1, :] *= 1.0 - cfg.motor_smoothing
    improved_motor[-1, :] = (1.0 - cfg.motor_smoothing) * improved_motor[-1, :]
    # Reduce contradictory left/right motor fights without changing format.
    if improved_motor.shape[1] >= 2:
        shared = 0.5 * (improved_motor[:, 0] + improved_motor[:, 1])
        improved_motor[:, 0] = (1.0 - cfg.motor_smoothing) * improved_motor[:, 0] + cfg.motor_smoothing * shared
        improved_motor[:, 1] = (1.0 - cfg.motor_smoothing) * improved_motor[:, 1] + cfg.motor_smoothing * shared

    model_path = out_path / "model.npz"
    np.savez_compressed(
        model_path,
        mean=mean,
        components=components,
        singular_values=singular_values,
        transition_weights=improved_transition,
        motor_weights=improved_motor,
        latent_dim=np.array([latent_dim], dtype=np.int64),
        alpha=np.array([cfg.alpha], dtype=np.float64),
    )
    digest = file_hash(model_path)
    metadata = {
        "schema": "wormsim-improved-substrate-v1",
        "method": cfg.method,
        "latent_dim": latent_dim,
        "source_dim": int(mean.shape[0]),
        "compression_ratio": float(mean.shape[0] / latent_dim),
        "config": cfg.to_dict(),
        "base_abstraction": str(base_abstraction) if base_abstraction is not None else None,
        "model_file": str(model_path),
        "model_hash": digest,
    }
    _write_json(out_path / "metadata.json", metadata)
    (out_path / "model_hash.txt").write_text(digest + "\n", encoding="utf-8")
    return metadata


def compute_equivalence_score(row: dict[str, Any]) -> float:
    return float(np.clip(row.get("behavior_fidelity", 0.0), 0.0, 1.0))


def compute_improvement_score(source_row: dict[str, Any], row: dict[str, Any]) -> float:
    source_viability = float(source_row.get("source_mean_viability", row.get("source_mean_viability", 1.0)) or 1.0)
    abstract_viability = float(row.get("abstract_mean_viability", 0.0))
    viability_delta = abstract_viability - source_viability
    self_maintenance = float(row.get("self_maintenance_retained", 0.0))
    stability_bonus = 1.0 / (1.0 + abs(float(row.get("latent_trajectory_divergence", 0.0))))
    return float(np.clip(0.45 * self_maintenance + 0.35 * max(0.0, viability_delta + 1.0) + 0.20 * stability_bonus, 0.0, 2.0))


def compute_efficiency_score(model_path: str | Path, row: dict[str, Any]) -> float:
    model = PCARidgeModel(model_path)
    checkpoint_size_score = 1.0 / (1.0 + Path(model.model_path).stat().st_size / 1_000_000.0)
    compression_score = min(1.0, float(row.get("compression_ratio", 1.0)) / 40.0)
    divergence_score = 1.0 if float(row.get("latent_trajectory_divergence", 1.0)) == 0.0 else 0.0
    return float(np.clip(0.45 * compression_score + 0.35 * checkpoint_size_score + 0.20 * divergence_score, 0.0, 1.0))


def compute_substrate_total_score(
    equivalence_score: float,
    improvement_score: float,
    efficiency_score: float,
    repair_score: float,
    threshold: float,
) -> float:
    gate = 1.0 if equivalence_score >= threshold else 0.0
    return float(gate * (0.45 * improvement_score + 0.35 * efficiency_score + 0.20 * repair_score))


def benchmark_improved_substrate(
    source_dataset: str | Path,
    base_model: str | Path,
    improved_model: str | Path,
    out: str | Path,
    task_name: str = "hard_mixed",
    steps: int = 100,
    migration_steps: int = 25,
    seed: int = 42,
    equivalence_threshold: float = 0.90,
    include_controls: bool = True,
) -> dict[str, Any]:
    """Score base/improved/control substrates with explicit Round 3 score split."""

    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)

    base_row = _score_model_run(base_model, out_path / "base", task_name, steps, seed, migration_steps, "Base PCA-Ridge", "base-pca-ridge")
    improved_row = _score_model_run(improved_model, out_path / "improved", task_name, steps, seed, migration_steps, "Improved substrate", "robust-regularized")

    repair_report = run_repair_test(improved_model, out_path / "repair", task_name=task_name, steps_before=max(5, steps // 5), steps_after=max(10, steps // 2), seed=seed)
    repair_score = float(repair_report["mean_repair_score"])

    source_row = {"source_mean_viability": improved_row.get("source_mean_viability", 1.0)}
    base_scores = _score_bundle(base_model, source_row, base_row, 0.0, equivalence_threshold)
    improved_scores = _score_bundle(improved_model, source_row, improved_row, repair_score, equivalence_threshold)

    controls: list[dict[str, Any]] = []
    if include_controls:
        latent_dim = PCARidgeModel(improved_model).latent_dim
        random_dir = out_path / "controls" / "random"
        over_dir = out_path / "controls" / "over_stable"
        train_random_latent_control(source_dataset, random_dir, latent_dim=latent_dim, seed=seed)
        train_over_stable_control(source_dataset, over_dir, latent_dim=latent_dim, seed=seed)
        random_row = _score_model_run(random_dir, out_path / "controls" / "random_run", task_name, steps, seed, migration_steps, "Random latent", "random-latent-control")
        over_row = _score_model_run(over_dir, out_path / "controls" / "over_stable_run", task_name, steps, seed, migration_steps, "Over-stable", "over-stable-control")
        controls = [
            {"row": random_row, "scores": _score_bundle(random_dir, source_row, random_row, 0.0, equivalence_threshold)},
            {"row": over_row, "scores": _score_bundle(over_dir, source_row, over_row, 0.0, equivalence_threshold)},
        ]

    report = {
        "status": "PROCESS-PRESERVING SUBSTRATE OPTIMIZATION COMPLETE",
        "task": task_name,
        "steps": steps,
        "migration_steps": migration_steps,
        "equivalence_threshold": equivalence_threshold,
        "source": "302-neuron organism-like process",
        "base": {"row": base_row, "scores": base_scores},
        "improved": {"row": improved_row, "scores": improved_scores, "repair_report": repair_report},
        "controls": controls,
        "conclusion": "passes_equivalence_gate" if improved_scores["equivalence_passed"] else "fails_equivalence_gate",
    }
    _write_json(out_path / "process_preserving_substrate_optimization_report.json", report)
    return report


def _score_bundle(model_path: str | Path, source_row: dict[str, Any], row: dict[str, Any], repair_score: float, threshold: float) -> dict[str, Any]:
    eq = compute_equivalence_score(row)
    imp = compute_improvement_score(source_row, row)
    eff = compute_efficiency_score(model_path, row)
    total = compute_substrate_total_score(eq, imp, eff, repair_score, threshold)
    return {
        "equivalence_score": eq,
        "equivalence_threshold": threshold,
        "equivalence_passed": bool(eq >= threshold),
        "improvement_score": imp,
        "efficiency_score": eff,
        "repairability_score": repair_score,
        "total_score": total,
    }
