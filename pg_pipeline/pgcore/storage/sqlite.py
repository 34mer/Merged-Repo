from __future__ import annotations

import json
import sqlite3
from pathlib import Path


def init_store(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS records "
            "(id TEXT PRIMARY KEY, kind TEXT NOT NULL, payload TEXT NOT NULL)"
        )


def put_record(path: Path, record: object) -> None:
    data = record.model_dump(mode="json")  # type: ignore[attr-defined]
    with sqlite3.connect(path) as conn:
        conn.execute(
            "INSERT OR REPLACE INTO records (id, kind, payload) VALUES (?, ?, ?)",
            (data["id"], data["kind"], json.dumps(data, sort_keys=True)),
        )

