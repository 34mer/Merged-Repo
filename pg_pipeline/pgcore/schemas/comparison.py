from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from .common import RecordEnvelope, StrictModel


class RealizationClassSummary(StrictModel):
    class_id: str
    label: str
    role: str
    features: list[str] = Field(default_factory=list)


class ComparisonPayload(StrictModel):
    comparison_id: str
    left: RealizationClassSummary
    right: RealizationClassSummary
    relation: Literal["equivalent", "distinct", "ordered_specialization", "inconclusive"]
    verdict: Literal["supported", "blocked", "open"]
    shared_layers: list[str]
    distinguishing_layers: list[str]
    specialization_direction: str | None = None
    unresolved_deficits: list[str] = Field(default_factory=list)
    authority_record_ids: list[str] = Field(default_factory=list)
    thread_claim_summary: str
    diagnostics: dict[str, Any] = Field(default_factory=dict)


class ComparisonRecord(RecordEnvelope):
    kind: Literal["comparison_record"] = "comparison_record"
    payload: ComparisonPayload
