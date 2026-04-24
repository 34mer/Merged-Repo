from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from .common import RecordEnvelope, StrictModel


class FailedConjecturePayload(StrictModel):
    family: str
    conjecture_type: Literal["recurrence", "equivalence", "invariant", "primitive_set", "completion"]
    normalized_expression: str
    failure_mode: str
    counterexample_ids: list[str]
    diagnostics: dict[str, Any] = Field(default_factory=dict)


class FailedConjectureRecord(RecordEnvelope):
    kind: Literal["failed_conjecture_record"] = "failed_conjecture_record"
    payload: FailedConjecturePayload

