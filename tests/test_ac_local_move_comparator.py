from __future__ import annotations

import json
from pathlib import Path

from scripts.check_ac_local_move_comparator import TARGET_ID, run_check, write_result


def test_ac_local_move_comparator_passes_partial_scope() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_PARTIAL_COMPARATOR"
    assert result.counterexamples == []
    assert result.compared_families == ["A", "C"]
    assert result.row_scope == ["R2", "R3"]
    assert result.observed_distinction["A_local_cover_mechanism_count"] == 1
    assert result.observed_distinction["C_local_cover_mechanism_count"] == 2
    assert result.observed_distinction["A_mechanisms"] == ["add_one_noncrossing_diagonal"]
    assert set(result.observed_distinction["C_mechanisms"]) == {"delete_bracket", "contract_minimal_bracket"}
    assert "not a realization-class theorem" in result.status_boundary


def test_ac_local_move_comparator_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "CMP-A-C-LOCAL-MOVE-BURDEN.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["comparator"] == "finite_artifact_local_move_burden_v1"
    assert data["status"] == "PASS_PARTIAL_COMPARATOR"
    assert data["counterexamples"] == []
    assert data["input_artifacts"] == [
        "formal_handoff/results/CHK-ASSOCIAHEDRON-UNIT-DESCENT.json",
        "formal_handoff/results/CHK-COSMO-MOVE-CLASSES.json",
        "formal_handoff/results/CHK-COSMO-NESTING-POSSET.json",
    ]
