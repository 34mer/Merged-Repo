from __future__ import annotations

import os
from pathlib import Path

DEFAULT_WORKSPACE_ROOT = Path(r"C:\ProjectX_codex_tmp")


def clone_workspace_root(repo_root: Path) -> Path:
    configured = os.getenv("PROJECTX_WORKSPACE_ROOT", "").strip() or os.getenv("PROJECTX_CODEX_TMP_ROOT", "").strip()
    if configured:
        root = Path(configured)
    elif DEFAULT_WORKSPACE_ROOT.exists():
        root = DEFAULT_WORKSPACE_ROOT
    else:
        root = repo_root.parent
    root.mkdir(parents=True, exist_ok=True)
    return root
