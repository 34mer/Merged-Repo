from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from .checkpoint import file_hash
from .config import WormConfig
from .dynamics import step
from .environment import sensory_vector
from .organism import initial_state
from .tasks import (
    apply_perturbation,
    apply_task_start,
    environment_for_task,
    get_task,
    parse_tasks,
    task_metrics,
    update_environment_for_task,
)

DATASET_SCHEMA = "wormsim-source-trace-v1"


def motor_from_muscles(muscle_state: np.ndarray) -> np.ndarray:
    half = muscle_state.shape[0] // 2
    left = float(np.mean(muscle_state[:half]))
    right = float(np.mean(muscle_state[half:]))
    return np.array([left, right, right - left, left + right], dtype=np.float64)


def body_vector(state) -> np.ndarray:
    return np.array(
        [
            float(state.position[0]),
            float(state.position[1]),
            float(state.velocity[0]),
            float(state.velocity[1]),
            float(state.orientation),
        ],
        dtype=np.float64,
    )


def collect_dataset(
    out: str | Path,
    tasks: str | list[str] = "food,harm,perturb,wall,mixed",
    episodes: int = 10,
    steps: int = 500,
    seed: int = 42,
    neurons: int = 302,
) -> dict[str, Any]:
    """Collect full 302-neuron traces across deterministic task episodes."""

    task_names = parse_tasks(tasks)
    config = WormConfig(seed=seed, neurons=neurons)
    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)

    neural_rows: list[np.ndarray] = []
    sensory_rows: list[np.ndarray] = []
    motor_rows: list[np.ndarray] = []
    body_rows: list[np.ndarray] = []
    env_rows: list[np.ndarray] = []
    viability_rows: list[float] = []
    episode_rows: list[list[float]] = []

    for episode in range(episodes):
        task_name = task_names[episode % len(task_names)]
        task = get_task(task_name, config)
        env = environment_for_task(task, config=config, step=0)
        state = apply_task_start(task, initial_state(WormConfig(seed=seed + episode, neurons=neurons)))
        for local_step in range(steps):
            env = update_environment_for_task(config, task, env, local_step)
            sensory = sensory_vector(config, env, state.position, state.orientation)
            metrics = task_metrics(config, task, state.position, step=local_step)
            neural_rows.append(state.neuron_state.copy())
            sensory_rows.append(sensory[:7].copy())
            motor_rows.append(motor_from_muscles(state.muscle_state))
            body_rows.append(body_vector(state))
            env_rows.append(np.array([env.food_position[0], env.food_position[1], env.wall_bounce_count], dtype=np.float64))
            viability_rows.append(metrics.viability)
            episode_rows.append([float(episode), float(local_step), float(task_names.index(task_name))])
            state = apply_perturbation(task, state)
            env, state = step(config, env, state)

    arrays = {
        "X_neural": np.vstack(neural_rows).astype(np.float64),
        "S_sensory": np.vstack(sensory_rows).astype(np.float64),
        "A_motor": np.vstack(motor_rows).astype(np.float64),
        "B_body": np.vstack(body_rows).astype(np.float64),
        "E_env": np.vstack(env_rows).astype(np.float64),
        "V_viability": np.array(viability_rows, dtype=np.float64),
        "episode_index": np.array(episode_rows, dtype=np.float64),
    }
    data_path = out_path / "dataset.npz"
    np.savez_compressed(data_path, **arrays)
    digest = file_hash(data_path)
    metadata = {
        "schema": DATASET_SCHEMA,
        "config": config.to_dict(),
        "tasks": task_names,
        "episodes": episodes,
        "steps_per_episode": steps,
        "total_steps": int(arrays["X_neural"].shape[0]),
        "neural_shape": list(arrays["X_neural"].shape),
        "dataset_file": str(data_path),
        "dataset_hash": digest,
    }
    (out_path / "metadata.json").write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (out_path / "dataset_hash.txt").write_text(digest + "\n", encoding="utf-8")
    return metadata


def load_dataset(path: str | Path) -> dict[str, np.ndarray]:
    dataset_path = Path(path)
    if dataset_path.is_dir():
        dataset_path = dataset_path / "dataset.npz"
    with np.load(dataset_path, allow_pickle=False) as data:
        return {key: data[key] for key in data.files}


def source_behavior_reference(config: WormConfig, task_name: str, steps: int, seed: int = 42) -> dict[str, Any]:
    task = get_task(task_name, config)
    env = environment_for_task(task, config=config, step=0)
    state = apply_task_start(task, initial_state(WormConfig(seed=seed, neurons=config.neurons)))
    viability: list[float] = []
    positions: list[np.ndarray] = []
    for local_step in range(steps):
        env = update_environment_for_task(config, task, env, local_step)
        state = apply_perturbation(task, state)
        env, state = step(config, env, state)
        viability.append(task_metrics(config, task, state.position, step=local_step).viability)
        positions.append(state.position.copy())
    positions_array = np.vstack(positions)
    return {
        "mean_viability": float(np.mean(viability)),
        "final_distance_to_food": float(task_metrics(config, task, state.position, step=max(steps - 1, 0)).distance_to_food),
        "positions": positions_array,
    }
