from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

from .capture import load_capture, make_capture_from_episodes
from .compiler import OBSERVABLES, compile_capture_to_packets
from .core import stable_hash, write_json
from .runtime import constrain_synthetic_runtime
from .verify import verify_blind_forcing


SPLIT_MODES = [
    "chronological",
    "interleaved",
    "stimulus_stratified",
    "leave_one_window_out",
]


def _clone_episode_with_split(episode: dict[str, Any], split: str) -> dict[str, Any]:
    cloned = copy.deepcopy(episode)
    cloned["split"] = split
    return cloned


def _indices_for_split(episodes: list[dict[str, Any]], mode: str, heldout_index: int | None = None) -> tuple[list[int], list[int]]:
    n = len(episodes)
    if n < 4:
        raise ValueError("CEF split ablation requires at least 4 episodes/windows")

    all_indices = list(range(n))
    if mode == "chronological":
        cut = max(3, n // 2)
        cut = min(cut, n - 1)
        return all_indices[:cut], all_indices[cut:]

    if mode == "interleaved":
        heldout = [idx for idx in all_indices if idx % 3 == 2]
        if not heldout:
            heldout = [n - 1]
        construction = [idx for idx in all_indices if idx not in heldout]
        if len(construction) < 3:
            heldout = [n - 1]
            construction = [idx for idx in all_indices if idx != n - 1]
        return construction, heldout

    if mode == "stimulus_stratified":
        ordered = sorted(
            all_indices,
            key=lambda idx: float(episodes[idx].get("observables", {}).get("stimulus_mean", 0.0)),
        )
        targets = sorted({0, len(ordered) // 2, len(ordered) - 1})
        heldout = [ordered[pos] for pos in targets]
        construction = [idx for idx in all_indices if idx not in heldout]
        while len(construction) < 3 and len(heldout) > 1:
            construction.append(heldout.pop(0))
        return sorted(construction), sorted(heldout)

    if mode == "leave_one_window_out":
        if heldout_index is None:
            raise ValueError("leave_one_window_out requires heldout_index")
        if heldout_index < 0 or heldout_index >= n:
            raise ValueError(f"heldout_index {heldout_index} outside 0..{n - 1}")
        return [idx for idx in all_indices if idx != heldout_index], [heldout_index]

    raise ValueError(f"Unknown split mode {mode!r}; expected one of {SPLIT_MODES}")


def make_resplit_capture(
    source_capture: str | Path,
    out: str | Path,
    split_mode: str,
    heldout_index: int | None = None,
) -> dict[str, Any]:
    """Rewrite an existing CEF capture with a named construction/heldout split."""

    capture = load_capture(source_capture)
    episodes = list(capture.get("episodes", []))
    construction, heldout = _indices_for_split(episodes, split_mode, heldout_index)
    heldout_set = set(heldout)
    resplit_episodes = [
        _clone_episode_with_split(ep, "heldout" if idx in heldout_set else "construction")
        for idx, ep in enumerate(episodes)
    ]
    metadata = dict(capture.get("anatomy_connectome_metadata", {}))
    metadata.update(
        {
            "split_ablation": True,
            "split_mode": split_mode,
            "heldout_index": heldout_index,
            "construction_indices": construction,
            "heldout_indices": heldout,
            "source_capture_hash": capture.get("capture_hash"),
        }
    )
    individual_suffix = split_mode if heldout_index is None else f"{split_mode}_{heldout_index:02d}"
    return make_capture_from_episodes(
        individual_id=f"{capture.get('individual_id', 'unknown')}_{individual_suffix}",
        episodes=resplit_episodes,
        out=out,
        capture_origin=str(capture.get("capture_origin", "real_dataset")),
        dataset_source=str(capture.get("dataset_source", "unknown")),
        optional_metadata=metadata,
    )


def _summarize_case(report: dict[str, Any], split_mode: str, windows: int, heldout_index: int | None) -> dict[str, Any]:
    verification = report.get("heldout_perturbation_verification", {})
    rows = verification.get("rows", [])
    failures = [row.get("feature") for row in rows if not row.get("passed")]
    return {
        "split_mode": split_mode,
        "windows": windows,
        "heldout_index": heldout_index,
        "real_data_ingestion": "PASS" if report.get("real_organism_constraints_loaded") else "FAIL",
        "oracle_leakage": bool(report.get("runtime_used_oracle_for_generation", True)),
        "controls_failed_as_expected": bool(report.get("controls_failed_as_expected", False)),
        "heldout_status": report.get("status", "UNKNOWN"),
        "heldout_verification_status": verification.get("status", "UNKNOWN"),
        "passed_features": f"{verification.get('passed_count', 0)}/{verification.get('total_count', len(OBSERVABLES))}",
        "failure_features": failures,
        "report_hash": report.get("report_hash"),
        "runtime_hash": report.get("runtime_hash"),
        "construction_packet_hash": report.get("construction_packet_hash"),
        "oracle_hash": report.get("oracle_hash"),
    }


def run_capture_split_case(
    source_capture: str | Path,
    out_root: str | Path,
    split_mode: str,
    heldout_index: int | None = None,
    protocol: str = "CEF-v0.2-ablation",
) -> dict[str, Any]:
    """Run one verifier-blind split-ablation case from an existing capture."""

    outp = Path(out_root)
    suffix = split_mode if heldout_index is None else f"{split_mode}_{heldout_index:02d}"
    case_dir = outp / suffix
    capture_path = case_dir / "capture.json"
    artifacts_dir = case_dir / "artifacts"
    runtime_dir = artifacts_dir / "synthetic_worm_runtime"
    report_path = case_dir / "cef_v0_2_protocol_readiness.json"

    capture = make_resplit_capture(source_capture, capture_path, split_mode, heldout_index)
    compile_capture_to_packets(capture_path, artifacts_dir)
    runtime = constrain_synthetic_runtime(artifacts_dir / "construction_packet.json", runtime_dir)
    report = verify_blind_forcing(
        artifacts_dir / "construction_packet.json",
        artifacts_dir / "verifier_oracle.json",
        artifacts_dir / "heldout_driver.json",
        runtime_dir / "synthetic_runtime.json",
        report_path,
        protocol=protocol,
    )
    windows = len(capture.get("episodes", []))
    summary = _summarize_case(report, split_mode=split_mode, windows=windows, heldout_index=heldout_index)
    summary.update(
        {
            "case_dir": str(case_dir),
            "capture_hash": capture.get("capture_hash"),
            "source_capture": str(source_capture),
            "projection_fit_mode": runtime.get("projection_model_source", "unknown"),
        }
    )
    write_json(case_dir / "case_summary.json", summary)
    return summary


def run_capture_split_ablation(
    source_capture: str | Path,
    out_root: str | Path,
    include_leave_one_out: bool = True,
) -> dict[str, Any]:
    """Run the CEF-v0.2 real-data split-ablation matrix from an existing capture."""

    capture = load_capture(source_capture)
    windows = len(capture.get("episodes", []))
    cases: list[dict[str, Any]] = []
    for mode in ["chronological", "interleaved", "stimulus_stratified"]:
        cases.append(run_capture_split_case(source_capture, out_root, mode))
    if include_leave_one_out:
        for heldout_index in range(windows):
            cases.append(run_capture_split_case(source_capture, out_root, "leave_one_window_out", heldout_index))

    matrix = {
        "schema": "cef-v0.2-real-data-split-ablation-matrix",
        "source_capture": str(source_capture),
        "source_capture_hash": capture.get("capture_hash"),
        "dataset_source": capture.get("dataset_source"),
        "capture_origin": capture.get("capture_origin"),
        "real_data_ingestion": "PASS" if capture.get("real_organism_constraints_loaded") else "FAIL",
        "windows": windows,
        "projection_fit_mode": "construction_packet_training_examples_named_driver_ridge_least_squares",
        "verifier_rule": "construction packet + heldout driver generate projection; verifier oracle is evaluation-only",
        "cases": cases,
    }
    matrix["matrix_hash"] = stable_hash(matrix)
    write_json(Path(out_root) / "split_ablation_matrix.json", matrix)
    return matrix
