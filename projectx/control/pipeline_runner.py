from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any

from projectx.eval.pipeline_monitor import evaluate_pipeline_summary
from projectx.kernel.state_store import append_authority_import, append_comparison_run, append_run
from projectx.review.decisions import decide_substrate_draft
from pg_pipeline.kb.ingest import ingest_records
from pg_pipeline.kb.retrieve import list_records
from pg_pipeline.pgcore.schemas.substrate_schema import SubstrateSchemaRecord
from pg_pipeline.scripts.ingest_exact_authority import ingest_exact_authority
from pg_pipeline.scripts.run_batch import run_vertical_slice
from pg_pipeline.scripts.run_realization_comparison import run_realization_comparison


@dataclass(frozen=True)
class ProjectXRunResult:
    run_id: str
    status: str
    output_dir: Path
    summary: dict[str, Any]


def run_research_pipeline(output_dir: Path | str = "runs/latest") -> ProjectXRunResult:
    """Outer-kernel entrypoint for the typed research operating slice.

    The supervised run records both the MVP positive-geometry lifecycle slice and the
    realization-class comparison carrier for the current R2↔R3 objective.
    """
    run_id = datetime.now(timezone.utc).strftime("projectx-%Y%m%dT%H%M%SZ")
    output_path = Path(output_dir)
    repo_root = Path(__file__).resolve().parents[2]
    catalog_path = repo_root / "exact_work" / "authority_catalog.yaml"

    summary = run_vertical_slice(run_id=run_id, output_dir=output_path)
    authority_summary = ingest_exact_authority(
        run_id=f"{run_id}-authority",
        catalog_path=catalog_path,
        output_dir=output_path / "exact_authority",
    )
    comparison_summary = run_realization_comparison(
        run_id=f"{run_id}-comparison",
        output_dir=output_path / "realization_comparison",
        catalog_path=catalog_path,
    )

    monitor = evaluate_pipeline_summary(summary)
    records = list_records(output_path / "records.sqlite")
    substrate_payload = next(
        record for record in records if record["id"] == summary["substrate_schema_id"]
    )
    substrate = SubstrateSchemaRecord.model_validate(substrate_payload)
    review_decision = decide_substrate_draft(substrate, run_id=run_id)
    ingest_records(output_path / "records.sqlite", [review_decision])
    review_path = output_path / "records" / f"{review_decision.id.replace(':', '_')}.json"
    review_path.write_text(
        json.dumps(review_decision.model_dump(mode="json"), indent=2, sort_keys=True),
        encoding="utf-8",
    )
    (output_path / "projectx_eval.json").write_text(
        json.dumps(monitor, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    state_path = Path("projectx/kernel/state/state.json")
    append_run(state_path, summary, str(output_path))
    append_authority_import(state_path, authority_summary, str(output_path / "exact_authority"))
    append_comparison_run(
        state_path,
        comparison_summary,
        str(output_path / "realization_comparison"),
    )

    combined_status = (
        "passed" if monitor["status"] == "passed" and comparison_summary["status"] == "passed" else "failed"
    )
    return ProjectXRunResult(
        run_id=run_id,
        status=combined_status,
        output_dir=output_path,
        summary={
            **summary,
            "projectx_eval": monitor,
            "review_decision_id": review_decision.id,
            "authority_summary": authority_summary,
            "comparison_summary": comparison_summary,
        },
    )
