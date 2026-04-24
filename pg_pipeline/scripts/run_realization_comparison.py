from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from pg_pipeline.check.comparison import check_r2_r3_comparison
from pg_pipeline.generators.families.ledger_catalog import generate_authority_records
from pg_pipeline.generators.families.realization_comparison import generate_r2_r3_comparison
from pg_pipeline.kb.ingest import ingest_records
from pg_pipeline.pgcore.storage.migrations import run_migrations


def _write_record(path: Path, record: object) -> None:
    path.write_text(json.dumps(record.model_dump(mode="json"), indent=2, sort_keys=True), encoding="utf-8")


def run_realization_comparison(
    run_id: str | None = None,
    output_dir: Path | str = "runs/realization_comparison",
    catalog_path: Path | str = "exact_work/authority_catalog.yaml",
) -> dict[str, object]:
    actual_run_id = run_id or datetime.now(timezone.utc).strftime("cmp-%Y%m%dT%H%M%SZ")
    out = Path(output_dir)
    records_dir = out / "records"
    records_dir.mkdir(parents=True, exist_ok=True)
    db_path = out / "records.sqlite"
    run_migrations(db_path)

    authority_records = generate_authority_records(Path(catalog_path), run_id=f"{actual_run_id}-authority")
    comparison = generate_r2_r3_comparison(authority_records, run_id=actual_run_id)
    check = check_r2_r3_comparison(comparison, run_id=actual_run_id)
    all_records: list[object] = [*authority_records, comparison, check]
    ingest_records(db_path, all_records)
    for record in all_records:
        _write_record(records_dir / f"{record.id.replace(':', '_')}.json", record)
    summary = {
        "run_id": actual_run_id,
        "status": "passed" if check.payload.passed else "failed",
        "family": "realization_class_comparison",
        "comparison_id": comparison.id,
        "check_id": check.id,
        "relation": comparison.payload.relation,
        "verdict": comparison.payload.verdict,
        "authority_record_count": len(authority_records),
        "unresolved_deficits": comparison.payload.unresolved_deficits,
    }
    (out / "comparison_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    return summary


if __name__ == "__main__":
    print(json.dumps(run_realization_comparison(), indent=2, sort_keys=True))
