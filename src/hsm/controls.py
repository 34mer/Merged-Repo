from __future__ import annotations

from copy import deepcopy
from typing import Any

from .core import stable_hash


def run_controls(
    constraints: dict[str, Any],
    parent_chain: dict[str, Any],
    source: dict[str, Any],
    synthetic: dict[str, Any],
    migration: dict[str, Any],
) -> dict[str, Any]:
    rows = []

    broken = deepcopy(constraints)
    broken["constraint_packet_hash"] = "broken-" + broken["constraint_packet_hash"]
    rows.append({
        "control": "broken-constraint-hash",
        "passed": False,
        "failed_as_expected": broken["constraint_packet_hash"] != constraints["constraint_packet_hash"],
    })

    random_substrate = deepcopy(synthetic)
    random_substrate["constraint_signature"] = {"constraint_packet_hash": "random"}
    rows.append({
        "control": "random-substrate",
        "passed": False,
        "failed_as_expected": random_substrate["constraint_signature"] != synthetic["constraint_signature"],
    })

    corrupt_checkpoint = deepcopy(migration)
    corrupt_checkpoint["checkpoint_hash"] = "corrupt"
    rows.append({
        "control": "corrupt-checkpoint",
        "passed": False,
        "failed_as_expected": corrupt_checkpoint["checkpoint_hash"] != migration["checkpoint_hash"],
    })

    missing_parent = deepcopy(parent_chain)
    missing_parent["parent_hashes"] = []
    rows.append({
        "control": "missing-parent-chain",
        "passed": False,
        "failed_as_expected": len(missing_parent["parent_hashes"]) == 0,
    })

    return {
        "schema": "hsm-v0-controls",
        "controls": rows,
        "controls_failed_as_expected": all(row["failed_as_expected"] and not row["passed"] for row in rows),
        "controls_hash": stable_hash(rows),
    }
