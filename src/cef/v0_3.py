from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

from .ablation import make_resplit_capture
from .capture import load_capture, make_capture_from_episodes
from .compiler import compile_capture_to_packets
from .core import clamp, mean, stable_hash, write_json
from .dryad import import_dryad_copper_h5
from .runtime import constrain_synthetic_runtime
from .verify import verify_blind_forcing


V0_3_DYNAMIC_FEATURES = [
    "neural_slope",
    "neural_variance",
    "neural_peak",
    "neural_lagged_response",
    "posture_slope",
    "motor_slope",
    "perturbation_response_peak",
    "perturbation_response_auc",
    "perturbation_response_decay",
    "population_activity_dispersion",
    "previous_stimulus_mean",
    "delta_stimulus",
    "previous_neural_mean",
    "delta_neural",
    "previous_perturbation_response",
    "delta_perturbation_response",
]


def _range01_signed(value: float) -> float:
    return clamp((float(value) + 1.0) / 2.0)


def _variance01(values: list[float]) -> float:
    if not values:
        return 0.0
    mu = mean(values)
    return clamp(sum((float(v) - mu) ** 2 for v in values) / max(len(values), 1))


def _series_slope01(values: list[float]) -> float:
    if len(values) < 2:
        return 0.5
    return _range01_signed(float(values[-1]) - float(values[0]))


def enrich_capture_with_v0_3_dynamics(source: str | Path, out: str | Path) -> dict[str, Any]:
    """Add CEF-v0.3 window-level dynamics and transition observables to a capture.

    The enrichment is deterministic and uses only per-episode channels plus the
    previous episode's observables. It does not inspect verifier oracle packets.
    """

    capture = load_capture(source)
    enriched: list[dict[str, Any]] = []
    previous: dict[str, Any] | None = None
    for index, episode in enumerate(capture.get("episodes", [])):
        ep = copy.deepcopy(episode)
        obs = dict(ep.get("observables", {}))
        channels = ep.get("channels", {})
        neural = [float(v) for v in channels.get("neural_activity", [])]
        posture = [float(v) for v in channels.get("posture_body_state", [])]
        motor = [float(v) for v in channels.get("motor_output", [])]
        perturbations = [float(p.get("magnitude", 0.0)) for p in channels.get("perturbation_events", [])]

        neural_mean = float(obs.get("neural_mean", mean(neural) if neural else 0.0))
        stimulus = float(obs.get("stimulus_mean", 0.0))
        perturbation_response = float(obs.get("perturbation_response", 0.0))
        posture_mean = float(obs.get("posture_mean", mean(posture) if posture else 0.0))
        motor_mean = float(obs.get("motor_mean", mean(motor) if motor else 0.0))

        prev_obs = obs if previous is None else previous.get("observables", {})
        prev_stimulus = float(prev_obs.get("stimulus_mean", stimulus))
        prev_neural = float(prev_obs.get("neural_mean", neural_mean))
        prev_response = float(prev_obs.get("perturbation_response", perturbation_response))
        prev_posture = float(prev_obs.get("posture_mean", posture_mean))
        prev_motor = float(prev_obs.get("motor_mean", motor_mean))

        dynamic = {
            "neural_slope": _series_slope01(neural),
            "neural_variance": _variance01(neural),
            "neural_peak": clamp(max(neural) if neural else neural_mean),
            "neural_lagged_response": clamp((neural_mean + prev_response) / 2.0),
            "posture_slope": _range01_signed(posture_mean - prev_posture),
            "motor_slope": _range01_signed(motor_mean - prev_motor),
            "perturbation_response_peak": clamp(max([perturbation_response] + perturbations) if perturbations else perturbation_response),
            "perturbation_response_auc": clamp((perturbation_response + sum(perturbations)) / (1.0 + len(perturbations))),
            "perturbation_response_decay": _range01_signed(perturbation_response - prev_response),
            "population_activity_dispersion": _variance01(neural),
            "previous_stimulus_mean": clamp(prev_stimulus),
            "delta_stimulus": _range01_signed(stimulus - prev_stimulus),
            "previous_neural_mean": clamp(prev_neural),
            "delta_neural": _range01_signed(neural_mean - prev_neural),
            "previous_perturbation_response": clamp(prev_response),
            "delta_perturbation_response": _range01_signed(perturbation_response - prev_response),
        }
        obs.update(dynamic)
        ep["observables"] = obs
        ep.setdefault("channels", {})["v0_3_dynamic_observables"] = dynamic
        ep["v0_3_window_index"] = index
        enriched.append(ep)
        previous = ep

    metadata = dict(capture.get("anatomy_connectome_metadata", {}))
    metadata.update(
        {
            "cef_v0_3_dynamic_features": V0_3_DYNAMIC_FEATURES,
            "source_capture_hash": capture.get("capture_hash"),
            "v0_3_enrichment": "window_level_dynamics_and_transition_features",
        }
    )
    return make_capture_from_episodes(
        individual_id=f"{capture.get('individual_id', 'unknown')}_v0_3",
        episodes=enriched,
        out=out,
        capture_origin=str(capture.get("capture_origin", "unknown")),
        dataset_source=str(capture.get("dataset_source", "unknown")),
        optional_metadata=metadata,
    )


def import_dryad_copper_h5_v0_3(
    source: str | Path,
    out: str | Path,
    individual_id: str | None = None,
    windows: int = 12,
) -> dict[str, Any]:
    """Import Dryad copper H5 with v0.3 dynamic observables."""

    if windows not in {12, 18, 24}:
        raise ValueError("CEF-v0.3 Dryad import expects windows to be one of 12, 18, or 24")
    temp = Path(out).with_suffix(".base_v0_2.json")
    import_dryad_copper_h5(source, temp, individual_id=individual_id, windows=windows)
    enriched = enrich_capture_with_v0_3_dynamics(temp, out)
    try:
        temp.unlink()
    except OSError:
        pass
    return enriched


def _gap_rows(report: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in report.get("heldout_perturbation_verification", {}).get("rows", []):
        lo, hi = [float(v) for v in row.get("oracle_range", [0.0, 0.0])]
        value = float(row.get("value", 0.0) or 0.0)
        if lo <= value <= hi:
            gap = 0.0
        elif value < lo:
            gap = lo - value
        else:
            gap = value - hi
        rows.append({"feature": row.get("feature"), "value": value, "oracle_range": [lo, hi], "passed": bool(row.get("passed")), "gap": gap})
    return sorted(rows, key=lambda item: float(item["gap"]), reverse=True)


def _run_case(source_capture: str | Path, out_root: str | Path, heldout_index: int) -> dict[str, Any]:
    case_dir = Path(out_root) / f"leave_one_window_out_{heldout_index:02d}"
    capture_path = case_dir / "capture.json"
    artifacts = case_dir / "artifacts"
    runtime_dir = artifacts / "synthetic_worm_runtime"
    report_path = case_dir / "cef_v0_3_protocol_readiness.json"
    capture = make_resplit_capture(source_capture, capture_path, "leave_one_window_out", heldout_index)
    compile_capture_to_packets(capture_path, artifacts)
    runtime = constrain_synthetic_runtime(artifacts / "construction_packet.json", runtime_dir)
    report = verify_blind_forcing(
        artifacts / "construction_packet.json",
        artifacts / "verifier_oracle.json",
        artifacts / "heldout_driver.json",
        runtime_dir / "synthetic_runtime.json",
        report_path,
        protocol="CEF-v0.3",
    )
    gaps = _gap_rows(report)
    failed = [row["feature"] for row in gaps if not row["passed"]]
    verification = report.get("heldout_perturbation_verification", {})
    summary = {
        "heldout_index": heldout_index,
        "status": report.get("status"),
        "passed_features": f"{verification.get('passed_count', 0)}/{verification.get('total_count', 0)}",
        "failure_features": failed,
        "ranked_invariant_gaps": gaps,
        "oracle_leakage": bool(report.get("runtime_used_oracle_for_generation", True)),
        "controls_failed_as_expected": bool(report.get("controls_failed_as_expected", False)),
        "projection_fit_mode": runtime.get("projection_model_source"),
        "capture_hash": capture.get("capture_hash"),
        "report_hash": report.get("report_hash"),
    }
    write_json(case_dir / "v0_3_case_summary.json", summary)
    return summary


def run_v0_3_robustness(source_capture: str | Path, out_root: str | Path) -> dict[str, Any]:
    """Run CEF-v0.3 formal leave-one-window-out robustness gate."""

    capture = load_capture(source_capture)
    episodes = capture.get("episodes", [])
    if len(episodes) < 4:
        raise ValueError("CEF-v0.3 robustness requires at least 4 windows")
    cases = [_run_case(source_capture, out_root, i) for i in range(len(episodes))]
    all_controls = all(case["controls_failed_as_expected"] for case in cases)
    no_leak = all(not case["oracle_leakage"] for case in cases)
    passed_cases = [case for case in cases if case["status"] == "PASS"]
    failed_cases = [case for case in cases if case["status"] != "PASS"]
    gap_records = []
    for case in failed_cases:
        for gap in case["ranked_invariant_gaps"]:
            if float(gap.get("gap", 0.0)) > 0.0:
                gap_records.append({"heldout_index": case["heldout_index"], **gap})
    gap_records.sort(key=lambda item: float(item["gap"]), reverse=True)
    status = "PASS" if no_leak and all_controls and not failed_cases else "PARTIAL"
    matrix = {
        "schema": "cef-v0.3-window-dynamics-robustness-report",
        "protocol": "CEF-v0.3",
        "source_capture": str(source_capture),
        "source_capture_hash": capture.get("capture_hash"),
        "capture_origin": capture.get("capture_origin"),
        "dataset_source": capture.get("dataset_source"),
        "real_data_ingestion": "PASS" if capture.get("real_organism_constraints_loaded") else "FAIL",
        "dynamic_features": V0_3_DYNAMIC_FEATURES,
        "windows": len(episodes),
        "status": status,
        "named_split_modes_required": "covered by CEF-v0.2 split-ablation; v0.3 formal gate is leave-one-window-out",
        "leave_one_window_out_status": "PASS" if not failed_cases else "PARTIAL",
        "passed_cases": len(passed_cases),
        "failed_cases": len(failed_cases),
        "oracle_leakage": not no_leak,
        "controls_failed_as_expected": all_controls,
        "cases": cases,
        "ranked_invariant_gap_report": gap_records,
    }
    matrix["report_hash"] = stable_hash(matrix)
    write_json(Path(out_root) / "cef_v0_3_robustness_report.json", matrix)
    return matrix


def import_and_run_dryad_v0_3(
    h5_source: str | Path,
    out_root: str | Path,
    windows: int = 12,
    individual_id: str | None = None,
) -> dict[str, Any]:
    outp = Path(out_root)
    capture_path = outp / f"dryad_v0_3_{windows}_window_capture.json"
    import_dryad_copper_h5_v0_3(h5_source, capture_path, individual_id=individual_id, windows=windows)
    return run_v0_3_robustness(capture_path, outp / f"robustness_{windows}_windows")
