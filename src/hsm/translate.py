from __future__ import annotations

from pathlib import Path
from typing import Any

from .core import read_json, stable_hash, write_json


def translate_to_synthetic(source: str | Path, out: str | Path = "artifacts/synthetic_human_substrate_v0") -> dict[str, Any]:
    spath = Path(source)
    src = read_json(spath / "source_substrate.json" if spath.is_dir() else spath)
    synthetic = {
        "schema": "synthetic-human-substrate-v0",
        "protocol": "HSM-v0",
        "kind": "SyntheticHumanSubstrateV0",
        "source_substrate_hash": src["source_substrate_hash"],
        "constraint_signature": src["constraint_signature"],
        "state": dict(src["state"]),
        "constraint_satisfaction": dict(src["constraint_satisfaction"]),
        "synthetic_properties": {
            "stability": True,
            "coherence": True,
            "inspectability": True,
            "efficiency": True,
            "repairability": True,
            "migratability": True,
            "scalability": True,
        },
        "deterministic_update_rule": src["deterministic_update_rule"],
        "migratable_state_boundary": src["migratable_state_boundary"],
    }
    synthetic["synthetic_substrate_hash"] = stable_hash(synthetic)
    write_json(Path(out) / "synthetic_substrate.json", synthetic)
    return synthetic
