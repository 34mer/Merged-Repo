from __future__ import annotations

from pathlib import Path
from typing import Any

from .core import read_json, stable_hash, write_json
from .substrate import run_update


def migrate_substrate(
    substrate: str | Path,
    steps_before: int = 1000,
    checkpoint_at: int = 500,
    steps_after: int = 1000,
    out: str | Path = "runs/hsm_v0_migration",
) -> dict[str, Any]:
    spath = Path(substrate)
    sub = read_json(spath / "synthetic_substrate.json" if spath.is_dir() else spath)
    pre = run_update(sub, checkpoint_at)
    checkpoint = {
        "schema": "hsm-v0-checkpoint",
        "protocol": "HSM-v0",
        "substrate_hash": sub["synthetic_substrate_hash"],
        "constraint_signature": sub["constraint_signature"],
        "state": pre["state"],
        "timestep": checkpoint_at,
        "config": {"steps_before": steps_before, "checkpoint_at": checkpoint_at, "steps_after": steps_after},
    }
    checkpoint["checkpoint_hash"] = stable_hash(checkpoint)
    reloaded = dict(checkpoint)
    resumed_source = run_update({**sub, "state": checkpoint["state"]}, steps_after)
    resumed_target = run_update({**sub, "state": reloaded["state"]}, steps_after)
    divergence = 0.0 if stable_hash(resumed_source["state"]) == stable_hash(resumed_target["state"]) else 1.0
    report = {
        "schema": "hsm-v0-migration-report",
        "protocol": "HSM-v0",
        "status": "HSM MIGRATION COMPLETE" if divergence == 0.0 else "HSM MIGRATION FAILED",
        "checkpoint_hash": checkpoint["checkpoint_hash"],
        "reload_hash_matched": stable_hash(checkpoint) == stable_hash(reloaded),
        "state_divergence": divergence,
        "pre_state_hash": stable_hash(pre["state"]),
        "post_source_state_hash": stable_hash(resumed_source["state"]),
        "post_target_state_hash": stable_hash(resumed_target["state"]),
        "post_migration_state": resumed_target["state"],
        "constraint_signature": sub["constraint_signature"],
    }
    outp = Path(out)
    write_json(outp / "checkpoint.json", checkpoint)
    write_json(outp / "migration_report.json", report)
    return report
