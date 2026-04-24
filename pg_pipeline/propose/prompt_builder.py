from __future__ import annotations


def build_recurrence_prompt(values: list[dict[str, int]]) -> str:
    return f"Propose a recurrence for these values: {values}"

