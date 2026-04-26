from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "CHK-PRIME-LOCAL-CARRIER-SOURCE-COVERAGE"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
SOURCE_MARKDOWN = ROOT / "sources" / "Markdowns" / "_MConverter.eu_Herrmann_2020_Amplituhedron-Prime-Positive-Geometry_arXiv-2009.05607.pdf.md"

REQUIRED_CLAIMS = {
    "EXT-AMP-PRIME-002": {
        "paper_id": "AMP_PRIME_2020",
        "required_terms": ["sign-flip conditions", "maximal sign-flip", "finite one-loop octagons", "chiral octagons"],
    },
    "EXT-AMP-PRIME-003": {
        "paper_id": "AMP_PRIME_2020",
        "required_terms": ["sign-flip-four", "four sign-flip positions", "chiral octagon", "eight boundaries"],
    },
    "EXT-AMP-PRIME-004": {
        "paper_id": "AMP_PRIME_2020",
        "required_terms": ["chiral octagons", "degenerate", "pentagon", "hexagon", "boundary cases"],
    },
    "EXT-AMP-PRIME-005": {
        "paper_id": "AMP_PRIME_2020",
        "required_terms": ["chiral pentagons", "Amplituhedron-Prime", "same logarithmic form", "same boundary", "differs in the bulk"],
    },
}

REQUIRED_SOURCE_TERMS = [
    "sign-flip conditions",
    "maximal sign-flip",
    "finite one-loop octagons",
    "sign-flip-four",
    "chiral octagons",
    "degenerate to simpler spaces",
    "pentagon and hexagon examples",
    "Amplituhedron-Prime",
    "same boundary structure",
    "same logarithmic form",
    "differs in the bulk",
]

FORMATION_FILES = [
    "research_ledger/PRIME_LOCAL_CARRIER_CANDIDATE.md",
    "research_ledger/PRIME_DIRECT_SOURCE_EXTRACTION_SUMMARY_001.md",
    "research_ledger/FORMATION_MEDIUM_BULK_READOUT_WITNESS_SCHEMA.md",
    "research_ledger/FORMATION_MEDIUM_CANDIDATE_VOCABULARY.md",
]

REQUIRED_SCOPE_TERMS = [
    "not a theorem",
    "not engineering",
    "not a physical substrate",
    "not source-extracted"  # at least in generated candidate artifacts; summary can have source extraction notice separately
]

FORBIDDEN_PROMOTION_PHRASES = [
    "prime proves physical substrate",
    "prime proves substrate",
    "prime proves formation medium",
    "sign-flip regions are the formation medium substrate",
    "chiral octagons prove formation medium readout",
    "prime local carrier is engineering feasible",
    "prime local carrier is checked",
    "prime establishes a universal carrier theorem",
    "prime proves a universal carrier theorem",
    "physical substrate evidence from prime",
]


@dataclass(frozen=True)
class PrimeLocalCarrierSourceCoverageResult:
    target_id: str
    checker: str
    status: str
    inspected_claim_ids: list[str]
    source_file: str
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


def check_claim_layer() -> tuple[list[dict[str, Any]], dict[str, Any]]:
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
            failures.append({"failure": "claim_missing_from_target", "claim_id": claim_id, "target_id": TARGET_ID})
        status = set(claim.get("status", []))
        summary["claim_statuses"][claim_id] = sorted(status)
        summary["paper_ids"][claim_id] = claim.get("paper_id")
        if claim.get("paper_id") != spec["paper_id"]:
            failures.append({"failure": "paper_id_mismatch", "claim_id": claim_id, "observed": claim.get("paper_id"), "expected": spec["paper_id"]})
        if "SOURCE_EXTRACTED" not in status or "NEEDS_FORMALIZATION" not in status:
            failures.append({"failure": "claim_not_source_extracted_needs_formalization", "claim_id": claim_id, "status": sorted(status)})
        if "CHECKED" in status or "FORMALLY_CHECKED" in status:
            failures.append({"failure": "claim_improperly_checked", "claim_id": claim_id, "status": sorted(status)})
        claim_text = normalize(claim.get("claim_text", ""))
        for term in spec["required_terms"]:
            if term.lower() not in claim_text:
                failures.append({"failure": "claim_missing_required_term", "claim_id": claim_id, "term": term})
        for phrase in FORBIDDEN_PROMOTION_PHRASES:
            if phrase in claim_text:
                failures.append({"failure": "claim_contains_forbidden_promotion", "claim_id": claim_id, "phrase": phrase})
    return failures, summary


def check_source_text() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {"source_terms_present": []}
    if not SOURCE_MARKDOWN.exists():
        return [{"failure": "missing_source_markdown", "path": str(SOURCE_MARKDOWN.relative_to(ROOT))}], summary
    text = normalize(SOURCE_MARKDOWN.read_text(encoding="utf-8"))
    for term in REQUIRED_SOURCE_TERMS:
        if term.lower() not in text:
            failures.append({"failure": "source_missing_required_term", "term": term})
        else:
            summary["source_terms_present"].append(term)
    return failures, summary


def check_scope_files() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {"scope_files_checked": [], "forbidden_promotions_absent": True}
    for rel in FORMATION_FILES:
        path = ROOT / rel
        if not path.exists():
            failures.append({"failure": "missing_scope_file", "path": rel})
            continue
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        summary["scope_files_checked"].append(rel)
        for phrase in FORBIDDEN_PROMOTION_PHRASES:
            if phrase in lower:
                failures.append({"failure": "forbidden_prime_promotion_phrase", "path": rel, "phrase": phrase})
                summary["forbidden_promotions_absent"] = False
        # Require most scope artifacts to contain explicit non-promotion language, but do not overfit exact term list.
        if rel != "research_ledger/PRIME_DIRECT_SOURCE_EXTRACTION_SUMMARY_001.md":
            required_hits = sum(1 for term in REQUIRED_SCOPE_TERMS if term in lower)
            if required_hits < 2:
                failures.append({"failure": "scope_file_missing_non_promotion_language", "path": rel, "hits": required_hits})
    return failures, summary


def check_result_registry_boundary() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    data = read_json(ROOT / "research_ledger" / "FORMAL_CHECK_RESULTS.json")
    summary: dict[str, Any] = {"formal_results_non_promotion_rule_present": bool(data.get("non_promotion_rule"))}
    entry = next((r for r in data.get("results", []) if r.get("target_id") == TARGET_ID), None)
    if entry is None:
        failures.append({"failure": "missing_result_registry_entry", "target_id": TARGET_ID})
    elif entry.get("result_status") not in {"DEFINED_NOT_RUN", "PASS_SOURCE_COVERAGE"}:
        failures.append({"failure": "unexpected_result_status", "target_id": TARGET_ID, "status": entry.get("result_status")})
    return failures, summary


def run_check() -> PrimeLocalCarrierSourceCoverageResult:
    failures: list[dict[str, Any]] = []
    claim_failures, claim_summary = check_claim_layer()
    source_failures, source_summary = check_source_text()
    scope_failures, scope_summary = check_scope_files()
    registry_failures, registry_summary = check_result_registry_boundary()
    failures.extend(claim_failures)
    failures.extend(source_failures)
    failures.extend(scope_failures)
    failures.extend(registry_failures)

    support_summary: dict[str, Any] = {
        **claim_summary,
        **source_summary,
        **scope_summary,
        **registry_summary,
        "checked_interface": "Prime source coverage for sign-flip local positive spaces, chiral-octagon regions, degenerations, and Amplituhedron-Prime gluing/bulk caution",
        "allowed_inference": "Prime supplies source-extracted positive-geometry facts about local sign-flip spaces and a same-boundary/log-form/different-bulk caution",
        "blocked_inference": "Formation Medium substrate, universal carrier theorem, physical realization, engineering feasibility, or corporate/investor proof",
    }
    return PrimeLocalCarrierSourceCoverageResult(
        target_id=TARGET_ID,
        checker="prime_local_carrier_source_coverage_guard_v1",
        status="PASS_SOURCE_COVERAGE" if not failures else "FAILED",
        inspected_claim_ids=sorted(REQUIRED_CLAIMS),
        source_file=str(SOURCE_MARKDOWN.relative_to(ROOT)),
        inspected_files=FORMATION_FILES,
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_SOURCE_COVERAGE means the Prime source text and extracted claims support the scoped sign-flip, "
            "chiral-octagon, degeneration, and Amplituhedron-Prime gluing facts. It is not a mathematical proof, "
            "not a formal carrier theorem, not an S1/S2*/S3/S4 theorem, not substrate evidence, "
            "not Formation Medium substrate evidence, not engineering readiness, and not a physical realization claim."
        ),
    )


def write_result(path: Path, result: PrimeLocalCarrierSourceCoverageResult) -> None:
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
