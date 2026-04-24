from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from .common import RecordEnvelope, StrictModel


class CheckResultPayload(StrictModel):
    proposal_id: str
    checker: Literal["symbolic", "combinatorial", "numeric", "smt", "formal"]
    passed: bool
    checked_record_ids: list[str]
    diagnostics: dict[str, Any] = Field(default_factory=dict)


class CheckResultRecord(RecordEnvelope):
    kind: Literal["check_result_record"] = "check_result_record"
    payload: CheckResultPayload

