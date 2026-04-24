from __future__ import annotations

import json
from pathlib import Path

from scripts.check_associahedron_unit_descent import TARGET_ID, run_check, write_result


def test_associahedron_unit_descent_checker_passes() -> None:
    result = run_check(range(4, 9))
    assert result.target_id == TARGET_ID
    assert result.status == "PASS"
    assert result.counterexamples == []
    assert result.n_range == [4, 5, 6, 7, 8]
    assert all(entry["all_covers_unit_rank"] for entry in result.per_n)
    assert all(entry["max_rank"] == entry["expected_max_rank"] for entry in result.per_n)


def test_associahedron_unit_descent_artifact_shape(tmp_path: Path) -> None:
    result = run_check(range(4, 7))
    path = tmp_path / "CHK-ASSOCIAHEDRON-UNIT-DESCENT.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "finite_noncrossing_chord_poset_v1"
    assert data["status"] == "PASS"
    assert data["counterexamples"] == []
    assert data["grading"] == "rank(face)=number_of_noncrossing_diagonals"
