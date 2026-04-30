from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


@dataclass(frozen=True)
class WormConfig:
    """Configuration for a deterministic 302-neuron worm-like organism."""

    neurons: int = 302
    muscles: int = 24
    seed: int = 42
    dt: float = 0.05
    world_size: float = 10.0
    sensory_gain: float = 0.6
    recurrent_gain: float = 0.72
    muscle_gain: float = 0.18
    drag: float = 0.88
    max_speed: float = 0.08

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "WormConfig":
        allowed = {field.name for field in cls.__dataclass_fields__.values()}
        return cls(**{key: value for key, value in data.items() if key in allowed})
