from __future__ import annotations

from substrate.core import BoundaryObject
from .baseline import channel_benchmark


def channel_boundary(kind: str = "sodium") -> BoundaryObject:
    params = channel_benchmark(kind)["parameters"]
    return BoundaryObject(
        layer="channel",
        parameters={"kind": kind, **params, "states": ["closed", "open", "inactivated"]},
        grammar={"state_graph": "closed<->open<->inactivated", "coupling": "voltage_dependent_transition"},
        constraints={"open_probability_range": [0, 1], "ion_selectivity": kind},
        observables=["gating_curve", "IV_curve", "conductance", "recovery"],
        unfold_rule="channel.markov_boundary_v1",
    )


def unfold(boundary: BoundaryObject) -> dict:
    return channel_benchmark(str(boundary.parameters["kind"]))
