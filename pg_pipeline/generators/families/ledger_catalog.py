from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from pg_pipeline.pgcore.ids import stable_id
from pg_pipeline.pgcore.schemas.common import ProducerInfo, Provenance, Scope, TrustInfo
from pg_pipeline.pgcore.schemas.geometry import GeometryPayload, GeometryRecord


def load_authority_catalog(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def generate_authority_records(catalog_path: Path, run_id: str) -> list[GeometryRecord]:
    catalog = load_authority_catalog(catalog_path)
    records: list[GeometryRecord] = []
    for family in catalog["families"]:
        payload = {
            "authority_family_id": family["id"],
            "label": family["label"],
            "safe_claim": family["safe_claim"],
            "authority_files": family["authority_files"],
            "source_type": family["source_type"],
        }
        records.append(
            GeometryRecord(
                id=stable_id("geometry_record", payload),
                producer=ProducerInfo(
                    producer_type="import",
                    name="exact_work_authority_catalog",
                    version="0.1.0",
                ),
                provenance=Provenance(
                    source_type="literature",
                    input_artifact_ids=family["authority_files"],
                    run_id=run_id,
                    notes="Source-backed authority record from research-ledger Lean/handoff files.",
                ),
                trust=TrustInfo(
                    level="high",
                    reason="Catalog entry points to imported Lean/handoff authority files.",
                ),
                scope=Scope(
                    family=family["id"],
                    parameters={"source_type": family["source_type"]},
                    representation="authority_catalog_v1",
                    applicability_domain=family["safe_claim"],
                ),
                payload=GeometryPayload(
                    canonical_representation="graph_encoding_v1",
                    raw_object=payload,
                    derived_features={"pipeline_role": family["pipeline_role"]},
                    symmetry_signature={},
                ),
            )
        )
    return records

