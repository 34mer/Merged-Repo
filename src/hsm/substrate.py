from __future__ import annotations

from pathlib import Path
from typing import Any

from .constraints import verify_constraint_packet
from .core import read_json, stable_hash, write_json


def _source_state(constraint_hash: str, parent_chain_hash: str) -> dict[str, float]:
    seed = int(stable_hash({"constraint": constraint_hash, "parent": parent_chain_hash})[:12], 16)
    return {
        "neuron_operator_state": (seed % 997) / 997.0,
        "microstructure_operator_state": ((seed // 7) % 991) / 991.0,
        "macrostate_operator_state": ((seed // 13) % 983) / 983.0,
        "structure_function_bridge_state": ((seed // 17) % 977) / 977.0,
        "migration_state": 0.0,
    }


def _update_state(state: dict[str, float], steps: int) -> dict[str, float]:
    s = dict(state)
    for _ in range(int(steps)):
        n = (0.91 * s["neuron_operator_state"] + 0.07 * s["macrostate_operator_state"] + 0.013) % 1.0
        m = (0.88 * s["microstructure_operator_state"] + 0.09 * s["structure_function_bridge_state"] + 0.021) % 1.0
        a = (0.86 * s["macrostate_operator_state"] + 0.11 * n + 0.017) % 1.0
        b = (0.90 * s["structure_function_bridge_state"] + 0.05 * m + 0.019) % 1.0
        s.update({
            "neuron_operator_state": n,
            "microstructure_operator_state": m,
            "macrostate_operator_state": a,
            "structure_function_bridge_state": b,
            "migration_state": s["migration_state"] + 1.0,
        })
    return s


def constraint_signature(packet: dict[str, Any], parent_chain: dict[str, Any]) -> dict[str, Any]:
    return {
        "constraint_packet_hash": packet["constraint_packet_hash"],
        "parent_chain_hash": parent_chain["parent_chain_hash"],
        "parent_hashes": parent_chain["parent_hashes"],
        "required_constraint_ids": [c["id"] for c in packet["constraints"] if c.get("required")],
    }


def build_source_substrate(constraints: str | Path, parent_chain: str | Path, out: str | Path = "artifacts/human_constrained_source_v0") -> dict[str, Any]:
    cpath = Path(constraints)
    packet = read_json(cpath / "constraints.json" if cpath.is_dir() else cpath)
    chain = read_json(parent_chain)
    v = verify_constraint_packet(packet)
    if v["status"] != "PASS" or not chain.get("verified"):
        raise ValueError("Cannot build source substrate without verified constraints and parent chain")
    sig = constraint_signature(packet, chain)
    initial = _source_state(packet["constraint_packet_hash"], chain["parent_chain_hash"])
    substrate = {
        "schema": "human-constrained-source-substrate-v0",
        "protocol": "HSM-v0",
        "kind": "HumanConstrainedSourceSubstrate",
        "constraint_signature": sig,
        "state": initial,
        "deterministic_update_rule": "hsm_v0_operator_update",
        "migratable_state_boundary": sorted(initial.keys()),
        "constraint_satisfaction": {
            "human_neuron_constraints": True,
            "human_microstructure_constraints": True,
            "human_macrostate_constraints": True,
            "structure_function_bridge_constraints": True,
        },
    }
    substrate["source_substrate_hash"] = stable_hash(substrate)
    write_json(Path(out) / "source_substrate.json", substrate)
    return substrate


def run_update(substrate: dict[str, Any], steps: int) -> dict[str, Any]:
    updated = dict(substrate)
    updated["state"] = _update_state(dict(substrate["state"]), steps)
    updated["runtime_hash"] = stable_hash(updated["state"])
    return updated


def verify_substrate_constraints(substrate: dict[str, Any], constraint_hash: str, parent_chain_hash: str) -> bool:
    sig = substrate.get("constraint_signature", {})
    return (
        sig.get("constraint_packet_hash") == constraint_hash
        and sig.get("parent_chain_hash") == parent_chain_hash
        and all(substrate.get("constraint_satisfaction", {}).values())
    )
