from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from .common import RecordEnvelope, StrictModel


class ProposalPayload(StrictModel):
    proposal_type: Literal["recurrence", "equivalence", "invariant", "primitive_set", "completion"]
    dsl: str
    normalized_expression: str
    supporting_record_ids: list[str]
    diagnostics: dict[str, Any] = Field(default_factory=dict)


class ProposalRecord(RecordEnvelope):
    kind: Literal["proposal_record"] = "proposal_record"
    payload: ProposalPayload

