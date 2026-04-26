from __future__ import annotations

import json
from pathlib import Path

from scripts.check_scaffold_kinematic_shift import TARGET_ID, run_check, write_result


def test_scaffold_kinematic_shift_guard_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_SOURCE_COVERAGE"
    assert result.counterexamples == []
    assert "not a mathematical proof" in result.status_boundary
    assert "not substrate evidence" in result.status_boundary
    assert "not engineering readiness" in result.status_boundary
    assert result.support_summary["blocked_inference"]


def test_scaffold_kinematic_shift_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "CHK-SCAFFOLD-KINEMATIC-SHIFT.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "scaffold_kinematic_shift_ledger_guard_v1"
    assert data["status"] == "PASS_SOURCE_COVERAGE"
    assert data["counterexamples"] == []
    assert "EXT-HIDDEN-ZEROS-2023-001" in data["inspected_claim_ids"]
    assert "EXT-SCAFFOLD-001" in data["inspected_claim_ids"]
    assert "EXT-BACKUS-2025-001" in data["inspected_claim_ids"]
