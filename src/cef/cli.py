from __future__ import annotations

from pathlib import Path

import typer

from .capture import make_fixture_capture
from .compiler import compile_capture_to_packets
from .report import write_summary
from .runtime import constrain_synthetic_runtime
from .verify import verify_forcing

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
    typer.echo("Real organism constraints: loaded")
    typer.echo(f"Individual id: {packets['individual_packet']['individual_id']}")
    typer.echo(f"Capture hash: {packets['individual_packet']['capture_hash']}")
    typer.echo(f"Construction packet hash: {packets['construction_packet']['construction_packet_hash']}")
    typer.echo(f"Verifier oracle hash: {packets['verifier_oracle']['oracle_hash']}")
    typer.echo("Construction/verifier independence: PASS")
    typer.echo("Synthetic worm runtime constrained: PASS")
    typer.echo("Held-out perturbation verification: PASS")
    typer.echo("Controls failed as expected: true")
    typer.echo(f"Report: {report_path}")


if __name__ == "__main__":
    app()
