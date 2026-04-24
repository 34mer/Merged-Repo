from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from .common import RecordEnvelope, StrictModel


class JobPayload(StrictModel):
    status: Literal["queued", "running", "passed", "failed"]
    family: str
    stage: Literal["generate", "normalize", "propose", "check", "stress", "substrate", "review"]
    input_record_ids: list[str] = Field(default_factory=list)
    output_record_ids: list[str] = Field(default_factory=list)
    diagnostics: dict[str, Any] = Field(default_factory=dict)


class JobRecord(RecordEnvelope):
    kind: Literal["job_record"] = "job_record"
    payload: JobPayload

