from __future__ import annotations

from pg_pipeline.pgcore.schemas.geometry import GeometryRecord


def break_symmetry(record: GeometryRecord) -> GeometryRecord:
    payload = record.payload.model_copy(
        update={"symmetry_signature": {**record.payload.symmetry_signature, "broken": True}}
    )
    return record.model_copy(update={"payload": payload})

