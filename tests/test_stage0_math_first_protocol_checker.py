from __future__ import annotations

import json
from pathlib import Path

from scripts.check_stage0_math_first_protocol import TARGET_ID, run_check, write_result


def test_stage0_math_first_protocol_guard_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_LEDGER_VALIDATION"
    assert result.counterexamples == []
    assert result.support_summary["stage_count"] == 4
    assert result.support_summary["tool_class_count"] >= 9
    assert result.support_summary["next_required_math_attack"] == "STAGE0-FM-MINIMAL-STATIC-FORMAL-SKELETON"
    assert result.support_summary["global_doctrine_stage0_present"] is True
    assert result.support_summary["registry_stage0_file_present"] is True
    assert result.support_summary["roadmap_stage0_present"] is True
    assert "not a substitute for actual reasoning" in result.status_boundary


def test_stage0_math_first_protocol_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "LEDGER-STAGE0-MATH-FIRST-PROTOCOL.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "stage0_math_first_protocol_guard_v1"
    assert data["status"] == "PASS_LEDGER_VALIDATION"
    assert data["counterexamples"] == []
    assert "Gr_+(0,n)" in data["support_summary"]["current_static_spine"]
    assert data["support_summary"]["blocked_inference"]
