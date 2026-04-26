from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "LEDGER-STAGE0-MATH-FIRST-PROTOCOL"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
PROTOCOL_JSON = ROOT / "research_ledger" / "FORMATION_MEDIUM_STAGE0_MATH_FIRST_PROTOCOL.json"
PROTOCOL_MD = ROOT / "research_ledger" / "FORMATION_MEDIUM_STAGE0_MATH_FIRST_PROTOCOL.md"
GLOBAL_DOCTRINE = ROOT / "research_ledger" / "PROJECT_GLOBAL_DOCTRINE.md"
GLOBAL_REGISTRY = ROOT / "research_ledger" / "PROJECT_GLOBAL_DOCTRINE_REGISTRY.json"
ROADMAP = ROOT / "research_ledger" / "FORMATION_MEDIUM_TECHNICAL_ROADMAP.json"

REQUIRED_STATUSES = {
    "OPERATIONAL_CONTROL",
    "ACTIVE",
    "MATH_FIRST_PROTOCOL",
    "NOT_SOURCE_EXTRACTED",
    "NOT_THEOREM",
}
REQUIRED_ROLES = {"GUARD", "RED_TEAM", "STATIC_GEOMETRY", "FORMAL_CHECK", "NEGATIVE_CONTROL"}
REQUIRED_STAGES = {
    "STAGE0_DEEP_MATH_ATTACK",
    "STAGE1_FORMAL_TARGETS",
    "STAGE2_LITERAL_COMPUTATION",
    "STAGE3_EMERGENCE_TRIAGE",
}
REQUIRED_TOOL_CLASSES = {
    "plain reasoning / scratch",
    "Python exact scripts",
    "Z3 / SMT",
    "Lean / Lake",
    "Aristotle",
    "Ax-Prover",
    "Sage",
    "polymake",
    "internet / external sources",
}
REQUIRED_STAGE0_TARGET_TERMS = [
    "Gr_+(0,n)",
    "Gr_+(1,n)",
    "canonical readout",
    "ordered residue route",
    "bulk object",
    "non-faithfulness",
    "settling relation",
    "falsify",
]
REQUIRED_MD_TERMS = [
    "Tools serve the math plan",
    "Tools do not choose the plan",
    "Stage 0 — Deep Math Attack",
    "Stage 1 — Formal Target Extraction",
    "Stage 2 — Literal Computation",
    "Stage 3 — Emergence Triage",
    "Z3 / SMT",
    "Lean / Lake",
    "Aristotle",
    "Ax-Prover",
    "Sage",
    "polymake",
    "STAGE0-FM-MINIMAL-STATIC-FORMAL-SKELETON",
]


@dataclass(frozen=True)
class Stage0MathFirstProtocolResult:
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


def check_protocol_json() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    data = read_json(PROTOCOL_JSON)
    statuses = set(data.get("status", []))
    roles = set(data.get("artifact_roles", []))
    stage_ids = {stage.get("id") for stage in data.get("stage_sequence", [])}
    tool_classes = {tool.get("tool_class") for tool in data.get("tool_escalation_matrix", [])}
    summary: dict[str, Any] = {
        "stage_count": len(stage_ids),
        "tool_class_count": len(tool_classes),
        "next_required_math_attack": data.get("next_required_math_attack", {}).get("id"),
        "current_static_spine": data.get("scope", {}).get("current_static_spine", []),
    }

    for status in REQUIRED_STATUSES:
        if status not in statuses:
            failures.append({"failure": "missing_status", "status": status})
    for role in REQUIRED_ROLES:
        if role not in roles:
            failures.append({"failure": "missing_artifact_role", "role": role})

    core = str(data.get("core_rule", "")).lower()
    for term in ["no major", "stage 0", "tools serve", "tools do not choose"]:
        if term not in core:
            failures.append({"failure": "core_rule_missing_term", "term": term})

    scope_text = json.dumps(data.get("scope", {}), ensure_ascii=False)
    for term in ["Formation Medium", "pre-spacetime", "Gr_+(0,n)", "Gr_+(1,n)", "n <= 7 or 8", "pattern-match"]:
        if term.lower() not in scope_text.lower():
            failures.append({"failure": "scope_missing_term", "term": term})

    missing_stages = sorted(REQUIRED_STAGES - stage_ids)
    if missing_stages:
        failures.append({"failure": "missing_stages", "missing": missing_stages})
    for stage in data.get("stage_sequence", []):
        if not stage.get("exit_condition") and stage.get("id") != "STAGE0_DEEP_MATH_ATTACK":
            failures.append({"failure": "stage_missing_exit_condition", "stage_id": stage.get("id")})
        if stage.get("id") == "STAGE0_DEEP_MATH_ATTACK":
            qtext = "\n".join(stage.get("required_questions", [])).lower()
            for term in ["mathematical object", "definitions", "smallest", "counterexample", "wrong", "thin stick", "delete"]:
                if term not in qtext:
                    failures.append({"failure": "stage0_questions_missing_term", "term": term})
            disallowed = "\n".join(stage.get("disallowed_by_default", [])).lower()
            for term in ["internet", "candidate", "validator", "physics", "symbolic", "promotion"]:
                if term not in disallowed:
                    failures.append({"failure": "stage0_disallowed_missing_term", "term": term})

    missing_tools = sorted(REQUIRED_TOOL_CLASSES - tool_classes)
    if missing_tools:
        failures.append({"failure": "missing_tool_classes", "missing": missing_tools})
    tool_text = normalize(json.dumps(data.get("tool_escalation_matrix", []), ensure_ascii=False))
    for term in ["z3 cli", "lean/lake", "configured but no submit tool exposed", "command not present", "sagemath 9.5", "polymake 4.11", "d-backed wsl", "pattern-matching physics"]:
        if term not in tool_text:
            failures.append({"failure": "tool_matrix_missing_status_or_boundary", "term": term})

    target_text = "\n".join(data.get("required_stage0_math_targets", []))
    for term in REQUIRED_STAGE0_TARGET_TERMS:
        if term.lower() not in target_text.lower():
            failures.append({"failure": "required_stage0_targets_missing_term", "term": term})

    stop_text = "\n".join(data.get("red_team_stop_conditions", [])).lower()
    for term in ["source shopping", "tools", "definitions", "sg0", "vocabulary", "actual computation", "falsify"]:
        if term not in stop_text:
            failures.append({"failure": "red_team_stop_conditions_missing_term", "term": term})

    next_attack = data.get("next_required_math_attack", {})
    if next_attack.get("id") != "STAGE0-FM-MINIMAL-STATIC-FORMAL-SKELETON":
        failures.append({"failure": "next_required_math_attack_wrong", "observed": next_attack.get("id")})
    next_text = normalize(json.dumps(next_attack, ensure_ascii=False))
    for term in ["gr_+(0,n)", "gr_+(1,n)", "n <= 7 or 8", "readout", "bulk/readout", "settling", "before any physics", "do not continue sn-c3"]:
        if term not in next_text:
            failures.append({"failure": "next_required_math_attack_missing_term", "term": term})

    non_promotion = str(data.get("non_promotion_rule", "")).lower()
    for term in ["does not prove", "define the final mathematical object", "validate any physical regime", "select a substrate", "engineering readiness", "replace actual reasoning"]:
        if term not in non_promotion:
            failures.append({"failure": "non_promotion_missing_term", "term": term})
    return failures, summary


def check_markdown() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    text = PROTOCOL_MD.read_text(encoding="utf-8")
    lower = text.lower()
    summary = {"markdown_terms_present": True}
    for term in REQUIRED_MD_TERMS:
        if term.lower() not in lower:
            failures.append({"failure": "markdown_missing_required_term", "term": term})
            summary["markdown_terms_present"] = False
    return failures, summary


def check_integration() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    doctrine = GLOBAL_DOCTRINE.read_text(encoding="utf-8")
    registry = read_json(GLOBAL_REGISTRY)
    roadmap = read_json(ROADMAP)
    doctrine_text = doctrine.lower()
    registry_text = normalize(json.dumps(registry, ensure_ascii=False))
    roadmap_text = normalize(json.dumps(roadmap, ensure_ascii=False))
    summary = {
        "global_doctrine_stage0_present": "stage 0" in doctrine_text and "math-first" in doctrine_text,
        "registry_stage0_file_present": registry.get("stage0_math_first_protocol_file") == "research_ledger/FORMATION_MEDIUM_STAGE0_MATH_FIRST_PROTOCOL.md",
        "roadmap_stage0_present": "stage0-fm-minimal-static-formal-skeleton" in roadmap_text,
    }
    # Integration is required after registration; this check intentionally fails before wiring.
    if not summary["global_doctrine_stage0_present"]:
        failures.append({"failure": "global_doctrine_missing_stage0_rule"})
    if not summary["registry_stage0_file_present"]:
        failures.append({"failure": "registry_missing_stage0_protocol_file"})
    for term in ["stage 0", "math-first", "tools serve", "stage0-fm-minimal-static-formal-skeleton"]:
        if term not in registry_text and term not in roadmap_text and term not in doctrine_text:
            failures.append({"failure": "integration_missing_term", "term": term})
    if not summary["roadmap_stage0_present"]:
        failures.append({"failure": "roadmap_missing_next_stage0_attack"})
    return failures, summary


def run_check() -> Stage0MathFirstProtocolResult:
    failures: list[dict[str, Any]] = []
    json_failures, json_summary = check_protocol_json()
    md_failures, md_summary = check_markdown()
    integration_failures, integration_summary = check_integration()
    failures.extend(json_failures)
    failures.extend(md_failures)
    failures.extend(integration_failures)
    support_summary = {
        **json_summary,
        **md_summary,
        **integration_summary,
        "checked_interface": "Stage 0 math-first protocol requiring tool-light mathematical attack before repo/source/physics expansion",
        "allowed_inference": "future major work must begin with Stage 0 math attack and explicit tool plan before Stage 1-3 execution",
        "blocked_inference": "proof of Formation Medium, final object definition, physical regime validation, substrate selection, engineering readiness, or replacement for actual reasoning",
    }
    return Stage0MathFirstProtocolResult(
        target_id=TARGET_ID,
        checker="stage0_math_first_protocol_guard_v1",
        status="PASS_LEDGER_VALIDATION" if not failures else "FAILED",
        inspected_files=[
            "research_ledger/FORMATION_MEDIUM_STAGE0_MATH_FIRST_PROTOCOL.json",
            "research_ledger/FORMATION_MEDIUM_STAGE0_MATH_FIRST_PROTOCOL.md",
            "research_ledger/PROJECT_GLOBAL_DOCTRINE.md",
            "research_ledger/PROJECT_GLOBAL_DOCTRINE_REGISTRY.json",
            "research_ledger/FORMATION_MEDIUM_TECHNICAL_ROADMAP.json",
        ],
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_LEDGER_VALIDATION means the repo now requires a tool-light Stage 0 mathematical attack before major "
            "source, physics, route, or repo-expansion work. It is not proof of Formation Medium, not a final mathematical "
            "definition, not physical validation, not substrate selection, not engineering readiness, and not a substitute for actual reasoning."
        ),
    )


def write_result(path: Path, result: Stage0MathFirstProtocolResult) -> None:
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
