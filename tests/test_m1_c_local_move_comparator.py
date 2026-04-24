from __future__ import annotations

import json
from pathlib import Path

from scripts.check_m1_c_local_move_comparator import TARGET_ID, run_check, write_result


def test_m1_c_local_move_comparator_passes_partial_scope() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_PARTIAL_COMPARATOR"
    assert result.counterexamples == []
    assert result.compared_families == ["M1", "C"]
    assert result.row_scope == ["R2", "R3"]
    assert result.observed_distinction["M1_local_cover_mechanism_count"] == 1
    assert result.observed_distinction["C_local_cover_mechanism_count"] == 2
    assert result.observed_distinction["M1_mechanisms"] == ["add_one_adjacent_sign_change_edge"]
    assert set(result.observed_distinction["C_mechanisms"]) == {"delete_bracket", "contract_minimal_bracket"}
    assert "not a realization-class theorem" in result.status_boundary
    assert "not a full amplituhedron theorem" in result.status_boundary


def test_m1_c_local_move_comparator_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "CMP-M1-C-LOCAL-MOVE-BURDEN.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["comparator"] == "finite_artifact_local_move_burden_v1"
    assert data["status"] == "PASS_PARTIAL_COMPARATOR"
    assert data["counterexamples"] == []
    assert data["input_artifacts"] == [
        "formal_handoff/results/CHK-M1-SIGN-DESCENT.json",
        "formal_handoff/results/CHK-COSMO-MOVE-CLASSES.json",
        "formal_handoff/results/CHK-COSMO-NESTING-POSSET.json",
    ]
