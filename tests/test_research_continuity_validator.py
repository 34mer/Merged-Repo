from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_research_continuity_validator_passes() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "scripts/validate_research_continuity.py"],
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout
    assert "research continuity validation passed" in result.stdout
