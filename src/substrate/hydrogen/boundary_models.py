from __future__ import annotations

from substrate.core import BoundaryObject


def hydrogen_boundary(rydberg_ev: float = 13.605693122994) -> BoundaryObject:
    return BoundaryObject(
        layer="hydrogen",
        parameters={"rydberg_ev": rydberg_ev, "energy_law": "E_n=-R/n^2", "degeneracy_law": "2n^2"},
        grammar={"state": ["n"], "n": "positive_integer"},
        constraints={"n_min": 1, "coulomb_bound_state": True},
        observables=["energy_levels", "ionization_energy", "degeneracy", "transitions"],
        unfold_rule="hydrogen.spectral_kernel_v1",
    )


def unfold(boundary: BoundaryObject, levels: int = 10) -> dict:
    r = float(boundary.parameters["rydberg_ev"])
    energies = [{"n": n, "energy_ev": -r / (n * n), "degeneracy": 2 * n * n} for n in range(1, levels + 1)]
    return {
        "ionization_energy_ev": r,
        "levels": energies,
        "lyman_alpha_ev": abs(energies[1]["energy_ev"] - energies[0]["energy_ev"]),
        "balmer_alpha_ev": abs(energies[2]["energy_ev"] - energies[1]["energy_ev"]),
    }
