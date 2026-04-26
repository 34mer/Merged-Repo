from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "CHK-R12-SUBMODULAR-LAW"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"

REQUIRED_CLAIMS = {
    "EXT-COSMO-002": {
        "paper_id": "COSMO_2024",
        "required_terms": [
            "cosmohedron inequalities",
            "grouped partial-triangulation inequalities",
            "positive delta parameters",
            "submodular-type compatibility law",
            "delta_full = 0",
        ],
    },
}

LEDGER_FILES = [
    "research_ledger/COMPARATOR_PACKAGE_REGISTER.md",
    "research_ledger/EXTRACTION_LEDGER.md",
    "research_ledger/FORMAL_CHECK_TARGETS.json",
    "research_ledger/FORMAL_CHECK_RESULTS.json",
]

REQUIRED_LEDGER_TERMS = [
    "cosmohedron",
    "R12",
    "submodular",
]

FORBIDDEN_PROMOTION_PHRASES = [
    "submodular law is proved",
    "submodular law theorem",
    "smt encoding is solved",
    "z3 proof completed",
    "delta-domain theorem",
    "formation medium substrate evidence",
    "physical settling law",
    "engineering readiness",
]


@dataclass(frozen=True)
class R12SubmodularLawResult:
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
                failures.append({"failure": "claim_missing_required_r12_term", "claim_id": claim_id, "term": term})
    return failures, summary


def check_ledgers() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {"ledger_files_have_required_terms": True, "forbidden_promotions_absent": True}
    for rel in LEDGER_FILES:
        path = ROOT / rel
        if not path.exists():
            failures.append({"failure": "missing_ledger_file", "path": rel})
            summary["ledger_files_have_required_terms"] = False
            continue
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        if rel.endswith("FORMAL_CHECK_TARGETS.json"):
            target = target_by_id()
            target_text = json.dumps(target, ensure_ascii=False).lower() if target else ""
            predicate = str((target or {}).get("predicate", "")).lower()
            failure_condition = str((target or {}).get("failure_condition", "")).lower()
            if "delta_p + delta_p'" not in predicate or "delta_full = 0" not in predicate:
                failures.append({"failure": "target_missing_delta_submodular_predicate", "path": rel})
                summary["ledger_files_have_required_terms"] = False
            if "violating assignment" not in failure_condition or "domain constraints" not in failure_condition:
                failures.append({"failure": "target_missing_smt_failure_boundary", "path": rel})
                summary["ledger_files_have_required_terms"] = False
            for phrase in FORBIDDEN_PROMOTION_PHRASES:
                if phrase in target_text:
                    failures.append({"failure": "forbidden_r12_promotion_phrase_in_target", "path": rel, "phrase": phrase})
                    summary["forbidden_promotions_absent"] = False
            continue
        if rel.endswith("FORMAL_CHECK_RESULTS.json"):
            if TARGET_ID in lower and "pass_source_coverage" in lower:
                for term in REQUIRED_LEDGER_TERMS:
                    if term.lower() not in lower:
                        failures.append({"failure": "r12_result_missing_term", "path": rel, "term": term})
                        summary["ledger_files_have_required_terms"] = False
            continue
        for term in REQUIRED_LEDGER_TERMS:
            if term.lower() not in lower:
                failures.append({"failure": "r12_file_missing_term", "path": rel, "term": term})
                summary["ledger_files_have_required_terms"] = False
        for phrase in FORBIDDEN_PROMOTION_PHRASES:
            if phrase in lower:
                failures.append({"failure": "forbidden_r12_promotion_phrase", "path": rel, "phrase": phrase})
                summary["forbidden_promotions_absent"] = False
    return failures, summary


def run_check() -> R12SubmodularLawResult:
    failures: list[dict[str, Any]] = []
    claim_failures, claim_summary = check_source_claims()
    ledger_failures, ledger_summary = check_ledgers()
    failures.extend(claim_failures)
    failures.extend(ledger_failures)

    support_summary: dict[str, Any] = {
        **claim_summary,
        **ledger_summary,
        "checked_interface": "ledger/source coverage for cosmohedron grouped-inequality delta/submodular compatibility language",
        "allowed_inference": "R12 may cite source-bound grouped inequality, positive delta, submodular-compatibility, and delta_full interface material",
        "blocked_inference": "SMT proof, Z3 proof, all-domain submodular theorem, Formation Medium substrate evidence, physical settling law, or engineering readiness",
    }
    return R12SubmodularLawResult(
        target_id=TARGET_ID,
        checker="r12_submodular_law_source_guard_v1",
        status="PASS_SOURCE_COVERAGE" if not failures else "FAILED",
        inspected_claim_ids=sorted(REQUIRED_CLAIMS),
        inspected_files=LEDGER_FILES,
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_SOURCE_COVERAGE means the ledger preserves source-bound cosmohedron grouped-inequality, positive-delta, "
            "submodular-compatibility, and delta_full=0 interface claims. It is not a mathematical proof, not an SMT/Z3 proof, "
            "not a full submodular-law theorem, not substrate evidence, not engineering readiness, and not a physical settling-law result."
        ),
    )


def write_result(path: Path, result: R12SubmodularLawResult) -> None:
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
