from __future__ import annotations

from pg_pipeline.pgcore.canon.normalize_geometry import normalize_geometry
from pg_pipeline.pgcore.schemas.geometry import GeometryRecord


def normalize_records(records: list[GeometryRecord]) -> list[GeometryRecord]:
    return [normalize_geometry(record) for record in records]

