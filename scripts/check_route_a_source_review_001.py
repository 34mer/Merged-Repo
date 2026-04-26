from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "LEDGER-ROUTE-A-SOURCE-REVIEW-001"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
REVIEW_MD = ROOT / "research_ledger" / "ROUTE_A_SOURCE_REVIEW_001.md"
REVIEW_JSON = ROOT / "research_ledger" / "ROUTE_A_SOURCE_REVIEW_001.json"
MATRIX = ROOT / "research_ledger" / "FORMATION_MEDIUM_ENGINEERING_GATE_MATRIX_001.json"

REQUIRED_MD_TERMS = [
    "STATUS: GENERATED / OPEN / EXTERNAL_SOURCE_REVIEW",
    "NOT_SOURCE_EXTRACTED_TO_CORPUS",
    "PROMOTION_STATUS: BLOCKED",
    "DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json",
    "SOURCE_REVIEWED_CONTINUE_AS_CANDIDATE",
    "READOUT_FAITHFULNESS_UNKNOWN",
    "EQUALITY_UNKNOWN",
    "CENTRAL_OPEN_GATE_WITH_SOURCE_CLUES",
    "not engineering feasibility",
    "not a selected substrate",
    "not a prototype architecture",
    "not corporate/investor language",
    "high-resonance / mesoscopic resonance-native",
    "CRBSM generated proxy",
]

REQUIRED_SOURCE_IDS = {"RA-SRC-001", "RA-SRC-002", "RA-SRC-003", "RA-SRC-004", "RA-SRC-005", "RA-SRC-006"}
REQUIRED_DOIS = {
    "10.1038/s42005-018-0035-2",
    "10.1038/s41567-018-0246-1",
    "10.1140/epjqt/s40507-016-0048-2",
    "10.1038/s41598-019-40891-1",
    "10.1038/s41467-019-10798-6",
    "10.1103/PhysRevLett.127.080505",
}
FORBIDDEN_ASSERTIONS = [
    "route a is feasible engineering",
    "route a is selected substrate",
    "route a is prototype ready",
    "route a is investor ready",
    "route a implements crbsm",
    "route a implements formation medium",
    "therefore high-resonance wins by default",
    "therefore scattering wins by default",
    "we assume high-resonance wins by default",
    "we assume scattering wins by default",
]

@dataclass(frozen=True)
class RouteASourceReviewResult:
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


def run_check() -> RouteASourceReviewResult:
    failures: list[dict[str, Any]] = []
    if not REVIEW_MD.exists():
        failures.append({"failure": "missing_review_md", "path": str(REVIEW_MD.relative_to(ROOT))})
        md = ""
    else:
        md = REVIEW_MD.read_text(encoding="utf-8")
    md_lower = md.lower()
    md_norm = normalize(md)
    for term in REQUIRED_MD_TERMS:
        if term.lower() not in md_lower:
            failures.append({"failure": "missing_required_review_guard_term", "term": term})
    for phrase in FORBIDDEN_ASSERTIONS:
        if phrase in md_norm:
            failures.append({"failure": "forbidden_assertive_review_promotion", "phrase": phrase})

    if not REVIEW_JSON.exists():
        failures.append({"failure": "missing_review_json", "path": str(REVIEW_JSON.relative_to(ROOT))})
        review: dict[str, Any] = {}
    else:
        review = read_json(REVIEW_JSON)
    status = set(review.get("status", []))
    for required in ["GENERATED", "OPEN", "EXTERNAL_SOURCE_REVIEW", "NOT_SOURCE_EXTRACTED_TO_CORPUS", "BLOCKED"]:
        if required not in status:
            failures.append({"failure": "json_status_missing", "required": required, "observed": sorted(status)})
    sources = review.get("reviewed_sources", [])
    source_ids = {str(s.get("id")) for s in sources}
    dois = {str(s.get("doi")) for s in sources}
    missing_source_ids = sorted(REQUIRED_SOURCE_IDS - source_ids)
    missing_dois = sorted(REQUIRED_DOIS - dois)
    if missing_source_ids:
        failures.append({"failure": "missing_review_source_ids", "missing": missing_source_ids})
    if missing_dois:
        failures.append({"failure": "missing_review_dois", "missing": missing_dois})
    if review.get("route_verdict") != "SOURCE_REVIEWED_CONTINUE_AS_CANDIDATE":
        failures.append({"failure": "unexpected_route_verdict", "observed": review.get("route_verdict")})

    if not MATRIX.exists():
        failures.append({"failure": "missing_engineering_matrix", "path": str(MATRIX.relative_to(ROOT))})
        matrix = {}
    else:
        matrix = read_json(MATRIX)
    route_a = [row for row in matrix.get("matrix", []) if row.get("route_id") == "ROUTE-A"]
    if len(route_a) != 9:
        failures.append({"failure": "route_a_gate_row_count_mismatch", "observed": len(route_a), "expected": 9})
    expected_status = review.get("gate_status_after_review", {})
    for row in route_a:
        gid = row.get("gate_id")
        if row.get("status") != expected_status.get(gid):
            failures.append({"failure": "route_a_gate_status_mismatch", "gate_id": gid, "observed": row.get("status"), "expected": expected_status.get(gid)})
        if row.get("promotion_status") != "BLOCKED":
            failures.append({"failure": "route_a_gate_not_blocked", "gate_id": gid, "promotion_status": row.get("promotion_status")})
        if row.get("source_status") != "EXTERNAL_SOURCE_REVIEWED_NOT_INGESTED":
            failures.append({"failure": "route_a_source_status_wrong", "gate_id": gid, "source_status": row.get("source_status")})
    matrix_norm = normalize(json.dumps(matrix, ensure_ascii=False))
    for phrase in FORBIDDEN_ASSERTIONS:
        if phrase in matrix_norm:
            failures.append({"failure": "forbidden_assertive_matrix_promotion", "phrase": phrase})

    summary = {
        "review_source_count": len(sources),
        "route_a_gate_rows": len(route_a),
        "route_verdict": review.get("route_verdict"),
        "checked_interface": "Route A external source review 001 and matrix status update",
        "allowed_inference": "Route A is source-reviewed as a candidate/bootstrap/proxy engineering lead only",
        "blocked_inference": "engineering feasibility, selected substrate, prototype readiness, Formation Medium implementation, CRBSM implementation, investor readiness",
    }
    return RouteASourceReviewResult(
        target_id=TARGET_ID,
        checker="route_a_source_review_001_guard_v1",
        status="PASS_LEDGER_VALIDATION" if not failures else "FAILED",
        inspected_files=[str(REVIEW_MD.relative_to(ROOT)), str(REVIEW_JSON.relative_to(ROOT)), str(MATRIX.relative_to(ROOT))],
        support_summary=summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_LEDGER_VALIDATION means Route A has a guarded external source review and matrix update, "
            "remaining SOURCE_REVIEWED_CONTINUE_AS_CANDIDATE only. It is not a mathematical proof, "
            "not source extraction into the corpus, not substrate evidence, not engineering readiness, "
            "not prototype readiness, not CRBSM implementation, not Formation Medium implementation, and not investor readiness."
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
