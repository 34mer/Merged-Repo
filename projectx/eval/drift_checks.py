from __future__ import annotations

from typing import Any


def _norm_list(xs: list[str]) -> list[str]:
    return [str(x).strip() for x in xs if str(x).strip()]


def detect_drift(previous_state: dict[str, Any], current_state: dict[str, Any]) -> list[str]:
    drift: list[str] = []

    prev_inv = previous_state.get("INVARIANT")
    curr_inv = current_state.get("INVARIANT")
    if prev_inv != curr_inv:
        drift.append("invariant_changed")

    prev_obj = previous_state.get("STATE", {}).get("current_objective")
    curr_obj = current_state.get("STATE", {}).get("current_objective")
    if prev_obj != curr_obj:
        drift.append("current_objective_changed")

    prev_priorities = _norm_list(previous_state.get("SALIENCE", {}).get("priority_order", []))
    curr_priorities = _norm_list(current_state.get("SALIENCE", {}).get("priority_order", []))
    if prev_priorities != curr_priorities:
        drift.append("salience_changed")
        prev_top = prev_priorities[:3]
        curr_top = curr_priorities[:3]
        if prev_top and curr_top and len(set(prev_top) & set(curr_top)) == 0:
            drift.append("salience_reordered_hard")

    prev_tasks = [t for t in previous_state.get("TASK_GRAPH", {}).get("active_tasks", []) if isinstance(t, dict)]
    curr_tasks = [t for t in current_state.get("TASK_GRAPH", {}).get("active_tasks", []) if isinstance(t, dict)]
    prev_titles = {str(t.get("title", "")).strip() for t in prev_tasks if str(t.get("title", "")).strip()}
    curr_titles = {str(t.get("title", "")).strip() for t in curr_tasks if str(t.get("title", "")).strip()}
    if prev_titles != curr_titles:
        drift.append("active_tasks_changed")
        if prev_titles and len(curr_titles) < max(1, len(prev_titles) // 2):
            drift.append("active_tasks_reset")

    prev_unknowns = previous_state.get("OPEN_UNKNOWNS", {}).get("items", [])
    curr_unknowns = current_state.get("OPEN_UNKNOWNS", {}).get("items", [])
    if len(curr_unknowns) < len(prev_unknowns):
        drift.append("unknowns_lost")

    prev_decisions = previous_state.get("DECISIONS", {}).get("decisions", [])
    curr_decisions = current_state.get("DECISIONS", {}).get("decisions", [])
    if len(curr_decisions) < len(prev_decisions):
        drift.append("decisions_lost")

    prev_mnf = _norm_list(previous_state.get("SALIENCE", {}).get("must_not_forget", []))
    curr_mnf = _norm_list(current_state.get("SALIENCE", {}).get("must_not_forget", []))
    if prev_mnf != curr_mnf:
        drift.append("must_not_forget_changed")

    return drift
