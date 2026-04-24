from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

TARGET_ID = "CMP-A-C-LOCAL-MOVE-BURDEN"
ROOT = Path(__file__).resolve().parents[1]
A_ARTIFACT = "formal_handoff/results/CHK-ASSOCIAHEDRON-UNIT-DESCENT.json"
C_MOVE_ARTIFACT = "formal_handoff/results/CHK-COSMO-MOVE-CLASSES.json"
C_NESTING_ARTIFACT = "formal_handoff/results/CHK-COSMO-NESTING-POSSET.json"


@dataclass(frozen=True)
class ACLocalMoveComparatorResult:
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


def run_check() -> ACLocalMoveComparatorResult:
    checks: list[dict[str, object]] = []
    counterexamples: list[dict[str, object]] = []

    try:
        a = read_artifact(A_ARTIFACT)
        c_move = read_artifact(C_MOVE_ARTIFACT)
        c_nesting = read_artifact(C_NESTING_ARTIFACT)
    except FileNotFoundError as exc:
        return ACLocalMoveComparatorResult(
            target_id=TARGET_ID,
            comparator="finite_artifact_local_move_burden_v1",
            status="FAILED",
            input_artifacts=[A_ARTIFACT, C_MOVE_ARTIFACT, C_NESTING_ARTIFACT],
            compared_families=["A", "C"],
            row_scope=["R2", "R3"],
            observed_distinction={},
            checks=[],
            counterexamples=[fail("missing_input_artifact", str(exc))],
            status_boundary="Comparator failed before evidence evaluation because an input artifact was missing.",
        )

    if a.get("target_id") != "CHK-ASSOCIAHEDRON-UNIT-DESCENT" or a.get("status") != "PASS":
        counterexamples.append(fail("A_artifact_status", "A baseline artifact is not a PASS unit-descent result"))
    else:
        checks.append(pass_check("A_artifact_status", "A baseline has PASS finite check status"))

    if a.get("counterexamples") != []:
        counterexamples.append(fail("A_counterexamples", "A baseline contains counterexamples"))
    else:
        checks.append(pass_check("A_counterexamples", "A baseline has no counterexamples"))

    if not all(entry.get("all_covers_unit_rank") is True for entry in a.get("per_n", [])):
        counterexamples.append(fail("A_unit_cover_property", "Not all A finite covers have unit rank"))
    else:
        checks.append(pass_check("A_unit_cover_property", "All checked A covers add exactly one noncrossing diagonal"))

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

    boundary_text = " ".join([c_move.get("status_boundary", ""), c_nesting.get("status_boundary", "")]).lower()
    if "not" not in boundary_text or "theorem" not in boundary_text:
        counterexamples.append(fail("C_partial_boundary", "C partial artifacts do not carry explicit non-theorem boundary"))
    else:
        checks.append(pass_check("C_partial_boundary", "C artifacts explicitly retain non-theorem/partial boundaries"))

    observed = {
        "A_local_cover_mechanism_count": 1,
        "A_mechanisms": ["add_one_noncrossing_diagonal"],
        "A_checked_n_range": a.get("n_range", []),
        "C_local_cover_mechanism_count": 2,
        "C_mechanisms": ["delete_bracket", "contract_minimal_bracket"],
        "C_move_fixture_count": len(c_move.get("tree_fixtures", [])),
        "C_nesting_fixture_count": len(c_nesting.get("fixture_results", [])),
        "finite_distinction": "one local cover mechanism in A baseline versus two source-stated local cover mechanisms in C baseline",
    }

    return ACLocalMoveComparatorResult(
        target_id=TARGET_ID,
        comparator="finite_artifact_local_move_burden_v1",
        status="PASS_PARTIAL_COMPARATOR" if not counterexamples else "FAILED",
        input_artifacts=[A_ARTIFACT, C_MOVE_ARTIFACT, C_NESTING_ARTIFACT],
        compared_families=["A", "C"],
        row_scope=["R2", "R3"],
        observed_distinction=observed,
        checks=checks,
        counterexamples=counterexamples,
        status_boundary="PASS_PARTIAL_COMPARATOR finite evidence only. This consumes finite baseline artifacts and records a bounded A/C local-move-burden distinction. It is not a realization-class theorem, not an all-n proof, not an R13 equality-layer result, and not physics/engineering evidence.",
    )


def write_result(path: Path, result: ACLocalMoveComparatorResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(result), indent=2, sort_keys=True), encoding="utf-8")


def main() -> None:
    result = run_check()
    write_result(Path("formal_handoff/results/CMP-A-C-LOCAL-MOVE-BURDEN.json"), result)
    print(json.dumps(asdict(result), indent=2, sort_keys=True))
    if result.status == "FAILED":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
