from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "CHK-SCAFFOLD-KINEMATIC-SHIFT"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"

REQUIRED_CLAIMS = {
    "EXT-HIDDEN-ZEROS-2023-001": {
        "paper_id": "HIDDEN_ZEROS_2023",
        "required_terms": [
            "hidden zero",
            "factorization",
            "pions and gluons",
            "kinematic shifts",
        ],
    },
    "EXT-SCAFFOLD-001": {
        "paper_id": "SCAFFOLD_GLUONS_2024",
        "required_terms": [
            "shifts",
            "even/even",
            "odd/odd",
            "mixed parity",
            "dy/y^2",
        ],
    },
    "EXT-BACKUS-2025-001": {
        "paper_id": "BACKUS_2025",
        "required_terms": [
            "soft limits",
            "tree level",
            "one loop",
            "W_e",
            "transmute",
            "Tr(phi^3)",
        ],
    },
}

BRIDGE_LEDGER_FILES = [
    "research_ledger/COMPARATOR_PACKAGE_REGISTER.md",
    "research_ledger/EXTRACTION_LEDGER.md",
    "research_ledger/FORMAL_CHECK_TARGETS.json",
    "research_ledger/FORMAL_CHECK_RESULTS.json",
]

REQUIRED_BRIDGE_TERMS = [
    "scaffold",
    "transmutation",
    "shift",
]

FORBIDDEN_PROMOTION_PHRASES = [
    "yang-mills has been derived",
    "proves yang-mills",
    "proves realization equivalence",
    "realization equivalence is checked",
    "same realization class",
    "substrate realization",
    "engineering readiness",
    "physical settling law",
]

ALLOWED_TARGET_FAILURE_TERMS = [
    "promoted to realization equivalence",
]


@dataclass(frozen=True)
class ScaffoldKinematicShiftResult:
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
                failures.append({"failure": "claim_missing_required_bridge_term", "claim_id": claim_id, "term": term})
    return failures, summary


def check_bridge_ledgers() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {"bridge_files_have_required_terms": True, "forbidden_promotions_absent": True}
    for rel in BRIDGE_LEDGER_FILES:
        path = ROOT / rel
        if not path.exists():
            failures.append({"failure": "missing_bridge_ledger_file", "path": rel})
            summary["bridge_files_have_required_terms"] = False
            continue
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        if rel.endswith("FORMAL_CHECK_TARGETS.json"):
            target = target_by_id()
            target_text = json.dumps(target, ensure_ascii=False).lower() if target else ""
            predicate = str((target or {}).get("predicate", "")).lower()
            failure_condition = str((target or {}).get("failure_condition", "")).lower()
            if "source-bound bridge claims" not in predicate or "without promoting" not in predicate:
                failures.append({"failure": "target_missing_bridge_nonpromotion_predicate", "path": rel})
                summary["bridge_files_have_required_terms"] = False
            if "promoted to realization equivalence" not in failure_condition:
                failures.append({"failure": "target_missing_realization_equivalence_failure_condition", "path": rel})
                summary["bridge_files_have_required_terms"] = False
            for phrase in FORBIDDEN_PROMOTION_PHRASES:
                if phrase in target_text and not any(allowed in failure_condition for allowed in ALLOWED_TARGET_FAILURE_TERMS):
                    failures.append({"failure": "forbidden_promotion_phrase_in_target", "path": rel, "phrase": phrase})
                    summary["forbidden_promotions_absent"] = False
            continue
        if rel.endswith("FORMAL_CHECK_RESULTS.json"):
            # Before registration this may be DEFINED_NOT_RUN. After registration it must include bridge terms.
            if TARGET_ID in lower and "pass_source_coverage" in lower:
                for term in REQUIRED_BRIDGE_TERMS:
                    if term not in lower:
                        failures.append({"failure": "bridge_result_missing_term", "path": rel, "term": term})
                        summary["bridge_files_have_required_terms"] = False
            continue
        for term in REQUIRED_BRIDGE_TERMS:
            if term not in lower:
                failures.append({"failure": "bridge_file_missing_term", "path": rel, "term": term})
                summary["bridge_files_have_required_terms"] = False
        for phrase in FORBIDDEN_PROMOTION_PHRASES:
            if phrase in lower:
                failures.append({"failure": "forbidden_bridge_promotion_phrase", "path": rel, "phrase": phrase})
                summary["forbidden_promotions_absent"] = False
    return failures, summary


def run_check() -> ScaffoldKinematicShiftResult:
    failures: list[dict[str, Any]] = []
    claim_failures, claim_summary = check_source_claims()
    ledger_failures, ledger_summary = check_bridge_ledgers()
    failures.extend(claim_failures)
    failures.extend(ledger_failures)

    support_summary: dict[str, Any] = {
        **claim_summary,
        **ledger_summary,
        "checked_interface": "ledger/source discipline for hidden-zero, scaffolded-gluon shift, and W_e/transmutation bridge claims",
        "allowed_inference": "the cited claims may be used as source-bound bridge material for scaffold/shift/transmutation roadmap work",
        "blocked_inference": "Yang-Mills derivation, realization-class equivalence, Formation Medium substrate evidence, physical settling law, or engineering readiness",
    }
    return ScaffoldKinematicShiftResult(
        target_id=TARGET_ID,
        checker="scaffold_kinematic_shift_ledger_guard_v1",
        status="PASS_SOURCE_COVERAGE" if not failures else "FAILED",
        inspected_claim_ids=sorted(REQUIRED_CLAIMS),
        inspected_files=BRIDGE_LEDGER_FILES,
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_SOURCE_COVERAGE means the ledger preserves hidden-zero, scalar-scaffolded-gluon shift, and W_e/transmutation "
            "claims as source-bound bridge material. It is not a mathematical proof, not a theorem deriving Yang-Mills, "
            "not realization-class equivalence, not substrate evidence, not engineering readiness, and not a physical settling-law result."
        ),
    )


def write_result(path: Path, result: ScaffoldKinematicShiftResult) -> None:
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
