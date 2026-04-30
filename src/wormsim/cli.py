from __future__ import annotations

import json
import shutil
from pathlib import Path

import typer

from .checkpoint import file_hash, load_checkpoint, save_checkpoint, verify_hash
from .config import WormConfig
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


if __name__ == "__main__":
    app()
