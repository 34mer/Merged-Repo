from __future__ import annotations

import numpy as np


def sigmoid(v: float, v_half: float, slope: float) -> float:
    return float(1.0 / (1.0 + np.exp(-(v - v_half) / slope)))


def channel_benchmark(kind: str = "sodium") -> dict:
    if kind == "sodium":
        params = {"g_max": 120.0, "e_rev_mv": 50.0, "v_half_mv": -35.0, "slope_mv": 7.0, "recovery_ms": 2.0}
    elif kind == "potassium":
        params = {"g_max": 36.0, "e_rev_mv": -77.0, "v_half_mv": -30.0, "slope_mv": 10.0, "recovery_ms": 4.0}
    else:
        params = {"g_max": 0.3, "e_rev_mv": -54.4, "v_half_mv": -60.0, "slope_mv": 20.0, "recovery_ms": 1.0}
    voltages = np.linspace(-90.0, 40.0, 40)
    curve = []
    for v in voltages:
        p_open = sigmoid(float(v), params["v_half_mv"], params["slope_mv"])
        current = params["g_max"] * p_open * (float(v) - params["e_rev_mv"])
        curve.append({"v_mv": float(v), "open_probability": p_open, "current": float(current)})
    return {"kind": kind, "parameters": params, "iv_curve": curve}
