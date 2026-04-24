from __future__ import annotations

from pathlib import Path

from pg_pipeline.pgcore.storage.sqlite import put_record


def ingest_records(db_path: Path, records: list[object]) -> None:
    for record in records:
        put_record(db_path, record)

