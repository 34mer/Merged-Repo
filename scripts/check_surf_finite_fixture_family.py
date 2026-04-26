from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "CHK-SURF-FINITE-FIXTURE-FAMILY"
FIXTURE_PATH = ROOT / "formal_handoff" / "fixtures" / "surfaceology_finite_fixture_family.json"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
REQUIRED_SOURCE_CLAIMS = {"EXT-SURF-COUNT-2023-001", "EXT-SURF-001"}
REQUIRED_TOP_STATUSES = {"GENERATED", "FINITE_FIXTURE_FAMILY", "HAND_CHECKABLE", "NOT_THEOREM", "NOT_SOURCE_EXTRACTED"}
REQUIRED_FIXTURE_IDS = {
    "SURF-TINY-TWO-CURVE-CROSSING",
    "SURF-TINY-DISJOINT-TWO-PAIRS",
    "SURF-TINY-THREE-CURVE-CHAIN",
}
FORBIDDEN_PROMOTION_PHRASES = [
    "surfaceology theorem",
    "general positive-region solver",
    "Formation Medium substrate evidence",
    "physical settling law",
    "engineering readiness",
]


@dataclass(frozen=True)
class SurfFiniteFixtureFamilyResult:
    target_id: str
    checker: str
    status: str
    family_id: str
    inspected_files: list[str]
    support_summary: dict[str, Any]
    counterexamples: list[dict[str, Any]]
    status_boundary: str


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_fraction(value: str | int | float) -> Fraction:
    if isinstance(value, int):
        return Fraction(value, 1)
    if isinstance(value, float):
        return Fraction(str(value))
    return Fraction(value)


def normalize_edge(edge: list[str]) -> tuple[str, str]:
    if len(edge) != 2:
        raise ValueError(f"edge must have two endpoints: {edge}")
    a, b = str(edge[0]), str(edge[1])
    return tuple(sorted((a, b)))  # type: ignore[return-value]


def expected_exponents_from_edges(edges: list[list[str]], curve_ids: set[str]) -> dict[str, dict[str, int]]:
    exponents: dict[str, dict[str, int]] = {curve_id: {} for curve_id in curve_ids}
    for raw_edge in edges:
        a, b = normalize_edge(raw_edge)
        if a == b:
            raise ValueError(f"self-edge not allowed in fixture family: {raw_edge}")
        exponents.setdefault(a, {})[b] = exponents.setdefault(a, {}).get(b, 0) + 1
        exponents.setdefault(b, {})[a] = exponents.setdefault(b, {}).get(a, 0) + 1
    return exponents


def derived_equation(curve_id: str, variable_by_curve: dict[str, str], exponents: dict[str, dict[str, int]]) -> str:
    variable = variable_by_curve[curve_id]
    factors: list[str] = []
    for crossing_id, exponent in sorted(exponents.get(curve_id, {}).items()):
        crossing_variable = variable_by_curve[crossing_id]
        if int(exponent) == 1:
            factors.append(crossing_variable)
        else:
            factors.append(f"{crossing_variable}^{int(exponent)}")
    product = " * ".join(factors) if factors else "1"
    return f"{variable} + {product} - 1 = 0"


def product_value(values: dict[str, Fraction], curve_id: str, variable_by_curve: dict[str, str], exponents: dict[str, dict[str, int]]) -> Fraction:
    product = Fraction(1, 1)
    for crossing_id, exponent in exponents.get(curve_id, {}).items():
        product *= values[variable_by_curve[crossing_id]] ** int(exponent)
    return product


def max_degree(exponents: dict[str, dict[str, int]]) -> int:
    return max((len(neighbors) for neighbors in exponents.values()), default=0)


def check_family_shape(family: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    statuses = set(family.get("status", []))
    source_claims = set(family.get("source_claim_ids", []))
    fixture_ids = {fixture.get("fixture_id") for fixture in family.get("fixtures", [])}
    non_promotion = str(family.get("non_promotion_boundary", ""))
    summary: dict[str, Any] = {
        "family_id": family.get("family_id"),
        "fixture_count": len(family.get("fixtures", [])),
        "fixture_ids": sorted(str(fid) for fid in fixture_ids),
        "source_claim_ids": sorted(source_claims),
    }
    for status in REQUIRED_TOP_STATUSES:
        if status not in statuses:
            failures.append({"failure": "missing_family_status", "status": status})
    if not REQUIRED_SOURCE_CLAIMS <= source_claims:
        failures.append({"failure": "missing_required_source_claims", "observed": sorted(source_claims), "required": sorted(REQUIRED_SOURCE_CLAIMS)})
    if not REQUIRED_FIXTURE_IDS <= fixture_ids:
        failures.append({"failure": "missing_required_fixture_ids", "observed": sorted(str(fid) for fid in fixture_ids), "required": sorted(REQUIRED_FIXTURE_IDS)})
    for phrase in FORBIDDEN_PROMOTION_PHRASES:
        if phrase.lower() not in non_promotion.lower():
            failures.append({"failure": "family_non_promotion_boundary_missing_phrase", "phrase": phrase})
    return failures, summary


def check_single_fixture(fixture: dict[str, Any], lower: Fraction, upper: Fraction) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    fixture_id = str(fixture.get("fixture_id"))
    curves = fixture.get("curves", [])
    curve_ids = {str(curve.get("id")) for curve in curves}
    variable_by_curve = {str(curve.get("id")): str(curve.get("variable")) for curve in curves}
    variables = set(variable_by_curve.values())
    expected_equations = {item["curve"]: item["normalized_equation"] for item in fixture.get("expected_equations", [])}
    declared_exponents = fixture.get("intersection_exponents", {})
    try:
        edge_exponents = expected_exponents_from_edges(fixture.get("crossing_edges", []), curve_ids)
    except ValueError as exc:
        failures.append({"failure": "bad_crossing_edge", "fixture_id": fixture_id, "error": str(exc)})
        edge_exponents = {}

    summary: dict[str, Any] = {
        "curve_count": len(curves),
        "edge_count": len(fixture.get("crossing_edges", [])),
        "max_degree": max_degree(edge_exponents),
        "sample_solution_count": len(fixture.get("sample_solutions", [])),
        "derived_equations": {},
    }

    if len(curve_ids) != len(curves):
        failures.append({"failure": "duplicate_curve_ids", "fixture_id": fixture_id})
    if len(variables) != len(curves):
        failures.append({"failure": "duplicate_variables", "fixture_id": fixture_id})

    for curve_id in sorted(curve_ids):
        declared_neighbors = {str(k): int(v) for k, v in declared_exponents.get(curve_id, {}).items()}
        edge_neighbors = edge_exponents.get(curve_id, {})
        if declared_neighbors != edge_neighbors:
            failures.append({"failure": "intersection_exponents_do_not_match_edges", "fixture_id": fixture_id, "curve_id": curve_id, "declared": declared_neighbors, "expected": edge_neighbors})
        equation = derived_equation(curve_id, variable_by_curve, declared_exponents)
        summary["derived_equations"][curve_id] = equation
        if expected_equations.get(curve_id) != equation:
            failures.append({"failure": "expected_equation_mismatch", "fixture_id": fixture_id, "curve_id": curve_id, "observed": expected_equations.get(curve_id), "expected": equation})

    for sample in fixture.get("sample_solutions", []):
        label = sample.get("label", "<missing>")
        raw_values = sample.get("values", {})
        values = {variable: parse_fraction(value) for variable, value in raw_values.items()}
        for variable in variables:
            if variable not in values:
                failures.append({"failure": "sample_missing_variable", "fixture_id": fixture_id, "label": label, "variable": variable})
                continue
            if values[variable] < lower or values[variable] > upper:
                failures.append({"failure": "sample_outside_positive_region", "fixture_id": fixture_id, "label": label, "variable": variable, "value": str(values[variable])})
        for curve_id in sorted(curve_ids):
            variable = variable_by_curve[curve_id]
            if variable not in values:
                continue
            lhs = values[variable] + product_value(values, curve_id, variable_by_curve, declared_exponents) - 1
            if lhs != 0:
                failures.append({"failure": "sample_does_not_satisfy_u_equation", "fixture_id": fixture_id, "label": label, "curve_id": curve_id, "lhs": str(lhs)})

    sample_by_label = {sample.get("label"): sample for sample in fixture.get("sample_solutions", [])}
    neighbors_by_variable = {
        variable_by_curve[curve_id]: {variable_by_curve[n] for n in declared_exponents.get(curve_id, {})}
        for curve_id in curve_ids
    }
    for limit in fixture.get("boundary_limits", []):
        when_zero = str(limit.get("when_zero"))
        forces_one = set(str(v) for v in limit.get("forces_one", []))
        expected_forces_one = neighbors_by_variable.get(when_zero, set())
        if forces_one != expected_forces_one:
            failures.append({"failure": "boundary_forces_one_not_neighbor_set", "fixture_id": fixture_id, "when_zero": when_zero, "observed": sorted(forces_one), "expected": sorted(expected_forces_one)})
        witness = sample_by_label.get(limit.get("witness_sample"))
        if witness is None:
            failures.append({"failure": "boundary_missing_witness_sample", "fixture_id": fixture_id, "when_zero": when_zero, "witness_sample": limit.get("witness_sample")})
            continue
        values = {variable: parse_fraction(value) for variable, value in witness.get("values", {}).items()}
        if values.get(when_zero) != 0:
            failures.append({"failure": "boundary_witness_does_not_zero_variable", "fixture_id": fixture_id, "witness_sample": witness.get("label"), "variable": when_zero, "value": str(values.get(when_zero))})
        for variable in forces_one:
            if values.get(variable) != 1:
                failures.append({"failure": "boundary_witness_does_not_force_one", "fixture_id": fixture_id, "witness_sample": witness.get("label"), "variable": variable, "value": str(values.get(variable))})
    return failures, summary


def check_fixtures(family: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    lower = parse_fraction(family.get("positive_region", {}).get("lower_bound", "0"))
    upper = parse_fraction(family.get("positive_region", {}).get("upper_bound", "1"))
    fixture_summaries: dict[str, Any] = {}
    has_multi_neighbor_fixture = False
    has_disconnected_fixture = False
    for fixture in family.get("fixtures", []):
        fixture_id = str(fixture.get("fixture_id"))
        fixture_failures, fixture_summary = check_single_fixture(fixture, lower, upper)
        failures.extend(fixture_failures)
        fixture_summaries[fixture_id] = fixture_summary
        if fixture_summary.get("max_degree", 0) >= 2:
            has_multi_neighbor_fixture = True
        if fixture_summary.get("edge_count", 0) >= 2 and fixture_summary.get("curve_count", 0) >= 4 and fixture_summary.get("max_degree", 0) == 1:
            has_disconnected_fixture = True
    if not has_multi_neighbor_fixture:
        failures.append({"failure": "family_missing_multi_neighbor_fixture"})
    if not has_disconnected_fixture:
        failures.append({"failure": "family_missing_disconnected_pair_fixture"})
    return failures, {"fixtures": fixture_summaries, "has_multi_neighbor_fixture": has_multi_neighbor_fixture, "has_disconnected_fixture": has_disconnected_fixture}


def run_check() -> SurfFiniteFixtureFamilyResult:
    family = read_json(FIXTURE_PATH)
    failures: list[dict[str, Any]] = []
    shape_failures, shape_summary = check_family_shape(family)
    fixture_failures, fixture_summary = check_fixtures(family)
    failures.extend(shape_failures)
    failures.extend(fixture_failures)
    support_summary: dict[str, Any] = {
        **shape_summary,
        **fixture_summary,
        "checked_interface": "finite family of declared crossing-graph u-equation fixtures with exact rational sample and boundary checks",
        "allowed_inference": "the three declared tiny fixtures satisfy their encoded u-equations and boundary-forcing samples",
        "blocked_inference": "general surfaceology theorem, general positive-region solver, Formation Medium substrate evidence, physical settling law, or engineering readiness",
    }
    return SurfFiniteFixtureFamilyResult(
        target_id=TARGET_ID,
        checker="surf_finite_fixture_family_check_v1",
        status="PASS" if not failures else "FAILED",
        family_id=str(family.get("family_id")),
        inspected_files=["formal_handoff/fixtures/surfaceology_finite_fixture_family.json"],
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS means only the declared finite fixture family satisfies its exact rational u-equation, positive-region, "
            "and boundary-forcing checks. It is not a mathematical proof of surfaceology, not a general positive-region solver, "
            "not Formation Medium substrate evidence, not a physical settling-law result, and not engineering readiness."
        ),
    )


def write_result(path: Path, result: SurfFiniteFixtureFamilyResult) -> None:
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
