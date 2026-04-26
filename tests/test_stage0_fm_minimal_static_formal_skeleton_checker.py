from __future__ import annotations

import json
from pathlib import Path

from scripts.check_stage0_fm_minimal_static_formal_skeleton import (
    TARGET_ID,
    compute_finite_witnesses,
    finite_witness,
    route_sign,
    run_check,
    write_result,
)


def test_stage0_fm_minimal_static_formal_skeleton_guard_passes() -> None:
    result = run_check()
    assert result.target_id == TARGET_ID
    assert result.status == "PASS_FINITE_STATIC_MODEL_CHECKS"
    assert result.counterexamples == []
    assert result.support_summary["finite_range_checked"] == "2 <= n <= 8"
    assert result.support_summary["finite_witness_count"] == 7
    assert result.support_summary["formal_object_count"] >= 8
    assert result.support_summary["finite_check_target_count"] >= 5
    assert result.support_summary["stage1_target_count"] >= 4
    assert result.support_summary["sage_status_available"] is True
    assert result.support_summary["polymake_status_available"] is True
    assert "not source extraction" in result.status_boundary
    assert "not theorem status" in result.status_boundary
    assert "not native dynamics" in result.status_boundary


def test_stage0_finite_witnesses_have_expected_counts_and_parity() -> None:
    witnesses, failures = compute_finite_witnesses(2, 8)
    assert failures == []
    assert len(witnesses) == 7
    for witness in witnesses:
        assert witness.face_count == witness.expected_face_count
        assert witness.terminal_route_count == witness.expected_terminal_route_count
        assert witness.terminal_even_routes == witness.terminal_odd_routes
        assert witness.adjacent_swap_failures == 0
        assert witness.min_bulk_fiber_size == 2
        assert witness.max_bulk_fiber_size == 2


def test_stage0_route_sign_adjacent_swap_flips() -> None:
    route = (1, 3, 2, 4)
    swapped = (1, 2, 3, 4)
    assert route_sign(route) == -route_sign(swapped)


def test_stage0_specific_n3_witness() -> None:
    witness = finite_witness(3)
    assert witness.face_count == 7
    assert witness.face_count_by_dimension == {"0": 3, "1": 3, "2": 1}
    assert witness.terminal_route_count == 6
    assert witness.terminal_even_routes == 3
    assert witness.terminal_odd_routes == 3


def test_stage0_fm_minimal_static_formal_skeleton_artifact_shape(tmp_path: Path) -> None:
    result = run_check()
    path = tmp_path / "LEDGER-STAGE0-FM-MINIMAL-STATIC-FORMAL-SKELETON.json"
    write_result(path, result)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["target_id"] == TARGET_ID
    assert data["checker"] == "stage0_fm_minimal_static_formal_skeleton_guard_v1"
    assert data["status"] == "PASS_FINITE_STATIC_MODEL_CHECKS"
    assert data["counterexamples"] == []
    assert data["finite_witnesses"][-1]["n"] == 8
    assert data["finite_witnesses"][-1]["terminal_route_count"] == 40320
    assert data["support_summary"]["blocked_inference"]
