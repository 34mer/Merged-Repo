from __future__ import annotations

import csv
import json

import pytest
from pathlib import Path
from typer.testing import CliRunner

from cef.adapters import import_real_dataset_csv, import_real_dataset_json
from cef.ablation import run_capture_split_ablation
from cef.capture import make_fixture_capture
from cef.cli import app
from cef.compiler import compile_capture_to_packets
from cef.dryad import import_dryad_copper_h5
from cef.runtime import constrain_synthetic_runtime, run_blind_heldout_projection
from cef.verify import evaluate_oracle, verify_blind_forcing
from cef.v0_3 import enrich_capture_with_v0_3_dynamics, run_v0_3_robustness, V0_3_DYNAMIC_FEATURES


def _real_rows() -> list[dict[str, float | str]]:
    return [
        {"episode_id": "real_train_0", "split": "construction", "stimulus_mean": 0.20, "perturbation_magnitude": 0.20, "neural_mean": 0.24, "posture_mean": 0.33, "motor_mean": 0.41, "perturbation_response": 0.50, "body_loop_coupling": 0.37},
        {"episode_id": "real_train_1", "split": "construction", "stimulus_mean": 0.70, "perturbation_magnitude": 0.30, "neural_mean": 0.59, "posture_mean": 0.49, "motor_mean": 0.57, "perturbation_response": 0.73, "body_loop_coupling": 0.53},
        {"episode_id": "real_train_2", "split": "construction", "stimulus_mean": 0.45, "perturbation_magnitude": 0.70, "neural_mean": 0.52, "posture_mean": 0.46, "motor_mean": 0.53, "perturbation_response": 0.86, "body_loop_coupling": 0.50},
        {"episode_id": "real_holdout_0", "split": "heldout", "stimulus_mean": 0.35, "perturbation_magnitude": 0.55, "neural_mean": 0.43, "posture_mean": 0.41, "motor_mean": 0.49, "perturbation_response": 0.72, "body_loop_coupling": 0.45},
        {"episode_id": "real_holdout_1", "split": "heldout", "stimulus_mean": 0.60, "perturbation_magnitude": 0.65, "neural_mean": 0.55, "posture_mean": 0.50, "motor_mean": 0.59, "perturbation_response": 0.90, "body_loop_coupling": 0.54},
    ]


def test_cef_v0_1_blind_fixture_projection(tmp_path: Path) -> None:
    source = tmp_path / "fixture_capture.json"
    artifacts = tmp_path / "artifacts"
    report_path = tmp_path / "cef_v0_1_report.json"
    make_fixture_capture(source)
    packets = compile_capture_to_packets(source, artifacts)
    runtime = constrain_synthetic_runtime(artifacts / "construction_packet.json", artifacts / "runtime")
    projection = run_blind_heldout_projection(runtime, packets["heldout_driver"])
    report = verify_blind_forcing(
        artifacts / "construction_packet.json",
        artifacts / "verifier_oracle.json",
        artifacts / "heldout_driver.json",
        artifacts / "runtime" / "synthetic_runtime.json",
        report_path,
        protocol="CEF-v0.1",
    )

    assert projection["oracle_used_for_generation"] is False
    assert report["status"] == "PASS"
    assert report["capture_origin"] == "fixture"
    assert report["real_organism_constraints_loaded"] is False
    assert report["runtime_used_oracle_for_generation"] is False
    assert report["verifier_blind_projection"] is True
    assert report["controls_failed_as_expected"] is True


def test_cef_v0_2_real_dataset_json_adapter_and_blind_proof(tmp_path: Path) -> None:
    raw = tmp_path / "real_shape.json"
    capture = tmp_path / "real_capture.json"
    artifacts = tmp_path / "artifacts"
    report_path = tmp_path / "cef_v0_2_report.json"
    raw.write_text(json.dumps({"individual_id": "real_shape_worm", "dataset_source": "unit_test_json_dataset", "episodes": _real_rows()}), encoding="utf-8")

    imported = import_real_dataset_json(raw, capture)
    compile_capture_to_packets(capture, artifacts)
    constrain_synthetic_runtime(artifacts / "construction_packet.json", artifacts / "runtime")
    report = verify_blind_forcing(
        artifacts / "construction_packet.json",
        artifacts / "verifier_oracle.json",
        artifacts / "heldout_driver.json",
        artifacts / "runtime" / "synthetic_runtime.json",
        report_path,
        protocol="CEF-v0.2",
    )

    assert imported["capture_origin"] == "real_dataset"
    assert imported["real_organism_constraints_loaded"] is True
    assert report["status"] == "PASS"
    assert report["protocol"] == "CEF-v0.2"
    assert report["capture_origin"] == "real_dataset"
    assert report["real_organism_constraints_loaded"] is True
    assert report["runtime_used_oracle_for_generation"] is False


def test_cef_v0_2_real_dataset_csv_adapter(tmp_path: Path) -> None:
    raw = tmp_path / "real_shape.csv"
    capture = tmp_path / "real_capture_csv.json"
    fieldnames = list(_real_rows()[0].keys())
    with raw.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(_real_rows())

    imported = import_real_dataset_csv(raw, capture, individual_id="real_csv_worm", dataset_source="unit_test_csv_dataset")
    assert imported["capture_origin"] == "real_dataset"
    assert imported["dataset_source"] == "unit_test_csv_dataset"
    assert imported["real_organism_constraints_loaded"] is True
    assert len(imported["episodes"]) == 5


def test_cef_v0_1_v0_2_cli_paths(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    runner = CliRunner()
    fixture = runner.invoke(app, ["make-fixture", "--out", "external/fixture_capture.json"])
    assert fixture.exit_code == 0, fixture.output
    blind = runner.invoke(app, ["prove-forcing-blind", "--source", "external/fixture_capture.json", "--out", "reports/cef_v0_1"])
    assert blind.exit_code == 0, blind.output
    assert "Protocol: CEF-v0.1" in blind.output
    assert "Real organism constraints loaded: false" in blind.output
    assert "Runtime used oracle for generation: false" in blind.output

    raw = Path("external/real_shape.json")
    raw.write_text(json.dumps({"individual_id": "real_shape_worm", "dataset_source": "unit_test_json_dataset", "episodes": _real_rows()}), encoding="utf-8")
    imported = runner.invoke(app, ["import-real-json", "--source", str(raw), "--out", "external/real_capture.json"])
    assert imported.exit_code == 0, imported.output
    assert "Capture origin: real_dataset" in imported.output
    real = runner.invoke(app, ["prove-forcing-blind", "--source", "external/real_capture.json", "--out", "reports/cef_v0_2"])
    assert real.exit_code == 0, real.output
    assert "Protocol: CEF-v0.2" in real.output
    assert "Real organism constraints loaded: true" in real.output


def test_cef_v0_2_dryad_copper_h5_adapter_and_cli(tmp_path: Path, monkeypatch) -> None:
    h5py = pytest.importorskip("h5py")
    np = pytest.importorskip("numpy")
    raw = tmp_path / "dryad_copper_fixture.h5"
    capture = tmp_path / "dryad_capture.json"
    with h5py.File(raw, "w") as h5:
        gcamp = h5.create_group("gcamp")
        stimulus_by_window = np.array([0.0, 1.0, 0.4, 0.6, 0.2, 0.8])
        perturbation_by_window = np.array([0.2, 1.0, 0.8, 0.9, 0.5, 1.0])
        stimulus = np.repeat(stimulus_by_window, 20)
        perturbation = np.repeat(perturbation_by_window, 20)
        traces = np.vstack([stimulus, stimulus, stimulus]).T
        gcamp.create_dataset("traces", data=traces)
        behavior = h5.create_group("behavior")
        behavior.create_dataset("velocity", data=np.zeros(120))
        behavior.create_dataset("reversal_events", data=perturbation)
        behavior.create_dataset("distance_from_copper_center", data=1.0 - stimulus)
        behavior.create_dataset("head_angle", data=stimulus)
        behavior.create_dataset("angular_velocity", data=np.zeros(120))
        timing = h5.create_group("timing")
        timing.create_dataset("timestamps", data=np.arange(120))

    imported = import_dryad_copper_h5(raw, capture, individual_id="dryad_unit_worm", windows=6)
    assert imported["capture_origin"] == "real_dataset"
    assert imported["real_organism_constraints_loaded"] is True
    assert imported["dataset_source"].startswith("Dryad DOI 10.5061/dryad.w9ghx3g4v")
    assert len(imported["episodes"]) == 6
    assert [row["split"] for row in imported["episodes"]].count("construction") == 3
    assert [row["split"] for row in imported["episodes"]].count("heldout") == 3
    assert imported["anatomy_connectome_metadata"]["adapter"] == "cef_dryad_copper_h5"

    artifacts = tmp_path / "dryad_artifacts"
    report_path = tmp_path / "dryad_cef_v0_2_report.json"
    compile_capture_to_packets(capture, artifacts)
    constrain_synthetic_runtime(artifacts / "construction_packet.json", artifacts / "runtime")
    report = verify_blind_forcing(
        artifacts / "construction_packet.json",
        artifacts / "verifier_oracle.json",
        artifacts / "heldout_driver.json",
        artifacts / "runtime" / "synthetic_runtime.json",
        report_path,
        protocol="CEF-v0.2",
    )
    assert report["status"] == "PASS"
    assert report["capture_origin"] == "real_dataset"
    assert report["real_organism_constraints_loaded"] is True
    assert report["runtime_used_oracle_for_generation"] is False

    monkeypatch.chdir(tmp_path)
    runner = CliRunner()
    result = runner.invoke(
        app,
        [
            "import-dryad-copper-h5",
            "--source",
            str(raw),
            "--out",
            "external/dryad_capture.json",
            "--individual-id",
            "dryad_cli_worm",
            "--windows",
            "6",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "CEF-v0.2 DRYAD COPPER H5 IMPORTED" in result.output
    assert "Real organism constraints loaded: true" in result.output
    assert Path("external/dryad_capture.json").exists()


def test_cef_v0_2_split_ablation_matrix(tmp_path: Path) -> None:
    raw = tmp_path / "real_shape.json"
    capture = tmp_path / "real_capture.json"
    out = tmp_path / "ablation"
    raw.write_text(
        json.dumps({"individual_id": "real_shape_worm", "dataset_source": "unit_test_json_dataset", "episodes": _real_rows()}),
        encoding="utf-8",
    )
    import_real_dataset_json(raw, capture)

    matrix = run_capture_split_ablation(capture, out, include_leave_one_out=True)

    assert matrix["schema"] == "cef-v0.2-real-data-split-ablation-matrix"
    assert matrix["real_data_ingestion"] == "PASS"
    assert matrix["projection_fit_mode"] == "construction_packet_training_examples_named_driver_ridge_least_squares"
    assert len(matrix["cases"]) == 8
    assert all(case["oracle_leakage"] is False for case in matrix["cases"])
    assert all(case["controls_failed_as_expected"] is True for case in matrix["cases"])
    assert (out / "split_ablation_matrix.json").exists()

    runner = CliRunner()
    result = runner.invoke(
        app,
        [
            "run-split-ablation",
            "--source",
            str(capture),
            "--out",
            str(tmp_path / "cli_ablation"),
            "--include-leave-one-out",
        ],
    )
    assert result.exit_code == 0, result.output
    assert "CEF-v0.2 SPLIT ABLATION MATRIX COMPLETE" in result.output


def test_cef_v0_3_dynamic_observables_and_robustness(tmp_path: Path) -> None:
    raw = tmp_path / "real_shape.json"
    capture = tmp_path / "real_capture.json"
    enriched = tmp_path / "real_capture_v0_3.json"
    artifacts = tmp_path / "artifacts_v0_3"
    robustness = tmp_path / "robustness_v0_3"
    raw.write_text(
        json.dumps({"individual_id": "real_shape_worm", "dataset_source": "unit_test_json_dataset", "episodes": _real_rows()}),
        encoding="utf-8",
    )
    import_real_dataset_json(raw, capture)
    v03 = enrich_capture_with_v0_3_dynamics(capture, enriched)
    packets = compile_capture_to_packets(enriched, artifacts)

    state_vars = packets["individual_packet"]["state_variables"]
    assert "neural_slope" in state_vars
    assert "delta_stimulus" in state_vars
    assert packets["individual_packet"]["dynamic_state_variables"]
    assert len(v03["anatomy_connectome_metadata"]["cef_v0_3_dynamic_features"]) == len(V0_3_DYNAMIC_FEATURES)

    runtime = constrain_synthetic_runtime(artifacts / "construction_packet.json", artifacts / "runtime")
    assert runtime["projection_model_source"] == "construction_packet_training_examples_named_driver_ridge_least_squares"
    assert "driver_names" in runtime["projection_model"]
    assert "delta_stimulus" in runtime["projection_model"]["driver_names"]

    report = run_v0_3_robustness(enriched, robustness)
    assert report["schema"] == "cef-v0.3-window-dynamics-robustness-report"
    assert report["protocol"] == "CEF-v0.3"
    assert report["real_data_ingestion"] == "PASS"
    assert report["oracle_leakage"] is False
    assert report["controls_failed_as_expected"] is True
    assert report["status"] in {"PASS", "PARTIAL"}
    assert "ranked_invariant_gap_report" in report

    runner = CliRunner()
    result = runner.invoke(app, ["run-v0-3-robustness", "--source", str(enriched), "--out", str(tmp_path / "cli_v0_3")])
    assert result.exit_code == 0, result.output
    assert "CEF-v0.3 WINDOW ROBUSTNESS COMPLETE" in result.output
