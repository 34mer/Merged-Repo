from __future__ import annotations

import json
from pathlib import Path

from scripts.check_surf_polygon_chord_fixtures import TARGET_ID, run_check, write_result


def test_surf_polygon_chord_fixtures_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS"
    assert result.counterexamples == []
    assert result.fixture_id == "SURF-POLYGON-CHORDS-N4-7"
    assert "not a mathematical proof" in result.status_boundary
    assert "not full source-faithful surface curve enumeration" in result.status_boundary
    assert result.support_summary["total_polygon_cases"] == 4
    assert result.support_summary["cases"]["n_4"]["chord_count"] == 2
    assert result.support_summary["cases"]["n_5"]["chord_count"] == 5
    assert result.support_summary["cases"]["n_6"]["chord_count"] == 9
    assert result.support_summary["cases"]["n_7"]["chord_count"] == 14
    assert result.support_summary["max_degree_seen"] >= 4


def test_surf_polygon_chord_fixtures_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "CHK-SURF-POLYGON-CHORD-FIXTURES.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "surf_polygon_chord_fixtures_check_v1"
    assert data["status"] == "PASS"
    assert data["counterexamples"] == []
    assert data["support_summary"]["total_chords"] == 30
    assert data["support_summary"]["total_crossing_edges"] == 56
    assert data["support_summary"]["blocked_inference"]
