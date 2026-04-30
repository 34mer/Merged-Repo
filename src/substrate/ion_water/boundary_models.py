from __future__ import annotations

from substrate.core import BoundaryObject
from .baseline import ION_TARGETS


def ion_water_boundary() -> BoundaryObject:
    return BoundaryObject(
        layer="ion_water",
        parameters={ion: dict(values) for ion, values in ION_TARGETS.items()},
        grammar={"objects": ["ion", "water_shell"], "relation": "charge_solvation_boundary"},
        constraints={"charge_conservation": True, "thermal_noise": True},
        observables=["charge", "diffusion", "hydration_energy"],
        unfold_rule="ion_water.solvation_shell_v1",
    )


def unfold(boundary: BoundaryObject) -> dict:
    return {"ions": boundary.parameters, "solvent": "water", "temperature_c": 25.0}
