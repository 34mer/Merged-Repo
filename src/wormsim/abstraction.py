from __future__ import annotations

import json
import shutil
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np

from .checkpoint import _canonical_json, file_hash
from .config import WormConfig
from .dataset import load_dataset, motor_from_muscles, source_behavior_reference
from .dynamics import step as full_step
from .environment import EnvironmentState, clamp_to_world, sensory_vector
from .organism import WormState, initial_state
from .tasks import apply_perturbation, apply_task_start, environment_for_task, get_task, task_metrics

ABSTRACTION_SCHEMA = "wormsim-pca-ridge-abstraction-v1"
ABSTRACT_CHECKPOINT_SCHEMA = "wormsim-abstract-checkpoint-v1"


@dataclass(frozen=True)
class AbstractState:
    step: int
    latent_state: np.ndarray
    position: np.ndarray
    velocity: np.ndarray
    orientation: float
    rng_state: dict[str, Any]


@dataclass(frozen=True)
class AbstractRunReport:
    status: str
    model_hash: str
    checkpoint_hash_matched: bool | None
    latent_trajectory_divergence: float | None
    mean_viability: float
    final_distance_to_food: float
    behavior_continuation: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _ridge(features: np.ndarray, targets: np.ndarray, alpha: float) -> np.ndarray:
    design = np.hstack([features, np.ones((features.shape[0], 1), dtype=np.float64)])
    gram = design.T @ design
    reg = alpha * np.eye(gram.shape[0], dtype=np.float64)
    reg[-1, -1] = 0.0
    return np.linalg.solve(gram + reg, design.T @ targets)


def train_pca_ridge(dataset: str | Path, out: str | Path, latent_dim: int = 64, alpha: float = 1e-6) -> dict[str, Any]:
    """Train a NumPy-only PCA + Ridge live abstraction."""

    arrays = load_dataset(dataset)
    x = arrays["X_neural"]
    sensory = arrays["S_sensory"]
    body = arrays["B_body"]
    motor = arrays["A_motor"]
    if latent_dim <= 0 or latent_dim > x.shape[1]:
        raise ValueError(f"latent_dim must be in [1, {x.shape[1]}]")

    mean = np.mean(x, axis=0)
    centered = x - mean
    _, singular_values, vt = np.linalg.svd(centered, full_matrices=False)
    components = vt[:latent_dim].astype(np.float64)
    z = centered @ components.T
    features = np.hstack([z[:-1], sensory[:-1], body[:-1]])
    transition_weights = _ridge(features, z[1:], alpha=alpha)
    motor_weights = _ridge(z, motor, alpha=alpha)

    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)
    model_path = out_path / "model.npz"
    np.savez_compressed(
        model_path,
        mean=mean.astype(np.float64),
        components=components,
        singular_values=singular_values[:latent_dim].astype(np.float64),
        transition_weights=transition_weights.astype(np.float64),
        motor_weights=motor_weights.astype(np.float64),
        latent_dim=np.array([latent_dim], dtype=np.int64),
        alpha=np.array([alpha], dtype=np.float64),
    )
    digest = file_hash(model_path)
    metadata = {
        "schema": ABSTRACTION_SCHEMA,
        "method": "pca-ridge",
        "latent_dim": latent_dim,
        "source_dim": int(x.shape[1]),
        "compression_ratio": float(x.shape[1] / latent_dim),
        "alpha": alpha,
        "model_file": str(model_path),
        "model_hash": digest,
    }
    (out_path / "metadata.json").write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (out_path / "model_hash.txt").write_text(digest + "\n", encoding="utf-8")
    return metadata


class PCARidgeModel:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        model_path = self.path / "model.npz" if self.path.is_dir() else self.path
        with np.load(model_path, allow_pickle=False) as data:
            self.mean = data["mean"].astype(np.float64)
            self.components = data["components"].astype(np.float64)
            self.transition_weights = data["transition_weights"].astype(np.float64)
            self.motor_weights = data["motor_weights"].astype(np.float64)
            self.latent_dim = int(data["latent_dim"][0])
        self.model_path = model_path
        self.model_hash = file_hash(model_path)

    def encode(self, neuron_state: np.ndarray) -> np.ndarray:
        return (neuron_state - self.mean) @ self.components.T

    def decode_motor(self, latent_state: np.ndarray) -> np.ndarray:
        design = np.concatenate([latent_state, np.ones(1, dtype=np.float64)])
        return design @ self.motor_weights

    def transition(self, latent_state: np.ndarray, sensory: np.ndarray, body: np.ndarray) -> np.ndarray:
        design = np.concatenate([latent_state, sensory, body, np.ones(1, dtype=np.float64)])
        return design @ self.transition_weights


def initial_abstract_state(model: PCARidgeModel, config: WormConfig, task_name: str, seed: int = 42) -> tuple[EnvironmentState, AbstractState]:
    task = get_task(task_name, config)
    env = environment_for_task(task)
    source_state = apply_task_start(task, initial_state(WormConfig(seed=seed, neurons=config.neurons)))
    return env, AbstractState(
        step=0,
        latent_state=model.encode(source_state.neuron_state),
        position=source_state.position.copy(),
        velocity=source_state.velocity.copy(),
        orientation=float(source_state.orientation),
        rng_state=source_state.rng_state,
    )


def _body_from_abstract(state: AbstractState) -> np.ndarray:
    return np.array([state.position[0], state.position[1], state.velocity[0], state.velocity[1], state.orientation], dtype=np.float64)


def abstract_step(config: WormConfig, model: PCARidgeModel, task_name: str, env: EnvironmentState, state: AbstractState) -> tuple[EnvironmentState, AbstractState, np.ndarray]:
    task = get_task(task_name, config)
    if task.perturb_every > 0 and state.step > 0 and state.step % task.perturb_every == 0:
        orientation = float((state.orientation + task.perturb_angle + np.pi) % (2.0 * np.pi) - np.pi)
        velocity = np.array([-state.velocity[1], state.velocity[0]], dtype=np.float64)
        state = AbstractState(state.step, state.latent_state, state.position, velocity, orientation, state.rng_state)

    sensory = sensory_vector(config, env, state.position, state.orientation)[:7]
    body = _body_from_abstract(state)
    motor = model.decode_motor(state.latent_state)
    left = float(motor[0])
    right = float(motor[1])
    turn = config.muscle_gain * (right - left)
    drive = float(np.clip(config.max_speed * (1.0 + left + right), 0.0, config.max_speed))
    orientation = float((state.orientation + turn + np.pi) % (2.0 * np.pi) - np.pi)
    heading = np.array([np.cos(orientation), np.sin(orientation)], dtype=np.float64)
    velocity = (config.drag * state.velocity + drive * heading).astype(np.float64)
    position = (state.position + config.dt * velocity).astype(np.float64)
    env2, position2, velocity2 = clamp_to_world(config, env, position, velocity)
    latent2 = model.transition(state.latent_state, sensory, body).astype(np.float64)
    next_state = AbstractState(
        step=state.step + 1,
        latent_state=latent2,
        position=position2,
        velocity=velocity2,
        orientation=orientation,
        rng_state=dict(state.rng_state),
    )
    return env2, next_state, motor.astype(np.float64)


def run_abstracted(model_path: str | Path, out: str | Path, task_name: str = "mixed", steps: int = 1000, seed: int = 42) -> dict[str, Any]:
    config = WormConfig(seed=seed)
    model = PCARidgeModel(model_path)
    env, state = initial_abstract_state(model, config, task_name, seed=seed)
    trajectory: list[list[float]] = []
    viability: list[float] = []
    for _ in range(steps):
        env, state, motor = abstract_step(config, model, task_name, env, state)
        metrics = task_metrics(config, get_task(task_name, config), state.position)
        trajectory.append([float(state.step), float(state.position[0]), float(state.position[1]), float(state.orientation), float(np.sum(state.latent_state))])
        viability.append(metrics.viability)
    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(out_path / "trajectory.npz", trajectory=np.array(trajectory, dtype=np.float64), viability=np.array(viability, dtype=np.float64))
    checkpoint_hash = save_abstract_checkpoint(out_path / f"checkpoint_t{state.step}.npz", config, model, task_name, env, state)
    report = {
        "status": "ABSTRACTED RUN COMPLETE",
        "model_hash": model.model_hash,
        "checkpoint_hash": checkpoint_hash,
        "task": task_name,
        "steps": steps,
        "mean_viability": float(np.mean(viability)) if viability else 0.0,
        "final_distance_to_food": float(task_metrics(config, get_task(task_name, config), state.position).distance_to_food),
    }
    (out_path / "run_report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def save_abstract_checkpoint(path: str | Path, config: WormConfig, model: PCARidgeModel, task_name: str, env: EnvironmentState, state: AbstractState) -> str:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    metadata = {
        "schema": ABSTRACT_CHECKPOINT_SCHEMA,
        "config": config.to_dict(),
        "task": task_name,
        "environment": env.to_dict(),
        "model_hash": model.model_hash,
        "rng_state": state.rng_state,
        "step": state.step,
        "orientation": state.orientation,
    }
    np.savez_compressed(
        path,
        metadata=np.array(_canonical_json(metadata)),
        latent_state=state.latent_state.astype(np.float64),
        position=state.position.astype(np.float64),
        velocity=state.velocity.astype(np.float64),
    )
    digest = file_hash(path)
    path.with_suffix(path.suffix + ".blake3").write_text(digest + "\n", encoding="utf-8")
    return digest


def load_abstract_checkpoint(path: str | Path) -> tuple[WormConfig, str, EnvironmentState, AbstractState, str]:
    with np.load(Path(path), allow_pickle=False) as data:
        metadata = json.loads(str(data["metadata"]))
        if metadata.get("schema") != ABSTRACT_CHECKPOINT_SCHEMA:
            raise ValueError(f"Unsupported abstract checkpoint schema: {metadata.get('schema')}")
        config = WormConfig.from_dict(metadata["config"])
        env = EnvironmentState.from_dict(metadata["environment"])
        state = AbstractState(
            step=int(metadata["step"]),
            latent_state=data["latent_state"].astype(np.float64),
            position=data["position"].astype(np.float64),
            velocity=data["velocity"].astype(np.float64),
            orientation=float(metadata["orientation"]),
            rng_state=metadata["rng_state"],
        )
        return config, str(metadata["task"]), env, state, str(metadata["model_hash"])


def migrate_abstracted(checkpoint: str | Path, out: str | Path) -> dict[str, Any]:
    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)
    target = out_path / Path(checkpoint).name
    shutil.copy2(checkpoint, target)
    expected = file_hash(checkpoint)
    matched = file_hash(target) == expected
    manifest = {"source": str(checkpoint), "target": str(target), "checkpoint_hash": expected, "hash_matched": matched}
    (out_path / "abstract_migration_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def verify_abstracted_migration(model_path: str | Path, checkpoint_a: str | Path, checkpoint_b: str | Path, steps: int = 250) -> AbstractRunReport:
    model = PCARidgeModel(model_path)
    config_a, task_a, env_a, state_a, model_hash_a = load_abstract_checkpoint(checkpoint_a)
    config_b, task_b, env_b, state_b, model_hash_b = load_abstract_checkpoint(checkpoint_b)
    traj_a: list[np.ndarray] = []
    traj_b: list[np.ndarray] = []
    viability: list[float] = []
    for _ in range(steps):
        env_a, state_a, _ = abstract_step(config_a, model, task_a, env_a, state_a)
        env_b, state_b, _ = abstract_step(config_b, model, task_b, env_b, state_b)
        traj_a.append(np.concatenate([state_a.latent_state, state_a.position, state_a.velocity, [state_a.orientation]]))
        traj_b.append(np.concatenate([state_b.latent_state, state_b.position, state_b.velocity, [state_b.orientation]]))
        viability.append(task_metrics(config_a, get_task(task_a, config_a), state_a.position).viability)
    divergence = float(np.max(np.abs(np.vstack(traj_a) - np.vstack(traj_b)))) if traj_a else 0.0
    hash_match = file_hash(checkpoint_a) == file_hash(checkpoint_b)
    model_match = model.model_hash == model_hash_a == model_hash_b
    status = "ABSTRACTED MIGRATION VERIFIED" if hash_match and model_match and divergence == 0.0 else "ABSTRACTED MIGRATION FAILED"
    return AbstractRunReport(
        status=status,
        model_hash=model.model_hash,
        checkpoint_hash_matched=hash_match,
        latent_trajectory_divergence=divergence,
        mean_viability=float(np.mean(viability)) if viability else 0.0,
        final_distance_to_food=float(task_metrics(config_a, get_task(task_a, config_a), state_a.position).distance_to_food),
        behavior_continuation="passed" if status == "ABSTRACTED MIGRATION VERIFIED" else "failed",
    )


def benchmark_abstraction(model_path: str | Path, out: str | Path, task_name: str = "mixed", steps: int = 1000, seed: int = 42) -> dict[str, Any]:
    config = WormConfig(seed=seed)
    model = PCARidgeModel(model_path)
    abstract_report = run_abstracted(model_path, Path(out) / "abstracted_live", task_name=task_name, steps=steps, seed=seed)
    source_ref = source_behavior_reference(config, task_name=task_name, steps=steps, seed=seed)
    abstract_viability = float(abstract_report["mean_viability"])
    source_viability = float(source_ref["mean_viability"])
    viability_fidelity = 1.0 - min(1.0, abs(source_viability - abstract_viability) / max(source_viability, 1e-9))
    source_distance = float(source_ref["final_distance_to_food"])
    abstract_distance = float(abstract_report["final_distance_to_food"])
    distance_fidelity = 1.0 - min(1.0, abs(source_distance - abstract_distance) / max(config.world_size, 1e-9))
    behavior_fidelity = float(np.clip(0.55 * viability_fidelity + 0.45 * distance_fidelity, 0.0, 1.0))
    report = {
        "status": "ABSTRACTION MIGRATION BENCHMARK COMPLETE",
        "source": "302-neuron organism-like process",
        "abstraction": f"PCA-Ridge {model.latent_dim} latent units",
        "compression_ratio": float(config.neurons / model.latent_dim),
        "model_hash": model.model_hash,
        "behavior_fidelity": behavior_fidelity,
        "self_maintenance_retained": float(np.clip(abstract_viability / max(source_viability, 1e-9), 0.0, 2.0)),
        "source_mean_viability": source_viability,
        "abstract_mean_viability": abstract_viability,
        "source_final_distance_to_food": source_distance,
        "abstract_final_distance_to_food": abstract_distance,
    }
    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)
    (out_path / "benchmark_report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report
