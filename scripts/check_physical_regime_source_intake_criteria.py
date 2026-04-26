from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "LEDGER-PHYSICAL-REGIME-SOURCE-INTAKE-CRITERIA"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
CRITERIA_JSON = ROOT / "research_ledger" / "PHYSICAL_REGIME_SOURCE_INTAKE_CRITERIA.json"
CRITERIA_MD = ROOT / "research_ledger" / "PHYSICAL_REGIME_SOURCE_INTAKE_CRITERIA.md"
ROADMAP_JSON = ROOT / "research_ledger" / "FORMATION_MEDIUM_TECHNICAL_ROADMAP.json"
HIGH_RESONANCE_PLAN = ROOT / "research_ledger" / "HIGH_RESONANCE_NATIVE_COMPARATOR_PLAN.json"
CRITICAL_DOCTRINE = ROOT / "research_ledger" / "MISSION_GRADE_CRITICAL_REVIEW_DOCTRINE.json"

REQUIRED_STATUSES = {
    "GENERATED",
    "OPEN",
    "SOURCE_INTAKE_CRITERIA",
    "NOT_SOURCE_EXTRACTED",
    "NOT_SUBSTRATE_SELECTION",
    "NOT_ENGINEERING_READY",
}
REQUIRED_ROLES = {"GUARD", "SOURCE_REVIEW", "COMPARATOR", "NEGATIVE_CONTROL", "ENGINEERING_GATE"}
REQUIRED_GATES = {
    "PG1_NATIVE_CARRIER",
    "PG2_NATIVE_ADMISSIBILITY",
    "PG3_RELAY_OR_TRANSPORT",
    "PG4_PERSISTENT_SUPPORT_IDENTITY",
    "PG5_INTRINSIC_READOUT",
    "PG6_BULK_READOUT_SEPARATION",
    "PG7_HARNESSABILITY",
    "PG8_NEGATIVE_CONTROL_CLARITY",
}
REQUIRED_TRACKS = {
    "TRACK_CRBSM": "MECHANISM_LANGUAGE",
    "TRACK_ROUTE_A": "HARDWARE_PROXY_ROUTE",
    "TRACK_SCATTERING_NATIVE": "MANDATORY_COMPARATOR",
    "TRACK_HIGH_RESONANCE_NATIVE": "POSSIBLE_BRIDGE_COMPARATOR",
    "TRACK_ISING_MACHINE": "COMBINATORIAL_MACHINE_COMPARATOR",
}
REQUIRED_REVIEW_IDS = {"PRI-001", "PRI-002", "PRI-003", "PRI-004", "PRI-005"}
REQUIRED_MD_TERMS = [
    "physical-regime triage and substrate uncertainty",
    "CRBSM = mechanism-language",
    "Route A = hardware/proxy",
    "scattering-native = mandatory comparator",
    "high-resonance = possible bridge comparator",
    "Ising machines = hardware-combinatorial",
    "persistent support identity",
    "SOURCE_EXTRACTED without ingested source",
    "WINNER_DECLARED",
]
FORBIDDEN_PROMOTION_PHRASES = [
    "substrate selected",
    "winner declared",
    "engineering ready",
    "crbsm validated",
    "route a validated",
    "high-resonance selected",
    "scattering-native selected",
]


@dataclass(frozen=True)
class PhysicalRegimeSourceIntakeCriteriaResult:
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


def check_criteria_json() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    data = read_json(CRITERIA_JSON)
    statuses = set(data.get("status", []))
    roles = set(data.get("artifact_roles", []))
    gates = {gate.get("id") for gate in data.get("global_gate_axes", [])}
    tracks = {track.get("id"): track for track in data.get("regime_tracks", [])}
    review_ids = {review.get("id") for review in data.get("review_queue", [])}
    summary: dict[str, Any] = {
        "gate_count": len(gates),
        "track_count": len(tracks),
        "review_queue_count": len(review_ids),
        "track_roles": {track_id: tracks[track_id].get("role") for track_id in tracks},
    }

    for status in REQUIRED_STATUSES:
        if status not in statuses:
            failures.append({"failure": "missing_status", "status": status})
    for role in REQUIRED_ROLES:
        if role not in roles:
            failures.append({"failure": "missing_artifact_role", "role": role})

    crit = data.get("critical_review_prework", {})
    for field in ["hard_bottleneck_attacked", "thin_stick_risks", "negative_progress_risk", "why_not_convenient_drift"]:
        if not crit.get(field):
            failures.append({"failure": "missing_critical_review_prework_field", "field": field})
    crit_text = normalize(json.dumps(crit, ensure_ascii=False))
    for term in ["physical-regime triage", "thin", "negative-progress", "convenient"]:
        if term not in crit_text:
            failures.append({"failure": "critical_review_prework_missing_term", "term": term})

    anti = str(data.get("anti_flattening_rule", "")).lower()
    for term in ["crbsm is mechanism-language", "route a is hardware/proxy", "scattering-native is a mandatory comparator", "high-resonance is a possible bridge comparator", "ising machines are hardware-combinatorial", "must not declare a winner"]:
        if term not in anti:
            failures.append({"failure": "anti_flattening_rule_missing_term", "term": term})

    missing_gates = sorted(REQUIRED_GATES - gates)
    if missing_gates:
        failures.append({"failure": "missing_global_gate_axes", "missing": missing_gates})
    for gate in data.get("global_gate_axes", []):
        for field in ["question", "required_source_evidence", "kill_condition"]:
            if not gate.get(field):
                failures.append({"failure": "gate_missing_field", "gate_id": gate.get("id"), "field": field})

    for track_id, expected_role in REQUIRED_TRACKS.items():
        track = tracks.get(track_id)
        if track is None:
            failures.append({"failure": "missing_regime_track", "track_id": track_id})
            continue
        if track.get("role") != expected_role:
            failures.append({"failure": "track_role_mismatch", "track_id": track_id, "observed": track.get("role"), "expected": expected_role})
        for field in ["intake_question", "must_find", "must_not_accept", "minimum_review_output", "kill_conditions"]:
            if not track.get(field):
                failures.append({"failure": "track_missing_field", "track_id": track_id, "field": field})
        if len(track.get("kill_conditions", [])) < 3:
            failures.append({"failure": "track_too_few_kill_conditions", "track_id": track_id})
        if len(track.get("must_not_accept", [])) < 3:
            failures.append({"failure": "track_too_few_must_not_accept", "track_id": track_id})

    missing_reviews = sorted(REQUIRED_REVIEW_IDS - review_ids)
    if missing_reviews:
        failures.append({"failure": "missing_review_queue_items", "missing": missing_reviews})
    for review in data.get("review_queue", []):
        for field in ["target_track", "question", "required_keywords", "expected_output"]:
            if not review.get(field):
                failures.append({"failure": "review_item_missing_field", "review_id": review.get("id"), "field": field})

    policy = data.get("source_promotion_policy", {})
    blocked = set(policy.get("blocked_statuses", []))
    for blocked_status in ["SOURCE_EXTRACTED without ingested source", "CHECKED without validator", "SUBSTRATE_SELECTED", "ENGINEERING_READY", "WINNER_DECLARED"]:
        if blocked_status not in blocked:
            failures.append({"failure": "source_promotion_policy_missing_blocked_status", "blocked_status": blocked_status})
    if policy.get("allowed_next_status") != "EXTERNAL_SOURCE_REVIEW or SOURCE_INTAKE_PLAN":
        failures.append({"failure": "source_promotion_policy_allowed_next_status_mismatch", "observed": policy.get("allowed_next_status")})
    if len(policy.get("minimum_for_source_extracted", [])) < 5:
        failures.append({"failure": "source_promotion_policy_too_weak"})

    json_text = normalize(json.dumps(data, ensure_ascii=False))
    for phrase in FORBIDDEN_PROMOTION_PHRASES:
        if phrase in json_text and f"not {phrase}" not in json_text and phrase.upper().replace(" ", "_") not in json_text:
            failures.append({"failure": "forbidden_promotion_phrase", "phrase": phrase})
    return failures, summary


def check_markdown() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    text = CRITERIA_MD.read_text(encoding="utf-8")
    lower = text.lower()
    summary = {"markdown_terms_present": True}
    for term in REQUIRED_MD_TERMS:
        if term.lower() not in lower:
            failures.append({"failure": "markdown_missing_required_term", "term": term})
            summary["markdown_terms_present"] = False
    return failures, summary


def check_alignment() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    roadmap = read_json(ROADMAP_JSON)
    hr_plan = read_json(HIGH_RESONANCE_PLAN)
    critical = read_json(CRITICAL_DOCTRINE)
    summary: dict[str, Any] = {
        "roadmap_q5_mentions_source_intake": False,
        "high_resonance_plan_present": bool(hr_plan.get("layered_candidates")),
        "critical_review_prework_present": bool(critical.get("required_prework_questions")),
    }
    q5 = None
    for item in roadmap.get("near_term_queue", []):
        if item.get("id") == "Q5_PHYSICAL_REGIME_SOURCE_INTAKE_PLAN":
            q5 = item
            break
    if q5 is None:
        failures.append({"failure": "roadmap_missing_q5"})
    else:
        q5_text = normalize(json.dumps(q5, ensure_ascii=False))
        summary["roadmap_q5_mentions_source_intake"] = "source-intake" in q5_text
        for term in ["source-intake", "high-resonance", "scattering-native", "route a", "ising", "without flattening"]:
            if term not in q5_text:
                failures.append({"failure": "roadmap_q5_missing_term", "term": term})
    hr_text = normalize(json.dumps(hr_plan, ensure_ascii=False))
    for term in ["crbsm is mechanism-language", "route a is hardware/proxy", "scattering-native is a mandatory comparator", "high-resonance may be the bridge"]:
        if term not in hr_text:
            failures.append({"failure": "high_resonance_plan_missing_role_term", "term": term})
    critical_text = normalize(json.dumps(critical, ensure_ascii=False))
    for term in ["hard bottleneck", "thin stick", "net-negative", "founder be wrong"]:
        if term not in critical_text:
            failures.append({"failure": "critical_doctrine_missing_prework_term", "term": term})
    return failures, summary


def run_check() -> PhysicalRegimeSourceIntakeCriteriaResult:
    failures: list[dict[str, Any]] = []
    json_failures, json_summary = check_criteria_json()
    md_failures, md_summary = check_markdown()
    align_failures, align_summary = check_alignment()
    failures.extend(json_failures)
    failures.extend(md_failures)
    failures.extend(align_failures)
    support_summary = {
        **json_summary,
        **md_summary,
        **align_summary,
        "checked_interface": "physical-regime source-intake criteria for CRBSM, Route A, scattering-native, high-resonance, and Ising-machine tracks",
        "allowed_inference": "future source review has role-separated criteria, PG1-PG8 gates, review queue, and promotion policy",
        "blocked_inference": "source ingestion, source extraction, CRBSM validation, Route A feasibility, scattering/high-resonance/Ising winner declaration, substrate selection, settling-law proof, or engineering readiness",
    }
    return PhysicalRegimeSourceIntakeCriteriaResult(
        target_id=TARGET_ID,
        checker="physical_regime_source_intake_criteria_guard_v1",
        status="PASS_LEDGER_VALIDATION" if not failures else "FAILED",
        inspected_files=[
            "research_ledger/PHYSICAL_REGIME_SOURCE_INTAKE_CRITERIA.json",
            "research_ledger/PHYSICAL_REGIME_SOURCE_INTAKE_CRITERIA.md",
            "research_ledger/FORMATION_MEDIUM_TECHNICAL_ROADMAP.json",
            "research_ledger/HIGH_RESONANCE_NATIVE_COMPARATOR_PLAN.json",
            "research_ledger/MISSION_GRADE_CRITICAL_REVIEW_DOCTRINE.json",
        ],
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_LEDGER_VALIDATION means the repo contains role-separated physical-regime source-intake criteria and kill gates. "
            "It is not source ingestion, not source extraction, not CRBSM validation, not Route A feasibility, not scattering-native "
            "or high-resonance winner status, not Ising-machine validation, not substrate selection, not a settling-law proof, and not engineering readiness."
        ),
    )


def write_result(path: Path, result: PhysicalRegimeSourceIntakeCriteriaResult) -> None:
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
