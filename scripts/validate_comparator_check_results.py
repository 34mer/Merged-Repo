from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path) -> dict[str, Any]:
    assert path.exists(), str(path)
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    targets = read_json(ROOT / "research_ledger" / "COMPARATOR_CHECK_TARGETS.json")
    results = read_json(ROOT / "research_ledger" / "COMPARATOR_CHECK_RESULTS.json")

    target_by_id = {target["id"]: target for target in targets["targets"]}
    target_ids = set(target_by_id)
    result_ids = {result["target_id"] for result in results["results"]}
    assert target_ids <= result_ids
    vocab = set(results["result_status_vocab"])

    for result in results["results"]:
        target_id = result["target_id"]
        assert target_id in target_ids
        assert result["result_status"] in vocab
        assert result["result_summary"]
        if result["result_status"] == "PASS_PARTIAL_COMPARATOR":
            target = target_by_id[target_id]
            artifact_path = ROOT / result["artifact"]
            artifact = read_json(artifact_path)
            assert artifact["target_id"] == target_id
            assert artifact["status"] == "PASS_PARTIAL_COMPARATOR"
            assert artifact["counterexamples"] == []
            assert artifact["compared_families"] == target["families"], target_id
            assert artifact["row_scope"] == target["rows"], target_id
            assert artifact["input_artifacts"] == target["input_artifacts"], target_id
            assert "not" in artifact["status_boundary"].lower()
            assert "not theorem status" in results["non_promotion_rule"]

    print("comparator check result validation passed")


if __name__ == "__main__":
    main()
