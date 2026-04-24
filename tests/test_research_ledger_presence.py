from __future__ import annotations

import json
from pathlib import Path


def test_r1_r14_ledger_has_all_rows() -> None:
    path = Path("research_ledger/R1_R14_DISCRIMINATOR_LEDGER.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = {row["id"] for row in data["rows"]}
    assert rows == {f"R{i}" for i in range(1, 15)}
    assert data["authority_status"] == "continuity_ledger_not_theorem_certification"


def test_r14_is_explicitly_open_deficit() -> None:
    data = json.loads(Path("research_ledger/R1_R14_DISCRIMINATOR_LEDGER.json").read_text(encoding="utf-8"))
    r14 = next(row for row in data["rows"] if row["id"] == "R14")
    assert "OPEN" in r14["status"]
    assert "DEFICIT" in r14["status"]


def test_realization_matrix_file_exists() -> None:
    assert Path("research_ledger/REALIZATION_CLASS_MATRIX.md").exists()
    assert Path("research_ledger/PROOF_OBLIGATIONS.md").exists()
