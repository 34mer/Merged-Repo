from __future__ import annotations

ION_TARGETS = {
    "Na+": {"charge": 1, "diffusion_um2_ms": 1.33, "hydration_energy_kj_mol": -365.0},
    "K+": {"charge": 1, "diffusion_um2_ms": 1.96, "hydration_energy_kj_mol": -295.0},
    "Cl-": {"charge": -1, "diffusion_um2_ms": 2.03, "hydration_energy_kj_mol": -340.0},
    "Ca2+": {"charge": 2, "diffusion_um2_ms": 0.79, "hydration_energy_kj_mol": -1505.0},
}


def benchmark() -> dict:
    return {"ions": ION_TARGETS, "solvent": "water", "temperature_c": 25.0}
