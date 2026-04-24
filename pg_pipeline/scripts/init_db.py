from __future__ import annotations

from pathlib import Path

from pg_pipeline.pgcore.storage.migrations import run_migrations


def init_db(path: Path | str = "runs/latest/records.sqlite") -> Path:
    db_path = Path(path)
    run_migrations(db_path)
    return db_path


if __name__ == "__main__":
    print(init_db())

