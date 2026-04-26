from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "LEDGER-MISSION-GRADE-CRITICAL-REVIEW-DOCTRINE"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
DOCTRINE_JSON = ROOT / "research_ledger" / "MISSION_GRADE_CRITICAL_REVIEW_DOCTRINE.json"
DOCTRINE_MD = ROOT / "research_ledger" / "MISSION_GRADE_CRITICAL_REVIEW_DOCTRINE.md"
GLOBAL_MD = ROOT / "research_ledger" / "PROJECT_GLOBAL_DOCTRINE.md"
GLOBAL_REGISTRY = ROOT / "research_ledger" / "PROJECT_GLOBAL_DOCTRINE_REGISTRY.json"

REQUIRED_STATUSES = {
    "OPERATIONAL_CONTROL",
    "ACTIVE",
    "INTERNAL_DOCTRINE",
    "NOT_SOURCE_EXTRACTED",
    "NOT_THEOREM",
}

REQUIRED_ARTIFACT_ROLES = {"GUARD", "NEGATIVE_CONTROL", "CORPORATE", "MATRIX"}

REQUIRED_CRIT_IDS = {
    "CRIT-001",
    "CRIT-002",
    "CRIT-003",
    "CRIT-004",
    "CRIT-005",
    "CRIT-006",
}

REQUIRED_PREWORK_TERMS = [
    "hard bottleneck",
    "net-negative",
    "thin stick",
    "smaller",
    "falsifiable",
    "delete",
    "demote",
    "quarantine",
    "founder be wrong",
]

REQUIRED_ALLOWED_CHALLENGES = [
    "challenge the mission",
    "challenge the founder",
    "challenge the repo",
    "challenge the math",
    "challenge a theorem's applicability",
    "challenge a source interpretation",
    "challenge a route or comparator",
    "recommend deletion or demotion",
]

REQUIRED_RED_TEAM_STOPS = [
    "locally clean but globally low-value",
    "avoids the bottleneck",
    "adds concepts faster than it removes ambiguity",
    "finite check is being narratively upgraded into a theorem",
    "source coverage is being narratively upgraded into physics",
    "output would impress a casual reader while misleading a serious reviewer",
    "accumulating artifacts faster than it is eliminating uncertainty",
    "following momentum instead of making a judgment call",
]

REQUIRED_MD_TERMS = [
    "Repo discipline is not enough",
    "critical thinking and deep reasoning cycles",
    "The assistant may challenge",
    "Unconsolidated Equations",
    "Inefficient or Ornamental Math",
    "Thin-Stick Theorem Leverage",
    "Easy-Work Drift",
    "Negative Progress Risk",
    "Mission-Level Challenge",
    "Do not use validators as evidence of understanding",
]

FORBIDDEN_SELF_SATISFACTION = [
    "validators prove understanding",
    "clean commits prove progress",
    "repo hygiene is sufficient",
    "the founder cannot be challenged",
    "the mission cannot be challenged",
]


@dataclass(frozen=True)
class MissionGradeCriticalReviewResult:
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


def check_json_doctrine() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    data = read_json(DOCTRINE_JSON)
    status = set(data.get("status", []))
    roles = set(data.get("artifact_roles", []))
    crit_ids = {item.get("id") for item in data.get("what_must_be_questioned", [])}
    prework_text = "\n".join(data.get("required_prework_questions", [])).lower()
    allowed = set(data.get("allowed_challenges", []))
    stop_text = "\n".join(data.get("red_team_stop_conditions", [])).lower()
    all_text = normalize(json.dumps(data, ensure_ascii=False))
    summary: dict[str, Any] = {
        "critical_item_count": len(crit_ids),
        "prework_question_count": len(data.get("required_prework_questions", [])),
        "red_team_stop_count": len(data.get("red_team_stop_conditions", [])),
        "allowed_challenge_count": len(allowed),
    }

    for required in REQUIRED_STATUSES:
        if required not in status:
            failures.append({"failure": "missing_doctrine_status", "status": required})
    for role in REQUIRED_ARTIFACT_ROLES:
        if role not in roles:
            failures.append({"failure": "missing_artifact_role", "role": role})
    missing_crit = sorted(REQUIRED_CRIT_IDS - crit_ids)
    if missing_crit:
        failures.append({"failure": "missing_critical_review_items", "missing": missing_crit})
    for item in data.get("what_must_be_questioned", []):
        for field in ["question", "danger", "required_action"]:
            if not item.get(field):
                failures.append({"failure": "critical_review_item_missing_field", "id": item.get("id"), "field": field})
    for term in REQUIRED_PREWORK_TERMS:
        if term.lower() not in prework_text:
            failures.append({"failure": "prework_questions_missing_term", "term": term})
    missing_challenges = sorted(set(REQUIRED_ALLOWED_CHALLENGES) - allowed)
    if missing_challenges:
        failures.append({"failure": "missing_allowed_challenges", "missing": missing_challenges})
    for fragment in REQUIRED_RED_TEAM_STOPS:
        if fragment.lower() not in stop_text:
            failures.append({"failure": "missing_red_team_stop_condition", "fragment": fragment})
    for phrase in FORBIDDEN_SELF_SATISFACTION:
        if phrase in all_text:
            failures.append({"failure": "forbidden_self_satisfaction_phrase", "phrase": phrase})
    if "validators" not in str(data.get("core_rule", "")).lower() or "not substitutes for judgment" not in str(data.get("core_rule", "")).lower():
        failures.append({"failure": "core_rule_missing_validator_judgment_boundary"})
    return failures, summary


def check_markdown_doctrine() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    text = DOCTRINE_MD.read_text(encoding="utf-8")
    lower = text.lower()
    summary = {"markdown_terms_present": True}
    for term in REQUIRED_MD_TERMS:
        if term.lower() not in lower:
            failures.append({"failure": "markdown_missing_required_term", "term": term})
            summary["markdown_terms_present"] = False
    normalized = normalize(text)
    for phrase in FORBIDDEN_SELF_SATISFACTION:
        if phrase in normalized:
            failures.append({"failure": "markdown_forbidden_self_satisfaction_phrase", "phrase": phrase})
    return failures, summary


def check_global_doctrine_alignment() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    global_text = GLOBAL_MD.read_text(encoding="utf-8")
    registry = read_json(GLOBAL_REGISTRY)
    lower = global_text.lower()
    questions = "\n".join(registry.get("mandatory_questions", [])).lower()
    stops = "\n".join(registry.get("stop_conditions", [])).lower()
    summary: dict[str, Any] = {
        "global_doctrine_has_critical_rule": "mission-grade critical review rule" in lower,
        "registry_has_critical_review_file": registry.get("critical_review_doctrine_file") == "research_ledger/MISSION_GRADE_CRITICAL_REVIEW_DOCTRINE.md",
    }
    for term in ["repo discipline is not enough", "validators", "not substitutes for judgment", "challenge", "founder", "mission"]:
        if term not in lower:
            failures.append({"failure": "global_doctrine_missing_critical_term", "term": term})
    for term in ["hard bottleneck", "net-negative", "thin stick", "founder be wrong"]:
        if term not in questions:
            failures.append({"failure": "global_registry_questions_missing_critical_term", "term": term})
    for term in ["globally low-value", "avoids the bottleneck", "adds concepts faster", "following momentum"]:
        if term not in stops:
            failures.append({"failure": "global_registry_stops_missing_critical_term", "term": term})
    if "critical_review_rule" not in registry:
        failures.append({"failure": "registry_missing_critical_review_rule"})
    return failures, summary


def run_check() -> MissionGradeCriticalReviewResult:
    failures: list[dict[str, Any]] = []
    json_failures, json_summary = check_json_doctrine()
    md_failures, md_summary = check_markdown_doctrine()
    global_failures, global_summary = check_global_doctrine_alignment()
    failures.extend(json_failures)
    failures.extend(md_failures)
    failures.extend(global_failures)
    support_summary = {
        **json_summary,
        **md_summary,
        **global_summary,
        "checked_interface": "mission-grade critical review doctrine requiring reasoning beyond repo hygiene and permitting challenge to mission/founder/repo/math/routes",
        "allowed_inference": "future major work has an explicit red-team control surface for bottlenecks, thin-stick theorem leverage, easy-work drift, and negative progress risk",
        "blocked_inference": "the doctrine itself guarantees deep reasoning, proves Formation Medium, validates any route, or makes validators evidence of understanding",
    }
    return MissionGradeCriticalReviewResult(
        target_id=TARGET_ID,
        checker="mission_grade_critical_review_doctrine_guard_v1",
        status="PASS_LEDGER_VALIDATION" if not failures else "FAILED",
        inspected_files=[
            "research_ledger/MISSION_GRADE_CRITICAL_REVIEW_DOCTRINE.json",
            "research_ledger/MISSION_GRADE_CRITICAL_REVIEW_DOCTRINE.md",
            "research_ledger/PROJECT_GLOBAL_DOCTRINE.md",
            "research_ledger/PROJECT_GLOBAL_DOCTRINE_REGISTRY.json",
        ],
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_LEDGER_VALIDATION means the repo contains a mission-grade critical-review control surface requiring "
            "reasoning beyond repo hygiene and allowing challenge to the mission, founder, repo, math, theorem leverage, sources, "
            "routes, and artifacts. It is not understanding itself, not a proof, not substrate evidence, not engineering readiness, "
            "not corporate readiness, and not a substitute for actual judgment."
        ),
    )


def write_result(path: Path, result: MissionGradeCriticalReviewResult) -> None:
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
