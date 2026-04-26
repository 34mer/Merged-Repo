from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "LEDGER-PRI001-HIGH-RESONANCE-SOURCE-CANDIDATES"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
CANDIDATES_JSON = ROOT / "research_ledger" / "PRI001_HIGH_RESONANCE_SOURCE_CANDIDATES.json"
CANDIDATES_MD = ROOT / "research_ledger" / "PRI001_HIGH_RESONANCE_SOURCE_CANDIDATES.md"
INTAKE_CRITERIA_JSON = ROOT / "research_ledger" / "PHYSICAL_REGIME_SOURCE_INTAKE_CRITERIA.json"

REQUIRED_STATUSES = {
    "GENERATED",
    "OPEN",
    "EXTERNAL_WEB_REVIEWED",
    "NOT_SOURCE_EXTRACTED",
    "NOT_SUBSTRATE_SELECTION",
    "NOT_ENGINEERING_READY",
}
REQUIRED_CLASSES = {
    "HR-C1_PHOTONIC_BIC_AND_TOPOLOGICAL_BIC",
    "HR-C2_TOPOLOGICAL_POLARITON_AND_TOPOLOGICAL_LASER_ARRAYS",
    "HR-C3_CAVITY_MAGNON_POLARITON_AND_MAGNON_PHONON_HYBRIDS",
    "HR-C4_MECHANICAL_AND_PHONONIC_BIC_RESONATORS",
}
REQUIRED_SOURCE_IDS = {f"HR-SRC-{i:03d}" for i in range(1, 12)}
REQUIRED_MD_TERMS = [
    "EXTERNAL_WEB_REVIEWED",
    "NOT_SOURCE_EXTRACTED",
    "High-resonance = possible bridge comparator",
    "high-Q resonance is not native settling law",
    "persistent support/channel identity",
    "Do Not Do Next",
]
FORBIDDEN_PROMOTIONS = [
    "high-resonance winner",
    "selected substrate",
    "engineering-ready",
    "native settling law by default",
    "canonical Formation Medium readout",
]


@dataclass(frozen=True)
class PRI001HighResonanceSourceCandidatesResult:
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


def check_candidates_json() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    data = read_json(CANDIDATES_JSON)
    statuses = set(data.get("status", []))
    classes = {item.get("id"): item for item in data.get("candidate_classes", [])}
    sources = {item.get("id"): item for item in data.get("source_candidates", [])}
    summary: dict[str, Any] = {
        "candidate_class_count": len(classes),
        "source_candidate_count": len(sources),
        "class_ids": sorted(classes),
        "source_ids": sorted(sources),
    }

    for status in REQUIRED_STATUSES:
        if status not in statuses:
            failures.append({"failure": "missing_status", "status": status})
    if data.get("priority_item") != "PRI-001":
        failures.append({"failure": "priority_item_mismatch", "observed": data.get("priority_item")})

    crit = data.get("critical_review_prework", {})
    for field in ["hard_bottleneck_attacked", "thin_stick_risks", "negative_progress_risk", "why_not_convenient_drift"]:
        if not crit.get(field):
            failures.append({"failure": "missing_critical_review_prework", "field": field})
    crit_text = normalize(json.dumps(crit, ensure_ascii=False))
    for term in ["persistent support", "thin", "negative", "convenient"]:
        if term not in crit_text:
            failures.append({"failure": "critical_review_prework_missing_term", "term": term})

    anti = str(data.get("anti_flattening_rule", "")).lower()
    for term in ["possible bridge comparator", "not crbsm", "not route a", "not selected substrate", "not native settling law"]:
        if term not in anti:
            failures.append({"failure": "anti_flattening_rule_missing_term", "term": term})

    missing_classes = sorted(REQUIRED_CLASSES - set(classes))
    if missing_classes:
        failures.append({"failure": "missing_candidate_classes", "missing": missing_classes})
    for class_id, item in classes.items():
        if len(item.get("pg_gate_tags", [])) < 5:
            failures.append({"failure": "candidate_class_too_few_pg_tags", "class_id": class_id})
        if len(item.get("kill_notes", [])) < 4:
            failures.append({"failure": "candidate_class_too_few_kill_notes", "class_id": class_id})
        if not item.get("source_candidates"):
            failures.append({"failure": "candidate_class_missing_sources", "class_id": class_id})
        for source_id in item.get("source_candidates", []):
            if source_id not in sources:
                failures.append({"failure": "candidate_class_references_unknown_source", "class_id": class_id, "source_id": source_id})

    missing_sources = sorted(REQUIRED_SOURCE_IDS - set(sources))
    if missing_sources:
        failures.append({"failure": "missing_source_candidates", "missing": missing_sources})
    for source_id, item in sources.items():
        for field in ["title", "authors_short", "venue_year", "doi", "track_relevance", "candidate_value", "blocked_inference"]:
            if not item.get(field):
                failures.append({"failure": "source_candidate_missing_field", "source_id": source_id, "field": field})
        doi = str(item.get("doi", ""))
        if not doi or "." not in doi or "/" not in doi:
            failures.append({"failure": "source_candidate_bad_doi", "source_id": source_id, "doi": doi})
        blocked = str(item.get("blocked_inference", "")).lower()
        if "not" not in blocked:
            failures.append({"failure": "source_candidate_blocked_inference_not_explicit", "source_id": source_id})

    policy = data.get("next_action_policy", {})
    policy_text = normalize(json.dumps(policy, ensure_ascii=False))
    for term in ["choose one candidate class", "do_not_do_next", "declare high-resonance winner", "source_extracted_claims"]:
        if term.replace("_", " ") not in policy_text and term not in policy_text:
            failures.append({"failure": "next_action_policy_missing_term", "term": term})

    non_promotion = str(data.get("non_promotion_rule", "")).lower()
    for term in ["does not ingest", "extract source claims", "validate high-resonance", "select a substrate", "engineering readiness"]:
        if term not in non_promotion:
            failures.append({"failure": "non_promotion_rule_missing_term", "term": term})
    return failures, summary


def check_markdown() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    text = CANDIDATES_MD.read_text(encoding="utf-8")
    lower = text.lower()
    summary = {"markdown_terms_present": True}
    for term in REQUIRED_MD_TERMS:
        if term.lower() not in lower:
            failures.append({"failure": "markdown_missing_required_term", "term": term})
            summary["markdown_terms_present"] = False
    normalized = normalize(text)
    # Allow forbidden phrases only when inside explicit negations / do-not-do / kill notes.
    for phrase in FORBIDDEN_PROMOTIONS:
        if phrase in normalized and f"not {phrase}" not in normalized and "do not" not in normalized:
            failures.append({"failure": "markdown_forbidden_unblocked_promotion", "phrase": phrase})
    return failures, summary


def check_intake_alignment() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    criteria = read_json(INTAKE_CRITERIA_JSON)
    review_ids = {item.get("id") for item in criteria.get("review_queue", [])}
    tracks = {item.get("id"): item for item in criteria.get("regime_tracks", [])}
    summary = {
        "pri001_in_intake_criteria": "PRI-001" in review_ids,
        "high_resonance_track_role": tracks.get("TRACK_HIGH_RESONANCE_NATIVE", {}).get("role"),
    }
    if "PRI-001" not in review_ids:
        failures.append({"failure": "intake_criteria_missing_pri001"})
    if tracks.get("TRACK_HIGH_RESONANCE_NATIVE", {}).get("role") != "POSSIBLE_BRIDGE_COMPARATOR":
        failures.append({"failure": "high_resonance_track_role_mismatch", "observed": tracks.get("TRACK_HIGH_RESONANCE_NATIVE", {}).get("role")})
    return failures, summary


def run_check() -> PRI001HighResonanceSourceCandidatesResult:
    failures: list[dict[str, Any]] = []
    json_failures, json_summary = check_candidates_json()
    md_failures, md_summary = check_markdown()
    align_failures, align_summary = check_intake_alignment()
    failures.extend(json_failures)
    failures.extend(md_failures)
    failures.extend(align_failures)
    support_summary = {
        **json_summary,
        **md_summary,
        **align_summary,
        "checked_interface": "PRI-001 sourced high-resonance candidate list under PG1-PG8 intake criteria",
        "allowed_inference": "the repo has an external-web-reviewed candidate queue for high-resonance source review",
        "blocked_inference": "source ingestion, source extraction, high-resonance validation, Route A validation, CRBSM validation, scattering-native defeat, substrate selection, settling-law proof, or engineering readiness",
    }
    return PRI001HighResonanceSourceCandidatesResult(
        target_id=TARGET_ID,
        checker="pri001_high_resonance_source_candidates_guard_v1",
        status="PASS_LEDGER_VALIDATION" if not failures else "FAILED",
        inspected_files=[
            "research_ledger/PRI001_HIGH_RESONANCE_SOURCE_CANDIDATES.json",
            "research_ledger/PRI001_HIGH_RESONANCE_SOURCE_CANDIDATES.md",
            "research_ledger/PHYSICAL_REGIME_SOURCE_INTAKE_CRITERIA.json",
        ],
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_LEDGER_VALIDATION means the repo has a bounded PRI-001 high-resonance source-candidate queue with PG tags, "
            "DOI-backed external candidates, kill notes, and anti-promotion boundaries. It is not source ingestion, not source "
            "extraction, not high-resonance validation, not CRBSM or Route A validation, not substrate selection, not a settling-law "
            "proof, and not engineering readiness."
        ),
    )


def write_result(path: Path, result: PRI001HighResonanceSourceCandidatesResult) -> None:
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
