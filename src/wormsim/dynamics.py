from __future__ import annotations

import numpy as np

from .config import WormConfig
from .environment import EnvironmentState, clamp_to_world, sensory_vector
from .organism import WormState


def _connectome_matrix(config: WormConfig) -> np.ndarray:
    """Build a deterministic worm-inspired recurrent matrix.

    The matrix is synthetic but stable: every machine reconstructs the exact same
    weights from config.seed, so checkpoints only need to store organism state.
    """

    rng = np.random.default_rng(config.seed + 30_200)
    base = rng.normal(0.0, 0.08, size=(config.neurons, config.neurons)).astype(np.float64)
    mask = rng.random((config.neurons, config.neurons)) < 0.055
    weights = np.where(mask, base, 0.0)

    # Add local ring continuity so the synthetic network has worm-like body waves.
    for i in range(config.neurons):
        weights[i, (i - 1) % config.neurons] += 0.08
        weights[i, (i + 1) % config.neurons] += 0.08

    # Normalize conservatively for stable deterministic dynamics.
    row_norm = np.maximum(np.sum(np.abs(weights), axis=1), 1.0)
    return (weights / row_norm[:, None] * config.recurrent_gain).astype(np.float64)


def _muscle_projection(config: WormConfig) -> np.ndarray:
    rng = np.random.default_rng(config.seed + 90_001)
    projection = rng.normal(0.0, 0.14, size=(config.muscles, config.neurons)).astype(np.float64)
    return projection / np.maximum(np.linalg.norm(projection, axis=1, keepdims=True), 1.0)


def step(config: WormConfig, env: EnvironmentState, state: WormState) -> tuple[EnvironmentState, WormState]:
    """Advance by one fixed deterministic time step."""

    weights = _connectome_matrix(config)
    muscles = _muscle_projection(config)
    sensory = sensory_vector(config, env, state.position, state.orientation)

    neurons = np.tanh(weights @ state.neuron_state + sensory).astype(np.float64)
    muscle_state = np.tanh(muscles @ neurons).astype(np.float64)

    half = config.muscles // 2
    left = float(np.mean(muscle_state[:half]))
    right = float(np.mean(muscle_state[half:]))
    turn = config.muscle_gain * (right - left)
    drive = float(np.clip(config.max_speed * (1.0 + left + right), 0.0, config.max_speed))

    orientation = float((state.orientation + turn + np.pi) % (2.0 * np.pi) - np.pi)
    heading = np.array([np.cos(orientation), np.sin(orientation)], dtype=np.float64)
    velocity = (config.drag * state.velocity + drive * heading).astype(np.float64)
    position = (state.position + config.dt * velocity).astype(np.float64)

    env2, position2, velocity2 = clamp_to_world(config, env, position, velocity)
    next_state = WormState(
        step=state.step + 1,
        neuron_state=neurons,
        muscle_state=muscle_state,
        position=position2,
        velocity=velocity2,
        orientation=orientation,
        rng_state=dict(state.rng_state),
    )
    return env2, next_state


def run_steps(config: WormConfig, env: EnvironmentState, state: WormState, steps: int) -> tuple[EnvironmentState, WormState, np.ndarray]:
    """Run and return a compact trajectory: step, x, y, orientation, neural checksum."""

    rows: list[list[float]] = []
    current_env = env
    current_state = state
    for _ in range(steps):
        current_env, current_state = step(config, current_env, current_state)
        rows.append(
            [
                float(current_state.step),
                float(current_state.position[0]),
                float(current_state.position[1]),
                float(current_state.orientation),
                float(np.sum(current_state.neuron_state)),
            ]
        )
    return current_env, current_state, np.array(rows, dtype=np.float64)
