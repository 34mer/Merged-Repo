from __future__ import annotations

from pathlib import Path
from typing import Any

from substrate.reports import build_ladder

from .core import stable_hash, write_json, read_json


def verify_parent_chain(out: str | Path = "reports/hsm_parent_chain_verification.json") -> dict[str, Any]:
    primitives = build_ladder()
    required_layers = ["hydrogen", "molecule", "ion_water", "membrane", "channel", "neuron", "synthetic_neuron"]
    layers = [p["layer"] for p in primitives]
    verified = all(str(p.get("verification", {}).get("status", "")).endswith("VERIFIED") for p in primitives)
    layer_ok = all(layer in layers for layer in required_layers)
    chain_hash = stable_hash([p["hash"] for p in primitives])
    report = {
        "schema": "hsm-parent-chain-verification-v0",
        "status": "BOUNDARY-TO-BIOLOGY PRIMITIVE CHAIN VERIFIED" if verified and layer_ok else "PARENT CHAIN FAILED",
        "verified": bool(verified and layer_ok),
        "primitive_count": len(primitives),
        "parent_hashes": [p["hash"] for p in primitives],
        "synthetic_neuron_hash": primitives[-1]["hash"],
        "worm_scale_migration_protocol_hash": stable_hash({"protocol": "primitive checkpoint/hash/migrate/verify", "version": "v0"}),
        "parent_chain_hash": chain_hash,
    }
    write_json(out, report)
    return report


def load_or_verify_parent_chain(path: str | Path | None = None) -> dict[str, Any]:
    if path and Path(path).exists():
        return read_json(path)
    return verify_parent_chain()
