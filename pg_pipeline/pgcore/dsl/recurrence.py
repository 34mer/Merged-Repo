from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class RecurrenceProposal(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    sequence_name: str
    expression: str
    base_cases: dict[int, int]


def parse_recurrence_dsl(dsl: str) -> RecurrenceProposal:
    if "C[n]" not in dsl or "sum(" not in dsl:
        raise ValueError("recurrence DSL must define C[n] using sum(...)")
    return RecurrenceProposal(
        sequence_name="grassmannian_boundary_count",
        expression=dsl,
        base_cases={1: 1},
    )

