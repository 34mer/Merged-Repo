from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Iterable

import numpy as np

from .config import WormConfig
from .environment import EnvironmentState
from .organism import WormState

TASK_NAMES = (
    "food",
    "harm",
    "perturb",
    "wall",
    "mixed",
    "dynamic_food",
    "time_harm",
    "memory",
    "switch",
    "hard_mixed",
)


@dataclass(frozen=True)
class TaskSpec:
    """Deterministic closed-loop task specification for the abstraction benchmark."""

    name: str
    food_position: tuple[float, float]
    start_position: tuple[float, float]
    harm_center: tuple[float, float] | None = None
    harm_radius: float = 0.0
    perturb_every: int = 0
    perturb_angle: float = 0.0
    wall_start: bool = False
    dynamic_food: bool = False
    food_orbit_radius: float = 0.0
    food_period: int = 200
    moving_harm: bool = False
    harm_period: int = 180
    delayed_harm_step: int = 0
    memory_switch_step: int = 0
    switch_food_position: tuple[float, float] | None = None
    displacement_magnitude: float = 0.0

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class TaskMetrics:
    distance_to_food: float
    food_reached: float
    harm_contact: float
    viability: float

    def to_vector(self) -> np.ndarray:
        return np.array(
            [self.distance_to_food, self.food_reached, self.harm_contact, self.viability],
            dtype=np.float64,
        )


def get_task(name: str, config: WormConfig) -> TaskSpec:
    if name not in TASK_NAMES:
        raise ValueError(f"Unknown task {name!r}; expected one of {TASK_NAMES}")
    size = config.world_size
    if name == "food":
        return TaskSpec(name=name, food_position=(0.82 * size, 0.52 * size), start_position=(0.25 * size, 0.5 * size))
    if name == "harm":
        return TaskSpec(
            name=name,
            food_position=(0.82 * size, 0.52 * size),
            start_position=(0.35 * size, 0.5 * size),
            harm_center=(0.48 * size, 0.5 * size),
            harm_radius=0.12 * size,
        )
    if name == "perturb":
        return TaskSpec(
            name=name,
            food_position=(0.82 * size, 0.52 * size),
            start_position=(0.25 * size, 0.5 * size),
            perturb_every=150,
            perturb_angle=0.65,
            displacement_magnitude=0.12 * size,
        )
    if name == "wall":
        return TaskSpec(
            name=name,
            food_position=(0.82 * size, 0.52 * size),
            start_position=(0.08 * size, 0.5 * size),
            wall_start=True,
        )
    if name == "dynamic_food":
        return TaskSpec(
            name=name,
            food_position=(0.62 * size, 0.52 * size),
            start_position=(0.20 * size, 0.35 * size),
            dynamic_food=True,
            food_orbit_radius=0.22 * size,
            food_period=120,
            perturb_every=80,
            perturb_angle=0.85,
            displacement_magnitude=0.10 * size,
        )
    if name == "time_harm":
        return TaskSpec(
            name=name,
            food_position=(0.80 * size, 0.60 * size),
            start_position=(0.20 * size, 0.40 * size),
            harm_center=(0.50 * size, 0.50 * size),
            harm_radius=0.18 * size,
            moving_harm=True,
            harm_period=90,
            delayed_harm_step=40,
            perturb_every=75,
            perturb_angle=-0.95,
            displacement_magnitude=0.08 * size,
        )
    if name == "memory":
        return TaskSpec(
            name=name,
            food_position=(0.82 * size, 0.25 * size),
            switch_food_position=(0.18 * size, 0.78 * size),
            start_position=(0.50 * size, 0.50 * size),
            harm_center=(0.50 * size, 0.50 * size),
            harm_radius=0.10 * size,
            memory_switch_step=120,
            delayed_harm_step=80,
            perturb_every=60,
            perturb_angle=1.05,
            displacement_magnitude=0.12 * size,
        )
    if name == "switch":
        return TaskSpec(
            name=name,
            food_position=(0.80 * size, 0.20 * size),
            switch_food_position=(0.20 * size, 0.80 * size),
            start_position=(0.18 * size, 0.18 * size),
            harm_center=(0.50 * size, 0.50 * size),
            harm_radius=0.16 * size,
            moving_harm=True,
            harm_period=110,
            memory_switch_step=100,
            perturb_every=50,
            perturb_angle=-1.15,
            displacement_magnitude=0.15 * size,
        )
    if name == "hard_mixed":
        return TaskSpec(
            name=name,
            food_position=(0.76 * size, 0.24 * size),
            switch_food_position=(0.22 * size, 0.82 * size),
            start_position=(0.15 * size, 0.35 * size),
            harm_center=(0.52 * size, 0.50 * size),
            harm_radius=0.18 * size,
            dynamic_food=True,
            food_orbit_radius=0.16 * size,
            food_period=100,
            moving_harm=True,
            harm_period=85,
            delayed_harm_step=30,
            memory_switch_step=125,
            perturb_every=45,
            perturb_angle=1.25,
            displacement_magnitude=0.16 * size,
        )
    return TaskSpec(
        name=name,
        food_position=(0.82 * size, 0.65 * size),
        start_position=(0.20 * size, 0.35 * size),
        harm_center=(0.50 * size, 0.50 * size),
        harm_radius=0.13 * size,
        perturb_every=175,
        perturb_angle=-0.55,
    )


def parse_tasks(value: str | Iterable[str]) -> list[str]:
    if isinstance(value, str):
        tasks = [item.strip() for item in value.split(",") if item.strip()]
    else:
        tasks = list(value)
    if not tasks:
        raise ValueError("At least one task is required")
    for task in tasks:
        if task not in TASK_NAMES:
            raise ValueError(f"Unknown task {task!r}; expected one of {TASK_NAMES}")
    return tasks


def food_position_at(config: WormConfig, task: TaskSpec, step: int) -> tuple[float, float]:
    base = task.food_position
    if task.memory_switch_step > 0 and task.switch_food_position is not None and step >= task.memory_switch_step:
        base = task.switch_food_position
    if not task.dynamic_food:
        return base
    angle = 2.0 * np.pi * (step % max(task.food_period, 1)) / max(task.food_period, 1)
    x = float(np.clip(base[0] + task.food_orbit_radius * np.cos(angle), 0.0, config.world_size))
    y = float(np.clip(base[1] + task.food_orbit_radius * np.sin(angle), 0.0, config.world_size))
    return (x, y)


def harm_center_at(config: WormConfig, task: TaskSpec, step: int) -> tuple[float, float] | None:
    if task.harm_center is None:
        return None
    if task.delayed_harm_step > 0 and step < task.delayed_harm_step:
        return None
    if not task.moving_harm:
        return task.harm_center
    angle = 2.0 * np.pi * (step % max(task.harm_period, 1)) / max(task.harm_period, 1)
    radius = 0.16 * config.world_size
    x = float(np.clip(task.harm_center[0] + radius * np.cos(angle), 0.0, config.world_size))
    y = float(np.clip(task.harm_center[1] + radius * np.sin(angle), 0.0, config.world_size))
    return (x, y)


def environment_for_task(task: TaskSpec, config: WormConfig | None = None, step: int = 0) -> EnvironmentState:
    if config is None:
        return EnvironmentState(food_position=task.food_position)
    return EnvironmentState(food_position=food_position_at(config, task, step))


def update_environment_for_task(config: WormConfig, task: TaskSpec, env: EnvironmentState, step: int) -> EnvironmentState:
    return EnvironmentState(food_position=food_position_at(config, task, step), wall_bounce_count=env.wall_bounce_count)


def apply_task_start(task: TaskSpec, state: WormState) -> WormState:
    started = state.copy()
    started.position = np.array(task.start_position, dtype=np.float64)
    if task.wall_start:
        started.orientation = np.pi
    return started


def apply_perturbation(task: TaskSpec, state: WormState) -> WormState:
    if task.perturb_every <= 0 or state.step <= 0 or state.step % task.perturb_every != 0:
        return state
    perturbed = state.copy()
    perturbed.orientation = float((perturbed.orientation + task.perturb_angle + np.pi) % (2.0 * np.pi) - np.pi)
    perturbed.velocity = np.array([-perturbed.velocity[1], perturbed.velocity[0]], dtype=np.float64)
    if task.displacement_magnitude > 0.0:
        heading = np.array([np.cos(perturbed.orientation), np.sin(perturbed.orientation)], dtype=np.float64)
        sideways = np.array([-heading[1], heading[0]], dtype=np.float64)
        sign = -1.0 if (state.step // task.perturb_every) % 2 else 1.0
        perturbed.position = np.clip(perturbed.position + sign * task.displacement_magnitude * sideways, 0.0, 10.0)
    return perturbed


def task_metrics(config: WormConfig, task: TaskSpec, position: np.ndarray, step: int = 0) -> TaskMetrics:
    food = np.array(food_position_at(config, task, step), dtype=np.float64)
    distance = float(np.linalg.norm(food - position))
    food_reached = 1.0 if distance <= 0.75 else 0.0
    harm_contact = 0.0
    harm_position = harm_center_at(config, task, step)
    if harm_position is not None:
        harm = np.array(harm_position, dtype=np.float64)
        harm_contact = 1.0 if float(np.linalg.norm(harm - position)) <= task.harm_radius else 0.0
    wall_margin = min(position[0], position[1], config.world_size - position[0], config.world_size - position[1])
    wall_penalty = 1.0 if wall_margin < 0.25 else 0.0
    delayed_penalty = 0.08 if task.delayed_harm_step > 0 and step >= task.delayed_harm_step and harm_contact else 0.0
    switch_penalty = 0.06 if task.memory_switch_step > 0 and step >= task.memory_switch_step and distance > config.world_size * 0.45 else 0.0
    viability = float(
        np.clip(
            1.0
            - 0.18 * distance / config.world_size
            - 0.62 * harm_contact
            - 0.20 * wall_penalty
            - delayed_penalty
            - switch_penalty,
            0.0,
            1.0,
        )
    )
    return TaskMetrics(
        distance_to_food=distance,
        food_reached=food_reached,
        harm_contact=harm_contact,
        viability=viability,
    )
