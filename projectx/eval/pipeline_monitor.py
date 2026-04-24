from __future__ import annotations

from typing import Any


def evaluate_pipeline_summary(summary: dict[str, Any]) -> dict[str, Any]:
    checks = summary.get("check_results", {})
    stresses = summary.get("stress_results", {})
    failures = [
        name for name, passed in {**checks, **stresses}.items() if passed is not True
    ]
    return {
        "run_id": summary.get("run_id"),
        "status": "passed" if not failures and summary.get("status") == "passed" else "failed",
        "failures": failures,
        "coherence": {
            "has_proposal": bool(summary.get("proposal_id")),
            "has_substrate": bool(summary.get("substrate_schema_id")),
            "has_family": bool(summary.get("family")),
        },
    }

