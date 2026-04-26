from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "CHK-REPRESENTATION-COMPARATOR"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"

REQUIRED_CLAIMS = {
    "EXT-MOM-AMP-2019-001": {
        "paper_id": "MOM_AMP_2019",
        "required_terms": [
            "positive geometry",
            "tree-level",
            "spinor-helicity space",
            "positive Grassmannian",
            "bosonized spinor-helicity data",
        ],
    },
    "EXT-LOOP-MOM-AMP-2022-001": {
        "paper_id": "LOOP_MOM_AMP_2022",
        "required_terms": [
            "loop integrands",
            "spinor-helicity variables",
            "loop two-planes",
            "global loop-momentum definition",
        ],
    },
}

REPRESENTATION_LEDGER_FILES = [
    "research_ledger/COMPARATOR_PACKAGE_REGISTER.md",
    "research_ledger/EXTRACTION_LEDGER.md",
    "research_ledger/PAPER_SOURCE_LEDGER.md",
    "research_ledger/FORMAL_CHECK_TARGETS.json",
    "research_ledger/FORMAL_CHECK_RESULTS.json",
]

REQUIRED_REPRESENTATION_TERMS = [
    "representation",
    "momentum amplituhedron",
    "loop momentum amplituhedron",
]

FORBIDDEN_PROMOTION_PHRASES = [
    "same realization class as the momentum-twistor amplituhedron",
    "treated as the same realization class",
    "proves realization equivalence",
    "proves bulk equivalence",
    "spinor-helicity presentation is the same bulk",
    "loop-momentum presentation is the same bulk",
    "representation equivalence is checked",
]

ALLOWED_TARGET_FAILURE_PHRASE = (
    "treated as the same realization class as the momentum-twistor amplituhedron "
    "without an explicit representation map and boundary/bulk compatibility check"
)


@dataclass(frozen=True)
class RepresentationComparatorResult:
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
            failures.append({"failure": "claim_improperly_checked", "claim_id": claim_id, "status": sorted(status)})
        claim_text = normalize(claim.get("claim_text", ""))
        for term in spec["required_terms"]:
            if term.lower() not in claim_text:
                failures.append({"failure": "claim_missing_required_representation_term", "claim_id": claim_id, "term": term})
    return failures, summary


def check_representation_ledger_files() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {"representation_files_have_required_terms": True, "forbidden_promotions_absent": True}
    for rel in REPRESENTATION_LEDGER_FILES:
        path = ROOT / rel
        if not path.exists():
            failures.append({"failure": "missing_representation_ledger_file", "path": rel})
            summary["representation_files_have_required_terms"] = False
            continue
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        if rel.endswith("FORMAL_CHECK_TARGETS.json"):
            target = target_by_id()
            target_text = json.dumps(target, ensure_ascii=False).lower() if target else ""
            failure_condition = str((target or {}).get("failure_condition", "")).lower()
            predicate = str((target or {}).get("predicate", "")).lower()
            if "same-physics" not in predicate or "equality of geometric realization class" not in predicate:
                failures.append({"failure": "target_missing_representation_separation_predicate", "path": rel})
                summary["representation_files_have_required_terms"] = False
            if "same realization class" not in failure_condition or "without an explicit representation map" not in failure_condition:
                failures.append({"failure": "target_missing_blocking_failure_condition", "path": rel})
                summary["representation_files_have_required_terms"] = False
            for phrase in FORBIDDEN_PROMOTION_PHRASES:
                if phrase in target_text and phrase not in failure_condition:
                    failures.append({"failure": "forbidden_promotion_phrase_in_target", "path": rel, "phrase": phrase})
                    summary["forbidden_promotions_absent"] = False
            continue
        if rel.endswith("FORMAL_CHECK_RESULTS.json"):
            # Before this checker is registered, the result entry is allowed to be DEFINED_NOT_RUN.
            # After registration, the summary will carry the explicit representation terms.
            if TARGET_ID in lower and "pass_source_coverage" in lower:
                for term in REQUIRED_REPRESENTATION_TERMS:
                    if term not in lower:
                        failures.append({"failure": "representation_result_missing_term", "path": rel, "term": term})
                        summary["representation_files_have_required_terms"] = False
            continue
        for term in REQUIRED_REPRESENTATION_TERMS:
            if term not in lower:
                failures.append({"failure": "representation_file_missing_term", "path": rel, "term": term})
                summary["representation_files_have_required_terms"] = False
        for phrase in FORBIDDEN_PROMOTION_PHRASES:
            if phrase in lower:
                failures.append({"failure": "forbidden_representation_promotion_phrase", "path": rel, "phrase": phrase})
                summary["forbidden_promotions_absent"] = False
    return failures, summary


def run_check() -> RepresentationComparatorResult:
    failures: list[dict[str, Any]] = []
    claim_failures, claim_summary = check_source_claims()
    file_failures, file_summary = check_representation_ledger_files()
    failures.extend(claim_failures)
    failures.extend(file_failures)

    support_summary: dict[str, Any] = {
        **claim_summary,
        **file_summary,
        "checked_interface": "ledger/source discipline for treating momentum and loop-momentum amplituhedra as representation-comparator records",
        "allowed_inference": "the sources support spinor-helicity/tree and loop-momentum positive-geometry programs as representation-comparator entries",
        "blocked_inference": "equality of geometric realization class, bulk equivalence, or Formation Medium substrate equivalence without separate map/boundary/bulk proof",
    }
    return RepresentationComparatorResult(
        target_id=TARGET_ID,
        checker="representation_comparator_ledger_guard_v1",
        status="PASS_SOURCE_COVERAGE" if not failures else "FAILED",
        inspected_claim_ids=sorted(REQUIRED_CLAIMS),
        inspected_files=REPRESENTATION_LEDGER_FILES,
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_SOURCE_COVERAGE means the ledger preserves momentum-amplituhedron and loop-momentum-amplituhedron "
            "claims as representation-comparator source records. It is not a mathematical proof, not a theorem that "
            "spinor-helicity and momentum-twistor geometries have the same realization class, not a boundary/bulk "
            "compatibility proof, not substrate evidence, and not engineering readiness."
        ),
    )


def write_result(path: Path, result: RepresentationComparatorResult) -> None:
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
