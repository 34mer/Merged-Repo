from __future__ import annotations

import numpy as np

H2_BOND_LENGTH_ANGSTROM = 0.7414
H2_BINDING_ENERGY_EV = 4.52
H2_VIBRATIONAL_CM = 4401.0


def morse_curve(r_values: list[float] | None = None) -> dict:
    if r_values is None:
        r_values = np.linspace(0.45, 2.5, 80).tolist()
    d_e = H2_BINDING_ENERGY_EV
    r_e = H2_BOND_LENGTH_ANGSTROM
    a = 1.94
    energy = [d_e * (1.0 - np.exp(-a * (r - r_e))) ** 2 - d_e for r in r_values]
    return {
        "molecule": "H2",
        "bond_length_angstrom": r_e,
        "binding_energy_ev": d_e,
        "vibrational_frequency_cm": H2_VIBRATIONAL_CM,
        "curve": [{"r_angstrom": float(r), "energy_ev": float(e)} for r, e in zip(r_values, energy)],
    }
