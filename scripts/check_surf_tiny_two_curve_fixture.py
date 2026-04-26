from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "CHK-SURF-TINY-TWO-CURVE-FIXTURE"
FIXTURE_PATH = ROOT / "formal_handoff" / "fixtures" / "surfaceology_tiny_two_curve_fixture.json"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
REQUIRED_SOURCE_CLAIMS = {"EXT-SURF-COUNT-2023-001", "EXT-SURF-001"}
REQUIRED_STATUSES = {"GENERATED", "FINITE_FIXTURE", "HAND_CHECKABLE", "NOT_THEOREM", "NOT_SOURCE_EXTRACTED"}
FORBIDDEN_PROMOTION_PHRASES = [
    "surfaceology theorem",
    "general positive-region solver",
    "formation medium substrate evidence",
    "physical settling law",
    "engineering readiness",
]


@dataclass(frozen=True)
class SurfTinyTwoCurveFixtureResult:
    target_id: str
    checker: str
    status: str
    fixture_id: str
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


def product_value(values: dict[str, Fraction], curve_id: str, variable_by_curve: dict[str, str], exponents: dict[str, dict[str, int]]) -> Fraction:
    product = Fraction(1, 1)
    for crossing_id, exponent in exponents.get(curve_id, {}).items():
        variable = variable_by_curve[crossing_id]
        product *= values[variable] ** int(exponent)
    return product


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


def check_fixture_shape(fixture: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    statuses = set(fixture.get("status", []))
    source_claims = set(fixture.get("source_claim_ids", []))
    curves = fixture.get("curves", [])
    variable_by_curve = {curve.get("id"): curve.get("variable") for curve in curves}
    curve_ids = set(variable_by_curve)
    variables = set(variable_by_curve.values())
    summary = {
        "fixture_id": fixture.get("fixture_id"),
        "curve_count": len(curves),
        "sample_solution_count": len(fixture.get("sample_solutions", [])),
        "source_claim_ids": sorted(source_claims),
    }

    for status in REQUIRED_STATUSES:
        if status not in statuses:
            failures.append({"failure": "missing_fixture_status", "status": status})
    if not REQUIRED_SOURCE_CLAIMS <= source_claims:
        failures.append({"failure": "missing_required_source_claims", "observed": sorted(source_claims), "required": sorted(REQUIRED_SOURCE_CLAIMS)})
    if len(curves) != 2:
        failures.append({"failure": "fixture_not_two_curve", "curve_count": len(curves)})
    if curve_ids != {"a", "b"}:
        failures.append({"failure": "unexpected_curve_ids", "observed": sorted(str(x) for x in curve_ids)})
    if variables != {"u_a", "u_b"}:
        failures.append({"failure": "unexpected_variables", "observed": sorted(str(x) for x in variables)})

    non_promotion = str(fixture.get("non_promotion_boundary", "")).lower()
    for phrase in FORBIDDEN_PROMOTION_PHRASES:
        if phrase not in non_promotion:
            failures.append({"failure": "non_promotion_boundary_missing_phrase", "phrase": phrase})
    return failures, summary


def check_intersections_and_equations(fixture: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    variable_by_curve = {curve["id"]: curve["variable"] for curve in fixture.get("curves", [])}
    exponents = fixture.get("intersection_exponents", {})
    expected_equations = {item["curve"]: item["normalized_equation"] for item in fixture.get("expected_equations", [])}
    summary: dict[str, Any] = {"derived_equations": {}}

    for curve_id in variable_by_curve:
        if curve_id in exponents.get(curve_id, {}):
            failures.append({"failure": "self_intersection_in_tiny_fixture", "curve_id": curve_id})
        for other_id, exponent in exponents.get(curve_id, {}).items():
            if other_id not in variable_by_curve:
                failures.append({"failure": "intersection_references_unknown_curve", "curve_id": curve_id, "other_id": other_id})
                continue
            if int(exponent) < 0:
                failures.append({"failure": "negative_intersection_exponent", "curve_id": curve_id, "other_id": other_id, "exponent": exponent})
            reverse = int(exponents.get(other_id, {}).get(curve_id, -1))
            if reverse != int(exponent):
                failures.append({"failure": "intersection_not_symmetric", "curve_id": curve_id, "other_id": other_id, "exponent": exponent, "reverse": reverse})
        equation = derived_equation(curve_id, variable_by_curve, exponents)
        summary["derived_equations"][curve_id] = equation
        if expected_equations.get(curve_id) != equation:
            failures.append({"failure": "expected_equation_mismatch", "curve_id": curve_id, "observed": expected_equations.get(curve_id), "expected": equation})
    return failures, summary


def check_sample_solutions(fixture: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    variable_by_curve = {curve["id"]: curve["variable"] for curve in fixture.get("curves", [])}
    exponents = fixture.get("intersection_exponents", {})
    lower = parse_fraction(fixture.get("positive_region", {}).get("lower_bound", "0"))
    upper = parse_fraction(fixture.get("positive_region", {}).get("upper_bound", "1"))
    summary: dict[str, Any] = {"sample_solution_labels": []}

    for sample in fixture.get("sample_solutions", []):
        label = sample.get("label", "<missing>")
        summary["sample_solution_labels"].append(label)
        raw_values = sample.get("values", {})
        values = {variable: parse_fraction(value) for variable, value in raw_values.items()}
        for variable in variable_by_curve.values():
            if variable not in values:
                failures.append({"failure": "sample_missing_variable", "label": label, "variable": variable})
                continue
            if values[variable] < lower or values[variable] > upper:
                failures.append({"failure": "sample_outside_positive_region", "label": label, "variable": variable, "value": str(values[variable]), "lower": str(lower), "upper": str(upper)})
        for curve_id, variable in variable_by_curve.items():
            if variable not in values:
                continue
            lhs = values[variable] + product_value(values, curve_id, variable_by_curve, exponents) - 1
            if lhs != 0:
                failures.append({"failure": "sample_does_not_satisfy_u_equation", "label": label, "curve_id": curve_id, "lhs": str(lhs)})
    return failures, summary


def check_boundary_limits(fixture: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    sample_by_label = {sample["label"]: sample for sample in fixture.get("sample_solutions", [])}
    boundary_limits = fixture.get("boundary_limits", [])
    summary = {"boundary_limit_count": len(boundary_limits)}

    expected = {
        "u_a": {"label": "boundary_a_zero", "forces_one": {"u_b"}},
        "u_b": {"label": "boundary_b_zero", "forces_one": {"u_a"}},
    }
    for limit in boundary_limits:
        when_zero = limit.get("when_zero")
        if when_zero not in expected:
            failures.append({"failure": "unexpected_boundary_limit", "when_zero": when_zero})
            continue
        forces_one = set(limit.get("forces_one", []))
        if forces_one != expected[when_zero]["forces_one"]:
            failures.append({"failure": "boundary_forces_one_mismatch", "when_zero": when_zero, "observed": sorted(forces_one), "expected": sorted(expected[when_zero]["forces_one"])})
        sample = sample_by_label.get(expected[when_zero]["label"])
        if sample is None:
            failures.append({"failure": "missing_boundary_sample", "label": expected[when_zero]["label"]})
            continue
        values = {variable: parse_fraction(value) for variable, value in sample.get("values", {}).items()}
        if values.get(when_zero) != 0:
            failures.append({"failure": "boundary_sample_does_not_zero_variable", "label": sample["label"], "variable": when_zero, "value": str(values.get(when_zero))})
        for variable in forces_one:
            if values.get(variable) != 1:
                failures.append({"failure": "boundary_sample_does_not_force_one", "label": sample["label"], "variable": variable, "value": str(values.get(variable))})
    return failures, summary


def run_check() -> SurfTinyTwoCurveFixtureResult:
    fixture = read_json(FIXTURE_PATH)
    failures: list[dict[str, Any]] = []
    shape_failures, shape_summary = check_fixture_shape(fixture)
    equation_failures, equation_summary = check_intersections_and_equations(fixture)
    sample_failures, sample_summary = check_sample_solutions(fixture)
    boundary_failures, boundary_summary = check_boundary_limits(fixture)
    failures.extend(shape_failures)
    failures.extend(equation_failures)
    failures.extend(sample_failures)
    failures.extend(boundary_failures)

    support_summary = {
        **shape_summary,
        **equation_summary,
        **sample_summary,
        **boundary_summary,
        "checked_interface": "finite two-curve crossing fixture for u_C + product_D u_D^I(C,D) = 1 and boundary forcing in the positive region",
        "allowed_inference": "the tiny two-curve fixture exactly satisfies its declared u-equations and boundary samples",
        "blocked_inference": "general surfaceology theorem, general positive-region solver, Formation Medium substrate evidence, physical settling law, or engineering readiness",
    }
    return SurfTinyTwoCurveFixtureResult(
        target_id=TARGET_ID,
        checker="surf_tiny_two_curve_fixture_check_v1",
        status="PASS" if not failures else "FAILED",
        fixture_id=str(fixture.get("fixture_id")),
        inspected_files=["formal_handoff/fixtures/surfaceology_tiny_two_curve_fixture.json"],
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS means only the declared two-curve crossing fixture satisfies its finite u-equations, positive-region samples, "
            "and boundary-forcing checks. It is not a mathematical proof of surfaceology, not a general positive-region solver, "
            "not Formation Medium substrate evidence, not a physical settling-law result, and not engineering readiness."
        ),
    )


def write_result(path: Path, result: SurfTinyTwoCurveFixtureResult) -> None:
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
