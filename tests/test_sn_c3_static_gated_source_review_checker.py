from __future__ import annotations

import json
from pathlib import Path

from scripts.check_sn_c3_static_gated_source_review import TARGET_ID, run_check, write_result


def test_sn_c3_static_gated_source_review_guard_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_LEDGER_VALIDATION"
    assert result.counterexamples == []
    assert result.support_summary["classification"] == "USEFUL_NEGATIVE_CONTROL_AND_WEAK_OBSERVABLE_COMPARATOR"
    assert result.support_summary["continue_or_demote"] == "CONTINUE_AS_NEGATIVE_CONTROL_AND_OBSERVABLE_COMPARATOR_ONLY"
    assert result.support_summary["source_count"] == 2
    assert result.support_summary["pg_gate_count"] == 8
    assert result.support_summary["static_gate_count"] == 5
    assert result.support_summary["pri002_has_sn_c3"] is True
    assert "not scattering-native validation" in result.status_boundary


def test_sn_c3_static_gated_source_review_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "LEDGER-SN-C3-STATIC-GATED-SOURCE-REVIEW.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "sn_c3_static_gated_source_review_guard_v1"
    assert data["status"] == "PASS_LEDGER_VALIDATION"
    assert data["counterexamples"] == []
    assert data["support_summary"]["blocked_inference"]
