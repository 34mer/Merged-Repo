from __future__ import annotations

import json
from pathlib import Path

from scripts.check_representation_comparator import TARGET_ID, run_check, write_result


def test_representation_comparator_guard_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_SOURCE_COVERAGE"
    assert result.counterexamples == []
    assert "not a mathematical proof" in result.status_boundary
    assert "not substrate evidence" in result.status_boundary
    assert "not engineering readiness" in result.status_boundary
    assert result.support_summary["blocked_inference"]


def test_representation_comparator_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "CHK-REPRESENTATION-COMPARATOR.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "representation_comparator_ledger_guard_v1"
    assert data["status"] == "PASS_SOURCE_COVERAGE"
    assert data["counterexamples"] == []
    assert "EXT-MOM-AMP-2019-001" in data["inspected_claim_ids"]
    assert "EXT-LOOP-MOM-AMP-2022-001" in data["inspected_claim_ids"]
