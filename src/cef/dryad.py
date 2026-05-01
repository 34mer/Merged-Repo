from __future__ import annotations

from pathlib import Path
from typing import Any

from .capture import make_capture_from_episodes
from .core import clamp


def _mean(values: Any) -> float:
    import numpy as np

    arr = np.asarray(values, dtype=float)
    finite = arr[np.isfinite(arr)]
    if finite.size == 0:
        return 0.0
    return float(np.mean(finite))


def _range01(value: float, values: Any) -> float:
    import numpy as np

    arr = np.asarray(values, dtype=float)
    finite = arr[np.isfinite(arr)]
    if finite.size == 0:
        return 0.0
    lo = float(np.min(finite))
    hi = float(np.max(finite))
    if hi <= lo:
        return 0.0
    return clamp((float(value) - lo) / (hi - lo))


def _find_dataset(handle: Any, candidates: list[str], tokens: list[str]) -> Any | None:
    """Find an H5 dataset by exact path first, then by case-insensitive tokens."""

    for candidate in candidates:
        if candidate in handle:
            return handle[candidate]

    found: list[Any] = []
    lower_tokens = [token.lower() for token in tokens]

    def visit(name: str, obj: Any) -> None:
        if found:
            return
        if getattr(obj, "shape", None) is None:
            return
        lowered = name.lower()
        if all(token in lowered for token in lower_tokens):
            found.append(obj)

    handle.visititems(visit)
    return found[0] if found else None


def _array(handle: Any, candidates: list[str], tokens: list[str]) -> Any | None:
    ds = _find_dataset(handle, candidates, tokens)
    if ds is None:
        return None
    return ds[()]


def _as_time_by_feature(traces: Any) -> Any:
    """Normalize neural traces to shape (time, neurons_or_features)."""

    import numpy as np

    arr = np.asarray(traces, dtype=float)
    if arr.ndim == 1:
        return arr[:, None]
    if arr.ndim > 2:
        arr = arr.reshape(arr.shape[0], -1)
    # Whole-brain traces are usually time x neurons, but some exports store
    # neuron x time. If the first axis is plausibly neuron count and the second
    # axis is longer, transpose so windows are temporal.
    if arr.shape[0] <= 302 and arr.shape[1] > arr.shape[0]:
        arr = arr.T
    return arr


def _series(values: Any | None, n: int, default: Any) -> Any:
    import numpy as np

    if values is None:
        if callable(default):
            return np.asarray(default(n), dtype=float).reshape(-1)
        return np.full(n, float(default), dtype=float)
    arr = np.asarray(values, dtype=float).reshape(-1)
    if arr.size == n:
        return arr
    if arr.size == 0:
        return np.zeros(n, dtype=float)
    if arr.size > n:
        return arr[:n]
    # Pad short behavioral vectors with their last value so all windows are valid.
    return np.pad(arr, (0, n - arr.size), mode="edge")


def _time_value(timing: Any, index: int) -> float:
    try:
        return float(timing[index])
    except Exception:
        return float(index)


def import_dryad_copper_h5(
    source: str | Path,
    out: str | Path,
    individual_id: str | None = None,
    windows: int = 6,
) -> dict[str, Any]:
    """Convert one Dryad copper-boundary C. elegans H5 file into a CEF capture.

    Target dataset: Dryad DOI 10.5061/dryad.w9ghx3g4v. The adapter expects one
    per-animal H5 file and looks for neural traces, behavior variables, and timing.
    It is tolerant to exact H5 names: documented paths are tried first, then
    token-based lookup is used.
    """

    if windows < 4:
        raise ValueError("Dryad copper adapter requires at least 4 windows to create construction and heldout splits")

    import numpy as np

    try:
        import h5py  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("CEF Dryad H5 adapter requires h5py") from exc

    path = Path(source)
    with h5py.File(path, "r") as h5:
        traces = _array(
            h5,
            [
                "gcamp/trace_array",
                "gcamp/traces",
                "calcium/trace_array",
                "calcium/traces",
                "neural/trace_array",
                "neural/traces",
                "trace_array",
                "traces",
            ],
            ["trace"],
        )
        if traces is None:
            traces = _array(h5, [], ["gcamp"])
        velocity = _array(h5, ["behavior/velocity", "locomotion/velocity", "velocity"], ["velocity"])
        reversal = _array(
            h5,
            ["behavior/reversal_events", "behavior/reversal", "reversal_events", "reversal"],
            ["reversal"],
        )
        distance = _array(
            h5,
            [
                "behavior/distance_from_copper_center",
                "behavior/distance_to_copper_boundary",
                "distance_from_copper_center",
                "distance_to_copper_boundary",
            ],
            ["distance", "copper"],
        )
        head_angle = _array(h5, ["behavior/head_angle", "posture/head_angle", "head_angle"], ["head", "angle"])
        angular_velocity = _array(
            h5,
            ["behavior/angular_velocity", "posture/angular_velocity", "angular_velocity"],
            ["angular", "velocity"],
        )
        timing = _array(h5, ["timing/timestamps", "timing/time", "time", "timestamps"], ["time"])

    if traces is None:
        raise ValueError("Dryad copper H5 adapter could not find a neural trace dataset")

    trace_arr = _as_time_by_feature(traces)
    n = int(trace_arr.shape[0])
    if n < windows:
        raise ValueError(f"Dryad copper H5 is too short for {windows} windows")

    velocity_arr = _series(velocity, n, 0.0)
    reversal_arr = _series(reversal, n, 0.0)
    distance_arr = _series(distance, n, lambda size: np.linspace(1.0, 0.0, size))
    head_arr = _series(head_angle, n, 0.0)
    angular_arr = _series(angular_velocity, n, 0.0)
    timing_arr = _series(timing, n, lambda size: np.arange(size))
    neural_series = np.nanmean(trace_arr, axis=1)

    episodes: list[dict[str, Any]] = []
    win = max(1, n // windows)
    construction_windows = max(3, windows // 2)
    for i in range(windows):
        start = i * win
        stop = n if i == windows - 1 else min(n, (i + 1) * win)
        if stop <= start:
            continue
        neural_win = neural_series[start:stop]
        velocity_win = velocity_arr[start:stop]
        reversal_win = reversal_arr[start:stop]
        distance_win = distance_arr[start:stop]
        head_win = head_arr[start:stop]
        angular_win = angular_arr[start:stop]

        neural_mean = _range01(_mean(neural_win), neural_series)
        posture_mean = clamp(
            (
                _range01(_mean(np.abs(head_win)), np.abs(head_arr))
                + _range01(_mean(np.abs(angular_win)), np.abs(angular_arr))
            )
            / 2.0
        )
        stimulus_mean = clamp(1.0 - _range01(_mean(distance_win), distance_arr))
        motor_mean = _range01(_mean(np.abs(velocity_win)), np.abs(velocity_arr))
        perturbation = clamp(max(_mean(np.abs(reversal_win)), stimulus_mean))
        perturbation_response = clamp(0.55 * neural_mean + 0.45 * motor_mean + 0.25 * perturbation)
        body_loop_coupling = clamp((posture_mean + motor_mean) / 2.0)

        episodes.append(
            {
                "episode_id": f"{path.stem}_window_{i:02d}",
                "split": "construction" if i < construction_windows else "heldout",
                "channels": {
                    "neural_activity": [float(x) for x in np.nan_to_num(neural_win[:50], nan=0.0)],
                    "posture_body_state": [float(posture_mean)],
                    "environment_stimulus_state": [float(stimulus_mean), float(perturbation)],
                    "motor_output": [float(motor_mean)],
                    "perturbation_events": [
                        {
                            "timestep": _time_value(timing_arr, start),
                            "kind": "copper_boundary",
                            "magnitude": float(perturbation),
                        }
                    ],
                },
                "observables": {
                    "neural_mean": float(neural_mean),
                    "posture_mean": float(posture_mean),
                    "stimulus_mean": float(stimulus_mean),
                    "motor_mean": float(motor_mean),
                    "perturbation_response": float(perturbation_response),
                    "body_loop_coupling": float(body_loop_coupling),
                },
            }
        )

    if len([ep for ep in episodes if ep["split"] == "construction"]) < 3 or not any(
        ep["split"] == "heldout" for ep in episodes
    ):
        raise ValueError("Dryad copper adapter could not create a valid construction/heldout split")

    return make_capture_from_episodes(
        individual_id=individual_id or path.stem,
        episodes=episodes,
        out=out,
        capture_origin="real_dataset",
        dataset_source="Dryad DOI 10.5061/dryad.w9ghx3g4v copper-boundary H5",
        optional_metadata={
            "available": True,
            "adapter": "cef_dryad_copper_h5",
            "file_name": path.name,
            "documented_dataset": "Dryad DOI 10.5061/dryad.w9ghx3g4v",
            "windows": windows,
            "neural_trace_shape_time_by_feature": list(trace_arr.shape),
        },
    )
