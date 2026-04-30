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

app = typer.Typer(help="Boundary-to-neuron substrate derivation ladder.")


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


if __name__ == "__main__":
    app()
