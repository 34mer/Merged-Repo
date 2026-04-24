from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

TARGET_ID = "CMP-M1-C-LOCAL-MOVE-BURDEN"
ROOT = Path(__file__).resolve().parents[1]
M1_ARTIFACT = "formal_handoff/results/CHK-M1-SIGN-DESCENT.json"
C_MOVE_ARTIFACT = "formal_handoff/results/CHK-COSMO-MOVE-CLASSES.json"
C_NESTING_ARTIFACT = "formal_handoff/results/CHK-COSMO-NESTING-POSSET.json"


@dataclass(frozen=True)
class M1CLocalMoveComparatorResult:
    target_id: str
    comparator: str
    status: str
    input_artifacts: list[str]
    compared_families: list[str]
    row_scope: list[str]
    observed_distinction: dict[str, object]
    checks: list[dict[str, object]]
    counterexamples: list[dict[str, object]]
    status_boundary: str


def read_artifact(relative_path: str) -> dict:
    path = ROOT / relative_path
    if not path.exists():
        raise FileNotFoundError(relative_path)
    return json.loads(path.read_text(encoding="utf-8"))


def pass_check(name: str, detail: str) -> dict[str, object]:
    return {"name": name, "status": "PASS", "detail": detail}


def fail(name: str, detail: str) -> dict[str, object]:
    return {"name": name, "detail": detail}


def run_check() -> M1CLocalMoveComparatorResult:
    checks: list[dict[str, object]] = []
    counterexamples: list[dict[str, object]] = []

    try:
        m1 = read_artifact(M1_ARTIFACT)
        c_move = read_artifact(C_MOVE_ARTIFACT)
        c_nesting = read_artifact(C_NESTING_ARTIFACT)
    except FileNotFoundError as exc:
        return M1CLocalMoveComparatorResult(
            target_id=TARGET_ID,
            comparator="finite_artifact_local_move_burden_v1",
            status="FAILED",
            input_artifacts=[M1_ARTIFACT, C_MOVE_ARTIFACT, C_NESTING_ARTIFACT],
            compared_families=["M1", "C"],
            row_scope=["R2", "R3"],
            observed_distinction={},
            checks=[],
            counterexamples=[fail("missing_input_artifact", str(exc))],
            status_boundary="Comparator failed before evidence evaluation because an input artifact was missing.",
        )

    if m1.get("target_id") != "CHK-M1-SIGN-DESCENT" or m1.get("status") != "PASS_PARTIAL":
        counterexamples.append(fail("M1_artifact_status", "M1 sign-descent artifact is not PASS_PARTIAL"))
    else:
        checks.append(pass_check("M1_artifact_status", "M1 sign-descent artifact has PASS_PARTIAL finite status"))

    if m1.get("counterexamples") != []:
        counterexamples.append(fail("M1_counterexamples", "M1 sign-descent artifact contains counterexamples"))
    else:
        checks.append(pass_check("M1_counterexamples", "M1 sign-descent artifact has no counterexamples"))

    if not all(entry.get("all_covers_unit_flip_delta") is True for entry in m1.get("per_n", [])):
        counterexamples.append(fail("M1_unit_flip_cover_property", "Not all M1 finite covers add one adjacent sign-change edge"))
    else:
        checks.append(pass_check("M1_unit_flip_cover_property", "All checked M1 covers add exactly one adjacent sign-change edge"))

    if not all(entry.get("global_sign_normalized_word_bijection") is True for entry in m1.get("per_n", [])):
        counterexamples.append(fail("M1_sign_word_bijection", "M1 finite model failed global-sign-normalized word bijection"))
    else:
        checks.append(pass_check("M1_sign_word_bijection", "M1 finite model preserves global-sign-normalized word/sign-flip-set bijection"))

    if "not" not in m1.get("status_boundary", "").lower() or "amplituhedron theorem" not in m1.get("status_boundary", "").lower():
        counterexamples.append(fail("M1_partial_boundary", "M1 artifact does not carry explicit non-theorem boundary"))
    else:
        checks.append(pass_check("M1_partial_boundary", "M1 artifact explicitly retains non-theorem/partial boundary"))

    if c_move.get("target_id") != "CHK-COSMO-MOVE-CLASSES" or c_move.get("status") != "PASS_PARTIAL":
        counterexamples.append(fail("C_move_artifact_status", "C move-class artifact is not PASS_PARTIAL"))
    else:
        checks.append(pass_check("C_move_artifact_status", "C move-class artifact has PASS_PARTIAL finite status"))

    if c_move.get("counterexamples") != []:
        counterexamples.append(fail("C_move_counterexamples", "C move-class artifact contains counterexamples"))
    else:
        checks.append(pass_check("C_move_counterexamples", "C move-class artifact has no counterexamples"))

    move_invariants = c_move.get("move_class_invariants", {})
    if not {"delete_bracket", "contract_minimal_bracket"} <= set(move_invariants):
        counterexamples.append(fail("C_two_move_classes", "C move artifact does not expose both source-stated move classes"))
    else:
        checks.append(pass_check("C_two_move_classes", "C finite artifact exposes delete-bracket and contract-minimal-bracket move mechanisms"))

    if c_nesting.get("target_id") != "CHK-COSMO-NESTING-POSSET" or c_nesting.get("status") != "PASS_PARTIAL":
        counterexamples.append(fail("C_nesting_artifact_status", "C nesting artifact is not PASS_PARTIAL"))
    else:
        checks.append(pass_check("C_nesting_artifact_status", "C nesting artifact has PASS_PARTIAL finite status"))

    if c_nesting.get("counterexamples") != []:
        counterexamples.append(fail("C_nesting_counterexamples", "C nesting artifact contains counterexamples"))
    else:
        checks.append(pass_check("C_nesting_counterexamples", "C nesting artifact has no counterexamples"))

    c_boundary_text = " ".join([c_move.get("status_boundary", ""), c_nesting.get("status_boundary", "")]).lower()
    if "not" not in c_boundary_text or "theorem" not in c_boundary_text:
        counterexamples.append(fail("C_partial_boundary", "C partial artifacts do not carry explicit non-theorem boundary"))
    else:
        checks.append(pass_check("C_partial_boundary", "C artifacts explicitly retain non-theorem/partial boundaries"))

    observed = {
        "M1_local_cover_mechanism_count": 1,
        "M1_mechanisms": ["add_one_adjacent_sign_change_edge"],
        "M1_checked_n_range": m1.get("n_range", []),
        "C_local_cover_mechanism_count": 2,
        "C_mechanisms": ["delete_bracket", "contract_minimal_bracket"],
        "C_move_fixture_count": len(c_move.get("tree_fixtures", [])),
        "C_nesting_fixture_count": len(c_nesting.get("fixture_results", [])),
        "finite_distinction": "one binary sign-descent cover mechanism in M1 baseline versus two source-stated local cover mechanisms in C baseline",
    }

    return M1CLocalMoveComparatorResult(
        target_id=TARGET_ID,
        comparator="finite_artifact_local_move_burden_v1",
        status="PASS_PARTIAL_COMPARATOR" if not counterexamples else "FAILED",
        input_artifacts=[M1_ARTIFACT, C_MOVE_ARTIFACT, C_NESTING_ARTIFACT],
        compared_families=["M1", "C"],
        row_scope=["R2", "R3"],
        observed_distinction=observed,
        checks=checks,
        counterexamples=counterexamples,
        status_boundary="PASS_PARTIAL_COMPARATOR finite evidence only. This consumes finite baseline artifacts and records a bounded M1/C local-move-burden distinction. It is not a realization-class theorem, not a full amplituhedron theorem, not an all-n proof, not an R13 equality-layer result, and not physics/engineering evidence.",
    )


def write_result(path: Path, result: M1CLocalMoveComparatorResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(result), indent=2, sort_keys=True), encoding="utf-8")


def main() -> None:
    result = run_check()
    write_result(Path("formal_handoff/results/CMP-M1-C-LOCAL-MOVE-BURDEN.json"), result)
    print(json.dumps(asdict(result), indent=2, sort_keys=True))
    if result.status == "FAILED":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
