from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from .common import RecordEnvelope, StrictModel


class StressResultPayload(StrictModel):
    proposal_id: str
    stressor: Literal["heldout", "symmetry_break", "adversarial", "robustness"]
    passed: bool
    diagnostics: dict[str, Any] = Field(default_factory=dict)


class StressResultRecord(RecordEnvelope):
    kind: Literal["stress_result_record"] = "stress_result_record"
    payload: StressResultPayload

