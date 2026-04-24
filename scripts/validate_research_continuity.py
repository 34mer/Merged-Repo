from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(relative: str) -> dict:
    path = ROOT / relative
    if not path.exists():
        raise AssertionError(f"missing file: {relative}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    ledger = load_json("research_ledger/R1_R14_DISCRIMINATOR_LEDGER.json")
    arch = load_json("research_ledger/CONTINUITY_ARCHITECTURE_STATE.json")
    matrix = load_json("research_ledger/ROW_FAMILY_COVERAGE_MATRIX.json")

    required_rows = {f"R{i}" for i in range(1, 15)}
    ledger_rows = {row["id"] for row in ledger["rows"]}
    matrix_rows = {row["row"] for row in matrix["rows"]}
    assert ledger_rows == required_rows
    assert matrix_rows == required_rows

    r14 = next(row for row in ledger["rows"] if row["id"] == "R14")
    assert "OPEN" in r14["status"]
    assert "DEFICIT" in r14["status"]

    family_ids = {family["id"] for family in matrix["families"]}
    required_families = {"A", "M1", "C", "GAssoc", "S", "PGfinite", "CRBSM"}
    assert required_families <= family_ids

    for row in matrix["rows"]:
        assert required_families <= set(row["coverage"])
        for entry in row["coverage"].values():
            assert entry["status"] in matrix["coverage_status_vocab"]
            assert entry["note"]

    for filename in arch["required_files"]:
        assert (ROOT / filename).exists(), filename

    paper_ids = {paper["id"] for paper in arch["paper_source_records"]}
    assert len(paper_ids) >= 16
    assert "SURF_COUNT_2023" in paper_ids
    assert "COSMO_COMB_2026" in paper_ids

    print("research continuity validation passed")


if __name__ == "__main__":
    main()
