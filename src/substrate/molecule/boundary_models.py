from __future__ import annotations

import numpy as np
from substrate.core import BoundaryObject


def h2_boundary() -> BoundaryObject:
    return BoundaryObject(
        layer="molecule",
        parameters={"nuclei": 2, "electrons": 2, "D_e_ev": 4.52, "r_e_angstrom": 0.7414, "morse_a": 1.94},
        grammar={"objects": ["hydrogen_primitive", "hydrogen_primitive"], "relation": "shared_electron_boundary"},
        constraints={"neutral": True, "singlet_ground_state": True},
        observables=["bond_length", "binding_energy", "potential_curve", "vibration"],
        unfold_rule="molecule.morse_boundary_v1",
    )


def unfold(boundary: BoundaryObject, r_values: list[float] | None = None) -> dict:
    if r_values is None:
        r_values = np.linspace(0.45, 2.5, 80).tolist()
    d_e = float(boundary.parameters["D_e_ev"])
    r_e = float(boundary.parameters["r_e_angstrom"])
    a = float(boundary.parameters["morse_a"])
    energy = [d_e * (1.0 - np.exp(-a * (r - r_e))) ** 2 - d_e for r in r_values]
    return {
        "molecule": "H2",
        "bond_length_angstrom": r_e,
        "binding_energy_ev": d_e,
        "vibrational_frequency_cm": 4401.0,
        "curve": [{"r_angstrom": float(r), "energy_ev": float(e)} for r, e in zip(r_values, energy)],
    }
