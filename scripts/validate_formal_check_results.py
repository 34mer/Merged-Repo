from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(name: str) -> dict:
    path = ROOT / "research_ledger" / name
    assert path.exists(), name
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    targets = read_json("FORMAL_CHECK_TARGETS.json")
    results = read_json("FORMAL_CHECK_RESULTS.json")

    target_ids = {target["id"] for target in targets["targets"]}
    result_target_ids = {result["target_id"] for result in results["results"] if result["target_id"].startswith("CHK-")}
    assert target_ids <= result_target_ids

    vocab = set(results["result_status_vocab"])
    for result in results["results"]:
        assert result["target_id"]
        assert result["result_status"] in vocab
        assert result["result_summary"]

    assert any(result["result_status"] == "PASS_LEDGER_VALIDATION" for result in results["results"])
    assert "DEFINED_NOT_RUN is not evidence" in results["non_promotion_rule"]
    print("formal check result validation passed")


if __name__ == "__main__":
    main()
