from __future__ import annotations

from typing import Any

from .burden_metrics import compute_cps, compute_drift_rate, compute_mlli, compute_rbr, compute_scs
from .coherence_checks import detect_failure_signatures


def build_report(session_data: dict[str, Any]) -> dict[str, Any]:
    failures = detect_failure_signatures(session_data)
    session_data = dict(session_data)
    session_data["failures"] = failures
    metrics = {
        "RBR": compute_rbr(session_data),
        "MLLI": compute_mlli(session_data),
        "SCS": compute_scs(session_data),
        "DR": compute_drift_rate(session_data),
        "CPS": compute_cps(session_data),
    }
    return {
        "run_id": session_data.get("run_id", "unknown"),
        "metrics": metrics,
        "failures": failures,
        "drift_events": session_data.get("drift_events", []),
    }
