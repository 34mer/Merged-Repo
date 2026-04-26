from __future__ import annotations

import json
from pathlib import Path

from scripts.check_formation_medium_readiness import TARGET_ID, run_check, write_result


def test_formation_medium_readiness_guard_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_LEDGER_VALIDATION"
    assert result.counterexamples == []
    assert "not a proof" in result.status_boundary
    assert "not a substrate selection" in result.status_boundary
    assert "not engineering readiness" in result.status_boundary
    assert result.support_summary["blocked_inference"]


def test_formation_medium_readiness_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "LEDGER-FORMATION-MEDIUM-READINESS.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "formation_medium_readiness_scope_guard_v1"
    assert data["status"] == "PASS_LEDGER_VALIDATION"
    assert data["counterexamples"] == []
    assert data["support_summary"]["layer_states"]["RL4_PHYSICAL_SUBSTRATE"] == "NOT_READY"
    assert data["support_summary"]["layer_states"]["RL7_CAPITAL_READINESS"] == "EARLY_TECHNICAL_ROADMAP_ONLY"
