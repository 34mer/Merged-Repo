from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from .common import RecordEnvelope, StrictModel


class SubstrateSchemaPayload(StrictModel):
    source_proposal_id: str
    primitive_operations: list[str]
    invariants: list[str]
    scaling_laws: list[str]
    readout_bottlenecks: list[str]
    domain_of_validity: str
    evidence_record_ids: list[str]
    diagnostics: dict[str, Any] = Field(default_factory=dict)


class SubstrateSchemaRecord(RecordEnvelope):
    kind: Literal["substrate_schema_record"] = "substrate_schema_record"
    payload: SubstrateSchemaPayload

