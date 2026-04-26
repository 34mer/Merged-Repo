from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"

REQUIRED_CLAIMS = {
    "EXT-AMP-PRIME-001": {
        "paper_id": "AMP_PRIME_2020",
        "required_terms": [
            "same boundary structure",
            "logarithmic form",
            "differs in the bulk",
            "cannot by itself prove realization equivalence",
        ],
    },
    "EXT-WILSON-POS-2024-001": {
        "paper_id": "WILSON_POS_2024",
        "required_terms": [
            "uniform sign",
            "bootstrap",
            "contradicts at three loops",
            "new alphabet letters",
        ],
    },
}

FORMATION_FILES = [
    "research_ledger/S2_STAR_S4_DISTINCTNESS_CANDIDATE.md",
    "research_ledger/FORMATION_MEDIUM_LAYER_0_SPEC.md",
    "research_ledger/FORMATION_MEDIUM_LAYER_1_SPEC.md",
    "research_ledger/FORMATION_MEDIUM_LAYER_1_CANDIDATE_CONSTRAINTS.json",
]

REQUIRED_CAUTION_TERMS = [
    "caution",
    "not a theorem",
    "physical realization",
    "bulk",
    "readout",
]

FORBIDDEN_PROMOTION_PHRASES = [
    "proves substrate realization",
    "proves physical realization",
    "proves bulk equivalence",
    "bulk equivalence is checked",
    "same boundary implies same bulk",
    "same logarithmic form implies same bulk",
    "unique faithful bulk reconstruction is required",
]


@dataclass(frozen=True)
class SameBoundaryDifferentBulkResult:
    target_id: str
    checker: str
    status: str
    inspected_claim_ids: list[str]
    inspected_files: list[str]
    support_summary: dict[str, Any]
    counterexamples: list[dict[str, Any]]
    status_boundary: str


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def claims_by_id() -> dict[str, dict[str, Any]]:
    data = read_json(ROOT / "research_ledger" / "SOURCE_EXTRACTED_CLAIMS.json")
    return {claim["id"]: claim for claim in data["claims"]}


def target_by_id() -> dict[str, Any] | None:
    data = read_json(ROOT / "research_ledger" / "FORMAL_CHECK_TARGETS.json")
    for target in data["targets"]:
        if target["id"] == TARGET_ID:
            return target
    return None


def check_source_claims() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {"claim_statuses": {}, "paper_ids": {}, "required_claim_count": len(REQUIRED_CLAIMS)}
    claims = claims_by_id()
    target = target_by_id()
    target_claim_ids = set(target.get("claim_ids", [])) if target else set()
    if target is None:
        failures.append({"failure": "missing_target", "target_id": TARGET_ID})

    for claim_id, spec in REQUIRED_CLAIMS.items():
        claim = claims.get(claim_id)
        if claim is None:
            failures.append({"failure": "missing_required_claim", "claim_id": claim_id})
            continue
        if claim_id not in target_claim_ids:
            failures.append({"failure": "claim_missing_from_target", "claim_id": claim_id})
        status = set(claim.get("status", []))
        summary["claim_statuses"][claim_id] = sorted(status)
        summary["paper_ids"][claim_id] = claim.get("paper_id")
        if claim.get("paper_id") != spec["paper_id"]:
            failures.append({"failure": "paper_id_mismatch", "claim_id": claim_id, "observed": claim.get("paper_id"), "expected": spec["paper_id"]})
        if "SOURCE_EXTRACTED" not in status or "NEEDS_FORMALIZATION" not in status:
            failures.append({"failure": "claim_not_source_extracted_needs_formalization", "claim_id": claim_id, "status": sorted(status)})
        if "CHECKED" in status or "FORMALLY_CHECKED" in status:
            failures.append({"failure": "source_claim_improperly_promoted", "claim_id": claim_id, "status": sorted(status)})
        claim_text = normalize(claim.get("claim_text", ""))
        for term in spec["required_terms"]:
            if term.lower() not in claim_text:
                failures.append({"failure": "claim_missing_required_caution_term", "claim_id": claim_id, "term": term})
    return failures, summary


def check_formation_files() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {"formation_files_preserve_caution": True, "forbidden_promotions_absent": True}
    for rel in FORMATION_FILES:
        path = ROOT / rel
        if not path.exists():
            failures.append({"failure": "missing_formation_file", "path": rel})
            summary["formation_files_preserve_caution"] = False
            continue
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        for term in REQUIRED_CAUTION_TERMS:
            if term not in lower:
                failures.append({"failure": "formation_file_missing_caution_term", "path": rel, "term": term})
                summary["formation_files_preserve_caution"] = False
        for phrase in FORBIDDEN_PROMOTION_PHRASES:
            if phrase in lower:
                failures.append({"failure": "forbidden_bulk_or_substrate_promotion_phrase", "path": rel, "phrase": phrase})
                summary["forbidden_promotions_absent"] = False
    return failures, summary


def check_result_registry_non_promotion() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    data = read_json(ROOT / "research_ledger" / "FORMAL_CHECK_RESULTS.json")
    non_promotion_rule = data.get("non_promotion_rule", "")
    summary: dict[str, Any] = {"formal_results_non_promotion_rule_present": bool(non_promotion_rule)}
    if not non_promotion_rule:
        failures.append({"failure": "missing_non_promotion_rule"})
    lower = json.dumps(data, ensure_ascii=False).lower()
    for phrase in FORBIDDEN_PROMOTION_PHRASES:
        if phrase in lower:
            failures.append({"failure": "forbidden_promotion_phrase_in_results", "phrase": phrase})
    return failures, summary


def run_check() -> SameBoundaryDifferentBulkResult:
    failures: list[dict[str, Any]] = []
    claim_failures, claim_summary = check_source_claims()
    file_failures, file_summary = check_formation_files()
    result_failures, result_summary = check_result_registry_non_promotion()
    failures.extend(claim_failures)
    failures.extend(file_failures)
    failures.extend(result_failures)

    support_summary: dict[str, Any] = {
        **claim_summary,
        **file_summary,
        **result_summary,
        "checked_interface": "ledger/source caution against promoting shared boundary, logarithmic form, sign behavior, or bootstrap success into bulk/substrate equivalence",
        "allowed_inference": "same-boundary/different-bulk and post-integration/bootstrap limitations are active caution flags for comparator and Formation Medium wording",
        "blocked_inference": "bulk equivalence, substrate realization, physical settling law, or investor-ready engineering proof",
    }
    return SameBoundaryDifferentBulkResult(
        target_id=TARGET_ID,
        checker="same_boundary_different_bulk_ledger_guard_v1",
        status="PASS_SOURCE_COVERAGE" if not failures else "FAILED",
        inspected_claim_ids=sorted(REQUIRED_CLAIMS),
        inspected_files=FORMATION_FILES,
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_SOURCE_COVERAGE means the ledger preserves the source-backed caution that shared boundary structure, "
            "shared logarithmic form, sign behavior, or bootstrap success must not be promoted into bulk equivalence or "
            "Formation Medium substrate realization. It is not a mathematical proof, not a theorem of positive geometry, "
            "not an S4 theorem, not substrate evidence, not engineering readiness, and not a physical settling-law result."
        ),
    )


def write_result(path: Path, result: SameBoundaryDifferentBulkResult) -> None:
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
