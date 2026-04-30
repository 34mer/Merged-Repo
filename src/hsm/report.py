from __future__ import annotations

from pathlib import Path
from typing import Any


def write_summary(report: dict[str, Any], out: str | Path = "reports/hsm_v0_summary.md") -> str:
    lines = [
        "# HSM-v0 Summary",
        "",
        f"Status: {report['status']}",
        f"Protocol: {report['protocol']}",
        "",
        "## Gates",
        "",
        f"- Human constraint packet: {report['human_constraints_verified']}",
        f"- Parent primitive chain: {report['parent_primitive_chain_verified']}",
        f"- Human-constrained source substrate: {report['source_substrate_constructed']}",
        f"- Synthetic substrate: {report['synthetic_substrate_constructed']}",
        f"- Migration verified: {report['migration_verified']}",
        f"- State divergence: {report['state_divergence']}",
        f"- Post-migration constraints preserved: {report['post_migration_constraints_preserved']}",
        f"- Controls failed as expected: {report['controls_failed_as_expected']}",
        "",
        "## Claim boundary",
        "",
        "This is a constructive demonstration that a human-constrained substrate object can undergo the migration operation under HSM-v0. It is not a claim that a human person has been migrated.",
        "",
    ]
    path = Path(out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return str(path)
