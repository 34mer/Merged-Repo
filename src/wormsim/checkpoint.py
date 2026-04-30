from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

try:
    import blake3  # type: ignore
except ImportError:  # pragma: no cover - fallback keeps tests usable without optional wheel
    blake3 = None
    import hashlib

from .config import WormConfig
from .environment import EnvironmentState
from .organism import WormState


SCHEMA_VERSION = "wormsim-checkpoint-v1"


def _canonical_json(data: dict[str, Any]) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def file_hash(path: str | Path) -> str:
    data = Path(path).read_bytes()
    if blake3 is not None:
        return blake3.blake3(data).hexdigest()
    return "sha256:" + hashlib.sha256(data).hexdigest()


def config_hash(config: WormConfig) -> str:
    data = _canonical_json(config.to_dict()).encode("utf-8")
    if blake3 is not None:
        return blake3.blake3(data).hexdigest()
    return "sha256:" + hashlib.sha256(data).hexdigest()


def save_checkpoint(path: str | Path, config: WormConfig, env: EnvironmentState, state: WormState) -> str:
    """Save the complete state required for exact continuation and return its hash."""

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    metadata = {
        "schema": SCHEMA_VERSION,
        "config": config.to_dict(),
        "environment": env.to_dict(),
        "rng_state": state.rng_state,
        "step": state.step,
        "orientation": state.orientation,
    }
    np.savez_compressed(
        path,
        metadata=np.array(_canonical_json(metadata)),
        neuron_state=state.neuron_state.astype(np.float64),
        muscle_state=state.muscle_state.astype(np.float64),
        position=state.position.astype(np.float64),
        velocity=state.velocity.astype(np.float64),
    )
    digest = file_hash(path)
    path.with_suffix(path.suffix + ".blake3").write_text(digest + "\n", encoding="utf-8")
    return digest


def load_checkpoint(path: str | Path) -> tuple[WormConfig, EnvironmentState, WormState]:
    with np.load(Path(path), allow_pickle=False) as data:
        metadata = json.loads(str(data["metadata"]))
        if metadata.get("schema") != SCHEMA_VERSION:
            raise ValueError(f"Unsupported checkpoint schema: {metadata.get('schema')}")
        config = WormConfig.from_dict(metadata["config"])
        env = EnvironmentState.from_dict(metadata["environment"])
        state = WormState(
            step=int(metadata["step"]),
            neuron_state=data["neuron_state"].astype(np.float64),
            muscle_state=data["muscle_state"].astype(np.float64),
            position=data["position"].astype(np.float64),
            velocity=data["velocity"].astype(np.float64),
            orientation=float(metadata["orientation"]),
            rng_state=metadata["rng_state"],
        )
        return config, env, state


def verify_hash(path: str | Path, expected: str) -> bool:
    return file_hash(path) == expected.strip()
