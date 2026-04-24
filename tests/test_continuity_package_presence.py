from __future__ import annotations

from pathlib import Path


REQUIRED_CONTINUITY_FILES = [
    "research_ledger/THREAD_CONTINUITY_ARCHITECTURE.md",
    "research_ledger/PAPER_SOURCE_LEDGER.md",
    "research_ledger/EXTRACTION_LEDGER.md",
    "research_ledger/SUPPORT_CAUTION_SURVIVOR_LEDGER.md",
    "research_ledger/COMPARATOR_PACKAGE_REGISTER.md",
    "research_ledger/SURFACEOLOGY_COMPARATOR_PACKAGE.md",
    "research_ledger/OPERATIONS_REGISTER.md",
    "research_ledger/COLD_START_CONTINUATION_PACKAGE.md",
]


def test_continuity_package_files_exist() -> None:
    for filename in REQUIRED_CONTINUITY_FILES:
        assert Path(filename).exists(), filename


def test_cold_start_package_preserves_no_promotion_rules() -> None:
    text = Path("research_ledger/COLD_START_CONTINUATION_PACKAGE.md").read_text(encoding="utf-8")
    assert "R14 is open/deficit" in text
    assert "Surfaceology is underrepresented" in text
    assert "Do not promote generated claims" in text


def test_operations_register_tracks_mcp_and_failure_modes() -> None:
    text = Path("research_ledger/OPERATIONS_REGISTER.md").read_text(encoding="utf-8")
    assert "Failure-mode registry" in text
    assert "Tool / MCP registry" in text
