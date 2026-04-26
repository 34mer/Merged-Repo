from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "LEDGER-PROJECT-GLOBAL-DOCTRINE"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
DOCTRINE_PATH = ROOT / "research_ledger" / "PROJECT_GLOBAL_DOCTRINE.md"
REGISTRY_PATH = ROOT / "research_ledger" / "PROJECT_GLOBAL_DOCTRINE_REGISTRY.json"

REQUIRED_DOCTRINE_TERMS = [
    "STATUS: OPERATIONAL_CONTROL / ACTIVE",
    "local correctness without global coherence",
    "does not have continuous total awareness",
    "Formation Medium",
    "CRBSM",
    "Route A",
    "Scattering-native",
    "High-Resonance",
    "The object is not",
    "Required Artifact Classification",
    "Mandatory Global Questions Before Long Work",
    "Required Stop Conditions",
    "Current Strategic Axis",
    "Validators do not mean",
    "founder-controlled technical spine",
    "not prove the Formation Medium",
]

REQUIRED_ROLES = {
    "OBJECT",
    "MECHANISM",
    "COMPARATOR",
    "ROUTE",
    "PROXY",
    "SOURCE_REVIEW",
    "SOURCE_EXTRACTED",
    "GUARD",
    "NEGATIVE_CONTROL",
    "MATRIX",
    "CORPORATE",
    "RESIDUAL_ORE",
    "FORMAL_CHECK",
    "ENGINEERING_GATE",
}

REQUIRED_GLOBAL_MAP_KEYS = {
    "object",
    "mechanism_proxy",
    "hardware_route",
    "law_native_comparator",
    "open_comparator_branch",
    "math_control_surface",
    "corporate_frame",
}

REQUIRED_STOP_SUBSTRINGS = [
    "procedurally correct but globally unclear",
    "route starts sounding like object",
    "generated mechanism starts sounding source-backed",
    "comparator starts sounding like default winner",
    "hardware stack starts sounding like substrate selection",
    "source review starts sounding like feasibility",
    "validator starts sounding like understanding",
    "corporate sentence hides open technical risk",
]

FORBIDDEN_PROMOTIONS = [
    "crbsm is the object",
    "route a is the object",
    "scattering is the default winner",
    "high-resonance is the default winner",
    "validators prove understanding",
    "route a is selected substrate",
    "crbsm is selected substrate",
    "formation medium is proved",
]


@dataclass(frozen=True)
class ProjectGlobalDoctrineResult:
    target_id: str
    checker: str
    status: str
    inspected_files: list[str]
    support_summary: dict[str, Any]
    counterexamples: list[dict[str, Any]]
    status_boundary: str


def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def check_doctrine_text() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {"doctrine_terms_present": []}
    if not DOCTRINE_PATH.exists():
        return [{"failure": "missing_doctrine", "path": str(DOCTRINE_PATH.relative_to(ROOT))}], summary
    text = DOCTRINE_PATH.read_text(encoding="utf-8")
    lower = text.lower()
    normalized = normalize(text)
    for term in REQUIRED_DOCTRINE_TERMS:
        if term.lower() not in lower:
            failures.append({"failure": "doctrine_missing_required_term", "term": term})
        else:
            summary["doctrine_terms_present"].append(term)
    # These exact role distinctions must remain explicit.
    for required_not_object in ["CRBSM", "Route A", "scattering-native physics", "high-resonance physics", "a validator suite", "a corporate pitch"]:
        if required_not_object.lower() not in lower:
            failures.append({"failure": "doctrine_missing_not_object_boundary", "term": required_not_object})
    for phrase in FORBIDDEN_PROMOTIONS:
        if phrase in normalized:
            failures.append({"failure": "forbidden_global_promotion_phrase", "phrase": phrase})
    return failures, summary


def check_registry() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {}
    if not REGISTRY_PATH.exists():
        return [{"failure": "missing_registry", "path": str(REGISTRY_PATH.relative_to(ROOT))}], summary
    data = read_json(REGISTRY_PATH)
    status = set(data.get("status", []))
    for required_status in ["OPERATIONAL_CONTROL", "ACTIVE", "INTERNAL_DOCTRINE", "NOT_SOURCE_EXTRACTED"]:
        if required_status not in status:
            failures.append({"failure": "registry_status_missing", "required": required_status, "observed": sorted(status)})
    if data.get("doctrine_file") != str(DOCTRINE_PATH.relative_to(ROOT)).replace("\\", "/"):
        failures.append({"failure": "registry_doctrine_file_mismatch", "observed": data.get("doctrine_file")})
    if "total awareness" not in str(data.get("assistant_total_awareness_limitation", "")).lower():
        failures.append({"failure": "registry_missing_awareness_limitation"})
    if "founder_correction_sanitized" not in data:
        failures.append({"failure": "registry_missing_founder_correction"})
    roles = {str(role.get("role")) for role in data.get("roles", [])}
    missing_roles = sorted(REQUIRED_ROLES - roles)
    extra_roles = sorted(roles - REQUIRED_ROLES)
    if missing_roles:
        failures.append({"failure": "registry_missing_roles", "missing": missing_roles})
    if extra_roles:
        failures.append({"failure": "registry_extra_roles", "extra": extra_roles})
    global_map = data.get("current_global_map", {})
    missing_keys = sorted(REQUIRED_GLOBAL_MAP_KEYS - set(global_map))
    if missing_keys:
        failures.append({"failure": "registry_missing_global_map_keys", "missing": missing_keys})
    mandatory_questions = data.get("mandatory_questions", [])
    if len(mandatory_questions) < 7:
        failures.append({"failure": "registry_too_few_mandatory_questions", "observed": len(mandatory_questions)})
    stop_text = "\n".join(data.get("stop_conditions", [])).lower()
    for fragment in REQUIRED_STOP_SUBSTRINGS:
        if fragment.lower() not in stop_text:
            failures.append({"failure": "registry_missing_stop_condition", "fragment": fragment})
    registry_text = normalize(json.dumps(data, ensure_ascii=False))
    for phrase in FORBIDDEN_PROMOTIONS:
        if phrase in registry_text:
            failures.append({"failure": "forbidden_registry_promotion_phrase", "phrase": phrase})
    summary.update({
        "registry_status": sorted(status),
        "role_count": len(roles),
        "mandatory_question_count": len(mandatory_questions),
        "stop_condition_count": len(data.get("stop_conditions", [])),
        "global_map_keys": sorted(global_map),
        "awareness_limitation_present": "assistant_total_awareness_limitation" in data,
        "founder_correction_present": "founder_correction_sanitized" in data,
    })
    return failures, summary


def run_check() -> ProjectGlobalDoctrineResult:
    failures: list[dict[str, Any]] = []
    doctrine_failures, doctrine_summary = check_doctrine_text()
    registry_failures, registry_summary = check_registry()
    failures.extend(doctrine_failures)
    failures.extend(registry_failures)
    summary = {
        **doctrine_summary,
        **registry_summary,
        "checked_interface": "global doctrine and machine-readable role registry for preserving total-project role awareness during long work",
        "allowed_inference": "future major work has a control surface for object/mechanism/comparator/route/proxy/source/guard/corporate classification",
        "blocked_inference": "the checker creates true total awareness, proves the project, validates routes, selects substrate, or replaces founder judgment",
    }
    return ProjectGlobalDoctrineResult(
        target_id=TARGET_ID,
        checker="project_global_doctrine_guard_v1",
        status="PASS_LEDGER_VALIDATION" if not failures else "FAILED",
        inspected_files=[str(DOCTRINE_PATH.relative_to(ROOT)), str(REGISTRY_PATH.relative_to(ROOT))],
        support_summary=summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_LEDGER_VALIDATION means the repo contains a compact global doctrine and role registry that explicitly acknowledges "
            "the assistant's total-awareness limitation and enforces global role vocabulary. It is not a mathematical proof, "
            "not understanding itself, not substrate evidence, not engineering readiness, not corporate readiness, and not a substitute for founder judgment."
        ),
    )


def main() -> None:
    result = run_check()
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(asdict(result), indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(asdict(result), indent=2, sort_keys=True))
    if result.status == "FAILED":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
