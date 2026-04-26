from __future__ import annotations

import json
from pathlib import Path

from scripts.check_surf_tiny_two_curve_fixture import TARGET_ID, run_check, write_result


def test_surf_tiny_two_curve_fixture_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS"
    assert result.counterexamples == []
    assert result.fixture_id == "SURF-TINY-TWO-CURVE-CROSSING"
    assert "not a mathematical proof" in result.status_boundary
    assert "not Formation Medium substrate evidence" in result.status_boundary
    assert result.support_summary["curve_count"] == 2
    assert result.support_summary["sample_solution_count"] == 3
    assert result.support_summary["derived_equations"]["a"] == "u_a + u_b - 1 = 0"
    assert result.support_summary["derived_equations"]["b"] == "u_b + u_a - 1 = 0"


def test_surf_tiny_two_curve_fixture_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "CHK-SURF-TINY-TWO-CURVE-FIXTURE.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "surf_tiny_two_curve_fixture_check_v1"
    assert data["status"] == "PASS"
    assert data["counterexamples"] == []
    assert data["support_summary"]["boundary_limit_count"] == 2
    assert data["support_summary"]["source_claim_ids"] == ["EXT-SURF-001", "EXT-SURF-COUNT-2023-001"]
