from __future__ import annotations

from pathlib import Path

from pg_pipeline.generators.families.grassmannian import generate_grassmannian_small
from pg_pipeline.kb.ingest import ingest_records
from pg_pipeline.scripts.init_db import init_db


def seed_kb(run_id: str, db_path: Path) -> int:
    records = generate_grassmannian_small(run_id=run_id)
    ingest_records(db_path, records)
    return len(records)


if __name__ == "__main__":
    path = init_db()
    print(seed_kb("manual-seed", path))

