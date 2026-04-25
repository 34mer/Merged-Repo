from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "research_ledger"

FM_MARKDOWN_FILES = [
    LEDGER / "S2_STAR_S4_DISTINCTNESS_CANDIDATE.md",
    LEDGER / "FORMATION_MEDIUM_LAYER_0_SPEC.md",
    LEDGER / "FORMATION_MEDIUM_LAYER_1_SPEC.md",
]

FM_JSON_FILES = [
    LEDGER / "FORMATION_MEDIUM_LAYER_1_CANDIDATE_CONSTRAINTS.json",
]

REQUIRED_HEADER_TAGS = [
    "STATUS:",
    "ARGUMENT_STATUS:",
    "CHECK_STATUS:",
    "PROMOTION_STATUS:",
    "DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json",
]

FORBIDDEN_PROMOTION_PATTERNS = [
    r"STATUS:\s*SOURCE_EXTRACTED\b",
    r"CHECK_STATUS:\s*CHECKED\b",
    r"FORMALLY_CHECKED",
    r"PASS_FINITE_CHECK",
    r"PASS_PARTIAL_FINITE_CHECK",
]

REQUIRED_CAUTION_TERMS = [
    "GENERATED",
    "OPEN",
    "CANDIDATE",
    "BLOCKED",
]

REQUIRED_BLOCKER_TERMS = [
    "Promotion blocker",
    "Promotion blockers",
    "PROMOTION_STATUS: BLOCKED",
    "Kill Conditions",
    "Non-Promotion Footer",
]


def read_text(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def read_json(path: Path) -> Any:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return json.loads(path.read_text(encoding="utf-8"))


def assert_markdown_discipline(path: Path) -> None:
    text = read_text(path)
    rel = path.relative_to(ROOT)

    for tag in REQUIRED_HEADER_TAGS:
        assert tag in text, f"{rel}: missing required header tag {tag!r}"

    for term in REQUIRED_CAUTION_TERMS:
        assert term in text, f"{rel}: missing caution/status term {term!r}"

    assert any(term in text for term in REQUIRED_BLOCKER_TERMS), f"{rel}: missing blocker/kill-condition language"
    assert "SOURCE_EXTRACTED_CLAIMS.json" in text, f"{rel}: must explicitly avoid source-extracted claim registry"
    assert "not a source-extracted claim" in text.lower(), f"{rel}: must include non-source-extracted notice"
    assert "not a theorem" in text.lower() or "not a formal theorem" in text.lower(), f"{rel}: must include non-theorem notice"

    for pattern in FORBIDDEN_PROMOTION_PATTERNS:
        assert not re.search(pattern, text), f"{rel}: forbidden promotion pattern {pattern!r}"

    if "Formation Medium" in text or "formation medium" in text:
        assert "physical realization" in text.lower() or "substrate interpretation" in text.lower(), (
            f"{rel}: formation-medium artifact must explicitly caution physical/substrate interpretation"
        )


def assert_json_constraint_discipline(path: Path) -> None:
    data = read_json(path)
    rel = path.relative_to(ROOT)
    statuses = set(data.get("status", []))
    assert "GENERATED" in statuses, f"{rel}: top-level status must include GENERATED"
    assert "OPEN" in statuses, f"{rel}: top-level status must include OPEN"
    assert "NOT_CHECKED" in statuses, f"{rel}: top-level status must include NOT_CHECKED"
    assert "NOT_SOURCE_EXTRACTED" in statuses, f"{rel}: top-level status must include NOT_SOURCE_EXTRACTED"
    assert data.get("non_promotion_rule"), f"{rel}: missing non_promotion_rule"

    constraints = data.get("candidate_constraints")
    assert isinstance(constraints, list) and constraints, f"{rel}: missing candidate_constraints"
    ids = [c.get("id") for c in constraints]
    assert len(ids) == len(set(ids)), f"{rel}: duplicate constraint ids"

    for c in constraints:
        cid = c.get("id")
        cstatus = set(c.get("status", []))
        assert cid and str(cid).startswith("FM1-C"), f"{rel}: malformed constraint id {cid!r}"
        assert c.get("slot"), f"{rel}:{cid}: missing slot"
        assert c.get("constraint"), f"{rel}:{cid}: missing constraint"
        assert "GENERATED" in cstatus, f"{rel}:{cid}: must include GENERATED"
        assert "OPEN" in cstatus, f"{rel}:{cid}: must include OPEN"
        assert c.get("source_leads"), f"{rel}:{cid}: missing source_leads"
        assert c.get("promotion_blockers"), f"{rel}:{cid}: missing promotion_blockers"
        assert "CHECKED" not in cstatus, f"{rel}:{cid}: cannot be CHECKED"
        assert "SOURCE_EXTRACTED" not in cstatus, f"{rel}:{cid}: cannot be SOURCE_EXTRACTED"


def assert_not_in_source_extracted_claims() -> None:
    claims = read_json(LEDGER / "SOURCE_EXTRACTED_CLAIMS.json")
    claim_text = json.dumps(claims, ensure_ascii=False)
    forbidden = [
        "FORMATION_MEDIUM_LAYER_0_SPEC",
        "FORMATION_MEDIUM_LAYER_1_SPEC",
        "S2_STAR_S4_DISTINCTNESS_CANDIDATE",
        "formation_medium_candidate",
        "FM1-C",
    ]
    for token in forbidden:
        assert token not in claim_text, f"SOURCE_EXTRACTED_CLAIMS.json contains generated FM token {token!r}"


def main() -> None:
    for path in FM_MARKDOWN_FILES:
        assert_markdown_discipline(path)
    for path in FM_JSON_FILES:
        assert_json_constraint_discipline(path)
    assert_not_in_source_extracted_claims()
    print("formation medium discipline validation passed")


if __name__ == "__main__":
    main()
