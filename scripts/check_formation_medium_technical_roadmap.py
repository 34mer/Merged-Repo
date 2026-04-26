from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "LEDGER-FORMATION-MEDIUM-TECHNICAL-ROADMAP"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
JSON_ROADMAP = ROOT / "research_ledger" / "FORMATION_MEDIUM_TECHNICAL_ROADMAP.json"
MD_ROADMAP = ROOT / "research_ledger" / "FORMATION_MEDIUM_TECHNICAL_ROADMAP.md"
READINESS_LEDGER = ROOT / "research_ledger" / "FORMATION_MEDIUM_READINESS_LEDGER.json"

REQUIRED_STATUSES = [
    "GENERATED",
    "OPEN",
    "ROADMAP_ONLY",
    "NOT_SOURCE_EXTRACTED",
    "NOT_THEOREM",
    "NOT_ENGINEERING_READY",
]

REQUIRED_QUEUE_IDS = [
    "Q1_STALE_STATUS_SWEEP",
    "Q2_FM1_SCHEMA_VALIDATION",
    "Q3_SURFACE_FINITE_MODEL_PLAN",
    "Q4_R12_R13_FORMALIZATION_PLAN",
    "Q5_PHYSICAL_REGIME_SOURCE_INTAKE_PLAN",
    "Q6_EARLY_DILIGENCE_PACKET",
]

REQUIRED_RESOURCE_TIERS = [
    "T0_CURRENT_REPO_COMPUTE",
    "T1_MODEST_RESEARCH_SUPPORT",
    "T2_CAPITALIZED_RESEARCH_PROGRAM",
]

FORBIDDEN_ALLOWED_LANGUAGE = [
    "physical substrate has been identified",
    "settling law is proven",
    "prototype ready",
    "lab-ready hardware path exists",
    "product readiness",
    "validated physical medium",
    "source coverage is theorem",
]

REQUIRED_MD_TERMS = [
    "not a source-extracted claim",
    "not a theorem",
    "not engineering readiness",
    "current repo compute",
    "capitalized research program",
    "do not do yet",
]


@dataclass(frozen=True)
class FormationMediumTechnicalRoadmapResult:
    target_id: str
    checker: str
    status: str
    inspected_files: list[str]
    support_summary: dict[str, Any]
    counterexamples: list[dict[str, Any]]
    status_boundary: str


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def check_json_roadmap() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    data = read_json(JSON_ROADMAP)
    status = set(data.get("status", []))
    summary: dict[str, Any] = {
        "near_term_queue_count": len(data.get("near_term_queue", [])),
        "capital_dependent_count": len(data.get("capital_dependent_queue", [])),
        "resource_tier_count": len(data.get("resource_tiers", [])),
    }

    for required in REQUIRED_STATUSES:
        if required not in status:
            failures.append({"failure": "missing_status", "status": required})

    tiers = {tier.get("id") for tier in data.get("resource_tiers", [])}
    for tier_id in REQUIRED_RESOURCE_TIERS:
        if tier_id not in tiers:
            failures.append({"failure": "missing_resource_tier", "tier_id": tier_id})

    queue = data.get("near_term_queue", [])
    queue_ids = [item.get("id") for item in queue]
    if queue_ids != REQUIRED_QUEUE_IDS:
        failures.append({"failure": "near_term_queue_order_mismatch", "observed": queue_ids, "expected": REQUIRED_QUEUE_IDS})
    for item in queue:
        if not item.get("exit_condition"):
            failures.append({"failure": "queue_item_missing_exit_condition", "id": item.get("id")})
        if not item.get("blocked_promotion"):
            failures.append({"failure": "queue_item_missing_blocked_promotion", "id": item.get("id")})
        if item.get("resource_tier") != "T0_CURRENT_REPO_COMPUTE":
            failures.append({"failure": "near_term_queue_item_not_t0", "id": item.get("id"), "resource_tier": item.get("resource_tier")})

    do_not_do = " ".join(data.get("do_not_do_yet", [])).lower()
    for phrase in ["physical substrate", "settling law", "hardware", "product readiness", "source coverage as theorem"]:
        if phrase not in do_not_do:
            failures.append({"failure": "do_not_do_missing_phrase", "phrase": phrase})

    all_allowed_text = " ".join(str(item.get("title", "")) + " " + str(item.get("exit_condition", "")) for item in queue).lower()
    for phrase in FORBIDDEN_ALLOWED_LANGUAGE:
        if phrase in all_allowed_text:
            failures.append({"failure": "forbidden_ready_language_in_queue", "phrase": phrase})

    return failures, summary


def check_markdown_roadmap() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    text = MD_ROADMAP.read_text(encoding="utf-8")
    lower = text.lower()
    summary = {"markdown_terms_present": True}
    for term in REQUIRED_MD_TERMS:
        if term.lower() not in lower:
            failures.append({"failure": "markdown_missing_required_term", "term": term})
            summary["markdown_terms_present"] = False
    return failures, summary


def check_readiness_alignment() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    readiness = read_json(READINESS_LEDGER)
    layers = {layer.get("id"): layer for layer in readiness.get("readiness_layers", [])}
    summary = {
        "readiness_physical_substrate": layers.get("RL4_PHYSICAL_SUBSTRATE", {}).get("current_state"),
        "readiness_settling_law": layers.get("RL5_SETTLING_LAW", {}).get("current_state"),
        "readiness_engineering": layers.get("RL6_ENGINEERING_PROTOTYPE", {}).get("current_state"),
        "readiness_capital": layers.get("RL7_CAPITAL_READINESS", {}).get("current_state"),
    }
    expected = {
        "readiness_physical_substrate": "NOT_READY",
        "readiness_settling_law": "NOT_READY",
        "readiness_engineering": "NOT_READY",
        "readiness_capital": "EARLY_TECHNICAL_ROADMAP_ONLY",
    }
    for key, value in expected.items():
        if summary.get(key) != value:
            failures.append({"failure": "roadmap_readiness_alignment_mismatch", "field": key, "observed": summary.get(key), "expected": value})
    return failures, summary


def run_check() -> FormationMediumTechnicalRoadmapResult:
    failures: list[dict[str, Any]] = []
    json_failures, json_summary = check_json_roadmap()
    md_failures, md_summary = check_markdown_roadmap()
    align_failures, align_summary = check_readiness_alignment()
    failures.extend(json_failures)
    failures.extend(md_failures)
    failures.extend(align_failures)

    support_summary = {
        **json_summary,
        **md_summary,
        **align_summary,
        "allowed_inference": "the repo has a bounded execution queue for the current low-compute phase",
        "blocked_inference": "pitch readiness, substrate selection, native settling-law proof, lab prototype readiness, or product readiness",
    }
    return FormationMediumTechnicalRoadmapResult(
        target_id=TARGET_ID,
        checker="formation_medium_technical_roadmap_guard_v1",
        status="PASS_LEDGER_VALIDATION" if not failures else "FAILED",
        inspected_files=[
            "research_ledger/FORMATION_MEDIUM_TECHNICAL_ROADMAP.json",
            "research_ledger/FORMATION_MEDIUM_TECHNICAL_ROADMAP.md",
            "research_ledger/FORMATION_MEDIUM_READINESS_LEDGER.json",
        ],
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_LEDGER_VALIDATION means the roadmap is a bounded execution queue aligned with readiness limits. "
            "It is not a proof, not a substrate selection, not engineering readiness, not capital readiness, and not a pitch deck."
        ),
    )


def write_result(path: Path, result: FormationMediumTechnicalRoadmapResult) -> None:
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
