from __future__ import annotations

from pathlib import Path
from typing import Any

from .constraints import verify_constraint_packet
from .core import read_json, stable_hash, write_json
from .controls import run_controls
from .substrate import verify_substrate_constraints


def verify_hsm(
    source: str | Path,
    target: str | Path,
    migrated: str | Path,
    constraints: str | Path = "artifacts/hsm_constraints_v0/constraints.json",
    parent_chain: str | Path = "reports/hsm_parent_chain_verification.json",
    out: str | Path = "reports/hsm_v0_verification.json",
) -> dict[str, Any]:
    packet = read_json(constraints)
    chain = read_json(parent_chain)
    spath = Path(source)
    tpath = Path(target)
    mpath = Path(migrated)
    src = read_json(spath / "source_substrate.json" if spath.is_dir() else spath)
    syn = read_json(tpath / "synthetic_substrate.json" if tpath.is_dir() else tpath)
    mig = read_json(mpath / "migration_report.json" if mpath.is_dir() else mpath)

    cverify = verify_constraint_packet(packet)
    constraints_ok = cverify["status"] == "PASS"
    parent_ok = bool(chain.get("verified"))
    source_ok = verify_substrate_constraints(src, packet["constraint_packet_hash"], chain["parent_chain_hash"])
    synthetic_ok = verify_substrate_constraints(syn, packet["constraint_packet_hash"], chain["parent_chain_hash"])
    migration_ok = bool(mig.get("status") == "HSM MIGRATION COMPLETE" and mig.get("state_divergence") == 0.0 and mig.get("reload_hash_matched"))
    preserved = mig.get("constraint_signature", {}).get("constraint_packet_hash") == packet["constraint_packet_hash"]
    controls = run_controls(packet, chain, src, syn, mig)
    passed = all([constraints_ok, parent_ok, source_ok, synthetic_ok, migration_ok, preserved, controls["controls_failed_as_expected"]])

    report = {
        "claim": "Human substrate migration is empirically possible",
        "protocol": "HSM-v0",
        "status": "PASS" if passed else "FAIL",
        "human_constraints_verified": constraints_ok,
        "parent_primitive_chain_verified": parent_ok,
        "source_substrate_constructed": source_ok,
        "synthetic_substrate_constructed": synthetic_ok,
        "migration_verified": migration_ok,
        "state_divergence": float(mig.get("state_divergence", 1.0)),
        "post_migration_constraints_preserved": preserved,
        "controls_failed_as_expected": controls["controls_failed_as_expected"],
        "constraint_packet_hash": packet["constraint_packet_hash"],
        "parent_chain_hash": chain["parent_chain_hash"],
        "source_substrate_hash": src["source_substrate_hash"],
        "synthetic_substrate_hash": syn["synthetic_substrate_hash"],
        "checkpoint_hash": mig["checkpoint_hash"],
        "controls": controls["controls"],
    }
    report["verification_hash"] = stable_hash(report)
    write_json(out, report)
    return report
