from __future__ import annotations

from pathlib import Path

import typer

from .capture import make_fixture_capture
from .adapters import import_real_dataset_csv, import_real_dataset_json
from .ablation import run_capture_split_ablation
from .dryad import import_dryad_copper_h5
from .compiler import compile_capture_to_packets
from .report import write_summary
from .runtime import constrain_synthetic_runtime
from .verify import verify_forcing, verify_blind_forcing
from .v0_3 import (
    enrich_capture_with_v0_3_dynamics,
    import_dryad_copper_h5_v0_3,
    run_v0_3_robustness,
    import_and_run_dryad_v0_3,
)

app = typer.Typer(help="CEF-v0 C. elegans forcing-function protocol tools")


@app.command("make-fixture")
def make_fixture(out: Path = Path("external/celegans_capture_v0.json")) -> None:
    capture = make_fixture_capture(out)
    typer.echo("CEF-v0 INDIVIDUAL WORM FIXTURE WRITTEN")
    typer.echo(f"Individual id: {capture['individual_id']}")
    typer.echo(f"Capture hash: {capture['capture_hash']}")
    typer.echo(f"Episodes: {len(capture['episodes'])}")


@app.command("compile-capture")
def compile_capture(
    source: Path = typer.Option(..., help="CEF-v0 individual worm capture JSON."),
    out: Path = typer.Option(Path("artifacts/cef_v0"), help="CEF-v0 packet output directory."),
) -> None:
    packets = compile_capture_to_packets(source, out)
    typer.echo("CEF-v0 CAPTURE COMPILED")
    typer.echo(f"Individual id: {packets['individual_packet']['individual_id']}")
    typer.echo(f"Individual packet hash: {packets['individual_packet']['packet_hash']}")
    typer.echo(f"Construction packet hash: {packets['construction_packet']['construction_packet_hash']}")
    typer.echo(f"Verifier oracle hash: {packets['verifier_oracle']['oracle_hash']}")


@app.command("constrain-runtime")
def constrain_runtime(
    construction_packet: Path = Path("artifacts/cef_v0/construction_packet.json"),
    out: Path = Path("artifacts/cef_v0/synthetic_worm_runtime"),
) -> None:
    runtime = constrain_synthetic_runtime(construction_packet, out)
    typer.echo("CEF-v0 SYNTHETIC WORM RUNTIME CONSTRAINED")
    typer.echo(f"Individual id: {runtime['individual_id']}")
    typer.echo(f"Construction packet hash: {runtime['construction_packet_hash']}")
    typer.echo(f"Runtime hash: {runtime['runtime_hash']}")


@app.command("verify-forcing")
def verify_forcing_cmd(
    construction_packet: Path = Path("artifacts/cef_v0/construction_packet.json"),
    verifier_oracle: Path = Path("artifacts/cef_v0/verifier_oracle.json"),
    runtime: Path = Path("artifacts/cef_v0/synthetic_worm_runtime/synthetic_runtime.json"),
    out: Path = Path("reports/cef_v0_protocol_readiness.json"),
) -> None:
    report = verify_forcing(construction_packet, verifier_oracle, runtime, out)
    write_summary(report, Path(out).with_name("cef_v0_summary.md"))
    if report["status"] == "PASS":
        typer.echo("C. ELEGANS FORCING FUNCTION PROTOCOL COMPLETE")
    typer.echo(f"Status: {report['status']}")
    typer.echo(f"Real organism constraints: {'loaded' if report['real_organism_constraints_loaded'] else 'missing'}")
    typer.echo(f"Construction/verifier independence: {report['construction_verifier_independence']['status']}")
    typer.echo(f"Synthetic worm runtime constrained: {'PASS' if report['synthetic_worm_runtime_constrained'] else 'FAIL'}")
    typer.echo(f"Held-out perturbation verification: {report['heldout_perturbation_verification']['status']}")
    typer.echo(f"Controls failed as expected: {str(report['controls_failed_as_expected']).lower()}")
    raise typer.Exit(0 if report["status"] == "PASS" else 1)


@app.command("prove-forcing")
def prove_forcing(
    source: Path = typer.Option(..., help="CEF-v0 individual worm capture JSON."),
    out: Path = typer.Option(Path("reports/cef_v0"), help="CEF-v0 report/output directory."),
) -> None:
    artifacts = Path("artifacts/cef_v0")
    packets = compile_capture_to_packets(source, artifacts)
    runtime = constrain_synthetic_runtime(artifacts / "construction_packet.json", artifacts / "synthetic_worm_runtime")
    out.mkdir(parents=True, exist_ok=True)
    report_path = out / "cef_v0_protocol_readiness.json"
    report = verify_forcing(
        artifacts / "construction_packet.json",
        artifacts / "verifier_oracle.json",
        artifacts / "synthetic_worm_runtime" / "synthetic_runtime.json",
        report_path,
    )
    write_summary(report, out / "cef_v0_summary.md")
    if report["status"] != "PASS":
        typer.echo("CEF-v0 forcing protocol failed. Final completion line withheld.")
        raise typer.Exit(code=1)

    typer.echo("C. ELEGANS FORCING FUNCTION PROTOCOL COMPLETE")
    typer.echo("Status: PASS")
    typer.echo(f"Capture origin: {packets['individual_packet'].get('capture_origin', 'unknown')}")
    typer.echo(f"Real organism constraints loaded: {str(packets['individual_packet'].get('real_organism_constraints_loaded', False)).lower()}")
    typer.echo(f"Individual id: {packets['individual_packet']['individual_id']}")
    typer.echo(f"Capture hash: {packets['individual_packet']['capture_hash']}")
    typer.echo(f"Construction packet hash: {packets['construction_packet']['construction_packet_hash']}")
    typer.echo(f"Verifier oracle hash: {packets['verifier_oracle']['oracle_hash']}")
    typer.echo("Construction/verifier independence: PASS")
    typer.echo("Synthetic worm runtime constrained: PASS")
    typer.echo("Held-out perturbation verification: PASS")
    typer.echo("Controls failed as expected: true")
    typer.echo(f"Report: {report_path}")


@app.command("import-real-json")
def import_real_json(
    source: Path = typer.Option(..., help="Real C. elegans dataset JSON with rows/episodes."),
    out: Path = typer.Option(Path("external/celegans_real_capture_v0_2.json"), help="CEF capture output JSON."),
    individual_id: str | None = typer.Option(None, help="Individual worm id override."),
    dataset_source: str | None = typer.Option(None, help="Dataset/source label override."),
) -> None:
    capture = import_real_dataset_json(source, out, individual_id=individual_id, dataset_source=dataset_source)
    typer.echo("CEF-v0.2 REAL DATASET JSON IMPORTED")
    typer.echo(f"Individual id: {capture['individual_id']}")
    typer.echo(f"Capture origin: {capture['capture_origin']}")
    typer.echo(f"Real organism constraints loaded: {str(capture['real_organism_constraints_loaded']).lower()}")
    typer.echo(f"Capture hash: {capture['capture_hash']}")


@app.command("import-real-csv")
def import_real_csv(
    source: Path = typer.Option(..., help="Row-per-episode real C. elegans CSV."),
    out: Path = typer.Option(Path("external/celegans_real_capture_v0_2.json"), help="CEF capture output JSON."),
    individual_id: str = typer.Option("real_celegans_individual", help="Individual worm id."),
    dataset_source: str = typer.Option("external_celegans_dataset_csv", help="Dataset/source label."),
) -> None:
    capture = import_real_dataset_csv(source, out, individual_id=individual_id, dataset_source=dataset_source)
    typer.echo("CEF-v0.2 REAL DATASET CSV IMPORTED")
    typer.echo(f"Individual id: {capture['individual_id']}")
    typer.echo(f"Capture origin: {capture['capture_origin']}")
    typer.echo(f"Real organism constraints loaded: {str(capture['real_organism_constraints_loaded']).lower()}")
    typer.echo(f"Capture hash: {capture['capture_hash']}")


@app.command("import-dryad-copper-h5")
def import_dryad_copper_h5_cmd(
    source: Path = typer.Option(..., help="Dryad copper-boundary per-worm H5 file."),
    out: Path = typer.Option(Path("external/celegans_dryad_copper_capture_v0_2.json"), help="CEF capture output JSON."),
    individual_id: str | None = typer.Option(None, help="Individual worm id override."),
    windows: int = typer.Option(6, help="Number of temporal windows to convert into construction/heldout episodes."),
) -> None:
    capture = import_dryad_copper_h5(source, out, individual_id=individual_id, windows=windows)
    typer.echo("CEF-v0.2 DRYAD COPPER H5 IMPORTED")
    typer.echo(f"Individual id: {capture['individual_id']}")
    typer.echo(f"Capture origin: {capture['capture_origin']}")
    typer.echo(f"Dataset source: {capture['dataset_source']}")
    typer.echo(f"Real organism constraints loaded: {str(capture['real_organism_constraints_loaded']).lower()}")
    typer.echo(f"Episodes: {len(capture['episodes'])}")
    typer.echo(f"Capture hash: {capture['capture_hash']}")


@app.command("prove-forcing-blind")
def prove_forcing_blind(
    source: Path = typer.Option(..., help="CEF individual worm capture JSON."),
    out: Path = typer.Option(Path("reports/cef_v0_1"), help="CEF-v0.1/v0.2 report directory."),
) -> None:
    # Compile once to determine capture origin, then use a versioned artifact root.
    probe_packets = compile_capture_to_packets(source, Path("artifacts/cef_probe"))
    protocol = "CEF-v0.2" if probe_packets['individual_packet'].get('real_organism_constraints_loaded') else "CEF-v0.1"
    artifacts = Path("artifacts/cef_v0_2") if protocol == "CEF-v0.2" else Path("artifacts/cef_v0_1")
    packets = compile_capture_to_packets(source, artifacts)
    constrain_synthetic_runtime(artifacts / "construction_packet.json", artifacts / "synthetic_worm_runtime")
    out.mkdir(parents=True, exist_ok=True)
    report_name = "cef_v0_2_protocol_readiness.json" if protocol == "CEF-v0.2" else "cef_v0_1_protocol_readiness.json"
    report_path = out / report_name
    report = verify_blind_forcing(
        artifacts / "construction_packet.json",
        artifacts / "verifier_oracle.json",
        artifacts / "heldout_driver.json",
        artifacts / "synthetic_worm_runtime" / "synthetic_runtime.json",
        report_path,
        protocol=protocol,
    )
    write_summary(report, out / "cef_v0_1_summary.md")
    if report["status"] != "PASS":
        typer.echo("CEF blind forcing protocol failed. Final completion line withheld.")
        raise typer.Exit(code=1)

    typer.echo("C. ELEGANS BLIND FORCING PROTOCOL COMPLETE")
    typer.echo("Status: PASS")
    typer.echo(f"Protocol: {protocol}")
    typer.echo(f"Capture origin: {report['capture_origin']}")
    typer.echo(f"Real organism constraints loaded: {str(report['real_organism_constraints_loaded']).lower()}")
    typer.echo("Construction/verifier independence: PASS")
    typer.echo("Verifier-blind runtime projection: PASS")
    typer.echo("Runtime used oracle for generation: false")
    typer.echo("Held-out perturbation verification: PASS")
    typer.echo("Controls failed as expected: true")
    typer.echo(f"Report: {report_path}")


@app.command("run-split-ablation")
def run_split_ablation_cmd(
    source: Path = typer.Option(..., help="CEF capture JSON to resplit and evaluate."),
    out: Path = typer.Option(Path("reports/cef_v0_2_split_ablation"), help="Split-ablation output directory."),
    include_leave_one_out: bool = typer.Option(True, help="Also run leave-one-window-out cases."),
) -> None:
    matrix = run_capture_split_ablation(source, out, include_leave_one_out=include_leave_one_out)
    typer.echo("CEF-v0.2 SPLIT ABLATION MATRIX COMPLETE")
    typer.echo(f"Source capture: {matrix['source_capture']}")
    typer.echo(f"Real data ingestion: {matrix['real_data_ingestion']}")
    typer.echo(f"Projection fit mode: {matrix['projection_fit_mode']}")
    for case in matrix["cases"]:
        suffix = "" if case.get("heldout_index") is None else f"[{case['heldout_index']}]"
        typer.echo(
            f"{case['split_mode']}{suffix}: {case['heldout_status']} "
            f"{case['passed_features']} failures={case['failure_features']} "
            f"oracle_leakage={str(case['oracle_leakage']).lower()}"
        )
    typer.echo(f"Matrix: {out / 'split_ablation_matrix.json'}")


@app.command("enrich-v0-3-dynamics")
def enrich_v0_3_dynamics_cmd(
    source: Path = typer.Option(..., help="Existing CEF capture JSON."),
    out: Path = typer.Option(Path("external/celegans_capture_v0_3.json"), help="CEF-v0.3 enriched capture output."),
) -> None:
    capture = enrich_capture_with_v0_3_dynamics(source, out)
    typer.echo("CEF-v0.3 DYNAMIC CAPTURE ENRICHED")
    typer.echo(f"Individual id: {capture['individual_id']}")
    typer.echo(f"Dynamic features: {len(capture['anatomy_connectome_metadata'].get('cef_v0_3_dynamic_features', []))}")
    typer.echo(f"Capture hash: {capture['capture_hash']}")


@app.command("import-dryad-copper-h5-v0-3")
def import_dryad_copper_h5_v0_3_cmd(
    source: Path = typer.Option(..., help="Dryad copper-boundary per-worm H5 file."),
    out: Path = typer.Option(Path("external/celegans_dryad_copper_capture_v0_3.json"), help="CEF-v0.3 capture output JSON."),
    individual_id: str | None = typer.Option(None, help="Individual worm id override."),
    windows: int = typer.Option(12, help="CEF-v0.3 window count: 12, 18, or 24."),
) -> None:
    capture = import_dryad_copper_h5_v0_3(source, out, individual_id=individual_id, windows=windows)
    typer.echo("CEF-v0.3 DRYAD COPPER H5 IMPORTED")
    typer.echo(f"Individual id: {capture['individual_id']}")
    typer.echo(f"Capture origin: {capture['capture_origin']}")
    typer.echo(f"Real organism constraints loaded: {str(capture['real_organism_constraints_loaded']).lower()}")
    typer.echo(f"Episodes: {len(capture['episodes'])}")
    typer.echo(f"Dynamic features: {len(capture['anatomy_connectome_metadata'].get('cef_v0_3_dynamic_features', []))}")
    typer.echo(f"Capture hash: {capture['capture_hash']}")


@app.command("run-v0-3-robustness")
def run_v0_3_robustness_cmd(
    source: Path = typer.Option(..., help="CEF-v0.3 capture JSON."),
    out: Path = typer.Option(Path("reports/cef_v0_3_robustness"), help="CEF-v0.3 robustness report directory."),
) -> None:
    report = run_v0_3_robustness(source, out)
    typer.echo("CEF-v0.3 WINDOW ROBUSTNESS COMPLETE")
    typer.echo(f"Status: {report['status']}")
    typer.echo(f"Real data ingestion: {report['real_data_ingestion']}")
    typer.echo(f"Windows: {report['windows']}")
    typer.echo(f"Leave-one-window-out: {report['leave_one_window_out_status']}")
    typer.echo(f"Passed cases: {report['passed_cases']}")
    typer.echo(f"Failed cases: {report['failed_cases']}")
    typer.echo(f"Oracle leakage: {str(report['oracle_leakage']).lower()}")
    typer.echo(f"Controls failed as expected: {str(report['controls_failed_as_expected']).lower()}")
    if report.get('ranked_invariant_gap_report'):
        top = report['ranked_invariant_gap_report'][0]
        typer.echo(f"Top invariant gap: window={top['heldout_index']} feature={top['feature']} gap={top['gap']}")
    typer.echo(f"Report: {out / 'cef_v0_3_robustness_report.json'}")


@app.command("import-and-run-dryad-v0-3")
def import_and_run_dryad_v0_3_cmd(
    source: Path = typer.Option(..., help="Dryad copper-boundary per-worm H5 file."),
    out: Path = typer.Option(Path("reports/cef_v0_3_real_dryad"), help="CEF-v0.3 output/report root."),
    individual_id: str | None = typer.Option(None, help="Individual worm id override."),
    windows: int = typer.Option(12, help="CEF-v0.3 window count: 12, 18, or 24."),
) -> None:
    report = import_and_run_dryad_v0_3(source, out, windows=windows, individual_id=individual_id)
    typer.echo("CEF-v0.3 DRYAD IMPORT AND ROBUSTNESS COMPLETE")
    typer.echo(f"Status: {report['status']}")
    typer.echo(f"Real data ingestion: {report['real_data_ingestion']}")
    typer.echo(f"Windows: {report['windows']}")
    typer.echo(f"Leave-one-window-out: {report['leave_one_window_out_status']}")
    typer.echo(f"Passed cases: {report['passed_cases']}")
    typer.echo(f"Failed cases: {report['failed_cases']}")
    typer.echo(f"Oracle leakage: {str(report['oracle_leakage']).lower()}")
    typer.echo(f"Controls failed as expected: {str(report['controls_failed_as_expected']).lower()}")


if __name__ == "__main__":
    app()
