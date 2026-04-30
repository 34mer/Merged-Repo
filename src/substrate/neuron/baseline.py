from __future__ import annotations

import numpy as np


def _alpha_m(v: float) -> float:
    x = v + 40.0
    return 1.0 if abs(x) < 1e-9 else 0.1 * x / (1.0 - np.exp(-x / 10.0))


def _beta_m(v: float) -> float:
    return 4.0 * np.exp(-(v + 65.0) / 18.0)


def _alpha_h(v: float) -> float:
    return 0.07 * np.exp(-(v + 65.0) / 20.0)


def _beta_h(v: float) -> float:
    return 1.0 / (1.0 + np.exp(-(v + 35.0) / 10.0))


def _alpha_n(v: float) -> float:
    x = v + 55.0
    return 0.1 if abs(x) < 1e-9 else 0.01 * x / (1.0 - np.exp(-x / 10.0))


def _beta_n(v: float) -> float:
    return 0.125 * np.exp(-(v + 65.0) / 80.0)


def simulate_hh(
    duration_ms: float = 80.0,
    dt: float = 0.025,
    current_uA: float = 10.0,
    pulse_start: float = 10.0,
    pulse_end: float = 60.0,
) -> dict:
    """Small Hodgkin-Huxley-like point-neuron benchmark with adaptation/energy states."""

    c_m = 1.0
    g_na, g_k, g_l = 120.0, 36.0, 0.3
    e_na, e_k, e_l = 50.0, -77.0, -54.387
    v = -65.0
    m = _alpha_m(v) / (_alpha_m(v) + _beta_m(v))
    h = _alpha_h(v) / (_alpha_h(v) + _beta_h(v))
    n = _alpha_n(v) / (_alpha_n(v) + _beta_n(v))
    ca = 0.0
    adapt = 0.0
    energy = 1.0
    times = np.arange(0.0, duration_ms + dt, dt)
    trace = []
    spikes = []
    prev_v = v
    for t in times:
        i_ext = current_uA if pulse_start <= t <= pulse_end else 0.0
        i_na = g_na * (m**3) * h * (v - e_na)
        i_k = g_k * (n**4) * (v - e_k)
        i_l = g_l * (v - e_l)
        dv = (i_ext - i_na - i_k - i_l - adapt) / c_m
        v += dt * dv
        m += dt * (_alpha_m(v) * (1.0 - m) - _beta_m(v) * m)
        h += dt * (_alpha_h(v) * (1.0 - h) - _beta_h(v) * h)
        n += dt * (_alpha_n(v) * (1.0 - n) - _beta_n(v) * n)
        if prev_v < 0.0 <= v:
            spikes.append(float(t))
            ca += 0.1
            adapt += 0.35
        ca += dt * (-ca / 80.0)
        adapt += dt * (-adapt / 120.0)
        energy += dt * ((1.0 - energy) / 200.0 - 0.0002 * abs(i_na + i_k))
        energy = float(np.clip(energy, 0.0, 1.2))
        trace.append(
            {
                "t_ms": float(t),
                "v_mv": float(v),
                "m": float(m),
                "h": float(h),
                "n": float(n),
                "ca": float(ca),
                "adapt": float(adapt),
                "energy": float(energy),
            }
        )
        prev_v = v
    return {"trace": trace, "spikes_ms": spikes, "spike_count": len(spikes), "final_v_mv": float(v), "final_energy": float(energy)}


def fi_curve(currents: list[float] | None = None) -> dict:
    if currents is None:
        currents = [0.0, 5.0, 10.0, 15.0, 20.0]
    rows = []
    for current in currents:
        sim = simulate_hh(current_uA=current)
        rows.append({"current_uA": current, "spike_count": sim["spike_count"], "rate_hz": sim["spike_count"] / 0.08})
    return {"rows": rows}


def neuron_benchmark() -> dict:
    sim = simulate_hh()
    return {
        "protocol": "pulse,ramp,noise,refractory,synaptic,energy_stress",
        "pulse_response": sim,
        "fi_curve": fi_curve(),
    }
