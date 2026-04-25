from __future__ import annotations

import json
from pathlib import Path

from scripts.check_s2star_readout_source_coverage import TARGET_ID, run_check, write_result


def test_s2star_readout_source_coverage_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_SOURCE_COVERAGE"
    assert result.counterexamples == []
    assert "not a mathematical proof" in result.status_boundary
    assert result.support_summary["blocked_inference"]


def test_s2star_readout_source_coverage_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "CHK-S2STAR-READOUT-SOURCE-COVERAGE.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "ledger_s2star_source_coverage_guard_v1"
    assert data["status"] == "PASS_SOURCE_COVERAGE"
    assert data["counterexamples"] == []
    assert "EXT-POS-GEOM-2017-001" in data["inspected_claim_ids"]
