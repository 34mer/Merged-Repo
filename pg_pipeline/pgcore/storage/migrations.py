from __future__ import annotations

from pathlib import Path

from .sqlite import init_store


def run_migrations(path: Path) -> None:
    init_store(path)

