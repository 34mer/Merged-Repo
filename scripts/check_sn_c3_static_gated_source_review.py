from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "LEDGER-SN-C3-STATIC-GATED-SOURCE-REVIEW"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
REVIEW_JSON = ROOT / "research_ledger" / "SN_C3_STATIC_GATED_SOURCE_REVIEW.json"
REVIEW_MD = ROOT / "research_ledger" / "SN_C3_STATIC_GATED_SOURCE_REVIEW.md"
PRI002_JSON = ROOT / "research_ledger" / "PRI002_SCATTERING_NATIVE_SOURCE_CANDIDATES.json"
STATIC_SPINE = ROOT / "research_ledger" / "PRE_SPACETIME_STATIC_GEOMETRY_SPINE.json"

REQUIRED_STATUSES = {
    "GENERATED",
    "EXTERNAL_WEB_REVIEWED",
    "STATIC_GATED_REVIEW",
    "NOT_SOURCE_EXTRACTED",
    "NOT_SUBSTRATE_SELECTION",
    "NOT_ENGINEERING_READY",
}
REQUIRED_ROLES = {"SOURCE_REVIEW", "COMPARATOR", "STATIC_GEOMETRY_GATE", "NEGATIVE_CONTROL", "PHYSICAL_REGIME_TRIAGE"}
REQUIRED_SOURCES = {"SN-SRC-009", "SN-SRC-010"}
REQUIRED_PG_GATES = {f"PG{i}" for i in range(1, 9)}
REQUIRED_STATIC_GATES = {
    "SG0_TERMINAL_ATOM_Gr_+(0,n)",
    "SG1_STATIC_SIMPLEX_Gr_+(1,n)",
    "SG2_ORDERED_RESIDUE_SIGN",
    "SG3_PRODUCT_STATIC_BLOCK_Gr_+(1,2)^m",
    "SG4_MUTATION_TRANSPORT",
}
REQUIRED_MD_TERMS = [
    "STATIC_GATED_REVIEW",
    "Do they pass SG0–SG4?",
    "Reflection zeros / scattering zeros are tempting analogues",
    "not terminal residue atoms",
    "not ordered residue-route sign/coherence",
    "FAIL_OR_UNSUPPORTED",
    "USEFUL_NEGATIVE_CONTROL_AND_WEAK_OBSERVABLE_COMPARATOR",
]


@dataclass(frozen=True)
class SNC3StaticGatedSourceReviewResult:
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


def check_review_json() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    data = read_json(REVIEW_JSON)
    statuses = set(data.get("status", []))
    roles = set(data.get("artifact_roles", []))
    source_ids = {item.get("source_id") for item in data.get("source_basis", [])}
    pg_rows = data.get("pg_gate_assessment", [])
    static_rows = data.get("static_spine_gate_assessment", [])
    pg_ids = {str(row.get("gate", "")).split("_")[0] for row in pg_rows}
    static_ids = {row.get("gate") for row in static_rows}
    summary: dict[str, Any] = {
        "review_id": data.get("review_id"),
        "parent_priority": data.get("parent_priority"),
        "candidate_class": data.get("candidate_class"),
        "source_count": len(source_ids),
        "pg_gate_count": len(pg_rows),
        "static_gate_count": len(static_rows),
        "classification": data.get("red_team_conclusion", {}).get("classification"),
        "continue_or_demote": data.get("red_team_conclusion", {}).get("continue_or_demote"),
    }

    if data.get("parent_priority") != "PRI-002":
        failures.append({"failure": "parent_priority_mismatch", "observed": data.get("parent_priority")})
    if data.get("candidate_class") != "SN-C3_PHYSICAL_SCATTERING_MATRIX_TOPOLOGY":
        failures.append({"failure": "candidate_class_mismatch", "observed": data.get("candidate_class")})
    for status in REQUIRED_STATUSES:
        if status not in statuses:
            failures.append({"failure": "missing_status", "status": status})
    for role in REQUIRED_ROLES:
        if role not in roles:
            failures.append({"failure": "missing_artifact_role", "role": role})

    missing_sources = sorted(REQUIRED_SOURCES - source_ids)
    if missing_sources:
        failures.append({"failure": "missing_sources", "missing": missing_sources})
    for source in data.get("source_basis", []):
        for field in ["title", "venue_year", "doi", "external_review_note", "local_status"]:
            if not source.get(field):
                failures.append({"failure": "source_missing_field", "source_id": source.get("source_id"), "field": field})
        if source.get("local_status") != "EXTERNAL_WEB_REVIEWED_ONLY / NOT_SOURCE_EXTRACTED":
            failures.append({"failure": "source_status_promoted", "source_id": source.get("source_id"), "status": source.get("local_status")})

    crit = data.get("critical_review_prework", {})
    for field in ["hard_bottleneck_attacked", "thin_stick_risks", "negative_progress_risk", "why_not_convenient_drift"]:
        if not crit.get(field):
            failures.append({"failure": "missing_critical_review_prework", "field": field})
    crit_text = normalize(json.dumps(crit, ensure_ascii=False))
    for term in ["static residue spine", "thin-stick", "sg0", "sg4", "negative"]:
        if term not in crit_text:
            failures.append({"failure": "critical_review_prework_missing_term", "term": term})

    missing_pg = sorted(REQUIRED_PG_GATES - pg_ids)
    if missing_pg:
        failures.append({"failure": "missing_pg_gate_assessments", "missing": missing_pg})
    for row in pg_rows:
        for field in ["gate", "assessment", "reason", "failure_mode"]:
            if not row.get(field):
                failures.append({"failure": "pg_row_missing_field", "gate": row.get("gate"), "field": field})

    missing_static = sorted(REQUIRED_STATIC_GATES - static_ids)
    if missing_static:
        failures.append({"failure": "missing_static_gate_assessments", "missing": missing_static})
    strong_failure_count = 0
    for row in static_rows:
        for field in ["gate", "assessment", "reason", "required_before_upgrade"]:
            if not row.get(field):
                failures.append({"failure": "static_row_missing_field", "gate": row.get("gate"), "field": field})
        if "FAIL" in str(row.get("assessment", "")) or "UNSUPPORTED" in str(row.get("assessment", "")):
            strong_failure_count += 1
    if strong_failure_count < 4:
        failures.append({"failure": "static_review_not_red_team_enough", "strong_failure_count": strong_failure_count, "expected_at_least": 4})

    conclusion = data.get("red_team_conclusion", {})
    if conclusion.get("classification") != "USEFUL_NEGATIVE_CONTROL_AND_WEAK_OBSERVABLE_COMPARATOR":
        failures.append({"failure": "classification_not_negative_control", "observed": conclusion.get("classification")})
    if conclusion.get("continue_or_demote") != "CONTINUE_AS_NEGATIVE_CONTROL_AND_OBSERVABLE_COMPARATOR_ONLY":
        failures.append({"failure": "continue_or_demote_not_bounded", "observed": conclusion.get("continue_or_demote")})
    conclusion_text = normalize(json.dumps(conclusion, ensure_ascii=False))
    for term in ["fails", "sg0", "sg4", "negative-control", "ising"]:
        if term not in conclusion_text:
            failures.append({"failure": "red_team_conclusion_missing_term", "term": term})

    non_promotion = str(data.get("non_promotion_rule", "")).lower()
    for term in ["external-web-reviewed only", "does not ingest", "extract source claims", "validate scattering-native", "select a substrate", "engineering readiness"]:
        if term not in non_promotion:
            failures.append({"failure": "non_promotion_missing_term", "term": term})
    return failures, summary


def check_markdown() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    text = REVIEW_MD.read_text(encoding="utf-8")
    lower = text.lower()
    summary = {"markdown_terms_present": True}
    for term in REQUIRED_MD_TERMS:
        if term.lower() not in lower:
            failures.append({"failure": "markdown_missing_required_term", "term": term})
            summary["markdown_terms_present"] = False
    return failures, summary


def check_alignment() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    pri002 = read_json(PRI002_JSON)
    spine = read_json(STATIC_SPINE)
    pri002_class_ids = {item.get("id") for item in pri002.get("candidate_classes", [])}
    static_layer_ids = {item.get("id") for item in spine.get("static_spine_layers", [])}
    summary = {
        "pri002_has_sn_c3": "SN-C3_PHYSICAL_SCATTERING_MATRIX_TOPOLOGY" in pri002_class_ids,
        "static_spine_layer_count": len(static_layer_ids),
    }
    if "SN-C3_PHYSICAL_SCATTERING_MATRIX_TOPOLOGY" not in pri002_class_ids:
        failures.append({"failure": "pri002_missing_sn_c3_class"})
    if not {"SG0_TERMINAL_ATOM", "SG1_STATIC_SIMPLEX", "SG2_ORDERED_RESIDUE_SIGN", "SG3_PRODUCT_STATIC_BLOCK", "SG4_MUTATION_TRANSPORT"} <= static_layer_ids:
        failures.append({"failure": "static_spine_missing_required_layers"})
    return failures, summary


def run_check() -> SNC3StaticGatedSourceReviewResult:
    failures: list[dict[str, Any]] = []
    json_failures, json_summary = check_review_json()
    md_failures, md_summary = check_markdown()
    align_failures, align_summary = check_alignment()
    failures.extend(json_failures)
    failures.extend(md_failures)
    failures.extend(align_failures)
    support_summary = {
        **json_summary,
        **md_summary,
        **align_summary,
        "checked_interface": "SN-C3 physical scattering-matrix topology reviewed against PG1-PG8 and SG0-SG4 static spine",
        "allowed_inference": "SN-C3 is currently only a useful negative control and weak observable comparator under the static-spine gate",
        "blocked_inference": "source extraction, scattering-native validation, S-matrix victory, Ising/high-resonance defeat, substrate selection, settling-law proof, or engineering readiness",
    }
    return SNC3StaticGatedSourceReviewResult(
        target_id=TARGET_ID,
        checker="sn_c3_static_gated_source_review_guard_v1",
        status="PASS_LEDGER_VALIDATION" if not failures else "FAILED",
        inspected_files=[
            "research_ledger/SN_C3_STATIC_GATED_SOURCE_REVIEW.json",
            "research_ledger/SN_C3_STATIC_GATED_SOURCE_REVIEW.md",
            "research_ledger/PRI002_SCATTERING_NATIVE_SOURCE_CANDIDATES.json",
            "research_ledger/PRE_SPACETIME_STATIC_GEOMETRY_SPINE.json",
        ],
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_LEDGER_VALIDATION means SN-C3 was reviewed under PG1-PG8 and SG0-SG4 and classified only as a useful "
            "negative control / weak observable comparator. It is not source extraction, not scattering-native validation, not "
            "S-matrix victory, not Ising/high-resonance defeat, not substrate selection, not a settling-law proof, and not engineering readiness."
        ),
    )


def write_result(path: Path, result: SNC3StaticGatedSourceReviewResult) -> None:
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
