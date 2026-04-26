from __future__ import annotations

import json
from pathlib import Path

from scripts.check_pri005_ising_machine_source_candidates import TARGET_ID, run_check, write_result


def test_pri005_ising_machine_source_candidates_guard_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_LEDGER_VALIDATION"
    assert result.counterexamples == []
    assert "not source ingestion" in result.status_boundary
    assert "not Ising-machine validation" in result.status_boundary
    assert result.support_summary["candidate_class_count"] == 5
    assert result.support_summary["source_candidate_count"] == 10
    assert result.support_summary["pri005_in_intake_criteria"] is True
    assert result.support_summary["ising_track_role"] == "COMBINATORIAL_MACHINE_COMPARATOR"


def test_pri005_ising_machine_source_candidates_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "LEDGER-PRI005-ISING-MACHINE-SOURCE-CANDIDATES.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "pri005_ising_machine_source_candidates_guard_v1"
    assert data["status"] == "PASS_LEDGER_VALIDATION"
    assert data["counterexamples"] == []
    assert "IM-C1_COHERENT_OPTICAL_ISING_MACHINES" in data["support_summary"]["class_ids"]
    assert "IM-C3_PROBABILISTIC_SPINTRONIC_AND_PBIT_ISING_MACHINES" in data["support_summary"]["class_ids"]
    assert "IM-SRC-010" in data["support_summary"]["source_ids"]
    assert data["support_summary"]["blocked_inference"]
