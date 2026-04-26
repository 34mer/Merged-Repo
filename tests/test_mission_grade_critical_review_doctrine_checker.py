from __future__ import annotations

import json
from pathlib import Path

from scripts.check_mission_grade_critical_review_doctrine import TARGET_ID, run_check, write_result


def test_mission_grade_critical_review_doctrine_guard_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_LEDGER_VALIDATION"
    assert result.counterexamples == []
    assert "reasoning beyond repo hygiene" in result.status_boundary
    assert "challenge to the mission" in result.status_boundary
    assert "not a substitute for actual judgment" in result.status_boundary
    assert result.support_summary["critical_item_count"] == 6
    assert result.support_summary["prework_question_count"] >= 8
    assert result.support_summary["allowed_challenge_count"] >= 8


def test_mission_grade_critical_review_doctrine_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "LEDGER-MISSION-GRADE-CRITICAL-REVIEW-DOCTRINE.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "mission_grade_critical_review_doctrine_guard_v1"
    assert data["status"] == "PASS_LEDGER_VALIDATION"
    assert data["counterexamples"] == []
    assert data["support_summary"]["global_doctrine_has_critical_rule"] is True
    assert data["support_summary"]["registry_has_critical_review_file"] is True
    assert data["support_summary"]["blocked_inference"]
