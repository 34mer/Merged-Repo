
from __future__ import annotations

import itertools
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "LEDGER-STAGE0-FM-MINIMAL-STATIC-FORMAL-SKELETON"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
SKELETON_JSON = ROOT / "research_ledger" / "STAGE0_FM_MINIMAL_STATIC_FORMAL_SKELETON.json"
SKELETON_MD = ROOT / "research_ledger" / "STAGE0_FM_MINIMAL_STATIC_FORMAL_SKELETON.md"
STAGE0_PROTOCOL_JSON = ROOT / "research_ledger" / "FORMATION_MEDIUM_STAGE0_MATH_FIRST_PROTOCOL.json"
STATIC_SPINE_JSON = ROOT / "research_ledger" / "PRE_SPACETIME_STATIC_GEOMETRY_SPINE.json"
ROADMAP_JSON = ROOT / "research_ledger" / "FORMATION_MEDIUM_TECHNICAL_ROADMAP.json"

REQUIRED_STATUSES = {
    "GENERATED", "OPEN", "MATH_FIRST", "FINITE_STATIC_MODEL",
    "NOT_SOURCE_EXTRACTED", "NOT_THEOREM", "NOT_PHYSICS",
}
REQUIRED_ROLES = {"STAGE0", "STATIC_GEOMETRY", "FORMAL_SKELETON", "RED_TEAM", "NEGATIVE_CONTROL"}
REQUIRED_OBJECTS = {
    "OBJ_LABEL_SET", "OBJ_TERMINAL_ATOM", "OBJ_STATIC_SIMPLEX_FACE", "OBJ_RESIDUE_DELETION",
    "OBJ_ORDERED_ROUTE_SIGN", "OBJ_READOUT_MAP", "OBJ_BULK_COVER", "OBJ_SETTLING_RELATION",
}
REQUIRED_CHECKS = {
    "FC1_FACE_COUNTS", "FC2_RESIDUE_CLOSURE_AND_ACYCLICITY", "FC3_ROUTE_PARITY_COHERENCE",
    "FC4_NON_FAITHFUL_BULK_COVER", "FC5_TERMINAL_ROUTE_COUNT",
}
REQUIRED_STAGE1_TARGETS = {
    "STAGE1-STATIC-FACE-TYPE", "STAGE1-RESIDUE-DECREASES-RANK",
    "STAGE1-ADJACENT-SWAP-FLIPS-SIGN", "STAGE1-BULK-READOUT-NONFAITHFUL",
}
REQUIRED_MD_TERMS = [
    "finite static support/residue surrogate", "Gr_+(0,n)", "Gr_+(1,n)",
    "OBJ_ORDERED_ROUTE_SIGN", "OBJ_BULK_COVER", "directed residue descent",
    "PASS_FINITE_STATIC_MODEL_CHECKS", "not native dynamics", "polymake 4.11", "SageMath 9.5",
]


@dataclass(frozen=True)
class Stage0FiniteWitness:
    n: int
    face_count: int
    expected_face_count: int
    face_count_by_dimension: dict[str, int]
    expected_by_dimension: dict[str, int]
    residue_step_count: int
    residue_step_failures: list[str]
    terminal_route_count: int
    expected_terminal_route_count: int
    terminal_even_routes: int
    terminal_odd_routes: int
    adjacent_swap_failures: int
    min_bulk_fiber_size: int
    max_bulk_fiber_size: int


@dataclass(frozen=True)
class Stage0MinimalStaticFormalSkeletonResult:
    target_id: str
    checker: str
    status: str
    inspected_files: list[str]
    support_summary: dict[str, Any]
    finite_witnesses: list[dict[str, Any]]
    counterexamples: list[dict[str, Any]]
    status_boundary: str


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def subsets(labels: tuple[int, ...]) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for size in range(1, len(labels) + 1):
        out.extend(tuple(c) for c in itertools.combinations(labels, size))
    return out


def inversion_parity(route: tuple[int, ...]) -> int:
    inversions = 0
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            if route[i] > route[j]:
                inversions += 1
    return inversions % 2


def route_sign(route: tuple[int, ...]) -> int:
    return -1 if inversion_parity(route) else 1


def finite_witness(n: int, decoration_count: int = 2) -> Stage0FiniteWitness:
    labels = tuple(range(1, n + 1))
    faces = subsets(labels)
    face_set = set(faces)
    by_dim: dict[str, int] = {}
    expected_by_dim: dict[str, int] = {}
    for d in range(n):
        by_dim[str(d)] = sum(1 for face in faces if len(face) - 1 == d)
        expected_by_dim[str(d)] = math.comb(n, d + 1)

    residue_step_count = 0
    residue_failures: list[str] = []
    for face in faces:
        for label in face:
            residue_step_count += 1
            if len(face) == 1:
                continue
            target = tuple(x for x in face if x != label)
            if target not in face_set:
                residue_failures.append(f"n={n}: residue target missing {face} delete {label} -> {target}")
            if len(target) >= len(face):
                residue_failures.append(f"n={n}: residue did not reduce rank {face} delete {label} -> {target}")

    even = 0
    odd = 0
    adjacent_failures = 0
    terminal_route_count = 0
    for perm in itertools.permutations(labels):
        terminal_route_count += 1
        sign = route_sign(perm)
        if sign == 1:
            even += 1
        else:
            odd += 1
        for i in range(n - 1):
            swapped = list(perm)
            swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
            if route_sign(tuple(swapped)) != -sign:
                adjacent_failures += 1

    fiber_sizes = [decoration_count for _ in faces]
    return Stage0FiniteWitness(
        n=n,
        face_count=len(faces),
        expected_face_count=(2**n) - 1,
        face_count_by_dimension=by_dim,
        expected_by_dimension=expected_by_dim,
        residue_step_count=residue_step_count,
        residue_step_failures=residue_failures,
        terminal_route_count=terminal_route_count,
        expected_terminal_route_count=math.factorial(n),
        terminal_even_routes=even,
        terminal_odd_routes=odd,
        adjacent_swap_failures=adjacent_failures,
        min_bulk_fiber_size=min(fiber_sizes),
        max_bulk_fiber_size=max(fiber_sizes),
    )


def compute_finite_witnesses(n_min: int = 2, n_max: int = 8) -> tuple[list[Stage0FiniteWitness], list[dict[str, Any]]]:
    witnesses: list[Stage0FiniteWitness] = []
    failures: list[dict[str, Any]] = []
    for n in range(n_min, n_max + 1):
        w = finite_witness(n)
        witnesses.append(w)
        if w.face_count != w.expected_face_count:
            failures.append({"failure": "face_count_mismatch", "n": n, "observed": w.face_count, "expected": w.expected_face_count})
        if w.face_count_by_dimension != w.expected_by_dimension:
            failures.append({"failure": "face_count_by_dimension_mismatch", "n": n, "observed": w.face_count_by_dimension, "expected": w.expected_by_dimension})
        if w.residue_step_failures:
            failures.append({"failure": "residue_step_failures", "n": n, "details": w.residue_step_failures[:10]})
        if w.terminal_route_count != w.expected_terminal_route_count:
            failures.append({"failure": "terminal_route_count_mismatch", "n": n, "observed": w.terminal_route_count, "expected": w.expected_terminal_route_count})
        if w.terminal_even_routes != w.terminal_odd_routes:
            failures.append({"failure": "terminal_parity_imbalance", "n": n, "even": w.terminal_even_routes, "odd": w.terminal_odd_routes})
        if w.adjacent_swap_failures != 0:
            failures.append({"failure": "adjacent_swap_sign_failures", "n": n, "count": w.adjacent_swap_failures})
        if w.min_bulk_fiber_size < 2:
            failures.append({"failure": "bulk_cover_faithful_or_singleton", "n": n, "min_fiber": w.min_bulk_fiber_size})
    return witnesses, failures


def check_skeleton_json() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    data = read_json(SKELETON_JSON)
    statuses = set(data.get("status", []))
    roles = set(data.get("artifact_roles", []))
    object_ids = {item.get("id") for item in data.get("formal_objects", [])}
    check_ids = {item.get("id") for item in data.get("finite_check_targets", [])}
    stage1_ids = {item.get("id") for item in data.get("next_stage1_formal_targets", [])}
    summary: dict[str, Any] = {
        "target_id": data.get("target_id"),
        "formal_object_count": len(object_ids),
        "finite_check_target_count": len(check_ids),
        "stage1_target_count": len(stage1_ids),
        "computed_status": data.get("computed_stage0_results", {}).get("status"),
        "recommended_next": data.get("recommended_next", ""),
    }

    if data.get("target_id") != "STAGE0-FM-MINIMAL-STATIC-FORMAL-SKELETON":
        failures.append({"failure": "target_id_mismatch", "observed": data.get("target_id")})
    for status in REQUIRED_STATUSES:
        if status not in statuses:
            failures.append({"failure": "missing_status", "status": status})
    for role in REQUIRED_ROLES:
        if role not in roles:
            failures.append({"failure": "missing_artifact_role", "role": role})

    answers = data.get("stage0_answers", {})
    for field in ["actual_mathematical_object", "definitions_to_fix_before_computation", "smallest_literal_finite_object", "project_changing_invariant_or_counterexample", "wrong_or_irrelevant_condition", "thin_stick_dependencies", "delete_demote_or_quarantine_if_fails"]:
        if not answers.get(field):
            failures.append({"failure": "stage0_answer_missing", "field": field})
    answer_text = normalize(json.dumps(answers, ensure_ascii=False))
    for term in ["gr_+(1,n)", "gr_+(0,n)", "n=2", "n=3", "counterexample", "thin", "demote"]:
        if term not in answer_text:
            failures.append({"failure": "stage0_answers_missing_term", "term": term})

    missing_objects = sorted(REQUIRED_OBJECTS - object_ids)
    if missing_objects:
        failures.append({"failure": "missing_formal_objects", "missing": missing_objects})
    for item in data.get("formal_objects", []):
        for field in ["id", "notation", "definition", "status"]:
            if not item.get(field):
                failures.append({"failure": "formal_object_missing_field", "object_id": item.get("id"), "field": field})

    missing_checks = sorted(REQUIRED_CHECKS - check_ids)
    if missing_checks:
        failures.append({"failure": "missing_finite_check_targets", "missing": missing_checks})
    for item in data.get("finite_check_targets", []):
        for field in ["id", "range", "expected", "falsifier"]:
            if not item.get(field):
                failures.append({"failure": "finite_check_target_missing_field", "check_id": item.get("id"), "field": field})

    computed = data.get("computed_stage0_results", {})
    if computed.get("status") != "PASS_FINITE_STATIC_MODEL_CHECKS":
        failures.append({"failure": "computed_status_not_pass", "observed": computed.get("status")})
    computed_text = normalize(json.dumps(computed, ensure_ascii=False))
    for term in ["2 <= n <= 8", "python", "2^n - 1", "permutation parity", "n!/2"]:
        if term not in computed_text:
            failures.append({"failure": "computed_results_missing_term", "term": term})

    missing_stage1 = sorted(REQUIRED_STAGE1_TARGETS - stage1_ids)
    if missing_stage1:
        failures.append({"failure": "missing_stage1_targets", "missing": missing_stage1})
    if len(data.get("red_team_falsifiers", [])) < 6:
        failures.append({"failure": "too_few_red_team_falsifiers"})
    if len(data.get("blocked_promotions", [])) < 6:
        failures.append({"failure": "too_few_blocked_promotions"})
    non_promotion = str(data.get("non_promotion_rule", "")).lower()
    for term in ["not a theorem", "not source extraction", "not a final object definition", "not a physical substrate", "not engineering readiness"]:
        if term not in non_promotion:
            failures.append({"failure": "non_promotion_missing_term", "term": term})
    return failures, summary


def check_markdown() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    text = SKELETON_MD.read_text(encoding="utf-8")
    lower = text.lower()
    summary = {"markdown_terms_present": True}
    for term in REQUIRED_MD_TERMS:
        if term.lower() not in lower:
            failures.append({"failure": "markdown_missing_required_term", "term": term})
            summary["markdown_terms_present"] = False
    return failures, summary


def check_integration() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    protocol = read_json(STAGE0_PROTOCOL_JSON)
    spine = read_json(STATIC_SPINE_JSON)
    roadmap = read_json(ROADMAP_JSON)
    protocol_text = normalize(json.dumps(protocol, ensure_ascii=False))
    spine_layers = {item.get("id") for item in spine.get("static_spine_layers", [])}
    roadmap_text = normalize(json.dumps(roadmap, ensure_ascii=False))
    summary = {
        "protocol_requires_stage0_attack": protocol.get("next_required_math_attack", {}).get("id") == "STAGE0-FM-MINIMAL-STATIC-FORMAL-SKELETON",
        "static_spine_layer_count": len(spine_layers),
        "roadmap_mentions_skeleton": "stage0-fm-minimal-static-formal-skeleton" in roadmap_text,
        "sage_status_available": "sagemath 9.5" in protocol_text,
        "polymake_status_available": "polymake 4.11" in protocol_text,
    }
    if not summary["protocol_requires_stage0_attack"]:
        failures.append({"failure": "protocol_no_longer_requires_stage0_attack"})
    if not {"SG0_TERMINAL_ATOM", "SG1_STATIC_SIMPLEX", "SG2_ORDERED_RESIDUE_SIGN", "SG3_PRODUCT_STATIC_BLOCK", "SG4_MUTATION_TRANSPORT"} <= spine_layers:
        failures.append({"failure": "static_spine_missing_required_layers"})
    if not summary["roadmap_mentions_skeleton"]:
        failures.append({"failure": "roadmap_missing_stage0_skeleton"})
    if not summary["sage_status_available"]:
        failures.append({"failure": "stage0_protocol_sage_status_stale"})
    if not summary["polymake_status_available"]:
        failures.append({"failure": "stage0_protocol_polymake_status_stale"})
    return failures, summary


def run_check() -> Stage0MinimalStaticFormalSkeletonResult:
    failures: list[dict[str, Any]] = []
    json_failures, json_summary = check_skeleton_json()
    md_failures, md_summary = check_markdown()
    integration_failures, integration_summary = check_integration()
    witnesses, finite_failures = compute_finite_witnesses()
    failures.extend(json_failures)
    failures.extend(md_failures)
    failures.extend(integration_failures)
    failures.extend(finite_failures)
    witness_dicts = [asdict(w) for w in witnesses]
    support_summary = {
        **json_summary,
        **md_summary,
        **integration_summary,
        "finite_range_checked": "2 <= n <= 8",
        "finite_witness_count": len(witnesses),
        "max_n_terminal_routes_checked": math.factorial(8),
        "checked_interface": "minimal static support/residue skeleton for Gr_+(0,n)/Gr_+(1,n) before physics mapping",
        "allowed_inference": "the Stage 0 support-subset skeleton is internally coherent for finite checks n<=8",
        "blocked_inference": "source extraction, theorem status, final Formation Medium definition, physical substrate, native dynamics, engineering readiness, or physical-regime winner status",
    }
    return Stage0MinimalStaticFormalSkeletonResult(
        target_id=TARGET_ID,
        checker="stage0_fm_minimal_static_formal_skeleton_guard_v1",
        status="PASS_FINITE_STATIC_MODEL_CHECKS" if not failures else "FAILED",
        inspected_files=[
            "research_ledger/STAGE0_FM_MINIMAL_STATIC_FORMAL_SKELETON.json",
            "research_ledger/STAGE0_FM_MINIMAL_STATIC_FORMAL_SKELETON.md",
            "research_ledger/FORMATION_MEDIUM_STAGE0_MATH_FIRST_PROTOCOL.json",
            "research_ledger/PRE_SPACETIME_STATIC_GEOMETRY_SPINE.json",
            "research_ledger/FORMATION_MEDIUM_TECHNICAL_ROADMAP.json",
        ],
        support_summary=support_summary,
        finite_witnesses=witness_dicts,
        counterexamples=failures,
        status_boundary=(
            "PASS_FINITE_STATIC_MODEL_CHECKS means the Stage 0 support-subset skeleton for Gr_+(0,n)/Gr_+(1,n) passed "
            "finite internal-coherence checks for n<=8: face counts, residue descent, route parity, terminal route parity balance, "
            "and toy non-faithful bulk fibers. It is not source extraction, not theorem status, not a final Formation Medium "
            "definition, not physical substrate, not native dynamics, and not engineering readiness."
        ),
    )


def write_result(path: Path, result: Stage0MinimalStaticFormalSkeletonResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(result), indent=2, sort_keys=True), encoding="utf-8")


def main() -> None:
    result = run_check()
    write_result(RESULT_PATH, result)
    print(json.dumps(asdict(result), indent=2, sort_keys=True))
    if result.status == "FAILED":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
