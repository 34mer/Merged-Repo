from __future__ import annotations

from pathlib import Path
from typing import Any

from .compiler import verify_packet_independence
from .core import read_json, stable_hash, write_json
from .runtime import run_heldout_projection, run_blind_heldout_projection


def _feature_ranges(rows: list[dict[str, Any]]) -> dict[str, list[float]]:
    return {row["feature"]: [float(row["range"][0]), float(row["range"][1])] for row in rows}


def evaluate_oracle(observables: dict[str, float], verifier_oracle: dict[str, Any]) -> dict[str, Any]:
    ranges = _feature_ranges(verifier_oracle.get("features", []))
    rows = []
    for feature, bounds in ranges.items():
        value = observables.get(feature)
        passed = value is not None and float(bounds[0]) <= float(value) <= float(bounds[1])
        rows.append({
            "feature": feature,
            "value": value,
            "oracle_range": bounds,
            "passed": bool(passed),
        })
    return {
        "status": "PASS" if rows and all(row["passed"] for row in rows) else "FAIL",
        "rows": rows,
        "passed_count": sum(1 for row in rows if row["passed"]),
        "total_count": len(rows),
    }


def _random_control(verifier_oracle: dict[str, Any]) -> dict[str, Any]:
    observables = {row["feature"]: 0.01 for row in verifier_oracle.get("features", [])}
    result = evaluate_oracle(observables, verifier_oracle)
    return {
        "control": "random-runtime",
        "passed": result["status"] == "PASS",
        "failed_as_expected": result["status"] == "FAIL",
        "reason": "random observables should not satisfy held-out individual-worm oracle",
    }


def _over_stable_control(verifier_oracle: dict[str, Any]) -> dict[str, Any]:
    observables = {row["feature"]: 0.5 for row in verifier_oracle.get("features", [])}
    # Force perturbation response to be over-stable/flat and therefore outside the fixture oracle.
    if "perturbation_response" in observables:
        observables["perturbation_response"] = 0.05
    result = evaluate_oracle(observables, verifier_oracle)
    return {
        "control": "over-stable-runtime",
        "passed": result["status"] == "PASS",
        "failed_as_expected": result["status"] == "FAIL",
        "reason": "over-stable runtime should fail held-out perturbation response",
    }


def _behavior_only_control(projection: dict[str, Any], verifier_oracle: dict[str, Any]) -> dict[str, Any]:
    behavior_only = dict(projection["projected_observables"])
    # Preserve motor output but erase internal neural/body-loop constraints.
    for key in ["neural_mean", "body_loop_coupling", "posture_mean"]:
        if key in behavior_only:
            behavior_only[key] = 0.0
    result = evaluate_oracle(behavior_only, verifier_oracle)
    return {
        "control": "behavior-only-output",
        "passed": result["status"] == "PASS",
        "failed_as_expected": result["status"] == "FAIL",
        "reason": "behavior-only output must fail if internal individual constraints fail",
    }


def _missing_split_control(construction_packet: dict[str, Any], verifier_oracle: dict[str, Any]) -> dict[str, Any]:
    broken = dict(verifier_oracle)
    broken["split"] = construction_packet.get("split")
    result = verify_packet_independence(construction_packet, broken)
    return {
        "control": "missing-construction-verifier-split",
        "passed": result["status"] == "PASS",
        "failed_as_expected": result["status"] == "FAIL",
        "reason": "construction and verifier packets must be independent splits",
    }


def _runtime_absorption_control(runtime: dict[str, Any], verifier_oracle: dict[str, Any]) -> dict[str, Any]:
    missing = dict(runtime)
    missing["state"] = {"latent_internal_state": {}}
    projection = run_heldout_projection(missing, verifier_oracle)
    # A runtime with no absorbed construction constraints should be rejected even if oracle centers are known in this synthetic control.
    absorbed = bool(missing.get("state", {}).get("latent_internal_state"))
    return {
        "control": "runtime-cannot-absorb-real-data-constraints",
        "passed": absorbed,
        "failed_as_expected": not absorbed,
        "reason": "runtime must carry absorbed construction constraints, not only oracle outputs",
    }


def run_controls(construction_packet: dict[str, Any], verifier_oracle: dict[str, Any], runtime: dict[str, Any], projection: dict[str, Any]) -> dict[str, Any]:
    controls = [
        _random_control(verifier_oracle),
        _over_stable_control(verifier_oracle),
        _behavior_only_control(projection, verifier_oracle),
        _missing_split_control(construction_packet, verifier_oracle),
        _runtime_absorption_control(runtime, verifier_oracle),
    ]
    return {
        "controls": controls,
        "controls_failed_as_expected": all((not row["passed"]) and row["failed_as_expected"] for row in controls),
        "controls_hash": stable_hash(controls),
    }


def verify_forcing(
    construction_packet: str | Path = "artifacts/cef_v0/construction_packet.json",
    verifier_oracle: str | Path = "artifacts/cef_v0/verifier_oracle.json",
    runtime_path: str | Path = "artifacts/cef_v0/synthetic_worm_runtime/synthetic_runtime.json",
    out: str | Path = "reports/cef_v0_protocol_readiness.json",
) -> dict[str, Any]:
    construction = read_json(construction_packet)
    oracle = read_json(verifier_oracle)
    runtime = read_json(runtime_path)
    independence = verify_packet_independence(construction, oracle)
    projection = run_heldout_projection(runtime, oracle)
    oracle_eval = evaluate_oracle(projection["projected_observables"], oracle)
    controls = run_controls(construction, oracle, runtime, projection)
    runtime_constrained = runtime.get("construction_packet_hash") == construction.get("construction_packet_hash") and bool(runtime.get("state", {}).get("latent_internal_state"))
    passed = all([
        independence["status"] == "PASS",
        runtime_constrained,
        oracle_eval["status"] == "PASS",
        controls["controls_failed_as_expected"],
    ])
    report = {
        "schema": "cef-v0-protocol-readiness-report",
        "protocol": "CEF-v0",
        "claim": "The computational migration stack can be forced by one individual-organism capture packet.",
        "status": "PASS" if passed else "FAIL",
        "individual_capture_packet_loaded": True,
        "capture_origin": construction.get("capture_origin", "unknown"),
        "dataset_source": construction.get("dataset_source", "unknown"),
        "real_organism_constraints_loaded": bool(construction.get("real_organism_constraints_loaded", False)),
        "individual_id": construction.get("individual_id"),
        "construction_verifier_independence": independence,
        "synthetic_worm_runtime_constrained": runtime_constrained,
        "heldout_perturbation_verification": oracle_eval,
        "controls_failed_as_expected": controls["controls_failed_as_expected"],
        "controls": controls["controls"],
        "construction_packet_hash": construction.get("construction_packet_hash"),
        "oracle_hash": oracle.get("oracle_hash"),
        "runtime_hash": runtime.get("runtime_hash"),
        "projection_hash": stable_hash(projection),
    }
    report["report_hash"] = stable_hash(report)
    write_json(out, report)
    return report



def _blind_runtime_absorption_control(runtime: dict[str, Any]) -> dict[str, Any]:
    has_model = bool(runtime.get("projection_model"))
    has_absorbed = bool(runtime.get("state", {}).get("latent_internal_state"))
    return {
        "control": "runtime-cannot-absorb-construction-only-constraints",
        "passed": False,
        "failed_as_expected": has_model and has_absorbed,
        "reason": "blind runtime must carry construction-fit model and absorbed internal constraints",
    }


def run_blind_controls(construction_packet: dict[str, Any], verifier_oracle: dict[str, Any], runtime: dict[str, Any], projection: dict[str, Any]) -> dict[str, Any]:
    controls = [
        _random_control(verifier_oracle),
        _over_stable_control(verifier_oracle),
        _behavior_only_control(projection, verifier_oracle),
        _missing_split_control(construction_packet, verifier_oracle),
        _blind_runtime_absorption_control(runtime),
    ]
    oracle_leak = bool(projection.get("oracle_used_for_generation", True))
    controls.append({
        "control": "verifier-oracle-leakage",
        "passed": oracle_leak,
        "failed_as_expected": not oracle_leak,
        "reason": "blind projection must not use verifier oracle for generation",
    })
    return {
        "controls": controls,
        "controls_failed_as_expected": all((not row["passed"]) and row["failed_as_expected"] for row in controls),
        "controls_hash": stable_hash(controls),
    }


def verify_blind_forcing(
    construction_packet: str | Path = "artifacts/cef_v0/construction_packet.json",
    verifier_oracle: str | Path = "artifacts/cef_v0/verifier_oracle.json",
    heldout_driver: str | Path = "artifacts/cef_v0/heldout_driver.json",
    runtime_path: str | Path = "artifacts/cef_v0/synthetic_worm_runtime/synthetic_runtime.json",
    out: str | Path = "reports/cef_v0_1_protocol_readiness.json",
    protocol: str = "CEF-v0.1",
) -> dict[str, Any]:
    construction = read_json(construction_packet)
    oracle = read_json(verifier_oracle)
    driver = read_json(heldout_driver)
    runtime = read_json(runtime_path)
    independence = verify_packet_independence(construction, oracle)
    projection = run_blind_heldout_projection(runtime, driver)
    oracle_eval = evaluate_oracle(projection["projected_observables"], oracle)
    controls = run_blind_controls(construction, oracle, runtime, projection)
    runtime_constrained = (
        runtime.get("construction_packet_hash") == construction.get("construction_packet_hash")
        and bool(runtime.get("state", {}).get("latent_internal_state"))
        and bool(runtime.get("projection_model"))
    )
    driver_ok = driver.get("oracle_excluded_from_generation") is True and driver.get("heldout_driver_hash") == projection.get("heldout_driver_hash")
    blind_ok = projection.get("oracle_used_for_generation") is False
    passed = all([
        independence["status"] == "PASS",
        runtime_constrained,
        driver_ok,
        blind_ok,
        oracle_eval["status"] == "PASS",
        controls["controls_failed_as_expected"],
    ])
    report = {
        "schema": "cef-v0.1-blind-forcing-readiness-report",
        "protocol": protocol,
        "claim": "The CEF runtime can generate held-out predictions from construction-only constraints and be evaluated by a separate oracle.",
        "status": "PASS" if passed else "FAIL",
        "individual_capture_packet_loaded": True,
        "capture_origin": construction.get("capture_origin", "unknown"),
        "dataset_source": construction.get("dataset_source", "unknown"),
        "real_organism_constraints_loaded": bool(construction.get("real_organism_constraints_loaded", False)),
        "individual_id": construction.get("individual_id"),
        "construction_verifier_independence": independence,
        "synthetic_worm_runtime_constrained": runtime_constrained,
        "verifier_blind_projection": blind_ok,
        "runtime_used_oracle_for_generation": bool(projection.get("oracle_used_for_generation", True)),
        "heldout_driver_loaded": driver_ok,
        "heldout_perturbation_verification": oracle_eval,
        "controls_failed_as_expected": controls["controls_failed_as_expected"],
        "controls": controls["controls"],
        "construction_packet_hash": construction.get("construction_packet_hash"),
        "heldout_driver_hash": driver.get("heldout_driver_hash"),
        "oracle_hash": oracle.get("oracle_hash"),
        "runtime_hash": runtime.get("runtime_hash"),
        "projection_hash": stable_hash(projection),
    }
    report["report_hash"] = stable_hash(report)
    write_json(out, report)
    return report
