from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from .config import WormConfig


@dataclass
class WormState:
    """Complete live state needed to continue the organism exactly."""

    step: int
    neuron_state: np.ndarray
    muscle_state: np.ndarray
    position: np.ndarray
    velocity: np.ndarray
    orientation: float
    rng_state: dict[str, Any]

    def copy(self) -> "WormState":
        return WormState(
            step=int(self.step),
            neuron_state=self.neuron_state.copy(),
            muscle_state=self.muscle_state.copy(),
            position=self.position.copy(),
            velocity=self.velocity.copy(),
            orientation=float(self.orientation),
            rng_state=dict(self.rng_state),
        )


def initial_state(config: WormConfig) -> WormState:
    """Create a deterministic initial organism state from a seed."""

    rng = np.random.default_rng(config.seed)
    neuron_state = rng.normal(0.0, 0.02, size=config.neurons).astype(np.float64)
    muscle_state = np.zeros(config.muscles, dtype=np.float64)
    position = np.array([config.world_size * 0.25, config.world_size * 0.5], dtype=np.float64)
    velocity = np.zeros(2, dtype=np.float64)
    orientation = 0.0
    return WormState(
        step=0,
        neuron_state=neuron_state,
        muscle_state=muscle_state,
        position=position,
        velocity=velocity,
        orientation=orientation,
        rng_state=rng.bit_generator.state,
    )
