from __future__ import annotations

"""Durable long-run wrapper for Worm-302 abstraction curves.

This script is intentionally repo-local rather than chat-tool dependent. It writes
heartbeat/status JSONL after every phase so a long benchmark can be resumed or
inspected even if a client/tool session times out.

Example:
    PYTHONPATH=src python scripts/run_worm_abstraction_curve_long.py \
      --out runs/curve_public_50x500 \
      --episodes 50 \
      --episode-steps 500 \
      --benchmark-steps 1000 \
      --migration-steps 250 \
      --latent-dims 150,64,32,16,8
"""

import argparse
import csv
import json
import sys
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from wormsim.abstraction import train_pca_ridge  # noqa: E402
from wormsim.curve import (  # noqa: E402
    _score_model_run,
    train_behavior_only_mean_control,
    train_random_latent_control,
)
from wormsim.dataset import collect_dataset  # noqa: E402
from wormsim.config import WormConfig  # noqa: E402


def now() -> float:
    return time.time()


def _json_safe(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(k): _json_safe(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    if isinstance(value, tuple):
        return [_json_safe(item) for item in value]
    return value


def append_heartbeat(path: Path, event: str, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {"time": now(), "event": event, **_json_safe(payload)}
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, sort_keys=True) + "\n")


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(_json_safe(payload), indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def parse_dims(value: str) -> list[int]:
    dims = [int(item.strip()) for item in value.split(",") if item.strip()]
    if not dims:
        raise ValueError("--latent-dims must contain at least one integer")
    return dims


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a resumable Worm-302 abstraction curve benchmark.")
    parser.add_argument("--out", type=Path, default=Path("runs/curve_public_long"))
    parser.add_argument("--tasks", default="food,harm,perturb,wall,mixed")
    parser.add_argument("--episodes", type=int, default=50)
    parser.add_argument("--episode-steps", type=int, default=500)
    parser.add_argument("--benchmark-steps", type=int, default=1000)
    parser.add_argument("--migration-steps", type=int, default=250)
    parser.add_argument("--latent-dims", default="150,64,32,16,8")
    parser.add_argument("--task", default="mixed")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--skip-controls", action="store_true")
    args = parser.parse_args()

    out = args.out
    dataset_dir = out / "dataset"
    models_dir = out / "models"
    runs_dir = out / "runs"
    rows_dir = out / "rows"
    heartbeat = out / "heartbeat.jsonl"
    status_path = out / "status.json"
    dims = parse_dims(args.latent_dims)

    out.mkdir(parents=True, exist_ok=True)
    append_heartbeat(heartbeat, "start", vars(args) | {"latent_dims_parsed": dims})

    metadata_path = dataset_dir / "metadata.json"
    if metadata_path.exists():
        append_heartbeat(heartbeat, "dataset_reuse", {"path": str(dataset_dir)})
    else:
        append_heartbeat(heartbeat, "dataset_start", {"path": str(dataset_dir)})
        metadata = collect_dataset(
            out=dataset_dir,
            tasks=args.tasks,
            episodes=args.episodes,
            steps=args.episode_steps,
            seed=args.seed,
        )
        append_heartbeat(heartbeat, "dataset_done", metadata)

    rows: list[dict[str, Any]] = [
        {
            "model": "Full source",
            "method": "source-reference",
            "latent_dim": WormConfig().neurons,
            "compression_ratio": 1.0,
            "behavior_fidelity": 1.0,
            "self_maintenance_retained": 1.0,
            "migration_verified": True,
            "checkpoint_hash_matched": True,
            "latent_trajectory_divergence": 0.0,
            "behavior_continuation": "baseline",
            "model_hash": "source-reference",
        }
    ]

    for latent_dim in dims:
        label = f"PCA-{latent_dim}"
        row_path = rows_dir / f"pca_{latent_dim}.json"
        if row_path.exists():
            row = read_json(row_path)
            append_heartbeat(heartbeat, "row_reuse", {"model": label, "path": str(row_path)})
        else:
            model_dir = models_dir / f"pca_{latent_dim}"
            append_heartbeat(heartbeat, "train_start", {"model": label, "latent_dim": latent_dim})
            train_pca_ridge(dataset_dir, model_dir, latent_dim=latent_dim)
            append_heartbeat(heartbeat, "train_done", {"model": label})
            append_heartbeat(heartbeat, "score_start", {"model": label})
            row = _score_model_run(
                model_dir,
                runs_dir / f"pca_{latent_dim}",
                task_name=args.task,
                steps=args.benchmark_steps,
                seed=args.seed,
                migration_steps=args.migration_steps,
                label=label,
                method="pca-ridge",
            )
            write_json(row_path, row)
            append_heartbeat(heartbeat, "score_done", {"model": label, "row": row})
        rows.append(row)
        write_json(out / "abstraction_curve.partial.json", rows)
        write_csv(out / "abstraction_curve.partial.csv", rows)
        write_json(status_path, {"status": "RUNNING", "completed_rows": len(rows), "latest_model": label})

    if not args.skip_controls:
        control_dim = min(dims)
        controls = [
            (f"Random-{control_dim}", "random-latent-control", train_random_latent_control, f"random_{control_dim}"),
            (
                f"BehaviorOnlyMean-{control_dim}",
                "behavior-only-mean-control",
                train_behavior_only_mean_control,
                f"behavior_only_mean_{control_dim}",
            ),
        ]
        for label, method, trainer, folder in controls:
            row_path = rows_dir / f"{folder}.json"
            if row_path.exists():
                row = read_json(row_path)
                append_heartbeat(heartbeat, "row_reuse", {"model": label, "path": str(row_path)})
            else:
                model_dir = models_dir / folder
                append_heartbeat(heartbeat, "control_train_start", {"model": label, "latent_dim": control_dim})
                trainer(dataset_dir, model_dir, latent_dim=control_dim, seed=args.seed)
                append_heartbeat(heartbeat, "control_train_done", {"model": label})
                append_heartbeat(heartbeat, "control_score_start", {"model": label})
                row = _score_model_run(
                    model_dir,
                    runs_dir / folder,
                    task_name=args.task,
                    steps=args.benchmark_steps,
                    seed=args.seed,
                    migration_steps=args.migration_steps,
                    label=label,
                    method=method,
                )
                write_json(row_path, row)
                append_heartbeat(heartbeat, "control_score_done", {"model": label, "row": row})
            rows.append(row)
            write_json(out / "abstraction_curve.partial.json", rows)
            write_csv(out / "abstraction_curve.partial.csv", rows)
            write_json(status_path, {"status": "RUNNING", "completed_rows": len(rows), "latest_model": label})

    write_json(out / "abstraction_curve.json", rows)
    write_csv(out / "abstraction_curve.csv", rows)
    summary = {
        "status": "ABSTRACTION CURVE COMPLETE",
        "out": str(out),
        "dataset": str(dataset_dir),
        "latent_dims": dims,
        "rows": len(rows),
        "curve_json": str(out / "abstraction_curve.json"),
        "curve_csv": str(out / "abstraction_curve.csv"),
    }
    write_json(out / "curve_summary.json", summary)
    write_json(status_path, summary)
    append_heartbeat(heartbeat, "complete", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
