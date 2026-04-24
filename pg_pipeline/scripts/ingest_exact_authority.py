from __future__ import annotations

import json
from pathlib import Path

from pg_pipeline.generators.families.ledger_catalog import generate_authority_records
from pg_pipeline.kb.ingest import ingest_records
from pg_pipeline.pgcore.storage.migrations import run_migrations


def ingest_exact_authority(
    run_id: str = "exact-authority-import",
    catalog_path: Path | str = "exact_work/authority_catalog.yaml",
    output_dir: Path | str = "runs/exact_authority",
) -> dict[str, object]:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    records_dir = out / "records"
    records_dir.mkdir(exist_ok=True)
    db_path = out / "records.sqlite"
    run_migrations(db_path)
    records = generate_authority_records(Path(catalog_path), run_id=run_id)
    ingest_records(db_path, records)
    for record in records:
        path = records_dir / f"{record.id.replace(':', '_')}.json"
        path.write_text(json.dumps(record.model_dump(mode="json"), indent=2, sort_keys=True), encoding="utf-8")
    summary = {
        "run_id": run_id,
        "status": "passed",
        "authority_records": len(records),
        "families": [record.scope.family for record in records],
    }
    (out / "authority_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    return summary


if __name__ == "__main__":
    print(json.dumps(ingest_exact_authority(), indent=2, sort_keys=True))

