from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Iterable

import numpy as np

from .config import WormConfig
from .environment import EnvironmentState
from .organism import WormState

TASK_NAMES = ("food", "harm", "perturb", "wall", "mixed")


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
        )
    if name == "wall":
        return TaskSpec(
            name=name,
            food_position=(0.82 * size, 0.52 * size),
            start_position=(0.08 * size, 0.5 * size),
            wall_start=True,
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


def environment_for_task(task: TaskSpec) -> EnvironmentState:
    return EnvironmentState(food_position=task.food_position)


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
    return perturbed


def task_metrics(config: WormConfig, task: TaskSpec, position: np.ndarray) -> TaskMetrics:
    food = np.array(task.food_position, dtype=np.float64)
    distance = float(np.linalg.norm(food - position))
    food_reached = 1.0 if distance <= 0.75 else 0.0
    harm_contact = 0.0
    if task.harm_center is not None:
        harm = np.array(task.harm_center, dtype=np.float64)
        harm_contact = 1.0 if float(np.linalg.norm(harm - position)) <= task.harm_radius else 0.0
    wall_margin = min(position[0], position[1], config.world_size - position[0], config.world_size - position[1])
    wall_penalty = 1.0 if wall_margin < 0.25 else 0.0
    viability = float(np.clip(1.0 - 0.18 * distance / config.world_size - 0.60 * harm_contact - 0.20 * wall_penalty, 0.0, 1.0))
    return TaskMetrics(
        distance_to_food=distance,
        food_reached=food_reached,
        harm_contact=harm_contact,
        viability=viability,
    )
