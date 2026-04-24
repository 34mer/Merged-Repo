from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT / "formal_handoff"


def read_json(path: Path) -> dict:
    assert path.exists(), str(path.relative_to(ROOT))
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    required_files = [
        HANDOFF / "README.md",
        HANDOFF / "FORMALIZATION_QUEUE.json",
        HANDOFF / "ARISTOTLE_TARGETS.md",
        HANDOFF / "SAGE_Z3_TARGETS.md",
    ]
    for path in required_files:
        assert path.exists(), str(path.relative_to(ROOT))

    queue = read_json(HANDOFF / "FORMALIZATION_QUEUE.json")
    targets = read_json(ROOT / "research_ledger" / "FORMAL_CHECK_TARGETS.json")
    target_ids = {target["id"] for target in targets["targets"]}

    items = queue["queue"]
    assert len(items) >= 5
    assert [item["priority"] for item in items] == sorted(item["priority"] for item in items)

    tool_union = set()
    for item in items:
        assert item["target_id"] in target_ids
        assert item["recommended_tools"]
        assert item["inputs"]
        assert item["expected_output"]
        assert item["status"] == "READY_FOR_FORMALIZATION"
        tool_union.update(item["recommended_tools"])

    assert "Aristotle" in tool_union
    assert "Lean" in tool_union
    assert "Sage" in tool_union
    assert "Z3" in tool_union

    aris_text = (HANDOFF / "ARISTOTLE_TARGETS.md").read_text(encoding="utf-8")
    sage_text = (HANDOFF / "SAGE_Z3_TARGETS.md").read_text(encoding="utf-8")
    assert "R13 equality-layer status" in aris_text
    assert "Cosmohedron move-class finite check" in sage_text
    assert "DEFINED_NOT_RUN" not in queue.get("status", "")

    print("formal handoff validation passed")


if __name__ == "__main__":
    main()
