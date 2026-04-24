from __future__ import annotations

from pg_pipeline.pgcore.schemas.geometry import GeometryRecord


def normalize_geometry(record: GeometryRecord) -> GeometryRecord:
    raw = dict(sorted(record.payload.raw_object.items()))
    features = dict(sorted(record.payload.derived_features.items()))
    payload = record.payload.model_copy(update={"raw_object": raw, "derived_features": features})
    return record.model_copy(update={"payload": payload})

