from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from pg_pipeline.check.combinatorial import check_combinatorial
from pg_pipeline.check.policy import all_checks_passed
from pg_pipeline.check.symbolic import check_symbolic
from pg_pipeline.generators.families.grassmannian import generate_grassmannian_small
from pg_pipeline.kb.ingest import ingest_records
from pg_pipeline.normalize.deterministic import normalize_records
from pg_pipeline.pgcore.storage.migrations import run_migrations
from pg_pipeline.propose.proposer_worker import propose_recurrence
from pg_pipeline.review.weekly import build_weekly_summary
from pg_pipeline.stress.heldout import stress_heldout
from pg_pipeline.stress.mutations import stress_symmetry_break
from pg_pipeline.substrate.compiler import compile_substrate_schema


def _write_record(path: Path, record: object) -> None:
    path.write_text(json.dumps(record.model_dump(mode="json"), indent=2, sort_keys=True), encoding="utf-8")


def run_vertical_slice(run_id: str | None = None, output_dir: Path | str = "runs/latest") -> dict[str, object]:
    actual_run_id = run_id or datetime.now(timezone.utc).strftime("pg-%Y%m%dT%H%M%SZ")
    out = Path(output_dir)
    records_dir = out / "records"
    records_dir.mkdir(parents=True, exist_ok=True)
    db_path = out / "records.sqlite"
    run_migrations(db_path)

    generated = generate_grassmannian_small(run_id=actual_run_id)
    normalized = normalize_records(generated)
    proposal = propose_recurrence(normalized, run_id=actual_run_id)
    checks = [
        check_symbolic(proposal, normalized, run_id=actual_run_id),
        check_combinatorial(proposal, normalized, run_id=actual_run_id),
    ]
    stresses = [
        stress_heldout(proposal, run_id=actual_run_id),
        stress_symmetry_break(proposal, run_id=actual_run_id),
    ]
    if not all_checks_passed(checks) or not all(stress.payload.passed for stress in stresses):
        status = "failed"
    else:
        status = "passed"
    substrate = compile_substrate_schema(proposal, checks, stresses, run_id=actual_run_id)
    summary = build_weekly_summary(normalized, proposal, checks, stresses, substrate)
    summary = {"run_id": actual_run_id, "status": status, **summary}

    all_records: list[object] = [*normalized, proposal, *checks, *stresses, substrate]
    ingest_records(db_path, all_records)
    for record in all_records:
        _write_record(records_dir / f"{record.id.replace(':', '_')}.json", record)
    (out / "weekly_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    return summary


if __name__ == "__main__":
    print(json.dumps(run_vertical_slice(), indent=2, sort_keys=True))

