from __future__ import annotations

import json
from pathlib import Path

from scripts.check_pre_spacetime_static_geometry_spine import TARGET_ID, run_check, write_result


def test_pre_spacetime_static_geometry_spine_guard_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_LEDGER_VALIDATION"
    assert result.counterexamples == []
    assert "Gr_+(0,n) terminal atom" in result.status_boundary
    assert "Gr_+(1,n) static simplex tower" in result.status_boundary
    assert "not source extraction" in result.status_boundary
    assert result.support_summary["static_layer_count"] == 5
    assert result.support_summary["red_team_finding_count"] == 4
    assert result.support_summary["static_gate_question_count"] >= 7
    assert "SN_C3" in result.support_summary["impact_targets"]
    assert "PRI005_ISING" in result.support_summary["impact_targets"]


def test_pre_spacetime_static_geometry_spine_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "LEDGER-PRE-SPACETIME-STATIC-GEOMETRY-SPINE.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "pre_spacetime_static_geometry_spine_guard_v1"
    assert data["status"] == "PASS_LEDGER_VALIDATION"
    assert data["counterexamples"] == []
    assert "9658-9972" in data["support_summary"]["prior_gpt_line_ranges"]
    assert data["support_summary"]["blocked_inference"]
