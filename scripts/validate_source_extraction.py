from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(name: str) -> dict:
    path = ROOT / "research_ledger" / name
    assert path.exists(), name
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    corpus = read_json("SOURCE_CORPUS.json")
    claims = read_json("SOURCE_EXTRACTED_CLAIMS.json")
    targets = read_json("FORMAL_CHECK_TARGETS.json")

    manifest_paper_ids = {p["paper_id"] for p in corpus["papers"]}
    claim_ids = [c["id"] for c in claims["claims"]]
    claim_id_set = set(claim_ids)
    target_ids = {t["id"] for t in targets["targets"]}
    claimed_paper_ids = {c["paper_id"] for c in claims["claims"]}

    assert corpus["paper_count"] == 16
    assert len(manifest_paper_ids) == 16
    assert len(claim_ids) == len(claim_id_set), "claim ids must be unique"
    assert manifest_paper_ids <= claimed_paper_ids, sorted(manifest_paper_ids - claimed_paper_ids)
    assert claimed_paper_ids <= manifest_paper_ids, sorted(claimed_paper_ids - manifest_paper_ids)
    assert len(claim_id_set) >= 16
    assert len(target_ids) >= 11

    for claim in claims["claims"]:
        assert claim["paper_id"] in manifest_paper_ids
        assert claim["source_file"]
        assert claim["source_anchor"]
        assert claim["claim_text"]
        assert "SOURCE_EXTRACTED" in claim["status"]
        assert claim["formal_check_targets"], claim["id"]
        for target_id in claim["formal_check_targets"]:
            assert target_id in target_ids, target_id

    for target in targets["targets"]:
        assert target["predicate"]
        assert target["failure_condition"]
        for claim_id in target["claim_ids"]:
            assert claim_id in claim_id_set, claim_id

    assert any("R13" in t.get("rows", []) for t in targets["targets"])
    assert any("S" in c.get("families", []) for c in claims["claims"])
    assert any(c["paper_id"] == "COSMO_COMB_2026" for c in claims["claims"])
    print("source extraction validation passed")


if __name__ == "__main__":
    main()
