from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "LEDGER-ROUTE-A-SOURCE-REVIEW-PLAN"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
PLAN_PATH = ROOT / "research_ledger" / "ROUTE_A_TOPOELECTRICAL_MICROWAVE_SOURCE_REVIEW_PLAN.md"

REQUIRED_TERMS = [
    "STATUS: GENERATED / OPEN / SOURCE_REVIEW_PLAN",
    "SOURCE_STATUS: EXTERNAL_SOURCE_NEEDED",
    "PROMOTION_STATUS: BLOCKED",
    "DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json",
    "not a source-extracted claim",
    "not engineering feasibility",
    "not a selected substrate",
    "not IP",
    "not corporate/investor language",
    "topoelectrical",
    "topological circuit",
    "superconducting microwave resonator/coupler",
    "boundary/readout",
    "transport/coupling",
    "NC-006",
    "NC-007",
    "NC-008",
    "G4 = READOUT_FAITHFULNESS_UNKNOWN",
    "G9 = EQUALITY_UNKNOWN",
    "SOURCE_REVIEW_NEEDED",
    "DO_NOT_PROMOTE",
    "FEASIBLE_ENGINEERING",
    "SELECTED_SUBSTRATE",
    "PROTOTYPE_READY",
    "INVESTOR_READY",
    "Kill Conditions",
    "Unsafe external sentence",
]

REQUIRED_REVIEW_TARGETS = [
    "Topolectrical Circuits",
    "Topolectrical-circuit realization of topological corner modes",
    "Tunable coupling of transmission-line microwave resonators mediated by an rf SQUID",
    "Tunable Superconducting Cavity using Superconducting Quantum Interference Device Metamaterials",
    "Coherent microwave-photon-mediated coupling",
    "Tunable Coupling Architecture for Fixed-Frequency Transmon Superconducting Qubits",
]

FORBIDDEN_ASSERTIVE_PROMOTIONS = [
    "route a is feasible engineering",
    "route a is selected substrate",
    "route a is prototype ready",
    "route a is investor ready",
    "route a proves formation medium",
    "topoelectrical circuits prove formation medium",
    "superconducting microwave couplers prove formation medium",
    "route a is engineering readiness",
    "route a is product readiness",
]


@dataclass(frozen=True)
class RouteASourceReviewPlanResult:
    target_id: str
    checker: str
    status: str
    inspected_file: str
    support_summary: dict[str, Any]
    counterexamples: list[dict[str, Any]]
    status_boundary: str


def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def check_plan() -> RouteASourceReviewPlanResult:
    failures: list[dict[str, Any]] = []
    if not PLAN_PATH.exists():
        failures.append({"failure": "missing_route_a_plan", "path": str(PLAN_PATH.relative_to(ROOT))})
        text = ""
    else:
        text = PLAN_PATH.read_text(encoding="utf-8")
    lower = text.lower()
    normalized = normalize(text)

    terms_present: list[str] = []
    for term in REQUIRED_TERMS:
        if term.lower() not in lower:
            failures.append({"failure": "missing_required_route_a_guard_term", "term": term})
        else:
            terms_present.append(term)

    targets_present: list[str] = []
    for target in REQUIRED_REVIEW_TARGETS:
        if target.lower() not in lower:
            failures.append({"failure": "missing_required_source_review_target", "target": target})
        else:
            targets_present.append(target)

    # Avoid false positives on explicitly unsafe/forbidden lists by only checking assertive phrases
    # that should never occur as ordinary prose in this plan.
    for phrase in FORBIDDEN_ASSERTIVE_PROMOTIONS:
        if phrase in normalized:
            failures.append({"failure": "forbidden_assertive_route_a_promotion", "phrase": phrase})

    # Ensure the plan has explicit route-status boundaries and does not allow promotion statuses as outputs.
    forbidden_status_block_required = [
        "forbidden route-status updates at this stage",
        "feasible_engineering",
        "selected_substrate",
        "prototype_ready",
        "investor_ready",
    ]
    for term in forbidden_status_block_required:
        if term not in normalized:
            failures.append({"failure": "missing_forbidden_status_boundary", "term": term})

    # Ensure allowed route-status updates are cautious only.
    for term in ["source_reviewed_no_promotion", "analog_demo_only", "negative_control_only", "continue_as_candidate", "reject_route_a"]:
        if term not in normalized:
            failures.append({"failure": "missing_allowed_cautious_status", "term": term})

    summary: dict[str, Any] = {
        "required_terms_present_count": len(terms_present),
        "required_terms_total": len(REQUIRED_TERMS),
        "review_targets_present_count": len(targets_present),
        "review_targets_total": len(REQUIRED_REVIEW_TARGETS),
        "checked_interface": "Route A source-review plan guard for review-only status, source-needed gates, negative-control risks, and non-promotion boundaries",
        "allowed_inference": "Route A is a generated/open source-review queue with explicit review targets and negative-control risks",
        "blocked_inference": "engineering feasibility, selected substrate, prototype readiness, product readiness, investor readiness, or Formation Medium proof",
        "source_review_layers": ["topoelectrical boundary/readout", "superconducting microwave transport/coupling", "hybrid interface"],
        "required_negative_controls": ["NC-006", "NC-007", "NC-008"],
        "required_gates": ["G4", "G8", "G9"],
    }

    return RouteASourceReviewPlanResult(
        target_id=TARGET_ID,
        checker="route_a_source_review_plan_guard_v1",
        status="PASS_LEDGER_VALIDATION" if not failures else "FAILED",
        inspected_file=str(PLAN_PATH.relative_to(ROOT)),
        support_summary=summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_LEDGER_VALIDATION means the Route A source-review plan preserves review-only status, "
            "source-needed gates, explicit negative-control risks, and blocked promotion boundaries. "
            "It is not a mathematical proof, not substrate evidence, not engineering readiness, "
            "not prototype readiness, not product readiness, and not investor readiness."
        ),
    )


def write_result(path: Path, result: RouteASourceReviewPlanResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(result), indent=2, sort_keys=True), encoding="utf-8")


def main() -> None:
    result = check_plan()
    write_result(RESULT_PATH, result)
    print(json.dumps(asdict(result), indent=2, sort_keys=True))
    if result.status == "FAILED":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
