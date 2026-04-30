from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Any


def grid_search(candidates: Iterable[dict[str, Any]], loss_fn: Callable[[dict[str, Any]], float]) -> dict[str, Any]:
    best: dict[str, Any] | None = None
    best_loss = float("inf")
    for candidate in candidates:
        loss = float(loss_fn(candidate))
        if loss < best_loss:
            best = candidate
            best_loss = loss
    if best is None:
        raise ValueError("No candidates supplied")
    return {"parameters": best, "loss": best_loss}
