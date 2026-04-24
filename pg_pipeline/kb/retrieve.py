from __future__ import annotations

import json
import sqlite3
from pathlib import Path


def list_records(db_path: Path) -> list[dict[str, object]]:
    with sqlite3.connect(db_path) as conn:
        rows = conn.execute("SELECT payload FROM records ORDER BY id").fetchall()
    return [json.loads(row[0]) for row in rows]

