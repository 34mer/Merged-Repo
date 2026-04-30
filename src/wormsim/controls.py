from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from .checkpoint import file_hash
from .config import WormConfig
from .curve import train_behavior_only_mean_control, train_random_latent_control
from .dataset import load_dataset


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _random_components(source_dim: int, latent_dim: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    raw = rng.normal(0.0, 1.0, size=(source_dim, latent_dim))
    q, _ = np.linalg.qr(raw)
    return q[:, :latent_dim].T.astype(np.float64)


def _write_model(
    out: str | Path,
    method: str,
    mean: np.ndarray,
    components: np.ndarray,
    transition_weights: np.ndarray,
    motor_weights: np.ndarray,
    latent_dim: int,
) -> dict[str, Any]:
    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)
    model_path = out_path / "model.npz"
    np.savez_compressed(
        model_path,
        mean=mean.astype(np.float64),
        components=components.astype(np.float64),
        singular_values=np.zeros(latent_dim, dtype=np.float64),
        transition_weights=transition_weights.astype(np.float64),
        motor_weights=motor_weights.astype(np.float64),
        latent_dim=np.array([latent_dim], dtype=np.int64),
        alpha=np.array([0.0], dtype=np.float64),
    )
    digest = file_hash(model_path)
    metadata = {
        "schema": "wormsim-control-abstraction-v1",
        "method": method,
        "latent_dim": latent_dim,
        "source_dim": int(mean.shape[0]),
        "compression_ratio": float(mean.shape[0] / latent_dim),
        "model_file": str(model_path),
        "model_hash": digest,
    }
    _write_json(out_path / "metadata.json", metadata)
    (out_path / "model_hash.txt").write_text(digest + "\n", encoding="utf-8")
    return metadata


def train_frozen_policy_control(dataset: str | Path, out: str | Path, latent_dim: int = 8, seed: int = 42) -> dict[str, Any]:
    """Train a stable but dumb controller that ignores sensory state."""

    arrays = load_dataset(dataset)
    x = arrays["X_neural"]
    source_dim = int(x.shape[1])
    mean = np.mean(x, axis=0)
    components = _random_components(source_dim, latent_dim, seed + 303)
    transition_weights = np.zeros((latent_dim + 7 + 5 + 1, latent_dim), dtype=np.float64)
    motor_weights = np.zeros((latent_dim + 1, 4), dtype=np.float64)
    motor_weights[-1, :] = np.array([-0.48, -0.48, 0.0, -0.96], dtype=np.float64)
    return _write_model(out, "frozen-policy-control", mean, components, transition_weights, motor_weights, latent_dim)


def train_over_stable_control(dataset: str | Path, out: str | Path, latent_dim: int = 8, seed: int = 42) -> dict[str, Any]:
    """Train a controller that prioritizes low movement and apparent stability."""

    arrays = load_dataset(dataset)
    x = arrays["X_neural"]
    source_dim = int(x.shape[1])
    mean = np.mean(x, axis=0)
    components = _random_components(source_dim, latent_dim, seed + 404)
    transition_weights = np.zeros((latent_dim + 7 + 5 + 1, latent_dim), dtype=np.float64)
    transition_weights[:latent_dim, :] = 0.10 * np.eye(latent_dim, dtype=np.float64)
    motor_weights = np.zeros((latent_dim + 1, 4), dtype=np.float64)
    motor_weights[-1, :] = np.array([-0.45, -0.45, 0.0, -0.90], dtype=np.float64)
    return _write_model(out, "over-stable-control", mean, components, transition_weights, motor_weights, latent_dim)


def train_shuffled_dynamics_control(base_model: str | Path, out: str | Path, seed: int = 42) -> dict[str, Any]:
    """Keep model size but shuffle transition/motor structure to break organization."""

    rng = np.random.default_rng(seed + 505)
    base_path = Path(base_model) / "model.npz" if Path(base_model).is_dir() else Path(base_model)
    with np.load(base_path, allow_pickle=False) as data:
        mean = data["mean"].astype(np.float64)
        components = data["components"].astype(np.float64)
        transition_weights = data["transition_weights"].astype(np.float64).copy()
        motor_weights = data["motor_weights"].astype(np.float64).copy()
        latent_dim = int(data["latent_dim"][0])
    flat_t = transition_weights.reshape(-1)
    flat_m = motor_weights.reshape(-1)
    rng.shuffle(flat_t)
    rng.shuffle(flat_m)
    return _write_model(
        out,
        "shuffled-dynamics-control",
        mean,
        components,
        flat_t.reshape(transition_weights.shape),
        flat_m.reshape(motor_weights.shape),
        latent_dim,
    )


__all__ = [
    "train_random_latent_control",
    "train_behavior_only_mean_control",
    "train_frozen_policy_control",
    "train_over_stable_control",
    "train_shuffled_dynamics_control",
]
