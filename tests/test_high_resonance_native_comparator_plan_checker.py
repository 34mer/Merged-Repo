from __future__ import annotations

import json
from pathlib import Path

from scripts.check_high_resonance_native_comparator_plan import TARGET_ID, run_check, write_result


def test_high_resonance_native_comparator_plan_guard_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_LEDGER_VALIDATION"
    assert result.counterexamples == []
    assert "CRBSM=mechanism-language" in result.status_boundary
    assert "Route A=hardware/proxy" in result.status_boundary
    assert "not substrate selection" in result.status_boundary
    assert result.support_summary["candidate_count"] == 4
    assert result.support_summary["candidate_roles"]["CRBSM"] == "MECHANISM"
    assert result.support_summary["candidate_roles"]["ROUTE_A"] == "ROUTE"
    assert result.support_summary["candidate_roles"]["SCATTERING_NATIVE"] == "COMPARATOR"
    assert result.support_summary["candidate_roles"]["HIGH_RESONANCE_NATIVE"] == "COMPARATOR"


def test_high_resonance_native_comparator_plan_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "LEDGER-HIGH-RESONANCE-NATIVE-COMPARATOR-PLAN.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "high_resonance_native_comparator_plan_guard_v1"
    assert data["status"] == "PASS_LEDGER_VALIDATION"
    assert data["counterexamples"] == []
    assert data["support_summary"]["required_review_count"] == 4
    assert data["support_summary"]["blocked_inference"]
