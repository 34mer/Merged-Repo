from __future__ import annotations

import json
from pathlib import Path

from scripts.check_pri002_scattering_native_source_candidates import TARGET_ID, run_check, write_result


def test_pri002_scattering_native_source_candidates_guard_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_LEDGER_VALIDATION"
    assert result.counterexamples == []
    assert "not source ingestion" in result.status_boundary
    assert "not scattering-native validation" in result.status_boundary
    assert result.support_summary["candidate_class_count"] == 4
    assert result.support_summary["source_candidate_count"] == 13
    assert result.support_summary["pri002_in_intake_criteria"] is True
    assert result.support_summary["scattering_track_role"] == "MANDATORY_COMPARATOR"


def test_pri002_scattering_native_source_candidates_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "LEDGER-PRI002-SCATTERING-NATIVE-SOURCE-CANDIDATES.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "pri002_scattering_native_source_candidates_guard_v1"
    assert data["status"] == "PASS_LEDGER_VALIDATION"
    assert data["counterexamples"] == []
    assert "SN-C1_POSITIVE_GEOMETRY_CANONICAL_FORMS" in data["support_summary"]["class_ids"]
    assert "SN-C3_PHYSICAL_SCATTERING_MATRIX_TOPOLOGY" in data["support_summary"]["class_ids"]
    assert "SN-SRC-013" in data["support_summary"]["source_ids"]
    assert data["support_summary"]["blocked_inference"]
