from __future__ import annotations

from substrate.core import BoundaryObject
from .baseline import neuron_benchmark


def neuron_boundary() -> BoundaryObject:
    return BoundaryObject(
        layer="neuron",
        parameters={
            "state": ["V", "m", "h", "n", "Ca", "Adapt", "Energy", "SynapticInput"],
            "channels": ["sodium", "potassium", "leak"],
            "compartments": ["point_soma"],
            "primitive_latents": [
                "excitability",
                "recovery",
                "boundary",
                "calcium",
                "energy",
                "plasticity",
                "modulation",
            ],
        },
        grammar={"process": "membrane + channels + adaptation + energy + synaptic_input"},
        constraints={"finite_voltage": True, "refractory_recovery": True, "energy_homeostasis": True},
        observables=["spikes", "FI_curve", "refractory", "adaptation", "energy_recovery"],
        unfold_rule="neuron.hh_boundary_process_v1",
    )


def unfold(boundary: BoundaryObject) -> dict:
    return neuron_benchmark()
