from __future__ import annotations

import json
from pathlib import Path

from scripts.check_cosmohedron_nesting_poset import TARGET_ID, run_check, write_result


def test_cosmohedron_nesting_poset_checker_passes_partial_finite_guard() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_PARTIAL"
    assert result.counterexamples == []
    assert result.total_states == 195
    assert result.total_cover_edges == 518
    assert result.total_delete_covers == 320
    assert result.total_contract_covers == 198
    assert all(entry["acyclic"] for entry in result.fixture_results)
    assert all(entry["antisymmetric_transitive_closure"] for entry in result.fixture_results)
    assert all(entry["all_covers_reduce_complexity"] for entry in result.fixture_results)


def test_cosmohedron_nesting_poset_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "CHK-COSMO-NESTING-POSSET.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "finite_prebracketing_poset_consistency_v1"
    assert data["status"] == "PASS_PARTIAL"
    assert data["counterexamples"] == []
    assert "not a proof of the cosmohedron face lattice" in data["status_boundary"]
    assert "the directed cover graph is acyclic" in data["checked_invariants"]
