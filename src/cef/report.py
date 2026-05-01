from __future__ import annotations

from pathlib import Path
from typing import Any


def write_summary(report: dict[str, Any], out: str | Path = "reports/cef_v0_summary.md") -> str:
    path = Path(out)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# CEF-v0 Protocol Readiness Summary",
        "",
        f"Status: {report['status']}",
        f"Protocol: {report['protocol']}",
        f"Individual id: {report.get('individual_id')}",
        "",
        "## Gates",
        "",
        f"- Real organism constraints loaded: {report['real_organism_constraints_loaded']}",
        f"- Construction/verifier independence: {report['construction_verifier_independence']['status']}",
        f"- Synthetic worm runtime constrained: {report['synthetic_worm_runtime_constrained']}",
        f"- Held-out perturbation verification: {report['heldout_perturbation_verification']['status']}",
        f"- Controls failed as expected: {report['controls_failed_as_expected']}",
        "",
        "## Claim boundary",
        "",
        "CEF-v0 does not prove worm migration. It proves the computational migration stack can be forced by one individual-organism capture packet under a construction/verifier split.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    return str(path)
