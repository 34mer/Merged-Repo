from __future__ import annotations

from pathlib import Path

import numpy as np

from wormsim.abstraction import (
    benchmark_abstraction,
    migrate_abstracted,
    run_abstracted,
    train_pca_ridge,
    verify_abstracted_migration,
)
from wormsim.dataset import collect_dataset, load_dataset


def test_collect_dataset_shapes(tmp_path: Path) -> None:
    dataset_dir = tmp_path / "dataset"
    metadata = collect_dataset(dataset_dir, tasks="food,harm", episodes=2, steps=12, seed=5)
    arrays = load_dataset(dataset_dir)

    assert metadata["total_steps"] == 24
    assert arrays["X_neural"].shape == (24, 302)
    assert arrays["S_sensory"].shape == (24, 7)
    assert arrays["A_motor"].shape == (24, 4)
    assert arrays["B_body"].shape == (24, 5)
    assert arrays["V_viability"].shape == (24,)


def test_pca_ridge_abstraction_migrates_and_benchmarks(tmp_path: Path) -> None:
    dataset_dir = tmp_path / "dataset"
    model_dir = tmp_path / "pca16"
    live_dir = tmp_path / "live"
    migrated_dir = tmp_path / "migrated"
    report_dir = tmp_path / "report"

    collect_dataset(dataset_dir, tasks="food,harm,perturb,wall,mixed", episodes=5, steps=20, seed=11)
    model_metadata = train_pca_ridge(dataset_dir, model_dir, latent_dim=16)
    live_report = run_abstracted(model_dir, live_dir, task_name="mixed", steps=30, seed=11)
    checkpoint = live_dir / "checkpoint_t30.npz"
    manifest = migrate_abstracted(checkpoint, migrated_dir)
    verification = verify_abstracted_migration(
        model_dir,
        checkpoint,
        migrated_dir / "checkpoint_t30.npz",
        steps=25,
    )
    benchmark = benchmark_abstraction(model_dir, report_dir, task_name="mixed", steps=30, seed=11)

    assert model_metadata["latent_dim"] == 16
    assert model_metadata["compression_ratio"] == 302 / 16
    assert live_report["status"] == "ABSTRACTED RUN COMPLETE"
    assert manifest["hash_matched"]
    assert verification.status == "ABSTRACTED MIGRATION VERIFIED"
    assert verification.latent_trajectory_divergence == 0.0
    assert 0.0 <= benchmark["behavior_fidelity"] <= 1.0
    assert benchmark["compression_ratio"] == 302 / 16
