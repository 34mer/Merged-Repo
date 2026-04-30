from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

import numpy as np

from .abstraction import (
    PCARidgeModel,
    migrate_abstracted,
    run_abstracted,
    train_pca_ridge,
    verify_abstracted_migration,
)
from .checkpoint import file_hash
from .config import WormConfig
from .dataset import load_dataset, source_behavior_reference


def _write_json(path: Path, payload: dict[str, Any] | list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _random_orthonormal_components(source_dim: int, latent_dim: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    raw = rng.normal(0.0, 1.0, size=(source_dim, latent_dim))
    q, _ = np.linalg.qr(raw)
    return q[:, :latent_dim].T.astype(np.float64)


def train_random_latent_control(
    dataset: str | Path,
    out: str | Path,
    latent_dim: int,
    seed: int = 42,
) -> dict[str, Any]:
    """Create a deterministic random latent control with no learned closed-loop skill."""

    arrays = load_dataset(dataset)
    x = arrays["X_neural"]
    source_dim = int(x.shape[1])
    if latent_dim <= 0 or latent_dim > source_dim:
        raise ValueError(f"latent_dim must be in [1, {source_dim}]")

    mean = np.mean(x, axis=0)
    components = _random_orthonormal_components(source_dim, latent_dim, seed=seed + 101)
    transition_weights = np.zeros((latent_dim + 7 + 5 + 1, latent_dim), dtype=np.float64)
    motor_weights = np.zeros((latent_dim + 1, 4), dtype=np.float64)
    # Bias the body toward no drive. The normal abstracted runtime computes
    # drive from (1 + left + right), so -0.5/-0.5 should stall this control.
    motor_weights[-1, :] = np.array([-0.5, -0.5, 0.0, -1.0], dtype=np.float64)

    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)
    model_path = out_path / "model.npz"
    np.savez_compressed(
        model_path,
        mean=mean.astype(np.float64),
        components=components,
        singular_values=np.zeros(latent_dim, dtype=np.float64),
        transition_weights=transition_weights,
        motor_weights=motor_weights,
        latent_dim=np.array([latent_dim], dtype=np.int64),
        alpha=np.array([0.0], dtype=np.float64),
    )
    digest = file_hash(model_path)
    metadata = {
        "schema": "wormsim-control-abstraction-v1",
        "method": "random-latent-control",
        "latent_dim": latent_dim,
        "source_dim": source_dim,
        "compression_ratio": float(source_dim / latent_dim),
        "model_file": str(model_path),
        "model_hash": digest,
    }
    _write_json(out_path / "metadata.json", metadata)
    (out_path / "model_hash.txt").write_text(digest + "\n", encoding="utf-8")
    return metadata


def train_behavior_only_mean_control(
    dataset: str | Path,
    out: str | Path,
    latent_dim: int,
    seed: int = 42,
) -> dict[str, Any]:
    """Create a behavior-only mean-motor control with no internal dynamics."""

    arrays = load_dataset(dataset)
    x = arrays["X_neural"]
    motor = arrays["A_motor"]
    source_dim = int(x.shape[1])
    if latent_dim <= 0 or latent_dim > source_dim:
        raise ValueError(f"latent_dim must be in [1, {source_dim}]")

    mean = np.mean(x, axis=0)
    components = _random_orthonormal_components(source_dim, latent_dim, seed=seed + 202)
    transition_weights = np.zeros((latent_dim + 7 + 5 + 1, latent_dim), dtype=np.float64)
    motor_weights = np.zeros((latent_dim + 1, 4), dtype=np.float64)
    motor_weights[-1, :] = np.mean(motor, axis=0)

    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)
    model_path = out_path / "model.npz"
    np.savez_compressed(
        model_path,
        mean=mean.astype(np.float64),
        components=components,
        singular_values=np.zeros(latent_dim, dtype=np.float64),
        transition_weights=transition_weights,
        motor_weights=motor_weights,
        latent_dim=np.array([latent_dim], dtype=np.int64),
        alpha=np.array([0.0], dtype=np.float64),
    )
    digest = file_hash(model_path)
    metadata = {
        "schema": "wormsim-control-abstraction-v1",
        "method": "behavior-only-mean-control",
        "latent_dim": latent_dim,
        "source_dim": source_dim,
        "compression_ratio": float(source_dim / latent_dim),
        "model_file": str(model_path),
        "model_hash": digest,
    }
    _write_json(out_path / "metadata.json", metadata)
    (out_path / "model_hash.txt").write_text(digest + "\n", encoding="utf-8")
    return metadata


def _score_model_run(
    model_path: str | Path,
    out: str | Path,
    task_name: str,
    steps: int,
    seed: int,
    migration_steps: int,
    label: str,
    method: str,
) -> dict[str, Any]:
    out_path = Path(out)
    live_path = out_path / "live"
    migrated_path = out_path / "migrated"
    model = PCARidgeModel(model_path)
    live_report = run_abstracted(model_path, live_path, task_name=task_name, steps=steps, seed=seed)
    trajectory_file = live_path / "trajectory.npz"
    with np.load(trajectory_file, allow_pickle=False) as data:
        trajectory = data["trajectory"].astype(np.float64)
        abstract_viability_series = data["viability"].astype(np.float64)
    abstract_positions = trajectory[:, 1:3]
    source_ref = source_behavior_reference(WormConfig(seed=seed), task_name=task_name, steps=steps, seed=seed)
    source_positions = source_ref["positions"]

    path_len = min(len(source_positions), len(abstract_positions))
    path_error = float(np.mean(np.linalg.norm(source_positions[:path_len] - abstract_positions[:path_len], axis=1))) if path_len else 0.0
    path_fidelity = 1.0 - min(1.0, path_error / WormConfig().world_size)

    source_viability = float(source_ref["mean_viability"])
    abstract_viability = float(np.mean(abstract_viability_series)) if abstract_viability_series.size else 0.0
    viability_fidelity = 1.0 - min(1.0, abs(source_viability - abstract_viability) / max(source_viability, 1e-9))

    source_distance = float(source_ref["final_distance_to_food"])
    abstract_distance = float(live_report["final_distance_to_food"])
    distance_fidelity = 1.0 - min(1.0, abs(source_distance - abstract_distance) / WormConfig().world_size)
    behavior_fidelity = float(np.clip(0.50 * path_fidelity + 0.30 * distance_fidelity + 0.20 * viability_fidelity, 0.0, 1.0))
    self_maintenance = float(np.clip(abstract_viability / max(source_viability, 1e-9), 0.0, 2.0))

    checkpoint = live_path / f"checkpoint_t{steps}.npz"
    manifest = migrate_abstracted(checkpoint, migrated_path)
    verification = verify_abstracted_migration(
        model_path,
        checkpoint,
        migrated_path / checkpoint.name,
        steps=migration_steps,
    )
    migration_verified = verification.status == "ABSTRACTED MIGRATION VERIFIED"

    row = {
        "model": label,
        "method": method,
        "latent_dim": model.latent_dim,
        "compression_ratio": float(WormConfig().neurons / model.latent_dim),
        "behavior_fidelity": behavior_fidelity,
        "self_maintenance_retained": self_maintenance,
        "path_fidelity": float(path_fidelity),
        "distance_fidelity": float(distance_fidelity),
        "viability_fidelity": float(viability_fidelity),
        "source_mean_viability": source_viability,
        "abstract_mean_viability": abstract_viability,
        "source_final_distance_to_food": source_distance,
        "abstract_final_distance_to_food": abstract_distance,
        "migration_verified": migration_verified,
        "checkpoint_hash_matched": bool(manifest["hash_matched"]),
        "latent_trajectory_divergence": verification.latent_trajectory_divergence,
        "behavior_continuation": verification.behavior_continuation,
        "model_hash": model.model_hash,
    }
    _write_json(out_path / "score.json", row)
    return row


def generate_abstraction_curve(
    dataset: str | Path,
    out: str | Path,
    latent_dims: list[int],
    task_name: str = "mixed",
    steps: int = 1000,
    seed: int = 42,
    migration_steps: int = 250,
    include_controls: bool = True,
) -> dict[str, Any]:
    """Train several abstractions, run live benchmarks, verify migration, and write the curve."""

    if not latent_dims:
        raise ValueError("latent_dims must not be empty")
    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, Any]] = [
        {
            "model": "Full source",
            "method": "source-reference",
            "latent_dim": WormConfig().neurons,
            "compression_ratio": 1.0,
            "behavior_fidelity": 1.0,
            "self_maintenance_retained": 1.0,
            "path_fidelity": 1.0,
            "distance_fidelity": 1.0,
            "viability_fidelity": 1.0,
            "migration_verified": True,
            "checkpoint_hash_matched": True,
            "latent_trajectory_divergence": 0.0,
            "behavior_continuation": "baseline",
            "model_hash": "source-reference",
        }
    ]

    for latent_dim in latent_dims:
        model_dir = out_path / "models" / f"pca_{latent_dim}"
        train_pca_ridge(dataset, model_dir, latent_dim=latent_dim)
        rows.append(
            _score_model_run(
                model_dir,
                out_path / "runs" / f"pca_{latent_dim}",
                task_name=task_name,
                steps=steps,
                seed=seed,
                migration_steps=migration_steps,
                label=f"PCA-{latent_dim}",
                method="pca-ridge",
            )
        )

    if include_controls:
        control_dim = min(latent_dims)
        random_dir = out_path / "models" / f"random_{control_dim}"
        train_random_latent_control(dataset, random_dir, latent_dim=control_dim, seed=seed)
        rows.append(
            _score_model_run(
                random_dir,
                out_path / "runs" / f"random_{control_dim}",
                task_name=task_name,
                steps=steps,
                seed=seed,
                migration_steps=migration_steps,
                label=f"Random-{control_dim}",
                method="random-latent-control",
            )
        )

        behavior_dir = out_path / "models" / f"behavior_only_mean_{control_dim}"
        train_behavior_only_mean_control(dataset, behavior_dir, latent_dim=control_dim, seed=seed)
        rows.append(
            _score_model_run(
                behavior_dir,
                out_path / "runs" / f"behavior_only_mean_{control_dim}",
                task_name=task_name,
                steps=steps,
                seed=seed,
                migration_steps=migration_steps,
                label=f"BehaviorOnlyMean-{control_dim}",
                method="behavior-only-mean-control",
            )
        )

    curve_path = out_path / "abstraction_curve.json"
    _write_json(curve_path, rows)
    csv_path = out_path / "abstraction_curve.csv"
    fieldnames = list(rows[0].keys())
    for row in rows[1:]:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    best_pca = max((row for row in rows if row["method"] == "pca-ridge"), key=lambda item: item["behavior_fidelity"], default=None)
    summary = {
        "status": "ABSTRACTION CURVE COMPLETE",
        "task": task_name,
        "steps": steps,
        "latent_dims": latent_dims,
        "include_controls": include_controls,
        "curve_json": str(curve_path),
        "curve_csv": str(csv_path),
        "best_pca_model": best_pca,
    }
    _write_json(out_path / "curve_summary.json", summary)
    return summary
