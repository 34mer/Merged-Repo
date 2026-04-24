from __future__ import annotations

import json
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
    assert result.summary["comparison_summary"]["status"] == "passed"
    assert result.summary["comparison_summary"]["relation"] == "ordered_specialization"
    assert result.summary["comparison_summary"]["verdict"] == "supported"
    assert (tmp_path / "outer" / "realization_comparison" / "comparison_summary.json").exists()

    state_path = tmp_path / "projectx" / "kernel" / "state" / "state.json"
    assert state_path.exists()
    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert state["comparison_runs"]
    assert state["comparison_runs"][-1]["family"] == "realization_class_comparison"
    assert state["comparison_runs"][-1]["relation"] == "ordered_specialization"
