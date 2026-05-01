from __future__ import annotations

from pathlib import Path
from typer.testing import CliRunner

from cef.capture import load_capture, make_fixture_capture
from cef.cli import app
from cef.compiler import compile_capture_to_packets, verify_packet_independence
from cef.runtime import constrain_synthetic_runtime, run_heldout_projection
from cef.verify import evaluate_oracle, verify_forcing


def test_cef_fixture_capture_schema(tmp_path: Path) -> None:
    source = tmp_path / "celegans_capture_v0.json"
    capture = make_fixture_capture(source)
    loaded = load_capture(source)

    assert loaded["schema"] == "cef-v0-individual-worm-capture"
    assert loaded["individual_id"] == "fixture_worm_A"
    assert loaded["capture_hash"] == capture["capture_hash"]
    assert len(loaded["episodes"]) == 5
    assert {episode["split"] for episode in loaded["episodes"]} == {"construction", "heldout"}


def test_cef_compile_runtime_verify_and_controls(tmp_path: Path) -> None:
    source = tmp_path / "capture.json"
    artifacts = tmp_path / "artifacts"
    report = tmp_path / "cef_v0_protocol_readiness.json"

    make_fixture_capture(source)
    packets = compile_capture_to_packets(source, artifacts)
    independence = verify_packet_independence(packets["construction_packet"], packets["verifier_oracle"])
    runtime = constrain_synthetic_runtime(artifacts / "construction_packet.json", artifacts / "synthetic_worm_runtime")
    result = verify_forcing(
        artifacts / "construction_packet.json",
        artifacts / "verifier_oracle.json",
        artifacts / "synthetic_worm_runtime" / "synthetic_runtime.json",
        report,
    )

    assert packets["individual_packet"]["schema"] == "cef-v0-individual-worm-constraint-packet"
    assert independence["status"] == "PASS"
    assert runtime["runtime"] == "wormsim-compatible-destination"
    assert result["status"] == "PASS"
    assert result["synthetic_worm_runtime_constrained"] is True
    assert result["heldout_perturbation_verification"]["status"] == "PASS"
    assert result["controls_failed_as_expected"] is True
    assert report.exists()


def test_cef_oracle_fails_corrupted_projection(tmp_path: Path) -> None:
    source = tmp_path / "capture.json"
    artifacts = tmp_path / "artifacts"
    make_fixture_capture(source)
    packets = compile_capture_to_packets(source, artifacts)
    runtime = constrain_synthetic_runtime(artifacts / "construction_packet.json", artifacts / "synthetic_worm_runtime")
    projection = run_heldout_projection(runtime, packets["verifier_oracle"])

    corrupted = dict(projection["projected_observables"])
    corrupted["perturbation_response"] = 0.0
    assert evaluate_oracle(corrupted, packets["verifier_oracle"])["status"] == "FAIL"


def test_cef_cli_make_fixture_and_prove_forcing(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    runner = CliRunner()
    fixture_result = runner.invoke(app, ["make-fixture", "--out", "external/celegans_capture_v0.json"])
    assert fixture_result.exit_code == 0, fixture_result.output

    prove_result = runner.invoke(
        app,
        [
            "prove-forcing",
            "--source",
            "external/celegans_capture_v0.json",
            "--out",
            "reports/cef_v0",
        ],
    )
    assert prove_result.exit_code == 0, prove_result.output
    assert "C. ELEGANS FORCING FUNCTION PROTOCOL COMPLETE" in prove_result.output
    assert "Status: PASS" in prove_result.output
    assert Path("reports/cef_v0/cef_v0_protocol_readiness.json").exists()
