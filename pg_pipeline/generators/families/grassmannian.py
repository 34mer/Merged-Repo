from __future__ import annotations

from math import comb

from pg_pipeline.pgcore.ids import stable_id
from pg_pipeline.pgcore.schemas.common import ProducerInfo, Provenance, Scope, TrustInfo
from pg_pipeline.pgcore.schemas.geometry import GeometryPayload, GeometryRecord


def catalan(index: int) -> int:
    return comb(2 * index, index) // (index + 1)


def generate_grassmannian_small(run_id: str, n_values: list[int] | None = None) -> list[GeometryRecord]:
    values = n_values or [4, 5, 6, 7]
    records: list[GeometryRecord] = []
    for n in values:
        payload = {
            "family": "grassmannian_small",
            "n": n,
            "boundary_count": catalan(n - 3),
        }
        record_id = stable_id("geometry_record", payload)
        records.append(
            GeometryRecord(
                id=record_id,
                producer=ProducerInfo(
                    producer_type="generator",
                    name="grassmannian_small_generator",
                    version="0.1.0",
                ),
                provenance=Provenance(
                    source_type="exact_computation",
                    run_id=run_id,
                    notes="MVP Catalan-style small-family baseline for the first pipeline slice.",
                ),
                trust=TrustInfo(level="high", reason="Computed by closed-form integer formula."),
                scope=Scope(
                    family="grassmannian_small",
                    parameters={"n": n},
                    representation="boundary_lattice_v1",
                    applicability_domain="MVP small positive-geometry proxy family.",
                ),
                payload=GeometryPayload(
                    canonical_representation="boundary_lattice_v1",
                    raw_object=payload,
                    derived_features={"boundary_count": payload["boundary_count"]},
                    symmetry_signature={"dihedral_proxy_order": 2 * n},
                ),
            )
        )
    return records

