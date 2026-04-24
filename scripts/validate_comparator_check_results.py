from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path) -> dict:
    assert path.exists(), str(path)
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    targets = read_json(ROOT / "research_ledger" / "COMPARATOR_CHECK_TARGETS.json")
    results = read_json(ROOT / "research_ledger" / "COMPARATOR_CHECK_RESULTS.json")

    target_ids = {target["id"] for target in targets["targets"]}
    result_ids = {result["target_id"] for result in results["results"]}
    assert target_ids <= result_ids
    vocab = set(results["result_status_vocab"])

    for result in results["results"]:
        assert result["target_id"] in target_ids
        assert result["result_status"] in vocab
        assert result["result_summary"]
        if result["result_status"] == "PASS_PARTIAL_COMPARATOR":
            artifact_path = ROOT / result["artifact"]
            artifact = read_json(artifact_path)
            assert artifact["target_id"] == result["target_id"]
            assert artifact["status"] == "PASS_PARTIAL_COMPARATOR"
            assert artifact["counterexamples"] == []
            assert artifact["compared_families"] == ["A", "C"]
            assert "not" in artifact["status_boundary"].lower()
            assert "not theorem status" in results["non_promotion_rule"]

    print("comparator check result validation passed")


if __name__ == "__main__":
    main()
