from __future__ import annotations

from pathlib import Path
from typing import Any

from .core import clamp, stable_hash, write_json, read_json

CAPTURE_SCHEMA = "cef-v0-individual-worm-capture"

REQUIRED_CHANNELS = [
    "neural_activity",
    "posture_body_state",
    "environment_stimulus_state",
    "motor_output",
    "perturbation_events",
]


def _episode(
    episode_id: str,
    split: str,
    stimulus: float,
    perturbation: float,
    neural_gain: float,
    posture_bias: float,
) -> dict[str, Any]:
    neural_activity = [clamp(neural_gain * stimulus + 0.10), clamp(neural_gain * perturbation + 0.15), clamp((stimulus + perturbation) / 2.0)]
    posture_body_state = [clamp(posture_bias + 0.30 * stimulus), clamp(posture_bias + 0.20 * perturbation)]
    environment_stimulus_state = [clamp(stimulus), clamp(perturbation)]
    motor_output = [clamp(0.35 + 0.40 * stimulus - 0.15 * perturbation), clamp(0.25 + 0.30 * perturbation)]
    perturbation_events = [{"timestep": 10, "kind": "touch" if perturbation > 0.4 else "odor_shift", "magnitude": perturbation}]
    return {
        "episode_id": episode_id,
        "split": split,
        "channels": {
            "neural_activity": neural_activity,
            "posture_body_state": posture_body_state,
            "environment_stimulus_state": environment_stimulus_state,
            "motor_output": motor_output,
            "perturbation_events": perturbation_events,
        },
        "observables": {
            "neural_mean": sum(neural_activity) / len(neural_activity),
            "posture_mean": sum(posture_body_state) / len(posture_body_state),
            "stimulus_mean": sum(environment_stimulus_state) / len(environment_stimulus_state),
            "motor_mean": sum(motor_output) / len(motor_output),
            "perturbation_response": clamp(motor_output[1] + neural_activity[1] - 0.20),
            "body_loop_coupling": clamp((posture_body_state[0] + motor_output[0]) / 2.0),
        },
    }


def make_fixture_capture(out: str | Path = "external/celegans_capture_v0.json") -> dict[str, Any]:
    episodes = [
        _episode("worm_A_train_0", "construction", 0.20, 0.20, 0.70, 0.25),
        _episode("worm_A_train_1", "construction", 0.45, 0.30, 0.70, 0.25),
        _episode("worm_A_train_2", "construction", 0.70, 0.40, 0.70, 0.25),
        _episode("worm_A_holdout_0", "heldout", 0.35, 0.55, 0.70, 0.25),
        _episode("worm_A_holdout_1", "heldout", 0.60, 0.65, 0.70, 0.25),
    ]
    capture = {
        "schema": CAPTURE_SCHEMA,
        "organism": "C. elegans",
        "individual_id": "fixture_worm_A",
        "capture_channels": REQUIRED_CHANNELS,
        "optional_channels": ["anatomy_connectome_metadata"],
        "anatomy_connectome_metadata": {
            "available": False,
            "note": "Fixture does not include individual connectome/anatomy; schema reserves the channel.",
        },
        "episodes": episodes,
    }
    capture["capture_hash"] = stable_hash(capture)
    write_json(out, capture)
    return capture


def load_capture(path: str | Path) -> dict[str, Any]:
    capture = read_json(path)
    if capture.get("schema") != CAPTURE_SCHEMA:
        raise ValueError(f"Unsupported CEF capture schema: {capture.get('schema')}")
    missing = [channel for channel in REQUIRED_CHANNELS if channel not in capture.get("capture_channels", [])]
    if missing:
        raise ValueError(f"CEF capture missing required channels: {missing}")
    if not capture.get("episodes"):
        raise ValueError("CEF capture must contain at least one episode")
    return capture


def split_episodes(capture: dict[str, Any], split: str) -> list[dict[str, Any]]:
    return [episode for episode in capture.get("episodes", []) if episode.get("split") == split]
