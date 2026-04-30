from __future__ import annotations

from typing import Any

import numpy as np


def detect_spikes(voltage_mv: list[float], dt_ms: float, threshold_mv: float = 0.0) -> list[float]:
    spikes: list[float] = []
    if not voltage_mv:
        return spikes
    prev = float(voltage_mv[0])
    for idx, value in enumerate(voltage_mv[1:], start=1):
        v = float(value)
        if prev < threshold_mv <= v:
            spikes.append(float(idx * dt_ms))
        prev = v
    return spikes


def voltage_trace_similarity(predicted: list[float], target: list[float]) -> float:
    n = min(len(predicted), len(target))
    if n == 0:
        return 0.0
    p = np.asarray(predicted[:n], dtype=np.float64)
    t = np.asarray(target[:n], dtype=np.float64)
    rmse = float(np.sqrt(np.mean((p - t) ** 2)))
    scale = max(float(np.max(t) - np.min(t)), 1.0)
    return float(np.clip(1.0 - rmse / scale, 0.0, 1.0))


def spike_timing_score(predicted: list[float], target: list[float], tolerance_ms: float = 2.0) -> float:
    if not target and not predicted:
        return 1.0
    if not target or not predicted:
        return 0.0
    used: set[int] = set()
    matches = 0
    timing_errors: list[float] = []
    for t in target:
        candidates = [(idx, abs(float(p) - float(t))) for idx, p in enumerate(predicted) if idx not in used]
        if not candidates:
            continue
        idx, err = min(candidates, key=lambda item: item[1])
        if err <= tolerance_ms:
            used.add(idx)
            matches += 1
            timing_errors.append(err / tolerance_ms)
    precision_recall = matches / max(len(target), len(predicted), 1)
    timing_bonus = 1.0 - float(np.mean(timing_errors)) if timing_errors else 0.0
    return float(np.clip(0.75 * precision_recall + 0.25 * timing_bonus, 0.0, 1.0))


def fi_curve_similarity(predicted_rows: list[dict[str, Any]], target_rows: list[dict[str, Any]]) -> float:
    if not predicted_rows or not target_rows:
        return 0.0
    pred_by_current = {float(row["current_uA"]): float(row["spike_count"]) for row in predicted_rows}
    errors: list[float] = []
    for row in target_rows:
        current = float(row["current_uA"])
        target = float(row["spike_count"])
        if current not in pred_by_current:
            errors.append(1.0)
            continue
        errors.append(abs(pred_by_current[current] - target) / max(abs(target), 1.0))
    return float(np.clip(1.0 - np.mean(errors), 0.0, 1.0))


def protocol_score(predicted: dict[str, Any], target: dict[str, Any]) -> dict[str, float]:
    dt = float(target.get("dt_ms", 0.025))
    target_voltage = [float(v) for v in target["voltage_mv"]]
    predicted_voltage = [float(v) for v in predicted["voltage_mv"]]
    target_spikes = target.get("spike_times_ms") or detect_spikes(target_voltage, dt)
    predicted_spikes = predicted.get("spike_times_ms") or detect_spikes(predicted_voltage, dt)
    voltage = voltage_trace_similarity(predicted_voltage, target_voltage)
    spikes = spike_timing_score(predicted_spikes, target_spikes)
    return {
        "voltage_trace_similarity": voltage,
        "spike_timing_score": spikes,
        "combined_protocol_score": float(np.clip(0.60 * voltage + 0.40 * spikes, 0.0, 1.0)),
    }


def summarize_protocol_scores(rows: list[dict[str, Any]]) -> dict[str, float]:
    if not rows:
        return {"voltage_fidelity": 0.0, "spike_timing_score": 0.0, "heldout_score": 0.0}
    return {
        "voltage_fidelity": float(np.mean([row["voltage_trace_similarity"] for row in rows])),
        "spike_timing_score": float(np.mean([row["spike_timing_score"] for row in rows])),
        "heldout_score": float(np.mean([row["combined_protocol_score"] for row in rows])),
    }
