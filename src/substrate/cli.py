from __future__ import annotations

from pathlib import Path

import typer

from .core import read_json, write_json
from .hydrogen.verify import verify_hydrogen
from .ion_water.verify import verify_ion_water
from .membrane.verify import verify_membrane
from .migrate import migrate_checkpoint, save_checkpoint, verify_migration
from .molecule.verify import verify_h2
from .channel.verify import verify_channel
from .neuron.primitive import extract_synthetic_neuron_primitive
from .neuron.verify import verify_neuron
from .reports import write_ladder_report
from .external.adhesion import (
    fit_primitive_to_ephys,
    generate_hh_neuroml_fixture,
    run_hh_neuroml_adhesion,
    verify_external_ephys,
)

app = typer.Typer(help="Boundary-to-biology bootstrapping and external adhesion tools.")


@app.command("build-ladder")
def build_ladder(out: Path = Path("reports/substrate_ladder")) -> None:
    report = write_ladder_report(out)
    typer.echo(report["status"])
    typer.echo(f"Final primitive hash: {report['final_primitive_hash']}")


@app.command("verify-rung")
def verify_rung(layer: str, out: Path = Path("reports/substrate_ladder/rung_report.json")) -> None:
    builders = {
        "hydrogen": verify_hydrogen,
        "molecule": verify_h2,
        "ion_water": verify_ion_water,
        "membrane": verify_membrane,
        "sodium_channel": lambda: verify_channel("sodium"),
        "potassium_channel": lambda: verify_channel("potassium"),
        "neuron": verify_neuron,
        "synthetic_neuron": extract_synthetic_neuron_primitive,
    }
    if layer not in builders:
        raise typer.BadParameter(f"Unknown layer {layer!r}; choose {sorted(builders)}")
    primitive = builders[layer]().to_dict()
    write_json(out, primitive)
    typer.echo(primitive["verification"]["status"])
    typer.echo(f"Primitive hash: {primitive['hash']}")


@app.command("checkpoint-primitive")
def checkpoint_primitive(source: Path, out: Path = Path("artifacts/primitive_checkpoint.json")) -> None:
    payload = read_json(source)
    checkpoint = save_checkpoint(payload, out)
    typer.echo("PRIMITIVE CHECKPOINT WRITTEN")
    typer.echo(f"Payload hash: {checkpoint['payload_hash']}")


@app.command("migrate-primitive")
def migrate_primitive(checkpoint: Path, out: Path = Path("runs/primitive_migrated")) -> None:
    manifest = migrate_checkpoint(checkpoint, out)
    typer.echo("PRIMITIVE MIGRATION VERIFIED" if manifest["checkpoint_hash_matched"] else "PRIMITIVE MIGRATION FAILED")
    typer.echo(f"Target: {manifest['target']}")


@app.command("verify-migration")
def verify_migration_command(a: Path, b: Path) -> None:
    report = verify_migration(a, b)
    typer.echo(report["status"])
    typer.echo(f"State divergence: {report['state_divergence']}")


@app.command("generate-hh-neuroml-fixture")
def generate_hh_neuroml_fixture_command(out: Path = Path("external/hh_neuroml_fixture.json")) -> None:
    dataset = generate_hh_neuroml_fixture(out)
    typer.echo("HH/NEUROML-STYLE FIXTURE WRITTEN")
    typer.echo(f"Source hash: {dataset['source_hash']}")
    typer.echo(f"Protocols: {len(dataset['protocols'])}")


@app.command("fit-primitive-to-ephys")
def fit_primitive_to_ephys_command(
    source: Path = typer.Option(..., help="External ephys JSON source."),
    out: Path = typer.Option(Path("primitives/external_ephys"), help="Primitive output directory."),
) -> None:
    primitive = fit_primitive_to_ephys(source, out)
    typer.echo("EXTERNAL EPHYS PRIMITIVE FIT COMPLETE")
    typer.echo(f"Primitive hash: {primitive['hash']}")
    typer.echo(f"Source hash: {primitive['observables']['source_hash']}")


@app.command("verify-external-ephys")
def verify_external_ephys_command(
    primitive: Path = typer.Option(..., help="Primitive directory or primitive.json."),
    source: Path = typer.Option(..., help="External ephys JSON source."),
    out: Path = typer.Option(Path("reports/external_ephys_adhesion"), help="Report output directory."),
    voltage_threshold: float = typer.Option(0.70, help="Minimum held-out voltage fidelity."),
    spike_threshold: float = typer.Option(0.50, help="Minimum spike and F-I threshold."),
    heldout_threshold: float = typer.Option(0.80, help="Minimum combined held-out score."),
    include_controls: bool = typer.Option(True, help="Run random/over-stable/leakage controls."),
) -> None:
    report = verify_external_ephys(
        primitive=primitive,
        source=source,
        out=out,
        voltage_threshold=voltage_threshold,
        spike_threshold=spike_threshold,
        heldout_threshold=heldout_threshold,
        include_controls=include_controls,
    )
    typer.echo(report["status"])
    typer.echo(f"Held-out score: {report['heldout_summary']['heldout_score']:.4f}")
    typer.echo(f"Voltage fidelity: {report['heldout_summary']['voltage_fidelity']:.4f}")
    typer.echo(f"Spike timing score: {report['heldout_summary']['spike_timing_score']:.4f}")
    typer.echo(f"F-I similarity: {report['fi_curve_similarity']:.4f}")
    typer.echo(f"Migration: {report['migration']['status']}")
    typer.echo(f"Honest controls failed: {report['honest_controls_failed']}")


@app.command("run-hh-neuroml-adhesion")
def run_hh_neuroml_adhesion_command(out: Path = Path("reports/hh_neuroml_adhesion")) -> None:
    report = run_hh_neuroml_adhesion(out)
    adhesion = report["adhesion_report"]
    typer.echo(report["status"])
    typer.echo(f"Source hash: {report['source_hash']}")
    typer.echo(f"Primitive hash: {report['primitive_hash']}")
    typer.echo(f"Held-out score: {adhesion['heldout_summary']['heldout_score']:.4f}")
    typer.echo(f"Migration: {adhesion['migration']['status']}")
    typer.echo(f"Honest controls failed: {adhesion['honest_controls_failed']}")


if __name__ == "__main__":
    app()
