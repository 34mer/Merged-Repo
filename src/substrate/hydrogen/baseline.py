from __future__ import annotations

RYDBERG_EV = 13.605693122994


def energy_level_ev(n: int) -> float:
    if n < 1:
        raise ValueError("n must be >= 1")
    return -RYDBERG_EV / (n * n)


def degeneracy(n: int) -> int:
    return 2 * n * n


def transition_energy_ev(n_initial: int, n_final: int) -> float:
    return abs(energy_level_ev(n_final) - energy_level_ev(n_initial))


def benchmark(levels: int = 10) -> dict:
    return {
        "ionization_energy_ev": RYDBERG_EV,
        "levels": [
            {"n": n, "energy_ev": energy_level_ev(n), "degeneracy": degeneracy(n)}
            for n in range(1, levels + 1)
        ],
        "lyman_alpha_ev": transition_energy_ev(2, 1),
        "balmer_alpha_ev": transition_energy_ev(3, 2),
    }
