from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from .common import RecordEnvelope, StrictModel


class GeometryPayload(StrictModel):
    canonical_representation: Literal[
        "boundary_lattice_v1",
        "sign_flip_v1",
        "triangulation_v1",
        "face_vector_v1",
        "graph_encoding_v1",
        "canonical_form_v1",
    ]
    raw_object: dict[str, Any]
    derived_features: dict[str, Any] = Field(default_factory=dict)
    symmetry_signature: dict[str, Any] = Field(default_factory=dict)


class GeometryRecord(RecordEnvelope):
    kind: Literal["geometry_record"] = "geometry_record"
    payload: GeometryPayload

