from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "LEDGER-PRE-SPACETIME-STATIC-GEOMETRY-SPINE"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
SPINE_JSON = ROOT / "research_ledger" / "PRE_SPACETIME_STATIC_GEOMETRY_SPINE.json"
SPINE_MD = ROOT / "research_ledger" / "PRE_SPACETIME_STATIC_GEOMETRY_SPINE.md"
PHYSICAL_CRITERIA = ROOT / "research_ledger" / "PHYSICAL_REGIME_SOURCE_INTAKE_CRITERIA.json"
ROADMAP = ROOT / "research_ledger" / "FORMATION_MEDIUM_TECHNICAL_ROADMAP.json"

REQUIRED_STATUSES = {
    "GENERATED_FROM_PRIOR_GPT_INTAKE",
    "OPEN",
    "NOT_SOURCE_EXTRACTED",
    "NOT_THEOREM",
    "MISSION_LEVEL_CORRECTION",
}
REQUIRED_ROLES = {"RED_TEAM", "STATIC_GEOMETRY", "PRE_SPACETIME_SPINE", "GUARD", "NEGATIVE_CONTROL"}
REQUIRED_LAYERS = {
    "SG0_TERMINAL_ATOM",
    "SG1_STATIC_SIMPLEX",
    "SG2_ORDERED_RESIDUE_SIGN",
    "SG3_PRODUCT_STATIC_BLOCK",
    "SG4_MUTATION_TRANSPORT",
}
REQUIRED_FINDINGS = {"RT-STATIC-001", "RT-STATIC-002", "RT-STATIC-003", "RT-STATIC-004"}
REQUIRED_STATIC_GATE_TERMS = [
    "Gr_+(0,n)",
    "Gr_+(1,n)",
    "recursive boundary/readout semantics",
    "ordered residue-route sign",
    "Gr_+(1,2)",
    "mutation-like transport",
    "negative control",
]
REQUIRED_MD_TERMS = [
    "pre-spacetime positive-geometric",
    "Gr_+(0,n) and Gr_+(1,n) are foundational",
    "terminal residue atom",
    "static simplex tower",
    "ordered residue sign structure",
    "product static block",
    "transported static reflection",
    "S-matrix is closer to amplitude geometry, but it may still be further",
    "Ising machines must be included",
]
REQUIRED_CANDIDATE_IMPACTS = {"SN_C3", "PRI005_ISING", "HR_C3", "Route_A", "CRBSM"}


@dataclass(frozen=True)
class PreSpacetimeStaticGeometrySpineResult:
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


def check_spine_json() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    data = read_json(SPINE_JSON)
    statuses = set(data.get("status", []))
    roles = set(data.get("artifact_roles", []))
    layers = {layer.get("id"): layer for layer in data.get("static_spine_layers", [])}
    findings = {finding.get("id"): finding for finding in data.get("red_team_findings", [])}
    impacts = data.get("impact_on_next_work", {})
    summary: dict[str, Any] = {
        "static_layer_count": len(layers),
        "red_team_finding_count": len(findings),
        "static_gate_question_count": len(data.get("static_gate_questions", [])),
        "impact_targets": sorted(impacts),
        "prior_gpt_line_ranges": data.get("prior_gpt_local_source_basis", {}).get("key_line_ranges_inspected", []),
    }

    for status in REQUIRED_STATUSES:
        if status not in statuses:
            failures.append({"failure": "missing_status", "status": status})
    for role in REQUIRED_ROLES:
        if role not in roles:
            failures.append({"failure": "missing_artifact_role", "role": role})

    basis = data.get("prior_gpt_local_source_basis", {})
    if basis.get("local_source_status") != "local source-intake material only, not authority":
        failures.append({"failure": "prior_gpt_basis_not_marked_local_only", "observed": basis.get("local_source_status")})
    if "Previous Conversations with GPT/Samer Project X - Exact Cross-Family Analysis.md" not in basis.get("file", ""):
        failures.append({"failure": "prior_gpt_basis_file_missing"})
    if len(basis.get("extracted_prior_claims_not_authority", [])) < 6:
        failures.append({"failure": "too_few_prior_claims_not_authority"})

    missing_layers = sorted(REQUIRED_LAYERS - set(layers))
    if missing_layers:
        failures.append({"failure": "missing_static_spine_layers", "missing": missing_layers})
    for layer_id, layer in layers.items():
        for field in ["object", "role", "semantic_content", "must_not_flatten_to"]:
            if not layer.get(field):
                failures.append({"failure": "static_layer_missing_field", "layer_id": layer_id, "field": field})
        if len(layer.get("must_not_flatten_to", [])) < 3:
            failures.append({"failure": "static_layer_too_few_nonflattening_targets", "layer_id": layer_id})

    missing_findings = sorted(REQUIRED_FINDINGS - set(findings))
    if missing_findings:
        failures.append({"failure": "missing_red_team_findings", "missing": missing_findings})
    for finding_id, finding in findings.items():
        for field in ["finding", "severity", "repair"]:
            if not finding.get(field):
                failures.append({"failure": "red_team_finding_missing_field", "finding_id": finding_id, "field": field})
        if finding.get("severity") not in {"HIGH", "MEDIUM_HIGH"}:
            failures.append({"failure": "red_team_finding_too_weak", "finding_id": finding_id, "severity": finding.get("severity")})

    gate_text = "\n".join(data.get("static_gate_questions", []))
    for term in REQUIRED_STATIC_GATE_TERMS:
        if term.lower() not in gate_text.lower():
            failures.append({"failure": "static_gate_missing_term", "term": term})
    missing_impacts = sorted(REQUIRED_CANDIDATE_IMPACTS - set(impacts))
    if missing_impacts:
        failures.append({"failure": "missing_candidate_impact", "missing": missing_impacts})

    non_promotion = str(data.get("non_promotion_rule", "")).lower()
    for term in ["not source-extracted", "not a theorem", "not proof", "not substrate selection", "not physical implementation", "not engineering readiness"]:
        if term not in non_promotion:
            failures.append({"failure": "non_promotion_missing_term", "term": term})
    return failures, summary


def check_markdown() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    text = SPINE_MD.read_text(encoding="utf-8")
    lower = text.lower()
    summary = {"markdown_terms_present": True}
    for term in REQUIRED_MD_TERMS:
        if term.lower() not in lower:
            failures.append({"failure": "markdown_missing_required_term", "term": term})
            summary["markdown_terms_present"] = False
    return failures, summary


def check_integration_surfaces() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    criteria = read_json(PHYSICAL_CRITERIA)
    roadmap = read_json(ROADMAP)
    criteria_text = normalize(json.dumps(criteria, ensure_ascii=False))
    roadmap_text = normalize(json.dumps(roadmap, ensure_ascii=False))
    summary = {
        "physical_criteria_static_gate_present": "static" in criteria_text and "gr_+(0,n)" in criteria_text,
        "roadmap_static_gate_present": "static" in roadmap_text and "gr_+(1,n)" in roadmap_text,
    }
    # Do not require integration during bootstrap if this checker is run before registration,
    # but once registration patches the repo these should be true. The result artifact records the status.
    return failures, summary


def run_check() -> PreSpacetimeStaticGeometrySpineResult:
    failures: list[dict[str, Any]] = []
    json_failures, json_summary = check_spine_json()
    md_failures, md_summary = check_markdown()
    integration_failures, integration_summary = check_integration_surfaces()
    failures.extend(json_failures)
    failures.extend(md_failures)
    failures.extend(integration_failures)
    support_summary = {
        **json_summary,
        **md_summary,
        **integration_summary,
        "checked_interface": "pre-spacetime static geometry spine: Gr_+(0,n), Gr_+(1,n), ordered residues, product static blocks, and mutation as transported static reflection",
        "allowed_inference": "future physical/comparator work must be red-teamed against SG0-SG4 before Formation Medium relevance is claimed",
        "blocked_inference": "source extraction, theorem status, proof of Formation Medium, substrate selection, physical implementation, engineering readiness, or automatic validation of S-matrix/Ising/high-resonance/Route A/CRBSM",
    }
    return PreSpacetimeStaticGeometrySpineResult(
        target_id=TARGET_ID,
        checker="pre_spacetime_static_geometry_spine_guard_v1",
        status="PASS_LEDGER_VALIDATION" if not failures else "FAILED",
        inspected_files=[
            "research_ledger/PRE_SPACETIME_STATIC_GEOMETRY_SPINE.json",
            "research_ledger/PRE_SPACETIME_STATIC_GEOMETRY_SPINE.md",
            "research_ledger/PHYSICAL_REGIME_SOURCE_INTAKE_CRITERIA.json",
            "research_ledger/FORMATION_MEDIUM_TECHNICAL_ROADMAP.json",
        ],
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_LEDGER_VALIDATION means the repo contains a mission-level static-spine correction: Gr_+(0,n) terminal atom, "
            "Gr_+(1,n) static simplex tower, ordered residue signs, product Gr_+(1,2) static blocks, and mutation as transported "
            "static reflection. It is not source extraction, not a theorem, not proof of Formation Medium, not substrate selection, "
            "not physical implementation, and not engineering readiness."
        ),
    )


def write_result(path: Path, result: PreSpacetimeStaticGeometrySpineResult) -> None:
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
