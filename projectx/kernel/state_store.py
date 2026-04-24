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
            "continuity": {
                "outer_kernel": "projectx",
                "inner_pipeline": "pg_pipeline",
                "authority_pack": "exact_work",
            },
            "blockers": [],
        }
    return json.loads(path.read_text(encoding="utf-8"))


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


def record_blocker(path: Path, blocker: dict[str, Any]) -> dict[str, Any]:
    state = load_state(path)
    blockers = list(state.get("blockers", []))
    blockers.append({"recorded_at": utc_now(), **blocker})
    state["blockers"] = blockers
    save_state(path, state)
    return state
