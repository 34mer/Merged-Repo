from __future__ import annotations

from pathlib import Path

from pg_pipeline.scripts.run_batch import run_vertical_slice
from projectx.control.pipeline_runner import run_research_pipeline


def test_inner_vertical_slice_passes(tmp_path: Path) -> None:
    summary = run_vertical_slice(run_id="test-inner", output_dir=tmp_path / "inner")
    assert summary["status"] == "passed"
    assert summary["substrate_schema_id"].startswith("substrate_schema_record:")
    assert (tmp_path / "inner" / "weekly_summary.json").exists()


def test_projectx_supervised_slice_records_review(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    result = run_research_pipeline(tmp_path / "outer")
    assert result.status == "passed"
    assert result.summary["review_decision_id"].startswith("review_decision_record:")
    assert result.summary["authority_summary"]["authority_records"] == 4
    assert (tmp_path / "projectx" / "kernel" / "state" / "state.json").exists()
