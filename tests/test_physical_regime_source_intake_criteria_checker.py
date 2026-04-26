from __future__ import annotations

import json
from pathlib import Path

from scripts.check_physical_regime_source_intake_criteria import TARGET_ID, run_check, write_result


def test_physical_regime_source_intake_criteria_guard_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_LEDGER_VALIDATION"
    assert result.counterexamples == []
    assert "not source ingestion" in result.status_boundary
    assert "not substrate selection" in result.status_boundary
    assert result.support_summary["gate_count"] == 8
    assert result.support_summary["track_count"] == 4
    assert result.support_summary["review_queue_count"] == 4
    assert result.support_summary["track_roles"]["TRACK_CRBSM"] == "MECHANISM_LANGUAGE"
    assert result.support_summary["track_roles"]["TRACK_ROUTE_A"] == "HARDWARE_PROXY_ROUTE"
    assert result.support_summary["track_roles"]["TRACK_SCATTERING_NATIVE"] == "MANDATORY_COMPARATOR"
    assert result.support_summary["track_roles"]["TRACK_HIGH_RESONANCE_NATIVE"] == "POSSIBLE_BRIDGE_COMPARATOR"


def test_physical_regime_source_intake_criteria_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "LEDGER-PHYSICAL-REGIME-SOURCE-INTAKE-CRITERIA.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "physical_regime_source_intake_criteria_guard_v1"
    assert data["status"] == "PASS_LEDGER_VALIDATION"
    assert data["counterexamples"] == []
    assert data["support_summary"]["roadmap_q5_mentions_source_intake"] is True
    assert data["support_summary"]["critical_review_prework_present"] is True
    assert data["support_summary"]["blocked_inference"]
