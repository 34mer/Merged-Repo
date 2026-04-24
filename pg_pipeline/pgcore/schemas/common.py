from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class StrictModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
        populate_by_name=True,
        str_strip_whitespace=True,
    )


class ProducerInfo(StrictModel):
    producer_type: Literal["human", "generator", "proposer", "checker", "controller", "import"]
    name: str
    version: str


class Provenance(StrictModel):
    source_type: Literal["literature", "exact_computation", "numeric_only", "conjectural"]
    citation_keys: list[str] = Field(default_factory=list)
    input_artifact_ids: list[str] = Field(default_factory=list)
    run_id: str | None = None
    notes: str | None = None


class TrustInfo(StrictModel):
    level: Literal["high", "medium", "low"]
    reason: str


class Scope(StrictModel):
    family: str
    parameters: dict[str, Any]
    representation: str
    applicability_domain: str | None = None


class RecordEnvelope(StrictModel):
    id: str
    kind: str
    version: str = "0.1.0"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    producer: ProducerInfo
    provenance: Provenance
    trust: TrustInfo
    scope: Scope

