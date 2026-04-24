from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(name: str) -> dict:
    path = ROOT / "research_ledger" / name
    assert path.exists(), name
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    claims = read_json("SOURCE_EXTRACTED_CLAIMS.json")
    targets = read_json("FORMAL_CHECK_TARGETS.json")
    claim_ids = {c["id"] for c in claims["claims"]}
    target_ids = {t["id"] for t in targets["targets"]}

    assert len(claim_ids) >= 8
    assert len(target_ids) >= 8
    assert {"COSMO_2024", "COSMO_COMB_2026", "SCAT_FORMS_2017", "BINARY_AMP_2017", "SCAFFOLD_GLUONS_2024"} <= {c["paper_id"] for c in claims["claims"]}

    for claim in claims["claims"]:
        assert claim["paper_id"]
        assert claim["source_anchor"]
        assert claim["claim_text"]
        assert "SOURCE_EXTRACTED" in claim["status"]
        for target_id in claim["formal_check_targets"]:
            assert target_id in target_ids

    for target in targets["targets"]:
        assert target["predicate"]
        assert target["failure_condition"]
        for claim_id in target["claim_ids"]:
            assert claim_id in claim_ids

    assert any("R13" in t.get("rows", []) for t in targets["targets"])
    assert any("S" in c.get("families", []) for c in claims["claims"])
    print("source extraction validation passed")


if __name__ == "__main__":
    main()
