from __future__ import annotations

"""Ambitious Round 3 scientific protocol runner.

Runs repeated-seed, multi-latent Process-Preserving Substrate Optimization with:
- train/validation/held-out task split
- hard held-out evaluation tasks
- repeated seeds
- base vs improved comparison
- random/over-stable controls
- repair tests
- migration verification
- task-switch-after-migration proxy via switch and hard_mixed held-out tasks
- aggregate mean/std and control-failure reporting

This is intentionally resumable. Each latent/task/seed row is written separately.
"""

import argparse
import csv
import json
import statistics
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
from wormsim.dataset import collect_dataset  # noqa: E402
from wormsim.improvement import benchmark_improved_substrate, train_improved_substrate  # noqa: E402
from wormsim.reports import generate_improved_substrate_report  # noqa: E402


def safe(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(k): safe(v) for k, v in value.items()}
    if isinstance(value, list):
        return [safe(v) for v in value]
    if isinstance(value, tuple):
        return [safe(v) for v in value]
    if hasattr(value, "item"):
        return value.item()
    return value


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(safe(payload), indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def heartbeat(path: Path, event: str, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {"time": time.time(), "event": event, **safe(payload)}
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, sort_keys=True) + "\n")


def parse_ints(value: str) -> list[int]:
    return [int(item.strip()) for item in value.split(",") if item.strip()]


def parse_tasks(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def mean_std(values: list[float]) -> dict[str, float]:
    if not values:
        return {"mean": 0.0, "std": 0.0}
    if len(values) == 1:
        return {"mean": float(values[0]), "std": 0.0}
    return {"mean": float(statistics.mean(values)), "std": float(statistics.stdev(values))}


def compact(latent_dim: int, seed: int, task: str, report: dict[str, Any]) -> dict[str, Any]:
    base = report["base"]
    improved = report["improved"]
    row = {
        "latent_dim": latent_dim,
        "seed": seed,
        "task": task,
        "compression_ratio": improved["row"]["compression_ratio"],
        "base_equivalence": base["scores"]["equivalence_score"],
        "base_passed": base["scores"]["equivalence_passed"],
        "improved_equivalence": improved["scores"]["equivalence_score"],
        "improved_passed": improved["scores"]["equivalence_passed"],
        "improved_improvement": improved["scores"]["improvement_score"],
        "improved_efficiency": improved["scores"]["efficiency_score"],
        "improved_repairability": improved["scores"]["repairability_score"],
        "improved_total": improved["scores"]["total_score"],
        "improved_migration": improved["row"]["migration_verified"],
        "improved_divergence": improved["row"]["latent_trajectory_divergence"],
        "base_migration": base["row"]["migration_verified"],
        "base_divergence": base["row"]["latent_trajectory_divergence"],
    }
    for control in report.get("controls", []):
        name = str(control["row"]["model"]).lower().replace(" ", "_").replace("-", "_")
        row[f"{name}_equivalence"] = control["scores"]["equivalence_score"]
        row[f"{name}_passed"] = control["scores"]["equivalence_passed"]
        row[f"{name}_total"] = control["scores"]["total_score"]
    return row


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
            writer.writerow(safe(row))


def aggregate(rows: list[dict[str, Any]], threshold: float) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    latent_dims = sorted({int(r["latent_dim"]) for r in rows}, reverse=True)
    for latent in latent_dims:
        group = [r for r in rows if int(r["latent_dim"]) == latent]
        controls = [k[:-len("_passed")] for k in group[0] if k.endswith("_passed") and k not in {"base_passed", "improved_passed"}]
        control_fail_rate = 0.0
        if controls:
            failures = []
            for r in group:
                failures.extend([not bool(r.get(f"{c}_passed", True)) for c in controls])
            control_fail_rate = sum(1 for x in failures if x) / len(failures)
        out.append({
            "latent_dim": latent,
            "compression_ratio": group[0]["compression_ratio"],
            "n_runs": len(group),
            "improved_equivalence_mean": mean_std([float(r["improved_equivalence"]) for r in group])["mean"],
            "improved_equivalence_std": mean_std([float(r["improved_equivalence"]) for r in group])["std"],
            "improved_pass_rate": sum(1 for r in group if r["improved_passed"]) / len(group),
            "base_equivalence_mean": mean_std([float(r["base_equivalence"]) for r in group])["mean"],
            "base_pass_rate": sum(1 for r in group if r["base_passed"]) / len(group),
            "improvement_mean": mean_std([float(r["improved_improvement"]) for r in group])["mean"],
            "efficiency_mean": mean_std([float(r["improved_efficiency"]) for r in group])["mean"],
            "repairability_mean": mean_std([float(r["improved_repairability"]) for r in group])["mean"],
            "total_mean": mean_std([float(r["improved_total"]) for r in group])["mean"],
            "migration_pass_rate": sum(1 for r in group if r["improved_migration"] and float(r["improved_divergence"]) == 0.0) / len(group),
            "control_fail_rate": control_fail_rate,
            "scientific_pass": (sum(1 for r in group if r["improved_passed"]) / len(group) >= 0.8) and control_fail_rate >= 0.8,
            "threshold": threshold,
        })
    return out


def md_summary(args: argparse.Namespace, agg: list[dict[str, Any]]) -> str:
    lines = [
        "# Ambitious Round 3 Scientific Protocol Summary",
        "",
        "Process-Preserving Substrate Optimization",
        "",
        "## Protocol",
        f"- Train tasks: `{args.train_tasks}`",
        f"- Validation tasks: `{args.validation_tasks}`",
        f"- Held-out tasks: `{args.heldout_tasks}`",
        f"- Dataset episodes: `{args.episodes}`",
        f"- Episode steps: `{args.episode_steps}`",
        f"- Evaluation seeds: `{args.eval_seeds}`",
        f"- Latent dims: `{args.latent_dims}`",
        f"- Benchmark steps per run: `{args.benchmark_steps}`",
        f"- Migration verification steps: `{args.migration_steps}`",
        f"- Equivalence threshold: `{args.equivalence_threshold}`",
        "",
        "## Aggregate results",
        "",
        "| Latent | Compression | Runs | Improved eq mean+/-std | Improved pass | Base eq mean | Base pass | Repair | Total | Migration | Control fail | Scientific pass |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in agg:
        lines.append(
            f"| {r['latent_dim']} | {float(r['compression_ratio']):.2f}x | {r['n_runs']} | "
            f"{r['improved_equivalence_mean']:.4f}±{r['improved_equivalence_std']:.4f} | "
            f"{r['improved_pass_rate']:.2f} | {r['base_equivalence_mean']:.4f} | {r['base_pass_rate']:.2f} | "
            f"{r['repairability_mean']:.4f} | {r['total_mean']:.4f} | {r['migration_pass_rate']:.2f} | "
            f"{r['control_fail_rate']:.2f} | {r['scientific_pass']} |"
        )
    lines.extend([
        "",
        "## Rule",
        "A result only counts if improved substrates pass the equivalence gate while controls fail it.",
        "",
        "Claim boundary: digital process-preserving substrate optimization only; no biological transfer claim.",
    ])
    return "\n".join(lines) + "\n"


def run(args: argparse.Namespace) -> dict[str, Any]:
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    hb = out / "heartbeat.jsonl"
    rows_dir = out / "rows"
    datasets_dir = out / "datasets"
    models_dir = out / "models"
    reports_dir = out / "reports"
    latent_dims = parse_ints(args.latent_dims)
    eval_seeds = parse_ints(args.eval_seeds)
    heldout_tasks = parse_tasks(args.heldout_tasks)
    train_tasks = args.train_tasks

    heartbeat(hb, "start", vars(args))
    rows: list[dict[str, Any]] = []

    for latent in latent_dims:
        dataset_dir = datasets_dir / f"latent_{latent}"
        if not (dataset_dir / "metadata.json").exists() or args.force:
            heartbeat(hb, "dataset_start", {"latent_dim": latent})
            collect_dataset(dataset_dir, tasks=train_tasks, episodes=args.episodes, steps=args.episode_steps, seed=args.train_seed)
            heartbeat(hb, "dataset_done", {"latent_dim": latent})

        base_dir = models_dir / f"base_pca{latent}"
        improved_dir = models_dir / f"improved_pca{latent}"
        if not (base_dir / "model.npz").exists() or args.force:
            heartbeat(hb, "base_train_start", {"latent_dim": latent})
            train_pca_ridge(dataset_dir, base_dir, latent_dim=latent)
            heartbeat(hb, "base_train_done", {"latent_dim": latent})
        if not (improved_dir / "model.npz").exists() or args.force:
            heartbeat(hb, "improved_train_start", {"latent_dim": latent})
            train_improved_substrate(base_dir, dataset_dir, improved_dir, latent_dim=latent)
            heartbeat(hb, "improved_train_done", {"latent_dim": latent})

        for task in heldout_tasks:
            for seed in eval_seeds:
                row_path = rows_dir / f"latent_{latent}__task_{task}__seed_{seed}.json"
                if row_path.exists() and not args.force:
                    row = read_json(row_path)
                    heartbeat(hb, "row_reuse", {"latent_dim": latent, "task": task, "seed": seed})
                else:
                    heartbeat(hb, "benchmark_start", {"latent_dim": latent, "task": task, "seed": seed})
                    report_dir = reports_dir / f"latent_{latent}" / task / f"seed_{seed}"
                    report = benchmark_improved_substrate(
                        source_dataset=dataset_dir,
                        base_model=base_dir,
                        improved_model=improved_dir,
                        out=report_dir,
                        task_name=task,
                        steps=args.benchmark_steps,
                        migration_steps=args.migration_steps,
                        seed=seed,
                        equivalence_threshold=args.equivalence_threshold,
                        include_controls=not args.skip_controls,
                    )
                    generate_improved_substrate_report(report, report_dir)
                    row = compact(latent, seed, task, report)
                    write_json(row_path, row)
                    heartbeat(hb, "benchmark_done", row)
                rows.append(row)
                write_json(out / "round3_scientific_rows.partial.json", rows)
                write_csv(out / "round3_scientific_rows.partial.csv", rows)
                write_json(out / "status.json", {"status": "RUNNING", "rows_done": len(rows), "latest": row})

    agg = aggregate(rows, args.equivalence_threshold)
    write_json(out / "round3_scientific_rows.json", rows)
    write_csv(out / "round3_scientific_rows.csv", rows)
    write_json(out / "round3_scientific_aggregate.json", agg)
    write_csv(out / "round3_scientific_aggregate.csv", agg)
    (out / "round3_scientific_summary.md").write_text(md_summary(args, agg), encoding="utf-8")
    manifest = {
        "status": "ROUND3 SCIENTIFIC PROTOCOL COMPLETE",
        "out": str(out),
        "summary": str(out / "round3_scientific_summary.md"),
        "rows_json": str(out / "round3_scientific_rows.json"),
        "aggregate_json": str(out / "round3_scientific_aggregate.json"),
        "aggregate_csv": str(out / "round3_scientific_aggregate.csv"),
    }
    write_json(out / "manifest.json", manifest)
    write_json(out / "status.json", manifest)
    heartbeat(hb, "complete", manifest)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Run ambitious Round 3 scientific protocol.")
    parser.add_argument("--out", default="runs/round3_scientific_full")
    parser.add_argument("--train-tasks", default="food,harm,wall")
    parser.add_argument("--validation-tasks", default="dynamic_food,time_harm")
    parser.add_argument("--heldout-tasks", default="memory,switch,hard_mixed")
    parser.add_argument("--episodes", type=int, default=50)
    parser.add_argument("--episode-steps", type=int, default=1000)
    parser.add_argument("--benchmark-steps", type=int, default=5000)
    parser.add_argument("--migration-steps", type=int, default=1000)
    parser.add_argument("--latent-dims", default="150,64,32,16,8")
    parser.add_argument("--train-seed", type=int, default=1)
    parser.add_argument("--eval-seeds", default="76,77,78,79,80,81,82,83,84,85")
    parser.add_argument("--equivalence-threshold", type=float, default=0.90)
    parser.add_argument("--skip-controls", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    manifest = run(args)
    print(json.dumps(safe(manifest), indent=2, sort_keys=True))
    print("Paste this back:", manifest["summary"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
