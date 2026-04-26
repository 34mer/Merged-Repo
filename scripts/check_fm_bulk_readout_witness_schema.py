from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "CHK-FM-BULK-READOUT-WITNESS-SCHEMA"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
SCHEMA_PATH = ROOT / "research_ledger" / "FORMATION_MEDIUM_BULK_READOUT_WITNESS_SCHEMA.md"
ENGINEERING_MATRIX_PATH = ROOT / "research_ledger" / "FORMATION_MEDIUM_ENGINEERING_GATE_MATRIX_001.json"

REQUIRED_SCHEMA_TERMS = [
    "same_readout(x, y) := readout(x) = readout(y)",
    "different_bulk(x, y) := bulk(x) != bulk(y)",
    "the readout map must be specified",
    "bulk equivalence relation",
    "positive-geometric bulk",
    "physical substrate",
    "boundary_determined(C)",
    "bulk_sensitive(C)",
    "READOUT_FAITHFULNESS_UNKNOWN",
    "not a source-extracted claim",
    "not a theorem",
]

REQUIRED_MATRIX_STATUSES = [
    "READOUT_FAITHFULNESS_UNKNOWN",
    "AMBIGUOUS_POSSIBLY_FAILS_S4",
    "STRONG_CANDIDATE",
]

FORBIDDEN_PROMOTIONS = [
    "physical substrate non-faithfulness is proved",
    "s4 is proved",
    "same_readout proves different_bulk",
    "prime proves physical substrate non-faithfulness",
    "engineering route is readout nonfaithful",
    "readout nonfaithfulness is checked for route a",
    "readout nonfaithfulness is checked for route b",
]


@dataclass(frozen=True)
class FmBulkReadoutWitnessSchemaResult:
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


def target_exists() -> bool:
    data = read_json(ROOT / "research_ledger" / "FORMAL_CHECK_TARGETS.json")
    return any(target.get("id") == TARGET_ID for target in data.get("targets", []))


def check_schema_text() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {"schema_terms_present": []}
    if not SCHEMA_PATH.exists():
        return [{"failure": "missing_schema", "path": str(SCHEMA_PATH.relative_to(ROOT))}], summary
    text = normalize(SCHEMA_PATH.read_text(encoding="utf-8"))
    for term in REQUIRED_SCHEMA_TERMS:
        if term.lower() not in text:
            failures.append({"failure": "schema_missing_required_term", "term": term})
        else:
            summary["schema_terms_present"].append(term)
    for phrase in FORBIDDEN_PROMOTIONS:
        if phrase.lower() in text:
            failures.append({"failure": "forbidden_promotion_phrase_in_schema", "phrase": phrase})
    return failures, summary


def check_engineering_matrix() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    summary: dict[str, Any] = {"routes_with_g4": [], "readout_statuses": {}}
    if not ENGINEERING_MATRIX_PATH.exists():
        return [{"failure": "missing_engineering_matrix", "path": str(ENGINEERING_MATRIX_PATH.relative_to(ROOT))}], summary
    data = read_json(ENGINEERING_MATRIX_PATH)
    matrix = data.get("matrix", [])
    g4_rows = [row for row in matrix if row.get("gate_id") == "G4"]
    if not g4_rows:
        failures.append({"failure": "missing_g4_bulk_readout_gate_rows"})
    for row in g4_rows:
        rid = row.get("route_id")
        status = row.get("status")
        summary["routes_with_g4"].append(rid)
        summary["readout_statuses"][rid] = status
        if not status:
            failures.append({"failure": "g4_missing_status", "route_id": rid})
        # Engineering/demo routes must stay unknown unless separately evidenced.
        # Physics benchmark / near-hit routes may carry cautious theory-level labels, but must not become engineering claims.
        if rid in {"ROUTE-A", "ROUTE-B", "ROUTE-C"} and status != "READOUT_FAITHFULNESS_UNKNOWN":
            failures.append({"failure": "engineering_route_readout_status_not_unknown", "route_id": rid, "status": status})
        if rid in {"ROUTE-D", "ROUTE-E"} and status in {"READOUT_FAITHFUL", "READOUT_NONFAITHFUL"}:
            failures.append({"failure": "theory_route_has_overstrong_readout_status", "route_id": rid, "status": status})
    # Make sure the matrix still contains explicit evidence-needed text for readout map/bulk relation somewhere.
    matrix_text = normalize(json.dumps(data, ensure_ascii=False))
    for term in ["declare readout map", "bulk equivalence relation", "faithful", "non-faithful", "unknown"]:
        if term not in matrix_text:
            failures.append({"failure": "engineering_matrix_missing_guard_term", "term": term})
    for phrase in FORBIDDEN_PROMOTIONS:
        if phrase.lower() in matrix_text:
            failures.append({"failure": "forbidden_promotion_phrase_in_engineering_matrix", "phrase": phrase})
    return failures, summary


def check_target_and_result_registry() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    targets = read_json(ROOT / "research_ledger" / "FORMAL_CHECK_TARGETS.json")
    results = read_json(ROOT / "research_ledger" / "FORMAL_CHECK_RESULTS.json")
    target = next((t for t in targets.get("targets", []) if t.get("id") == TARGET_ID), None)
    result = next((r for r in results.get("results", []) if r.get("target_id") == TARGET_ID), None)
    summary = {
        "target_present": target is not None,
        "result_present": result is not None,
        "target_status": target.get("status") if target else None,
        "result_status": result.get("result_status") if result else None,
    }
    if target is None:
        failures.append({"failure": "missing_target", "target_id": TARGET_ID})
    if result is None:
        failures.append({"failure": "missing_result", "target_id": TARGET_ID})
    elif result.get("result_status") not in {"DEFINED_NOT_RUN", "PASS_SOURCE_COVERAGE"}:
        failures.append({"failure": "unexpected_result_status", "target_id": TARGET_ID, "status": result.get("result_status")})
    return failures, summary


def run_check() -> FmBulkReadoutWitnessSchemaResult:
    failures: list[dict[str, Any]] = []
    schema_failures, schema_summary = check_schema_text()
    matrix_failures, matrix_summary = check_engineering_matrix()
    registry_failures, registry_summary = check_target_and_result_registry()
    failures.extend(schema_failures)
    failures.extend(matrix_failures)
    failures.extend(registry_failures)

    support_summary: dict[str, Any] = {
        **schema_summary,
        **matrix_summary,
        **registry_summary,
        "checked_interface": "ledger/schema guard for same_readout/different_bulk witness vocabulary and route readout-faithfulness discipline",
        "allowed_inference": "Formation Medium artifacts define a generated formal-candidate interface requiring explicit readout maps and scoped bulk equivalence relations",
        "blocked_inference": "S4 theorem, physical substrate non-faithfulness, engineering route non-faithfulness, product readiness, or investor proof",
    }
    return FmBulkReadoutWitnessSchemaResult(
        target_id=TARGET_ID,
        checker="fm_bulk_readout_witness_schema_guard_v1",
        status="PASS_SOURCE_COVERAGE" if not failures else "FAILED",
        inspected_files=[
            str(SCHEMA_PATH.relative_to(ROOT)),
            str(ENGINEERING_MATRIX_PATH.relative_to(ROOT)),
            "research_ledger/FORMAL_CHECK_TARGETS.json",
            "research_ledger/FORMAL_CHECK_RESULTS.json",
        ],
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_SOURCE_COVERAGE means the repo preserves a scoped generated witness-schema interface for "
            "same_readout/different_bulk and keeps physical engineering routes at READOUT_FAITHFULNESS_UNKNOWN unless "
            "separate evidence exists. It is not a mathematical proof, not an S4 theorem, not substrate evidence, "
            "not engineering readiness, not product readiness, and not a physical realization claim."
        ),
    )


def write_result(path: Path, result: FmBulkReadoutWitnessSchemaResult) -> None:
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
