from __future__ import annotations

import json
from pathlib import Path

from scripts.check_pri001_high_resonance_source_candidates import TARGET_ID, run_check, write_result


def test_pri001_high_resonance_source_candidates_guard_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_LEDGER_VALIDATION"
    assert result.counterexamples == []
    assert "not source ingestion" in result.status_boundary
    assert "not high-resonance validation" in result.status_boundary
    assert result.support_summary["candidate_class_count"] == 4
    assert result.support_summary["source_candidate_count"] == 11
    assert result.support_summary["pri001_in_intake_criteria"] is True
    assert result.support_summary["high_resonance_track_role"] == "POSSIBLE_BRIDGE_COMPARATOR"


def test_pri001_high_resonance_source_candidates_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "LEDGER-PRI001-HIGH-RESONANCE-SOURCE-CANDIDATES.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "pri001_high_resonance_source_candidates_guard_v1"
    assert data["status"] == "PASS_LEDGER_VALIDATION"
    assert data["counterexamples"] == []
    assert "HR-C3_CAVITY_MAGNON_POLARITON_AND_MAGNON_PHONON_HYBRIDS" in data["support_summary"]["class_ids"]
    assert "HR-SRC-011" in data["support_summary"]["source_ids"]
    assert data["support_summary"]["blocked_inference"]
