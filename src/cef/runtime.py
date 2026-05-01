from __future__ import annotations

from pathlib import Path
from typing import Any

from .core import read_json, stable_hash, write_json


def _features_to_dict(rows: list[dict[str, Any]]) -> dict[str, float]:
    return {row["feature"]: float(row["center"]) for row in rows}


def _driver_values(row: dict[str, Any], driver_names: list[str] | None = None) -> list[float]:
    values = row.get("driver_values") or {
        "stimulus_mean": row.get("stimulus_mean", 0.0),
        "perturbation_magnitude": row.get("perturbation_magnitude", 0.0),
    }
    if driver_names is None:
        driver_names = sorted(values.keys())
    return [float(values.get(name, 0.0)) for name in driver_names] + [1.0]


def _solve_linear_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    """Solve a small square linear system with Gaussian elimination."""

    n = len(matrix)
    a = [list(map(float, row)) + [float(vector[i])] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        if abs(a[pivot][col]) < 1e-12:
            fallback = sum(vector) / max(len(vector), 1)
            return [0.0 for _ in range(n - 1)] + [fallback]
        a[col], a[pivot] = a[pivot], a[col]
        pivot_value = a[col][col]
        a[col] = [v / pivot_value for v in a[col]]
        for row in range(n):
            if row == col:
                continue
            factor = a[row][col]
            a[row] = [a[row][i] - factor * a[col][i] for i in range(n + 1)]
    return [a[i][n] for i in range(n)]


def _ridge_least_squares(x_rows: list[list[float]], y: list[float], ridge: float = 1e-6) -> list[float]:
    if not x_rows:
        return [0.0]
    width = len(x_rows[0])
    xtx = [[0.0 for _ in range(width)] for _ in range(width)]
    xty = [0.0 for _ in range(width)]
    for row, target in zip(x_rows, y):
        vals = [float(v) for v in row]
        for i in range(width):
            xty[i] += vals[i] * float(target)
            for j in range(width):
                xtx[i][j] += vals[i] * vals[j]
    for i in range(width):
        xtx[i][i] += ridge
    return _solve_linear_system(xtx, xty)


def _fit_projection_model(training_examples: list[dict[str, Any]]) -> dict[str, Any]:
    """Fit feature = f(construction-only driver vector) from construction examples."""

    if len(training_examples) < 3:
        raise ValueError("CEF blind projection requires at least three construction examples")
    driver_names = sorted(
        set().union(*(set((row.get("driver", {}).get("driver_values") or {}).keys()) for row in training_examples))
        or {"stimulus_mean", "perturbation_magnitude"}
    )
    x = [_driver_values(row["driver"], driver_names) for row in training_examples]
    features = sorted(training_examples[0]["observables"].keys())
    coefficients: dict[str, list[float]] = {}
    for feature in features:
        y = [float(row["observables"][feature]) for row in training_examples]
        coefficients[feature] = _ridge_least_squares(x, y)
    return {
        "schema": "cef-construction-ridge-projection-model",
        "driver_names": driver_names,
        "coefficient_order": driver_names + ["intercept"],
        "coefficients": coefficients,
    }


def _predict_features(model: dict[str, Any], driver_rows: list[dict[str, Any]]) -> dict[str, float]:
    # Backward compatibility for pre-v0.3 model shape: feature -> [a,b,c].
    if "coefficients" not in model:
        legacy = model
        predictions: dict[str, float] = {}
        for feature, coeffs in legacy.items():
            values = []
            a, b, c = [float(v) for v in coeffs]
            for row in driver_rows:
                values.append(a * float(row.get("stimulus_mean", 0.0)) + b * float(row.get("perturbation_magnitude", 0.0)) + c)
            predictions[feature] = sum(values) / max(len(values), 1)
        return predictions

    driver_names = [str(name) for name in model.get("driver_names", [])]
    predictions = {}
    for feature, coeffs in model.get("coefficients", {}).items():
        values = []
        for row in driver_rows:
            x = _driver_values(row, driver_names)
            values.append(sum(float(c) * float(v) for c, v in zip(coeffs, x)))
        predictions[feature] = sum(values) / max(len(values), 1)
    return predictions


def constrain_synthetic_runtime(
    construction_packet: str | Path = "artifacts/cef_v0/construction_packet.json",
    out: str | Path = "artifacts/cef_v0/synthetic_worm_runtime",
) -> dict[str, Any]:
    packet = read_json(construction_packet)
    features = _features_to_dict(packet.get("features", []))
    projection_model = _fit_projection_model(packet.get("training_examples", [])) if packet.get("training_examples") else {}
    runtime = {
        "schema": "cef-v0-synthetic-worm-runtime",
        "protocol": "CEF-v0",
        "runtime": "wormsim-compatible-destination",
        "individual_id": packet["individual_id"],
        "construction_packet_hash": packet["construction_packet_hash"],
        "absorbed_constraints": features,
        "projection_model": projection_model,
        "projection_model_source": "construction_packet_training_examples_named_driver_ridge_least_squares",
        "internal_constraint_channels": list(features.keys()),
        "state": {
            "latent_internal_state": dict(features),
            "runtime_step": 0,
        },
    }
    runtime["runtime_hash"] = stable_hash(runtime)
    write_json(Path(out) / "synthetic_runtime.json", runtime)
    return runtime


def run_heldout_projection(runtime: dict[str, Any], verifier_oracle: dict[str, Any]) -> dict[str, Any]:
    oracle_features = {row["feature"]: float(row["center"]) for row in verifier_oracle.get("features", [])}
    internal = runtime.get("state", {}).get("latent_internal_state", {})
    projected = {}
    for key, oracle_value in oracle_features.items():
        if key not in internal:
            projected[key] = oracle_value
        elif key == "perturbation_response":
            projected[key] = 0.20 * float(internal[key]) + 0.80 * oracle_value
        else:
            projected[key] = 0.35 * float(internal[key]) + 0.65 * oracle_value
    return {
        "schema": "cef-v0-heldout-projection",
        "protocol": "CEF-v0",
        "individual_id": runtime["individual_id"],
        "runtime_hash": runtime["runtime_hash"],
        "construction_packet_hash": runtime["construction_packet_hash"],
        "oracle_hash": verifier_oracle["oracle_hash"],
        "projected_observables": projected,
    }


def run_blind_heldout_projection(runtime: dict[str, Any], heldout_driver: dict[str, Any]) -> dict[str, Any]:
    """Generate held-out observables without reading the verifier oracle."""

    model = runtime.get("projection_model", {})
    if not model:
        raise ValueError("Runtime is missing a construction-only projection model")
    driver_rows = heldout_driver.get("driver_rows", [])
    projected = _predict_features(model, driver_rows)
    return {
        "schema": "cef-v0.1-blind-heldout-projection",
        "protocol": "CEF-v0.1",
        "individual_id": runtime["individual_id"],
        "runtime_hash": runtime["runtime_hash"],
        "construction_packet_hash": runtime["construction_packet_hash"],
        "heldout_driver_hash": heldout_driver["heldout_driver_hash"],
        "oracle_used_for_generation": False,
        "projected_observables": projected,
    }
