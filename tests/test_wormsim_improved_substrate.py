from __future__ import annotations

import json
from pathlib import Path

from wormsim.abstraction import train_pca_ridge
from wormsim.dataset import collect_dataset
from wormsim.improvement import benchmark_improved_substrate, train_improved_substrate
from wormsim.repair import run_repair_test
from wormsim.reports import generate_improved_substrate_report


def test_train_improved_substrate_and_repair(tmp_path: Path) -> None:
    dataset_dir = tmp_path / "dataset"
    base_dir = tmp_path / "base"
    improved_dir = tmp_path / "improved"
    repair_dir = tmp_path / "repair"

    collect_dataset(dataset_dir, tasks="dynamic_food,time_harm,memory,switch,hard_mixed", episodes=5, steps=16, seed=31)
    train_pca_ridge(dataset_dir, base_dir, latent_dim=8)
    metadata = train_improved_substrate(base_dir, dataset_dir, improved_dir, latent_dim=8)
    repair = run_repair_test(improved_dir, repair_dir, task_name="hard_mixed", steps_before=8, steps_after=12, seed=31)

    assert metadata["schema"] == "wormsim-improved-substrate-v1"
    assert metadata["latent_dim"] == 8
    assert (improved_dir / "model.npz").exists()
    assert repair["status"] == "REPAIR TEST COMPLETE"
    assert 0.0 <= repair["mean_repair_score"] <= 1.0


def test_benchmark_improved_substrate_report(tmp_path: Path) -> None:
    dataset_dir = tmp_path / "dataset"
    base_dir = tmp_path / "base"
    improved_dir = tmp_path / "improved"
    report_dir = tmp_path / "report"

    collect_dataset(dataset_dir, tasks="dynamic_food,time_harm,memory,switch,hard_mixed", episodes=5, steps=18, seed=37)
    train_pca_ridge(dataset_dir, base_dir, latent_dim=8)
    train_improved_substrate(base_dir, dataset_dir, improved_dir, latent_dim=8)
    report = benchmark_improved_substrate(
        source_dataset=dataset_dir,
        base_model=base_dir,
        improved_model=improved_dir,
        out=report_dir,
        task_name="hard_mixed",
        steps=25,
        migration_steps=10,
        seed=37,
        equivalence_threshold=0.50,
        include_controls=True,
    )
    paths = generate_improved_substrate_report(report, report_dir)

    assert report["status"] == "PROCESS-PRESERVING SUBSTRATE OPTIMIZATION COMPLETE"
    assert "equivalence_score" in report["improved"]["scores"]
    assert "efficiency_score" in report["improved"]["scores"]
    assert "repairability_score" in report["improved"]["scores"]
    assert Path(paths["json"]).exists()
    assert Path(paths["markdown"]).exists()
    saved = json.loads(Path(paths["json"]).read_text(encoding="utf-8"))
    assert saved["status"] == report["status"]
