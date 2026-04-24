from __future__ import annotations

import json
from pathlib import Path

from scripts.check_cosmohedron_move_classes import TARGET_ID, run_check, write_result


def test_cosmohedron_move_class_checker_has_two_move_classes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_PARTIAL"
    assert result.counterexamples == []
    assert result.total_deletion_moves > 0
    assert result.total_contraction_moves > 0
    assert all(entry["has_delete_bracket_moves"] for entry in result.tree_fixtures)
    assert all(entry["has_contract_minimal_bracket_moves"] for entry in result.tree_fixtures)


def test_cosmohedron_move_class_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "CHK-COSMO-MOVE-CLASSES.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "finite_bracketed_tree_cover_rule_v1"
    assert data["status"] == "PASS_PARTIAL"
    assert data["counterexamples"] == []
    assert "delete_bracket" in data["move_class_invariants"]
    assert "contract_minimal_bracket" in data["move_class_invariants"]
    assert "not the full" in data["status_boundary"]
