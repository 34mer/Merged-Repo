from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "CHK-S2STAR-READOUT-SOURCE-COVERAGE"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"

REQUIRED_SOURCE_CLAIMS = {
    "EXT-POS-GEOM-2017-001": {
        "paper_id": "POS_GEOM_2017",
        "required_terms": ["canonical", "boundaries", "residues"],
    },
    "EXT-POS-GEOM-2017-002": {
        "paper_id": "POS_GEOM_2017",
        "required_terms": ["canonical form", "boundaries", "residues"],
    },
    "EXT-SCAT-FORMS-001": {
        "paper_id": "SCAT_FORMS_2017",
        "required_terms": ["canonical form", "associahedron"],
    },
    "EXT-INTO-AMP-2013-001": {
        "paper_id": "INTO_AMP_2013",
        "required_terms": ["faces", "cuts"],
    },
}

FORMATION_FILES = [
    "research_ledger/S2_STAR_S4_DISTINCTNESS_CANDIDATE.md",
    "research_ledger/FORMATION_MEDIUM_LAYER_0_SPEC.md",
    "research_ledger/FORMATION_MEDIUM_LAYER_1_SPEC.md",
    "research_ledger/FORMATION_MEDIUM_LAYER_1_CANDIDATE_CONSTRAINTS.json",
]

FORBIDDEN_SOURCE_CLAIM_TERMS = [
    "formation medium",
    "substrate",
    "S2*",
    "settling law",
]

REQUIRED_NON_PROMOTION_TERMS = [
    "GENERATED",
    "OPEN",
    "NOT_CHECKED",
]


@dataclass(frozen=True)
class S2StarCoverageResult:
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


def load_claims() -> dict[str, dict[str, Any]]:
    data = read_json(ROOT / "research_ledger" / "SOURCE_EXTRACTED_CLAIMS.json")
    return {claim["id"]: claim for claim in data["claims"]}


def load_targets() -> dict[str, dict[str, Any]]:
    data = read_json(ROOT / "research_ledger" / "FORMAL_CHECK_TARGETS.json")
    return {target["id"]: target for target in data["targets"]}


def check_claims(claims: dict[str, dict[str, Any]], target: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {
        "required_claim_count": len(REQUIRED_SOURCE_CLAIMS),
        "claim_statuses": {},
        "paper_ids": {},
        "all_required_claims_source_extracted_not_checked": True,
        "source_claims_avoid_generated_fm_language": True,
    }

    target_claim_ids = set(target.get("claim_ids", []))
    missing_from_target = sorted(set(REQUIRED_SOURCE_CLAIMS) - target_claim_ids)
    if missing_from_target:
        failures.append({"failure": "required_claims_missing_from_target", "claim_ids": missing_from_target})

    for claim_id, spec in REQUIRED_SOURCE_CLAIMS.items():
        claim = claims.get(claim_id)
        if claim is None:
            failures.append({"failure": "missing_required_claim", "claim_id": claim_id})
            summary["all_required_claims_source_extracted_not_checked"] = False
            continue

        status = set(claim.get("status", []))
        summary["claim_statuses"][claim_id] = sorted(status)
        summary["paper_ids"][claim_id] = claim.get("paper_id")

        if claim.get("paper_id") != spec["paper_id"]:
            failures.append({
                "failure": "paper_id_mismatch",
                "claim_id": claim_id,
                "observed": claim.get("paper_id"),
                "expected": spec["paper_id"],
            })

        if "SOURCE_EXTRACTED" not in status or "NEEDS_FORMALIZATION" not in status:
            failures.append({"failure": "claim_not_source_extracted_needs_formalization", "claim_id": claim_id, "status": sorted(status)})
            summary["all_required_claims_source_extracted_not_checked"] = False

        if "CHECKED" in status or "FORMALLY_CHECKED" in status:
            failures.append({"failure": "claim_promoted_to_checked", "claim_id": claim_id, "status": sorted(status)})
            summary["all_required_claims_source_extracted_not_checked"] = False

        claim_text = claim.get("claim_text", "").lower()
        for term in spec["required_terms"]:
            if term.lower() not in claim_text:
                failures.append({"failure": "required_source_support_term_missing", "claim_id": claim_id, "term": term})
        for term in FORBIDDEN_SOURCE_CLAIM_TERMS:
            if term.lower() in claim_text:
                failures.append({"failure": "generated_fm_language_in_source_claim", "claim_id": claim_id, "term": term})
                summary["source_claims_avoid_generated_fm_language"] = False

    return failures, summary


def check_formation_files() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {
        "formation_files_preserve_non_promotion": True,
        "formation_files_acknowledge_positive_geometry_intake_started": True,
    }

    stale_gap_phrases = [
        "2017 Positive Geometry source missing",
        "2017 Positive Geometry source not in corpus",
        "2017 Positive Geometry paper is not in the current source corpus",
        "NOT IN CURRENT SOURCE_CORPUS",
    ]

    for rel in FORMATION_FILES:
        path = ROOT / rel
        if not path.exists():
            failures.append({"failure": "missing_formation_file", "path": rel})
            summary["formation_files_preserve_non_promotion"] = False
            continue
        text = path.read_text(encoding="utf-8")
        upper = text.upper()
        for term in REQUIRED_NON_PROMOTION_TERMS:
            if term not in upper:
                failures.append({"failure": "formation_file_missing_non_promotion_term", "path": rel, "term": term})
                summary["formation_files_preserve_non_promotion"] = False
        if "STATUS: SOURCE_EXTRACTED" in upper or "CHECK_STATUS: CHECKED" in upper or "FORMALLY_CHECKED" in upper:
            failures.append({"failure": "formation_file_appears_promoted", "path": rel})
            summary["formation_files_preserve_non_promotion"] = False
        for phrase in stale_gap_phrases:
            if phrase in text:
                failures.append({"failure": "stale_positive_geometry_source_gap_phrase", "path": rel, "phrase": phrase})
                summary["formation_files_acknowledge_positive_geometry_intake_started"] = False
        if rel.endswith(".md") and "POS_GEOM_2017" not in text:
            failures.append({"failure": "formation_file_missing_pos_geom_2017_reference", "path": rel})
            summary["formation_files_acknowledge_positive_geometry_intake_started"] = False

    return failures, summary


def run_check() -> S2StarCoverageResult:
    claims = load_claims()
    targets = load_targets()
    failures: list[dict[str, Any]] = []
    target = targets.get(TARGET_ID)
    if target is None:
        failures.append({"failure": "missing_target", "target_id": TARGET_ID})
        target = {"claim_ids": []}

    claim_failures, claim_summary = check_claims(claims, target)
    formation_failures, formation_summary = check_formation_files()
    failures.extend(claim_failures)
    failures.extend(formation_failures)

    support_summary: dict[str, Any] = {
        **claim_summary,
        **formation_summary,
        "allowed_inference": "source coverage for canonical boundary/readout only",
        "blocked_inference": "checked S2*, physical substrate realization, settling law, or framework separation",
    }

    return S2StarCoverageResult(
        target_id=TARGET_ID,
        checker="ledger_s2star_source_coverage_guard_v1",
        status="PASS_SOURCE_COVERAGE" if not failures else "FAILED",
        inspected_claim_ids=sorted(REQUIRED_SOURCE_CLAIMS),
        inspected_files=FORMATION_FILES,
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_SOURCE_COVERAGE means the source ledger now contains the required canonical-boundary/readout support claims "
            "and the Formation Medium artifacts preserve non-promotion discipline. It is not a mathematical proof, not a "
            "formal S2* theorem, not substrate evidence, and not a physical settling-law result."
        ),
    )


def write_result(path: Path, result: S2StarCoverageResult) -> None:
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
