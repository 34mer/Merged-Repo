from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from .capture import make_capture_from_episodes
from .core import clamp


def _as_float_list(value: Any) -> list[float]:
    if isinstance(value, list):
        return [float(v) for v in value]
    if value is None or value == "":
        return []
    text = str(value).replace(";", ",")
    return [float(part.strip()) for part in text.split(",") if part.strip()]


def _episode_from_observables(row: dict[str, Any]) -> dict[str, Any]:
    stimulus = float(row.get("stimulus_mean", row.get("stimulus", 0.0)))
    perturbation = float(row.get("perturbation_magnitude", row.get("perturbation", 0.0)))
    neural_mean = float(row.get("neural_mean", clamp(0.7 * stimulus + 0.1)))
    posture_mean = float(row.get("posture_mean", clamp(0.25 + 0.25 * stimulus + 0.10 * perturbation)))
    motor_mean = float(row.get("motor_mean", clamp(0.30 + 0.35 * stimulus + 0.10 * perturbation)))
    perturbation_response = float(row.get("perturbation_response", clamp(motor_mean + neural_mean - 0.20)))
    body_loop_coupling = float(row.get("body_loop_coupling", clamp((posture_mean + motor_mean) / 2.0)))
    neural_activity = _as_float_list(row.get("neural_activity")) or [neural_mean]
    posture_body_state = _as_float_list(row.get("posture_body_state")) or [posture_mean]
    environment_stimulus_state = _as_float_list(row.get("environment_stimulus_state")) or [stimulus, perturbation]
    motor_output = _as_float_list(row.get("motor_output")) or [motor_mean]
    perturbation_events = row.get("perturbation_events")
    if isinstance(perturbation_events, str) and perturbation_events.strip():
        try:
            perturbation_events = json.loads(perturbation_events)
        except Exception:
            perturbation_events = None
    if not perturbation_events:
        perturbation_events = [{"timestep": int(row.get("perturbation_timestep", 10)), "kind": str(row.get("perturbation_kind", "external_dataset_event")), "magnitude": perturbation}]
    return {
        "episode_id": str(row.get("episode_id", row.get("id", "episode"))),
        "split": str(row.get("split", "construction")),
        "channels": {
            "neural_activity": neural_activity,
            "posture_body_state": posture_body_state,
            "environment_stimulus_state": environment_stimulus_state,
            "motor_output": motor_output,
            "perturbation_events": perturbation_events,
        },
        "observables": {
            "neural_mean": neural_mean,
            "posture_mean": posture_mean,
            "stimulus_mean": stimulus,
            "motor_mean": motor_mean,
            "perturbation_response": perturbation_response,
            "body_loop_coupling": body_loop_coupling,
        },
    }


def import_real_dataset_json(source: str | Path, out: str | Path, individual_id: str | None = None, dataset_source: str | None = None) -> dict[str, Any]:
    payload = json.loads(Path(source).read_text(encoding="utf-8-sig"))
    rows = payload.get("episodes", payload.get("rows", []))
    if not rows:
        raise ValueError("CEF real dataset JSON must include episodes or rows")
    episodes = [_episode_from_observables(row) for row in rows]
    return make_capture_from_episodes(
        individual_id=individual_id or str(payload.get("individual_id", "real_celegans_individual")),
        episodes=episodes,
        out=out,
        capture_origin="real_dataset",
        dataset_source=dataset_source or str(payload.get("dataset_source", "external_celegans_dataset_json")),
        optional_metadata=payload.get("metadata", {"available": False}),
    )


def import_real_dataset_csv(source: str | Path, out: str | Path, individual_id: str = "real_celegans_individual", dataset_source: str = "external_celegans_dataset_csv") -> dict[str, Any]:
    with Path(source).open("r", newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("CEF real dataset CSV must contain at least one row")
    episodes = [_episode_from_observables(row) for row in rows]
    return make_capture_from_episodes(
        individual_id=individual_id,
        episodes=episodes,
        out=out,
        capture_origin="real_dataset",
        dataset_source=dataset_source,
        optional_metadata={"available": False, "adapter": "cef_real_dataset_csv"},
    )
