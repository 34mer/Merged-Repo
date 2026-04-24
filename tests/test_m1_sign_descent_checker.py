from __future__ import annotations

import json
from pathlib import Path

from scripts.check_m1_sign_descent import TARGET_ID, run_check, write_result


def test_m1_sign_descent_checker_passes_partial_finite_scope() -> None:
    result = run_check(range(3, 10))
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_PARTIAL"
    assert result.counterexamples == []
    assert result.n_range == [3, 4, 5, 6, 7, 8, 9]
    assert all(entry["all_covers_unit_flip_delta"] for entry in result.per_n)
    assert all(entry["global_sign_normalized_word_bijection"] for entry in result.per_n)
    assert all(entry["state_count"] == entry["expected_state_count"] for entry in result.per_n)
    assert all(entry["cover_count"] == entry["expected_cover_count"] for entry in result.per_n)
    assert "not a full amplituhedron theorem" in result.status_boundary


def test_m1_sign_descent_artifact_shape(tmp_path: Path) -> None:
    result = run_check(range(3, 7))
    path = tmp_path / "CHK-M1-SIGN-DESCENT.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "finite_global_sign_normalized_sign_flip_poset_v1"
    assert data["status"] == "PASS_PARTIAL"
    assert data["counterexamples"] == []
    assert data["grading"] == "rank(sign_flip_set)=number_of_adjacent_sign_changes"
    assert data["cover_relation"] == "lower < upper when upper is obtained from lower by adding exactly one adjacent sign-change edge"
