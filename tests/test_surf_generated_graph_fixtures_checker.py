from __future__ import annotations

import json
from pathlib import Path

from scripts.check_surf_generated_graph_fixtures import TARGET_ID, run_check, write_result


def test_surf_generated_graph_fixtures_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS"
    assert result.counterexamples == []
    assert result.fixture_id == "SURF-GENERATED-SIMPLE-GRAPHS-N1-4"
    assert "not a mathematical proof" in result.status_boundary
    assert "not Formation Medium substrate evidence" in result.status_boundary
    assert result.support_summary["total_graphs"] == 75
    assert result.support_summary["n_1_graphs"] == 1
    assert result.support_summary["n_2_graphs"] == 2
    assert result.support_summary["n_3_graphs"] == 8
    assert result.support_summary["n_4_graphs"] == 64
    assert result.support_summary["has_triangle_graph"] is True
    assert result.support_summary["has_degree_at_least_3_graph"] is True
    assert result.support_summary["has_graph_with_multiple_maximal_independent_sets"] is True


def test_surf_generated_graph_fixtures_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "CHK-SURF-GENERATED-GRAPH-FIXTURES.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "surf_generated_graph_fixtures_check_v1"
    assert data["status"] == "PASS"
    assert data["counterexamples"] == []
    assert data["support_summary"]["total_maximal_independent_witnesses"] > 75
    assert data["support_summary"]["max_degree_seen"] == 3
    assert data["support_summary"]["blocked_inference"]
