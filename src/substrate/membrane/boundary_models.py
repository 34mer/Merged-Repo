from __future__ import annotations

import numpy as np
from substrate.core import BoundaryObject


def membrane_boundary() -> BoundaryObject:
    return BoundaryObject(
        layer="membrane",
        parameters={"C_m": 1.0, "g_leak": 0.1, "E_leak_mv": -65.0, "Na_out": 145, "K_in": 140, "Cl_out": 110},
        grammar={"surface": "inside_outside_boundary", "flux": "conductance_times_driving_force"},
        constraints={"charge_boundary": True, "finite_capacitance": True},
        observables=["resting_potential", "RC_decay", "capacitance", "leak_current"],
        unfold_rule="membrane.rc_boundary_v1",
    )


def unfold(boundary: BoundaryObject, duration_ms: float = 50.0, dt: float = 0.05) -> dict:
    c_m = float(boundary.parameters["C_m"])
    g_l = float(boundary.parameters["g_leak"])
    e_l = float(boundary.parameters["E_leak_mv"])
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
