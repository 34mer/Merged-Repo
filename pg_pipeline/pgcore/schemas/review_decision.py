from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from .common import RecordEnvelope, StrictModel


class ReviewDecisionPayload(StrictModel):
    subject_record_id: str
    decision: Literal["accept", "revise", "reject", "archive"]
    rationale: str
    diagnostics: dict[str, Any] = Field(default_factory=dict)


class ReviewDecisionRecord(RecordEnvelope):
    kind: Literal["review_decision_record"] = "review_decision_record"
    payload: ReviewDecisionPayload

