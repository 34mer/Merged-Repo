from __future__ import annotations

import json
import shutil
from pathlib import Path

import typer

from .abstraction import (
    benchmark_abstraction,
    migrate_abstracted as migrate_abstracted_checkpoint,
    run_abstracted as run_abstracted_model,
    train_pca_ridge,
    verify_abstracted_migration,
)
from .checkpoint import file_hash, load_checkpoint, save_checkpoint, verify_hash
from .config import WormConfig
from .curve import generate_abstraction_curve
from .dataset import collect_dataset
from .dynamics import run_steps
from .environment import initial_environment
from .organism import initial_state
from .verify import compare_from_checkpoints, write_report

app = typer.Typer(help="Deterministic worm-inspired substrate migration demo.")


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


@app.command()
def init(
    neurons: int = typer.Option(302, help="Number of neurons in the digital organism."),
    seed: int = typer.Option(42, help="Deterministic seed."),
    out: Path = typer.Option(Path("runs/run_001"), help="Run directory."),
) -> None:
    config = WormConfig(neurons=neurons, seed=seed)
    env = initial_environment(config)
    state = initial_state(config)
    out.mkdir(parents=True, exist_ok=True)
    _write_json(out / "config.json", config.to_dict())
    _write_json(out / "environment.json", env.to_dict())
    digest = save_checkpoint(out / "checkpoint_t0.npz", config, env, state)
    typer.echo(f"initialized {out}")
    typer.echo(f"checkpoint_t0 hash: {digest}")


@app.command()
def run(
    checkpoint: Path = typer.Option(Path("runs/run_001/checkpoint_t0.npz"), help="Checkpoint to start from."),
    steps: int = typer.Option(5000, help="Number of deterministic steps."),
    out: Path = typer.Option(Path("runs/run_001"), help="Run directory."),
) -> None:
    config, env, state = load_checkpoint(checkpoint)
    env2, state2, trajectory = run_steps(config, env, state, steps)
    final_path = out / f"checkpoint_t{state2.step}.npz"
    digest = save_checkpoint(final_path, config, env2, state2)
    _write_json(
        out / "run_log.json",
        {
            "start_checkpoint": str(checkpoint),
            "start_step": state.step,
            "end_step": state2.step,
            "trajectory_rows": int(trajectory.shape[0]),
            "final_checkpoint": str(final_path),
            "final_hash": digest,
        },
    )
    typer.echo(f"ran {steps} steps to step {state2.step}")
    typer.echo(f"final checkpoint: {final_path}")
    typer.echo(f"final hash: {digest}")


@app.command("hash")
def hash_file(file: Path) -> None:
    typer.echo(file_hash(file))


@app.command("verify-hash")
def verify_hash_command(file: Path, expected: str) -> None:
    matched = verify_hash(file, expected)
    typer.echo("HASH MATCHED" if matched else "HASH MISMATCH")
    raise typer.Exit(0 if matched else 1)


@app.command()
def migrate(
    checkpoint: Path = typer.Option(..., help="Source checkpoint."),
    out: Path = typer.Option(Path("runs/migrated_run"), help="Destination folder simulating another substrate."),
) -> None:
    out.mkdir(parents=True, exist_ok=True)
    target = out / checkpoint.name
    shutil.copy2(checkpoint, target)
    expected = file_hash(checkpoint)
    matched = verify_hash(target, expected)
    _write_json(out / "migration_manifest.json", {"source": str(checkpoint), "target": str(target), "hash": expected, "hash_matched": matched})
    typer.echo(f"copied checkpoint to {target}")
    typer.echo("hash verified" if matched else "hash mismatch")
    raise typer.Exit(0 if matched else 1)


@app.command()
def resume(
    checkpoint: Path = typer.Option(..., help="Checkpoint to resume."),
    steps: int = typer.Option(5000, help="Number of deterministic steps after resume."),
    out: Path = typer.Option(Path("runs/migrated_run"), help="Output folder."),
) -> None:
    config, env, state = load_checkpoint(checkpoint)
    env2, state2, trajectory = run_steps(config, env, state, steps)
    final_path = out / f"checkpoint_t{state2.step}.npz"
    digest = save_checkpoint(final_path, config, env2, state2)
    _write_json(out / "resume_log.json", {"start_step": state.step, "end_step": state2.step, "trajectory_rows": int(trajectory.shape[0]), "final_checkpoint": str(final_path), "final_hash": digest})
    typer.echo(f"resumed {steps} steps to step {state2.step}")
    typer.echo(f"final hash: {digest}")


@app.command()
def compare(
    checkpoint_a: Path = typer.Option(..., help="Original checkpoint."),
    checkpoint_b: Path = typer.Option(..., help="Migrated checkpoint."),
    steps: int = typer.Option(1000, help="Steps to compare after resume."),
    out: Path = typer.Option(Path("runs/verification_report.json"), help="Report JSON path."),
) -> None:
    report = compare_from_checkpoints(checkpoint_a, checkpoint_b, steps=steps)
    write_report(out, report)
    typer.echo(report.status)
    typer.echo(f"Checkpoint hash: {'matched' if report.checkpoint_hash_matched else 'mismatch'}")
    typer.echo(f"Config hash: {'matched' if report.config_hash_matched else 'mismatch'}")
    typer.echo(f"Trajectory divergence: {report.max_trajectory_error}")
    raise typer.Exit(0 if report.status == "MIGRATION VERIFIED" else 1)


@app.command("collect-dataset")
def collect_dataset_command(
    tasks: str = typer.Option("food,harm,perturb,wall,mixed", help="Comma-separated task battery."),
    episodes: int = typer.Option(100, help="Number of deterministic episodes."),
    steps: int = typer.Option(2000, help="Steps per episode."),
    seed: int = typer.Option(42, help="Base deterministic seed."),
    out: Path = typer.Option(Path("datasets/source_302_v1"), help="Dataset output directory."),
) -> None:
    metadata = collect_dataset(out=out, tasks=tasks, episodes=episodes, steps=steps, seed=seed)
    typer.echo("Dataset created")
    typer.echo(f"Episodes: {metadata['episodes']}")
    typer.echo(f"Total steps: {metadata['total_steps']}")
    typer.echo(f"Neural shape: {metadata['neural_shape'][0]} x {metadata['neural_shape'][1]}")
    typer.echo(f"Dataset hash: {metadata['dataset_hash']}")


@app.command("train-abstraction")
def train_abstraction_command(
    method: str = typer.Option("pca-ridge", help="Abstraction method. Currently only pca-ridge."),
    latent_dim: int = typer.Option(64, help="Latent dimensionality."),
    dataset: Path = typer.Option(Path("datasets/source_302_v1"), help="Dataset directory or dataset.npz."),
    out: Path = typer.Option(Path("abstractions/pca64"), help="Model output directory."),
) -> None:
    if method != "pca-ridge":
        raise typer.BadParameter("Only method='pca-ridge' is implemented in the MVP")
    metadata = train_pca_ridge(dataset=dataset, out=out, latent_dim=latent_dim)
    typer.echo("Abstraction trained")
    typer.echo(f"Method: {metadata['method']}")
    typer.echo(f"Latent dim: {metadata['latent_dim']}")
    typer.echo(f"Compression ratio: {metadata['compression_ratio']:.2f}x")
    typer.echo(f"Model hash: {metadata['model_hash']}")


@app.command("run-abstracted")
def run_abstracted_command(
    model: Path = typer.Option(..., help="Abstraction model directory."),
    task: str = typer.Option("mixed", help="Task name."),
    steps: int = typer.Option(10000, help="Live closed-loop steps."),
    seed: int = typer.Option(42, help="Deterministic seed."),
    out: Path = typer.Option(Path("runs/pca64_live"), help="Run output directory."),
) -> None:
    report = run_abstracted_model(model_path=model, out=out, task_name=task, steps=steps, seed=seed)
    typer.echo(report["status"])
    typer.echo(f"Model hash: {report['model_hash']}")
    typer.echo(f"Checkpoint hash: {report['checkpoint_hash']}")
    typer.echo(f"Mean viability: {report['mean_viability']:.4f}")


@app.command("migrate-abstracted")
def migrate_abstracted_command(
    checkpoint: Path = typer.Option(..., help="Abstracted checkpoint to migrate."),
    out: Path = typer.Option(Path("runs/pca64_migrated"), help="Destination folder."),
) -> None:
    manifest = migrate_abstracted_checkpoint(checkpoint=checkpoint, out=out)
    typer.echo(f"copied checkpoint to {manifest['target']}")
    typer.echo("hash verified" if manifest["hash_matched"] else "hash mismatch")
    raise typer.Exit(0 if manifest["hash_matched"] else 1)


@app.command("verify-abstracted-migration")
def verify_abstracted_migration_command(
    model: Path = typer.Option(..., help="Abstraction model directory."),
    checkpoint_a: Path = typer.Option(..., help="Original abstract checkpoint."),
    checkpoint_b: Path = typer.Option(..., help="Migrated abstract checkpoint."),
    steps: int = typer.Option(1000, help="Post-migration comparison steps."),
    out: Path = typer.Option(Path("reports/abstracted_migration_report.json"), help="Report path."),
) -> None:
    report = verify_abstracted_migration(model_path=model, checkpoint_a=checkpoint_a, checkpoint_b=checkpoint_b, steps=steps)
    _write_json(out, report.to_dict())
    typer.echo(report.status)
    typer.echo(f"Model hash: {report.model_hash}")
    typer.echo(f"Checkpoint hash: {'matched' if report.checkpoint_hash_matched else 'mismatch'}")
    typer.echo(f"Latent trajectory divergence: {report.latent_trajectory_divergence}")
    typer.echo(f"Behavior continuation: {report.behavior_continuation}")
    raise typer.Exit(0 if report.status == "ABSTRACTED MIGRATION VERIFIED" else 1)


@app.command("benchmark-abstraction")
def benchmark_abstraction_command(
    model: Path = typer.Option(..., help="Abstraction model directory."),
    task: str = typer.Option("mixed", help="Task name."),
    steps: int = typer.Option(1000, help="Benchmark steps."),
    seed: int = typer.Option(42, help="Deterministic seed."),
    out: Path = typer.Option(Path("reports/pca64_report"), help="Report directory."),
) -> None:
    report = benchmark_abstraction(model_path=model, out=out, task_name=task, steps=steps, seed=seed)
    typer.echo(report["status"])
    typer.echo(f"Source: {report['source']}")
    typer.echo(f"Abstraction: {report['abstraction']}")
    typer.echo(f"Compression ratio: {report['compression_ratio']:.2f}x")
    typer.echo(f"Behavior fidelity: {report['behavior_fidelity']:.4f}")
    typer.echo(f"Self-maintenance retained: {report['self_maintenance_retained']:.4f}")


@app.command("benchmark-curve")
def benchmark_curve_command(
    dataset: Path = typer.Option(Path("datasets/source_302_v1"), help="Dataset directory or dataset.npz."),
    latent_dims: str = typer.Option("150,64,32,16,8", help="Comma-separated latent dimensions."),
    task: str = typer.Option("mixed", help="Task name."),
    steps: int = typer.Option(1000, help="Live benchmark steps per model."),
    migration_steps: int = typer.Option(250, help="Post-migration verification steps per model."),
    seed: int = typer.Option(42, help="Deterministic seed."),
    include_controls: bool = typer.Option(True, help="Include random and behavior-only controls."),
    out: Path = typer.Option(Path("reports/abstraction_curve"), help="Curve report directory."),
) -> None:
    dims = [int(item.strip()) for item in latent_dims.split(",") if item.strip()]
    summary = generate_abstraction_curve(
        dataset=dataset,
        out=out,
        latent_dims=dims,
        task_name=task,
        steps=steps,
        seed=seed,
        migration_steps=migration_steps,
        include_controls=include_controls,
    )
    typer.echo(summary["status"])
    typer.echo(f"Task: {summary['task']}")
    typer.echo(f"Latent dims: {summary['latent_dims']}")
    typer.echo(f"Curve JSON: {summary['curve_json']}")
    typer.echo(f"Curve CSV: {summary['curve_csv']}")
    best = summary.get("best_pca_model")
    if best:
        typer.echo(f"Best PCA: {best['model']} behavior={best['behavior_fidelity']:.4f} self-maintenance={best['self_maintenance_retained']:.4f}")


if __name__ == "__main__":
    app()
