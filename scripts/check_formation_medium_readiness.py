from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "LEDGER-FORMATION-MEDIUM-READINESS"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
JSON_LEDGER = ROOT / "research_ledger" / "FORMATION_MEDIUM_READINESS_LEDGER.json"
MD_LEDGER = ROOT / "research_ledger" / "FORMATION_MEDIUM_READINESS_LEDGER.md"
FORMAL_RESULTS = ROOT / "research_ledger" / "FORMAL_CHECK_RESULTS.json"

REQUIRED_LAYER_STATES = {
    "RL1_SOURCE_COVERAGE": "ADVANCING",
    "RL2_FINITE_CHECKS": "PARTIAL",
    "RL3_FORMAL_THEOREMS": "NOT_READY",
    "RL4_PHYSICAL_SUBSTRATE": "NOT_READY",
    "RL5_SETTLING_LAW": "NOT_READY",
    "RL6_ENGINEERING_PROTOTYPE": "NOT_READY",
    "RL7_CAPITAL_READINESS": "EARLY_TECHNICAL_ROADMAP_ONLY",
}

REQUIRED_GAPS = [
    "no selected physical substrate",
    "no native settling law",
    "no S2* theorem",
    "no lab protocol",
    "no engineering prototype",
]

REQUIRED_MD_TERMS = [
    "not a source-extracted claim",
    "not a theorem",
    "not engineering readiness",
    "no selected physical substrate",
    "no native settling law",
    "early technical diligence conversation",
]

FORBIDDEN_READY_PHRASES = [
    "substrate has been identified",
    "settling law is proven",
    "engineering prototype is ready",
    "lab-ready hardware path exists",
    "product proof",
    "validated physical medium exists",
    "formation medium is built",
    "formation medium is proven",
]


@dataclass(frozen=True)
class FormationMediumReadinessResult:
    target_id: str
    checker: str
    status: str
    inspected_files: list[str]
    support_summary: dict[str, Any]
    counterexamples: list[dict[str, Any]]
    status_boundary: str


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def check_json_ledger() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    data = read_json(JSON_LEDGER)
    statuses = set(data.get("status", []))
    summary: dict[str, Any] = {"layer_states": {}, "critical_gap_count": len(data.get("critical_gaps", []))}

    for status in ["GENERATED", "OPEN", "NOT_SOURCE_EXTRACTED", "NOT_CHECKED_AS_PHYSICS", "ROADMAP_ONLY"]:
        if status not in statuses:
            failures.append({"failure": "missing_top_level_status", "status": status})

    layers = {layer.get("id"): layer for layer in data.get("readiness_layers", [])}
    for layer_id, expected_state in REQUIRED_LAYER_STATES.items():
        layer = layers.get(layer_id)
        if layer is None:
            failures.append({"failure": "missing_readiness_layer", "layer_id": layer_id})
            continue
        observed = layer.get("current_state")
        summary["layer_states"][layer_id] = observed
        if observed != expected_state:
            failures.append({"failure": "readiness_state_mismatch", "layer_id": layer_id, "observed": observed, "expected": expected_state})
        if not layer.get("blocked_claims"):
            failures.append({"failure": "readiness_layer_missing_blocked_claims", "layer_id": layer_id})

    gaps_lower = [str(gap).lower() for gap in data.get("critical_gaps", [])]
    for gap in REQUIRED_GAPS:
        if gap.lower() not in gaps_lower:
            failures.append({"failure": "missing_critical_gap", "gap": gap})

    all_text = json.dumps(data, ensure_ascii=False).lower()
    # Forbidden phrases are allowed only when they appear as blocked claims, not allowed claims.
    for layer in data.get("readiness_layers", []):
        allowed = str(layer.get("allowed_claim", "")).lower()
        for phrase in FORBIDDEN_READY_PHRASES:
            if phrase in allowed:
                failures.append({"failure": "forbidden_ready_phrase_in_allowed_claim", "layer_id": layer.get("id"), "phrase": phrase})
    for phrase in ["not source-extracted", "roadmap"]:
        if phrase not in all_text:
            failures.append({"failure": "missing_nonpromotion_language", "phrase": phrase})

    return failures, summary


def check_markdown_ledger() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    text = MD_LEDGER.read_text(encoding="utf-8")
    lower = text.lower()
    summary: dict[str, Any] = {"markdown_terms_present": True}
    for term in REQUIRED_MD_TERMS:
        if term.lower() not in lower:
            failures.append({"failure": "markdown_missing_required_term", "term": term})
            summary["markdown_terms_present"] = False
    for phrase in FORBIDDEN_READY_PHRASES:
        if phrase in lower and "blocked claim" not in lower:
            failures.append({"failure": "forbidden_ready_phrase_in_markdown", "phrase": phrase})
    return failures, summary


def check_results_consistency() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    data = read_json(FORMAL_RESULTS)
    results = data.get("results", [])
    statuses = [result.get("result_status") for result in results]
    summary = {
        "pass_source_coverage_count": statuses.count("PASS_SOURCE_COVERAGE"),
        "pass_finite_check_count": statuses.count("PASS_FINITE_CHECK"),
        "pass_partial_finite_check_count": statuses.count("PASS_PARTIAL_FINITE_CHECK"),
    }
    if summary["pass_source_coverage_count"] < 10:
        failures.append({"failure": "too_few_source_coverage_results_for_readiness_summary", **summary})
    if summary["pass_finite_check_count"] < 1:
        failures.append({"failure": "missing_finite_check_result", **summary})
    if summary["pass_partial_finite_check_count"] < 1:
        failures.append({"failure": "missing_partial_finite_check_result", **summary})
    non_promotion = data.get("non_promotion_rule", "").lower()
    for term in ["pass_source_coverage", "not theorem status", "not substrate"]:
        if term not in non_promotion:
            failures.append({"failure": "formal_results_nonpromotion_rule_missing_term", "term": term})
    return failures, summary


def run_check() -> FormationMediumReadinessResult:
    failures: list[dict[str, Any]] = []
    json_failures, json_summary = check_json_ledger()
    md_failures, md_summary = check_markdown_ledger()
    result_failures, result_summary = check_results_consistency()
    failures.extend(json_failures)
    failures.extend(md_failures)
    failures.extend(result_failures)

    support_summary = {
        **json_summary,
        **md_summary,
        **result_summary,
        "allowed_inference": "repo can support an early technical diligence conversation about evidence apparatus and roadmap discipline",
        "blocked_inference": "physical substrate readiness, native settling-law proof, engineering prototype readiness, product proof, or validated physical medium",
    }
    return FormationMediumReadinessResult(
        target_id=TARGET_ID,
        checker="formation_medium_readiness_scope_guard_v1",
        status="PASS_LEDGER_VALIDATION" if not failures else "FAILED",
        inspected_files=[
            "research_ledger/FORMATION_MEDIUM_READINESS_LEDGER.json",
            "research_ledger/FORMATION_MEDIUM_READINESS_LEDGER.md",
            "research_ledger/FORMAL_CHECK_RESULTS.json",
        ],
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_LEDGER_VALIDATION means the readiness ledger consistently separates source/finite-check progress from formal theorem, "
            "physics, substrate, engineering, and capital-readiness claims. It is not a proof, not a substrate selection, "
            "not engineering readiness, and not a product-readiness claim."
        ),
    )


def write_result(path: Path, result: FormationMediumReadinessResult) -> None:
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
