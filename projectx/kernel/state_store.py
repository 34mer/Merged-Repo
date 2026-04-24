from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {
            "schema": "projectx_state_v1",
            "created_at": utc_now(),
            "updated_at": utc_now(),
            "runs": [],
            "authority_imports": [],
            "comparison_runs": [],
            "continuity": {
                "outer_kernel": "projectx",
                "inner_pipeline": "pg_pipeline",
                "authority_pack": "exact_work",
            },
            "blockers": [],
        }
    state = json.loads(path.read_text(encoding="utf-8"))
    state.setdefault("runs", [])
    state.setdefault("authority_imports", [])
    state.setdefault("comparison_runs", [])
    state.setdefault("blockers", [])
    state.setdefault(
        "continuity",
        {
            "outer_kernel": "projectx",
            "inner_pipeline": "pg_pipeline",
            "authority_pack": "exact_work",
        },
    )
    return state


def save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = utc_now()
    path.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")


def append_run(path: Path, run_summary: dict[str, Any], output_dir: str) -> dict[str, Any]:
    state = load_state(path)
    runs = list(state.get("runs", []))
    runs.append(
        {
            "run_id": run_summary["run_id"],
            "status": run_summary["status"],
            "family": run_summary["family"],
            "substrate_schema_id": run_summary["substrate_schema_id"],
            "output_dir": output_dir,
            "record_count": run_summary.get("geometry_records"),
            "recorded_at": utc_now(),
        }
    )
    state["runs"] = runs
    save_state(path, state)
    return state


def append_authority_import(path: Path, authority_summary: dict[str, Any], output_dir: str) -> dict[str, Any]:
    state = load_state(path)
    imports = list(state.get("authority_imports", []))
    imports.append(
        {
            "run_id": authority_summary["run_id"],
            "status": authority_summary["status"],
            "authority_records": authority_summary["authority_records"],
            "families": authority_summary["families"],
            "output_dir": output_dir,
            "recorded_at": utc_now(),
        }
    )
    state["authority_imports"] = imports
    save_state(path, state)
    return state


def append_comparison_run(path: Path, comparison_summary: dict[str, Any], output_dir: str) -> dict[str, Any]:
    """Record a supervised realization-class comparison run in ProjectX continuity state."""
    state = load_state(path)
    comparisons = list(state.get("comparison_runs", []))
    comparisons.append(
        {
            "run_id": comparison_summary["run_id"],
            "status": comparison_summary["status"],
            "family": comparison_summary["family"],
            "comparison_id": comparison_summary["comparison_id"],
            "check_id": comparison_summary["check_id"],
            "relation": comparison_summary["relation"],
            "verdict": comparison_summary["verdict"],
            "authority_record_count": comparison_summary["authority_record_count"],
            "output_dir": output_dir,
            "recorded_at": utc_now(),
        }
    )
    state["comparison_runs"] = comparisons
    save_state(path, state)
    return state


def record_blocker(path: Path, blocker: dict[str, Any]) -> dict[str, Any]:
    state = load_state(path)
    blockers = list(state.get("blockers", []))
    blockers.append({"recorded_at": utc_now(), **blocker})
    state["blockers"] = blockers
    save_state(path, state)
    return state
