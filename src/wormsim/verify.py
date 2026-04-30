from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

import json
import numpy as np

from .checkpoint import config_hash, load_checkpoint
from .dynamics import run_steps


@dataclass(frozen=True)
class VerificationReport:
    status: str
    checkpoint_hash_matched: bool
    config_hash_matched: bool
    compared_steps: int
    max_trajectory_error: float
    tolerance: float

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def compare_from_checkpoints(
    checkpoint_a: str | Path,
    checkpoint_b: str | Path,
    steps: int = 1000,
    tolerance: float = 1e-12,
) -> VerificationReport:
    """Resume two checkpoints and compare deterministic continuations."""

    config_a, env_a, state_a = load_checkpoint(checkpoint_a)
    config_b, env_b, state_b = load_checkpoint(checkpoint_b)
    config_match = config_hash(config_a) == config_hash(config_b)

    env_a2, state_a2, traj_a = run_steps(config_a, env_a, state_a, steps)
    env_b2, state_b2, traj_b = run_steps(config_b, env_b, state_b, steps)
    del env_a2, state_a2, env_b2, state_b2

    max_error = float(np.max(np.abs(traj_a - traj_b))) if traj_a.size and traj_b.size else 0.0
    passed = config_match and max_error <= tolerance
    return VerificationReport(
        status="MIGRATION VERIFIED" if passed else "MIGRATION FAILED",
        checkpoint_hash_matched=Path(checkpoint_a).read_bytes() == Path(checkpoint_b).read_bytes(),
        config_hash_matched=config_match,
        compared_steps=steps,
        max_trajectory_error=max_error,
        tolerance=tolerance,
    )


def write_report(path: str | Path, report: VerificationReport) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(report.to_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
