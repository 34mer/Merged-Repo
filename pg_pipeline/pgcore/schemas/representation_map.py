from __future__ import annotations

from typing import Any, Literal

from .common import RecordEnvelope, StrictModel


class RepresentationMapPayload(StrictModel):
    from_representation: str
    to_representation: str
    map_type: Literal["exact", "lossless_normalization", "derived_summary", "approximate"]
    mapping_spec: dict[str, Any]
    validation_artifact_ids: list[str]


class RepresentationMapRecord(RecordEnvelope):
    kind: Literal["representation_map_record"] = "representation_map_record"
    payload: RepresentationMapPayload

