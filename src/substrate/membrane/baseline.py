from __future__ import annotations

import numpy as np


def membrane_benchmark(duration_ms: float = 50.0, dt: float = 0.05) -> dict:
    c_m = 1.0
    g_l = 0.1
    e_l = -65.0
    v0 = -55.0
    t = np.arange(0.0, duration_ms + dt, dt)
    tau = c_m / g_l
    v = e_l + (v0 - e_l) * np.exp(-t / tau)
    return {
        "resting_potential_mv": e_l,
        "capacitance_uF_cm2": c_m,
        "leak_conductance_mS_cm2": g_l,
        "tau_ms": tau,
        "trace": [{"t_ms": float(tt), "v_mv": float(vv)} for tt, vv in zip(t, v)],
    }
