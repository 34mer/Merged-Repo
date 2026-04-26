from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "LEDGER-HIGH-RESONANCE-NATIVE-COMPARATOR-PLAN"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
PLAN_JSON = ROOT / "research_ledger" / "HIGH_RESONANCE_NATIVE_COMPARATOR_PLAN.json"
PLAN_MD = ROOT / "research_ledger" / "HIGH_RESONANCE_NATIVE_COMPARATOR_PLAN.md"
DOCTRINE_JSON = ROOT / "research_ledger" / "PROJECT_GLOBAL_DOCTRINE_REGISTRY.json"
DOCTRINE_MD = ROOT / "research_ledger" / "PROJECT_GLOBAL_DOCTRINE.md"

REQUIRED_CANDIDATES = {
    "CRBSM": {
        "primary_role": "MECHANISM",
        "required_layer_terms": ["mechanism", "proxy"],
        "required_blocked_flattening_terms": ["selected substrate", "source-backed", "Route A", "Formation Medium"],
    },
    "ROUTE_A": {
        "primary_role": "ROUTE",
        "required_layer_terms": ["hardware", "proxy"],
        "required_blocked_flattening_terms": ["selected substrate", "CRBSM implemented", "Formation Medium implemented", "engineering feasibility"],
    },
    "SCATTERING_NATIVE": {
        "primary_role": "COMPARATOR",
        "required_layer_terms": ["law-native", "comparator"],
        "required_blocked_flattening_terms": ["default winner", "selected substrate", "engineering route", "proof"],
    },
    "HIGH_RESONANCE_NATIVE": {
        "primary_role": "COMPARATOR",
        "required_layer_terms": ["bridge", "comparator"],
        "required_blocked_flattening_terms": ["default winner", "selected substrate", "Route A", "native settling law"],
    },
}

REQUIRED_AXES = [
    "native carrier",
    "native admissibility",
    "native relay/transport",
    "persistent support/channel identity",
    "intrinsic readout",
    "bulk/readout separation",
    "harnessability/buildability",
    "simulation/control/measurement failure mode",
    "negative-control clarity",
]

REQUIRED_NEXT_REVIEWS = {"HR-N1", "HR-N2", "HR-N3", "HR-N4"}
REQUIRED_MD_TERMS = [
    "CRBSM is mechanism-language",
    "Route A is hardware/proxy",
    "Scattering-native is a mandatory comparator",
    "High-resonance / mesoscopic resonance-native regimes may be the bridge",
    "not a source-extracted claim",
    "not a substrate selection",
    "not engineering feasibility",
]
REQUIRED_DOCTRINE_TERMS = [
    "CRBSM = mechanism-language / generated proxy vocabulary",
    "Route A = hardware/proxy engineering route",
    "scattering-native = mandatory law-native comparator, not default winner",
    "high-resonance = possible bridge comparator",
]
FORBIDDEN_ALLOWED_PHRASES = [
    "selected substrate",
    "default winner",
    "crbsm implemented",
    "formation medium implemented",
    "native settling law",
    "engineering feasibility",
]


@dataclass(frozen=True)
class HighResonanceComparatorPlanResult:
    target_id: str
    checker: str
    status: str
    inspected_files: list[str]
    support_summary: dict[str, Any]
    counterexamples: list[dict[str, Any]]
    status_boundary: str


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def check_plan_json() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    data = read_json(PLAN_JSON)
    status = set(data.get("status", []))
    roles = set(data.get("artifact_roles", []))
    candidates = {candidate.get("id"): candidate for candidate in data.get("layered_candidates", [])}
    matrix = {row.get("candidate_id"): row for row in data.get("preliminary_matrix", [])}
    summary: dict[str, Any] = {
        "candidate_count": len(candidates),
        "comparison_axis_count": len(data.get("comparison_axes", [])),
        "required_review_count": len(data.get("required_next_reviews", [])),
        "candidate_roles": {},
    }

    for required_status in ["GENERATED", "OPEN", "NOT_SOURCE_EXTRACTED", "NOT_SUBSTRATE_SELECTION", "NOT_ENGINEERING_READY"]:
        if required_status not in status:
            failures.append({"failure": "missing_plan_status", "status": required_status})
    for required_role in ["COMPARATOR", "MECHANISM", "ROUTE", "PROXY", "GUARD", "NEGATIVE_CONTROL"]:
        if required_role not in roles:
            failures.append({"failure": "missing_artifact_role", "role": required_role})

    anti_flattening = str(data.get("anti_flattening_rule", "")).lower()
    for term in ["crbsm is mechanism-language", "route a is hardware/proxy", "scattering-native", "mandatory comparator", "high-resonance", "bridge"]:
        if term not in anti_flattening:
            failures.append({"failure": "anti_flattening_rule_missing_term", "term": term})

    object_blocked = " ".join(data.get("global_object", {}).get("blocked_confusion", [])).lower()
    for term in ["crbsm", "route a", "scattering", "high-resonance"]:
        if term not in object_blocked:
            failures.append({"failure": "global_object_missing_blocked_confusion", "term": term})

    for candidate_id, spec in REQUIRED_CANDIDATES.items():
        candidate = candidates.get(candidate_id)
        if candidate is None:
            failures.append({"failure": "missing_candidate", "candidate_id": candidate_id})
            continue
        summary["candidate_roles"][candidate_id] = candidate.get("primary_role")
        if candidate.get("primary_role") != spec["primary_role"]:
            failures.append({"failure": "candidate_primary_role_mismatch", "candidate_id": candidate_id, "observed": candidate.get("primary_role"), "expected": spec["primary_role"]})
        layer = str(candidate.get("layer_label", "")).lower()
        for term in spec["required_layer_terms"]:
            if term.lower() not in layer:
                failures.append({"failure": "candidate_layer_label_missing_term", "candidate_id": candidate_id, "term": term})
        blocked = " ".join(candidate.get("blocked_flattenings", [])).lower()
        for term in spec["required_blocked_flattening_terms"]:
            if term.lower() not in blocked:
                failures.append({"failure": "candidate_blocked_flattening_missing_term", "candidate_id": candidate_id, "term": term})
        if candidate_id not in matrix:
            failures.append({"failure": "candidate_missing_from_preliminary_matrix", "candidate_id": candidate_id})

    axes = [axis.lower() for axis in data.get("comparison_axes", [])]
    for axis in REQUIRED_AXES:
        if axis.lower() not in axes:
            failures.append({"failure": "missing_comparison_axis", "axis": axis})

    next_reviews = {review.get("id") for review in data.get("required_next_reviews", [])}
    missing_reviews = sorted(REQUIRED_NEXT_REVIEWS - next_reviews)
    if missing_reviews:
        failures.append({"failure": "missing_required_next_reviews", "missing": missing_reviews})
    for review in data.get("required_next_reviews", []):
        output = str(review.get("required_output", "")).lower()
        if "winner" in output and "not" not in output:
            failures.append({"failure": "review_output_allows_winner_declaration", "review_id": review.get("id")})

    kill_text = " ".join(data.get("kill_conditions", [])).lower()
    for term in ["crbsm", "route a", "scattering", "high-resonance", "source review", "investor"]:
        if term not in kill_text:
            failures.append({"failure": "kill_conditions_missing_term", "term": term})

    for candidate in data.get("layered_candidates", []):
        positive_fields = " ".join(str(candidate.get(field, "")) for field in ["positive_function", "current_status"]).lower()
        for phrase in FORBIDDEN_ALLOWED_PHRASES:
            if phrase in positive_fields and "not_" not in positive_fields and "not " not in positive_fields:
                failures.append({"failure": "forbidden_positive_promotion_phrase_in_candidate", "candidate_id": candidate.get("id"), "phrase": phrase})
    return failures, summary


def check_plan_markdown() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    text = PLAN_MD.read_text(encoding="utf-8")
    lower = text.lower()
    summary = {"markdown_terms_present": True}
    for term in REQUIRED_MD_TERMS:
        if term.lower() not in lower:
            failures.append({"failure": "markdown_missing_required_term", "term": term})
            summary["markdown_terms_present"] = False
    return failures, summary


def check_doctrine_alignment() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    doctrine_text = DOCTRINE_MD.read_text(encoding="utf-8")
    registry = read_json(DOCTRINE_JSON)
    lower = doctrine_text.lower()
    summary: dict[str, Any] = {"doctrine_anti_flattening_present": True}
    for term in REQUIRED_DOCTRINE_TERMS:
        if term.lower() not in lower:
            failures.append({"failure": "doctrine_missing_anti_flattening_term", "term": term})
            summary["doctrine_anti_flattening_present"] = False
    anti = registry.get("anti_flattening_rule", {})
    for key in ["CRBSM", "Route A", "scattering_native", "high_resonance_native"]:
        if key not in anti:
            failures.append({"failure": "registry_missing_anti_flattening_key", "key": key})
    stop_text = " ".join(registry.get("stop_conditions", [])).lower()
    if "flattened into one route/substrate/winner" not in stop_text:
        failures.append({"failure": "registry_missing_flattening_stop_condition"})
    return failures, summary


def run_check() -> HighResonanceComparatorPlanResult:
    failures: list[dict[str, Any]] = []
    json_failures, json_summary = check_plan_json()
    md_failures, md_summary = check_plan_markdown()
    doctrine_failures, doctrine_summary = check_doctrine_alignment()
    failures.extend(json_failures)
    failures.extend(md_failures)
    failures.extend(doctrine_failures)
    support_summary = {
        **json_summary,
        **md_summary,
        **doctrine_summary,
        "checked_interface": "CRBSM / Route A / scattering-native / high-resonance role separation and high-resonance comparator planning",
        "allowed_inference": "the repo now has an explicit anti-flattening plan and next-review queue for high-resonance/native comparator work",
        "blocked_inference": "CRBSM validation, Route A implementation, scattering-native default victory, high-resonance default victory, substrate selection, settling-law proof, or engineering readiness",
    }
    return HighResonanceComparatorPlanResult(
        target_id=TARGET_ID,
        checker="high_resonance_native_comparator_plan_guard_v1",
        status="PASS_LEDGER_VALIDATION" if not failures else "FAILED",
        inspected_files=[
            "research_ledger/HIGH_RESONANCE_NATIVE_COMPARATOR_PLAN.json",
            "research_ledger/HIGH_RESONANCE_NATIVE_COMPARATOR_PLAN.md",
            "research_ledger/PROJECT_GLOBAL_DOCTRINE.md",
            "research_ledger/PROJECT_GLOBAL_DOCTRINE_REGISTRY.json",
        ],
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_LEDGER_VALIDATION means the repo preserves the layer separation CRBSM=mechanism-language, Route A=hardware/proxy, "
            "scattering-native=mandatory comparator, and high-resonance=possible bridge comparator. It is not a source claim, "
            "not a proof, not CRBSM validation, not Route A validation, not substrate selection, not engineering readiness, "
            "and not corporate readiness."
        ),
    )


def write_result(path: Path, result: HighResonanceComparatorPlanResult) -> None:
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
