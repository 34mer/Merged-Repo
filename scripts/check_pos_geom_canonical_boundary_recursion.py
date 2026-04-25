from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "CHK-POS-GEOM-CANONICAL-BOUNDARY-RECURSION"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
SOURCE_MARKDOWN = ROOT / "sources" / "Markdowns" / "Arkani-Hamed_2017_Positive-Geometries-and-Canonical-Forms_arXiv-1703.04541.pdf.md"

REQUIRED_CLAIMS = {
    "EXT-POS-GEOM-2017-001": {
        "paper_id": "POS_GEOM_2017",
        "required_terms": ["unique", "canonical", "logarithmic", "boundaries", "residues", "canonical form on that boundary"],
    },
    "EXT-POS-GEOM-2017-002": {
        "paper_id": "POS_GEOM_2017",
        "required_terms": ["canonical form", "logarithmic", "poles", "boundaries", "residues", "boundary geometries"],
    },
}

REQUIRED_SOURCE_WINDOWS = [
    {
        "name": "abstract_unique_log_boundary_residue",
        "terms": ["unique", "logarithmic", "boundaries", "residues", "canonical form on that boundary"],
        "max_span_chars": 1400,
    },
    {
        "name": "definition_methods_triangulation_pushforward_context",
        "terms": ["positive geometries", "canonical forms", "triangulation", "push-forward"],
        "max_span_chars": 1800,
    },
]

FORBIDDEN_PROMOTIONS = [
    "formation medium",
    "substrate",
    "settling law",
    "S2*",
    "physical realization",
]


@dataclass(frozen=True)
class PosGeomCanonicalBoundaryResult:
    target_id: str
    checker: str
    status: str
    inspected_claim_ids: list[str]
    source_file: str
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


def smallest_span(text: str, terms: list[str]) -> tuple[int | None, str]:
    lower = text.lower()
    positions: list[tuple[str, int]] = []
    for term in terms:
        idx = lower.find(term.lower())
        if idx == -1:
            return None, term
        positions.append((term, idx))
    starts = [idx for _, idx in positions]
    ends = [idx + len(term) for term, idx in positions]
    return max(ends) - min(starts), ""


def check_claim_layer(claims: dict[str, dict[str, Any]], target: dict[str, Any] | None) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {"claim_statuses": {}, "paper_ids": {}, "required_claim_count": len(REQUIRED_CLAIMS)}

    if target is None:
        failures.append({"failure": "missing_target", "target_id": TARGET_ID})
        target_claim_ids: set[str] = set()
    else:
        target_claim_ids = set(target.get("claim_ids", []))

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
        for term in FORBIDDEN_PROMOTIONS:
            if term.lower() in claim_text:
                failures.append({"failure": "claim_contains_forbidden_promotion_term", "claim_id": claim_id, "term": term})
    return failures, summary


def check_source_windows() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {"source_windows": {}}
    if not SOURCE_MARKDOWN.exists():
        return [{"failure": "missing_source_markdown", "path": str(SOURCE_MARKDOWN.relative_to(ROOT))}], summary
    text = SOURCE_MARKDOWN.read_text(encoding="utf-8")
    normalized = normalize(text)
    for window in REQUIRED_SOURCE_WINDOWS:
        span, missing = smallest_span(normalized, window["terms"])
        if span is None:
            failures.append({"failure": "source_window_missing_term", "window": window["name"], "term": missing})
            summary["source_windows"][window["name"]] = {"status": "FAILED", "missing_term": missing}
            continue
        if span > int(window["max_span_chars"]):
            failures.append({"failure": "source_terms_too_far_apart", "window": window["name"], "span_chars": span, "max_span_chars": window["max_span_chars"]})
        summary["source_windows"][window["name"]] = {"status": "PASS", "span_chars": span, "max_span_chars": window["max_span_chars"]}
    return failures, summary


def run_check() -> PosGeomCanonicalBoundaryResult:
    failures: list[dict[str, Any]] = []
    claim_failures, claim_summary = check_claim_layer(claims_by_id(), target_by_id())
    source_failures, source_summary = check_source_windows()
    failures.extend(claim_failures)
    failures.extend(source_failures)

    support_summary: dict[str, Any] = {
        **claim_summary,
        **source_summary,
        "checked_interface": "source coverage for canonical form uniqueness/logarithmic-boundary/residue-recursion language",
        "allowed_inference": "the source-extracted claims contain the required canonical-boundary-recursion ingredients",
        "blocked_inference": "formal residue theorem, all positive-geometry theorem, S2* theorem, Formation Medium substrate realization, or physical settling law",
    }

    return PosGeomCanonicalBoundaryResult(
        target_id=TARGET_ID,
        checker="pos_geom_canonical_boundary_recursion_source_guard_v1",
        status="PASS_SOURCE_COVERAGE" if not failures else "FAILED",
        inspected_claim_ids=sorted(REQUIRED_CLAIMS),
        source_file=str(SOURCE_MARKDOWN.relative_to(ROOT)),
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_SOURCE_COVERAGE means the POS_GEOM_2017 source text and extracted claims contain the canonical-form, "
            "boundary-only logarithmic singularity, and residue-on-boundary recursion language required by the target. "
            "It is not a mathematical proof, not a formal residue theorem, not an all-positive-geometries theorem, "
            "not substrate evidence, and not a physical settling-law result."
        ),
    )


def write_result(path: Path, result: PosGeomCanonicalBoundaryResult) -> None:
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
