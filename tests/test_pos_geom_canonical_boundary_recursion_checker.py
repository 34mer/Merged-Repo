from __future__ import annotations

import json
from pathlib import Path

from scripts.check_pos_geom_canonical_boundary_recursion import TARGET_ID, run_check, write_result


def test_pos_geom_canonical_boundary_recursion_source_guard_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_SOURCE_COVERAGE"
    assert result.counterexamples == []
    assert "not a mathematical proof" in result.status_boundary
    assert "not substrate evidence" in result.status_boundary
    assert result.support_summary["blocked_inference"]


def test_pos_geom_canonical_boundary_recursion_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "CHK-POS-GEOM-CANONICAL-BOUNDARY-RECURSION.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "pos_geom_canonical_boundary_recursion_source_guard_v1"
    assert data["status"] == "PASS_SOURCE_COVERAGE"
    assert data["counterexamples"] == []
    assert "EXT-POS-GEOM-2017-001" in data["inspected_claim_ids"]
