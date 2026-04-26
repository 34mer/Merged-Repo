from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "LEDGER-R14-CLASS-MATRIX-SCHEMA"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
MATRIX_PATH = ROOT / "research_ledger" / "R1_R14_CLASS_MATRIX_CANDIDATE.json"

REQUIRED_TOP_STATUS = {"GENERATED", "OPEN", "DEFICIT", "CANDIDATE", "NOT_CHECKED"}
REQUIRED_ROWS = {f"R{i}" for i in range(1, 15)}
REQUIRED_PRIME_CONTACTS = {
    "R1": {
        "source": {"EXT-AMP-PRIME-002", "EXT-AMP-PRIME-003", "EXT-AMP-PRIME-004"},
        "checks": {"CHK-PRIME-LOCAL-CARRIER-SOURCE-COVERAGE"},
    },
    "R7": {
        "source": {"EXT-AMP-PRIME-001", "EXT-AMP-PRIME-002", "EXT-AMP-PRIME-003", "EXT-AMP-PRIME-004", "EXT-AMP-PRIME-005"},
        "checks": {"CHK-PRIME-LOCAL-CARRIER-SOURCE-COVERAGE", "CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION"},
    },
    "R13": {
        "source": {"EXT-AMP-PRIME-001", "EXT-AMP-PRIME-005"},
        "checks": {"CHK-PRIME-LOCAL-CARRIER-SOURCE-COVERAGE", "CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION"},
    },
    "R14": {
        "source": {"EXT-AMP-PRIME-001", "EXT-AMP-PRIME-002", "EXT-AMP-PRIME-003", "EXT-AMP-PRIME-004", "EXT-AMP-PRIME-005"},
        "checks": {"CHK-PRIME-LOCAL-CARRIER-SOURCE-COVERAGE", "CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION"},
    },
}

FORBIDDEN_PROMOTIONS = [
    "r14 is solved",
    "r14 solved",
    "class matrix solved",
    "substrate proven",
    "physical substrate proven",
    "matrix proves engineering readiness",
    "matrix proves product readiness",
    "matrix is investor proof",
    "matrix has theorem status",
]


@dataclass(frozen=True)
class R14ClassMatrixSchemaResult:
    target_id: str
    checker: str
    status: str
    inspected_file: str
    support_summary: dict[str, Any]
    counterexamples: list[dict[str, Any]]
    status_boundary: str


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def entry_key(entry: dict[str, Any]) -> tuple[str, str]:
    return str(entry.get("family_or_route")), str(entry.get("row"))


def check_matrix() -> R14ClassMatrixSchemaResult:
    failures: list[dict[str, Any]] = []
    if not MATRIX_PATH.exists():
        failures.append({"failure": "missing_matrix", "path": str(MATRIX_PATH.relative_to(ROOT))})
        data: dict[str, Any] = {}
    else:
        data = read_json(MATRIX_PATH)

    top_status = set(data.get("status", []))
    missing_status = sorted(REQUIRED_TOP_STATUS - top_status)
    if missing_status:
        failures.append({"failure": "top_status_missing", "missing": missing_status, "observed": sorted(top_status)})

    non_promotion = str(data.get("non_promotion_rule", ""))
    if "does not solve R14" not in non_promotion and "does not solve r14" not in non_promotion.lower():
        failures.append({"failure": "non_promotion_rule_does_not_preserve_r14_open"})

    rows = data.get("rows", [])
    row_ids = {str(row.get("row")) for row in rows}
    if row_ids != REQUIRED_ROWS:
        failures.append({"failure": "row_set_mismatch", "observed": sorted(row_ids), "expected": sorted(REQUIRED_ROWS)})

    families = data.get("families", [])
    family_ids = {str(f.get("family_or_route")) for f in families}
    if len(family_ids) < 11:
        failures.append({"failure": "too_few_families_or_routes", "observed_count": len(family_ids)})

    entries = data.get("matrix_entries", [])
    expected_entry_count = len(row_ids) * len(family_ids)
    if len(entries) != expected_entry_count:
        failures.append({"failure": "matrix_entry_count_mismatch", "observed": len(entries), "expected": expected_entry_count})

    seen_keys: set[tuple[str, str]] = set()
    for entry in entries:
        key = entry_key(entry)
        if key in seen_keys:
            failures.append({"failure": "duplicate_matrix_entry", "family_or_route": key[0], "row": key[1]})
        seen_keys.add(key)
        for field in ["family_or_route", "row", "row_name", "cell_status", "promotion_status", "notes"]:
            if not entry.get(field):
                failures.append({"failure": "entry_missing_required_field", "family_or_route": key[0], "row": key[1], "field": field})
        if entry.get("promotion_status") != "BLOCKED":
            failures.append({"failure": "entry_not_promotion_blocked", "family_or_route": key[0], "row": key[1], "promotion_status": entry.get("promotion_status")})
        if key[1] == "R14" and "OPEN" not in str(entry.get("cell_status", "")):
            failures.append({"failure": "r14_cell_not_open", "family_or_route": key[0], "cell_status": entry.get("cell_status")})

    entries_by_key = {entry_key(entry): entry for entry in entries}
    for row, spec in REQUIRED_PRIME_CONTACTS.items():
        entry = entries_by_key.get(("Prime", row))
        if entry is None:
            failures.append({"failure": "missing_prime_populated_cell", "row": row})
            continue
        source_contacts = set(entry.get("source_contacts", []))
        check_contacts = set(entry.get("check_contacts", []))
        missing_source = sorted(spec["source"] - source_contacts)
        missing_checks = sorted(spec["checks"] - check_contacts)
        if missing_source:
            failures.append({"failure": "prime_cell_missing_source_contacts", "row": row, "missing": missing_source})
        if missing_checks:
            failures.append({"failure": "prime_cell_missing_check_contacts", "row": row, "missing": missing_checks})
        notes = normalize(str(entry.get("notes", "")))
        if "not" not in notes or "substrate" not in notes and row in {"R1", "R7", "R14"}:
            failures.append({"failure": "prime_cell_notes_missing_non_promotion_caution", "row": row})

    matrix_text = normalize(json.dumps(data, ensure_ascii=False))
    for phrase in FORBIDDEN_PROMOTIONS:
        if phrase in matrix_text:
            failures.append({"failure": "forbidden_promotion_phrase", "phrase": phrase})

    summary: dict[str, Any] = {
        "row_count": len(row_ids),
        "family_or_route_count": len(family_ids),
        "matrix_entry_count": len(entries),
        "expected_entry_count": expected_entry_count,
        "prime_cells_checked": sorted(REQUIRED_PRIME_CONTACTS),
        "r14_cells_open": all("OPEN" in str(entry.get("cell_status", "")) for entry in entries if entry.get("row") == "R14"),
        "top_status": sorted(top_status),
        "checked_interface": "R14 class-matrix candidate schema, Prime source/check-populated cells, and R14-open preservation",
        "allowed_inference": "the matrix is a structured work surface with partial source/check contacts for Prime cells",
        "blocked_inference": "R14 closure, theorem status, Formation Medium substrate evidence, engineering readiness, product readiness, or investor proof",
    }

    return R14ClassMatrixSchemaResult(
        target_id=TARGET_ID,
        checker="r14_class_matrix_schema_guard_v1",
        status="PASS_LEDGER_VALIDATION" if not failures else "FAILED",
        inspected_file=str(MATRIX_PATH.relative_to(ROOT)),
        support_summary=summary,
        counterexamples=failures,
        status_boundary=(
            "PASS_LEDGER_VALIDATION means the R14 matrix candidate has the expected row/family shape, "
            "required blocked statuses, Prime source/check contacts, and explicit R14-open preservation. "
            "It is not a mathematical proof, not a class-matrix completion, not theorem status, "
            "not substrate evidence, not engineering readiness, and not product readiness."
        ),
    )


def write_result(path: Path, result: R14ClassMatrixSchemaResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(result), indent=2, sort_keys=True), encoding="utf-8")


def main() -> None:
    result = check_matrix()
    write_result(RESULT_PATH, result)
    print(json.dumps(asdict(result), indent=2, sort_keys=True))
    if result.status == "FAILED":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
