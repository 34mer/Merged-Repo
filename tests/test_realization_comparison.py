from pathlib import Path

from pg_pipeline.scripts.run_realization_comparison import run_realization_comparison


def test_realization_comparison_passes(tmp_path: Path) -> None:
    summary = run_realization_comparison(run_id="test-comparison", output_dir=tmp_path / "comparison")
    assert summary["status"] == "passed"
    assert summary["relation"] == "ordered_specialization"
    assert summary["verdict"] == "supported"
    assert summary["authority_record_count"] == 4
