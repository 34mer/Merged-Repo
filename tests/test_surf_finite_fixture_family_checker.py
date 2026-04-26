from __future__ import annotations

import json
from pathlib import Path

from scripts.check_surf_finite_fixture_family import TARGET_ID, run_check, write_result


def test_surf_finite_fixture_family_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS"
    assert result.counterexamples == []
    assert result.family_id == "SURF-FINITE-U-EQUATION-FAMILY-001"
    assert "not a mathematical proof" in result.status_boundary
    assert "not Formation Medium substrate evidence" in result.status_boundary
    assert result.support_summary["fixture_count"] == 3
    assert result.support_summary["has_multi_neighbor_fixture"] is True
    assert result.support_summary["has_disconnected_fixture"] is True
    chain = result.support_summary["fixtures"]["SURF-TINY-THREE-CURVE-CHAIN"]
    assert chain["derived_equations"]["b"] == "u_b + u_a * u_c - 1 = 0"
    assert chain["max_degree"] == 2


def test_surf_finite_fixture_family_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "CHK-SURF-FINITE-FIXTURE-FAMILY.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "surf_finite_fixture_family_check_v1"
    assert data["status"] == "PASS"
    assert data["counterexamples"] == []
    assert "SURF-TINY-DISJOINT-TWO-PAIRS" in data["support_summary"]["fixture_ids"]
    assert "SURF-TINY-THREE-CURVE-CHAIN" in data["support_summary"]["fixture_ids"]
