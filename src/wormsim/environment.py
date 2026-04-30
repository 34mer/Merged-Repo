from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

import numpy as np

from .config import WormConfig


@dataclass(frozen=True)
class EnvironmentState:
    food_position: tuple[float, float]
    wall_bounce_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "EnvironmentState":
        food = tuple(float(x) for x in data["food_position"])
        return cls(food_position=food, wall_bounce_count=int(data.get("wall_bounce_count", 0)))


def initial_environment(config: WormConfig) -> EnvironmentState:
    return EnvironmentState(food_position=(config.world_size * 0.82, config.world_size * 0.52))


def sensory_vector(config: WormConfig, env: EnvironmentState, position: np.ndarray, orientation: float) -> np.ndarray:
    """Return deterministic sensory inputs projected into the first neurons."""

    food = np.array(env.food_position, dtype=np.float64)
    delta = food - position
    distance = float(np.linalg.norm(delta) + 1e-12)
    heading = np.array([np.cos(orientation), np.sin(orientation)], dtype=np.float64)
    left_sensor = np.array([np.cos(orientation + 0.55), np.sin(orientation + 0.55)], dtype=np.float64)
    right_sensor = np.array([np.cos(orientation - 0.55), np.sin(orientation - 0.55)], dtype=np.float64)
    direction = delta / distance

    wall_left = max(0.0, 1.0 - position[0])
    wall_right = max(0.0, 1.0 - (config.world_size - position[0]))
    wall_bottom = max(0.0, 1.0 - position[1])
    wall_top = max(0.0, 1.0 - (config.world_size - position[1]))

    sensory = np.zeros(config.neurons, dtype=np.float64)
    sensory[0] = np.dot(direction, heading) / distance
    sensory[1] = np.dot(direction, left_sensor) / distance
    sensory[2] = np.dot(direction, right_sensor) / distance
    sensory[3] = wall_left
    sensory[4] = wall_right
    sensory[5] = wall_bottom
    sensory[6] = wall_top
    return config.sensory_gain * sensory


def clamp_to_world(config: WormConfig, env: EnvironmentState, position: np.ndarray, velocity: np.ndarray) -> tuple[EnvironmentState, np.ndarray, np.ndarray]:
    next_position = position.copy()
    next_velocity = velocity.copy()
    bounces = env.wall_bounce_count
    for axis in (0, 1):
        if next_position[axis] < 0.0:
            next_position[axis] = 0.0
            next_velocity[axis] = abs(next_velocity[axis]) * 0.5
            bounces += 1
        elif next_position[axis] > config.world_size:
            next_position[axis] = config.world_size
            next_velocity[axis] = -abs(next_velocity[axis]) * 0.5
            bounces += 1
    return EnvironmentState(food_position=env.food_position, wall_bounce_count=bounces), next_position, next_velocity
