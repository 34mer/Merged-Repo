from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from .abstraction import PCARidgeModel, AbstractState, abstract_step, initial_abstract_state
from .config import WormConfig
from .tasks import get_task, task_metrics


def corrupt_latent_state(latent: np.ndarray, corruption: str, seed: int = 42) -> np.ndarray:
    """Apply deterministic latent corruption for repairability tests."""

    rng = np.random.default_rng(seed)
    corrupted = latent.copy().astype(np.float64)
    if corruption == "zero_10_percent":
        count = max(1, int(np.ceil(0.10 * corrupted.shape[0])))
        idx = rng.choice(corrupted.shape[0], size=count, replace=False)
        corrupted[idx] = 0.0
    elif corruption == "gaussian_noise":
        scale = float(np.std(corrupted) + 1e-9) * 0.25
        corrupted = corrupted + rng.normal(0.0, scale, size=corrupted.shape)
    elif corruption == "sign_flip":
        count = max(1, int(np.ceil(0.10 * corrupted.shape[0])))
        idx = rng.choice(corrupted.shape[0], size=count, replace=False)
        corrupted[idx] *= -1.0
    elif corruption == "none":
        pass
    else:
        raise ValueError(f"Unknown corruption: {corruption}")
    return corrupted.astype(np.float64)


def run_repair_test(
    model_path: str | Path,
    out: str | Path,
    corruptions: list[str] | None = None,
    task_name: str = "hard_mixed",
    steps_before: int = 20,
    steps_after: int = 60,
    seed: int = 42,
) -> dict[str, Any]:
    """Run corruption-at-midpoint repair tests and score recovery."""

    if corruptions is None:
        corruptions = ["zero_10_percent", "gaussian_noise", "sign_flip"]
    config = WormConfig(seed=seed)
    model = PCARidgeModel(model_path)
    task = get_task(task_name, config)
    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []

    for corruption in corruptions:
        env, state = initial_abstract_state(model, config, task_name, seed=seed)
        for _ in range(steps_before):
            env, state, _ = abstract_step(config, model, task_name, env, state)
        baseline_latent = state.latent_state.copy()
        state = AbstractState(
            step=state.step,
            latent_state=corrupt_latent_state(state.latent_state, corruption, seed=seed),
            position=state.position.copy(),
            velocity=state.velocity.copy(),
            orientation=state.orientation,
            rng_state=dict(state.rng_state),
        )
        viability: list[float] = []
        latent_distances: list[float] = []
        for _ in range(steps_after):
            env, state, _ = abstract_step(config, model, task_name, env, state)
            viability.append(task_metrics(config, task, state.position, step=max(state.step - 1, 0)).viability)
            latent_distances.append(float(np.linalg.norm(state.latent_state - baseline_latent) / max(np.sqrt(model.latent_dim), 1.0)))
        mean_viability = float(np.mean(viability)) if viability else 0.0
        final_latent_distance = float(latent_distances[-1]) if latent_distances else 0.0
        repair_score = float(np.clip(0.70 * mean_viability + 0.30 * (1.0 / (1.0 + final_latent_distance)), 0.0, 1.0))
        rows.append(
            {
                "corruption": corruption,
                "mean_viability_after_corruption": mean_viability,
                "final_latent_distance": final_latent_distance,
                "repair_score": repair_score,
            }
        )

    report = {
        "status": "REPAIR TEST COMPLETE",
        "model": str(model_path),
        "model_hash": model.model_hash,
        "task": task_name,
        "steps_before": steps_before,
        "steps_after": steps_after,
        "mean_repair_score": float(np.mean([row["repair_score"] for row in rows])) if rows else 0.0,
        "rows": rows,
    }
    (out_path / "repair_report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def compute_repair_score(report: dict[str, Any]) -> float:
    return float(report.get("mean_repair_score", 0.0))
