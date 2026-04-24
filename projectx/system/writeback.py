from __future__ import annotations

from typing import Any

from .utils import utc_now_iso
from .provenance import ensure_provenance, stamp_origin, touch_item


def _next_id(prefix: str, items: list[dict[str, Any]]) -> str:
    max_n = 0
    for item in items:
        raw = str(item.get("id", ""))
        if raw.startswith(f"{prefix}-"):
            try:
                max_n = max(max_n, int(raw.split("-")[1]))
            except (IndexError, ValueError):
                pass
    return f"{prefix}-{max_n + 1:03d}"


def _as_unknown(entry: Any) -> dict[str, str]:
    if isinstance(entry, dict):
        return {
            "question": str(entry.get("question", "")).strip(),
            "class": str(entry.get("class", "engineering")).strip() or "engineering",
            "status": str(entry.get("status", "open")).strip() or "open",
        }
    return {"question": str(entry).strip(), "class": "engineering", "status": "open"}


def _as_task(entry: Any) -> dict[str, str]:
    if isinstance(entry, dict):
        return {
            "title": str(entry.get("title", "")).strip(),
            "status": str(entry.get("status", "active")).strip() or "active",
        }
    return {"title": str(entry).strip(), "status": "active"}


def _dedupe_keep_order(items: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for raw in items:
        item = str(raw).strip()
        if not item or item in seen:
            continue
        seen.add(item)
        out.append(item)
    return out


def apply_writeback(kernel_state: dict[str, Any], delta: dict[str, Any], update_plan: dict[str, bool]) -> dict[str, Any]:
    updated = {k: v for k, v in kernel_state.items()}
    now = utc_now_iso()

    state = dict(updated.get("STATE", {}))
    if state:
        state["last_updated"] = now
        updated["STATE"] = state

    if update_plan.get("DECISIONS"):
        decisions_obj = dict(updated.get("DECISIONS", {"decisions": []}))
        decisions = [ensure_provenance(d, now=now) for d in list(decisions_obj.get("decisions", []))]
        by_statement = {str(item.get("statement", "")).strip(): idx for idx, item in enumerate(decisions)}
        for statement in delta.get("decisions", []):
            clean = str(statement).strip()
            if not clean:
                continue
            if clean in by_statement:
                idx = by_statement[clean]
                current = decisions[idx]
                current["status"] = current.get("status", "active") or "active"
                current["last_touched"] = now
                decisions[idx] = touch_item(current, now, via="session_update")
                continue
            item = stamp_origin({
                "id": _next_id("D", decisions),
                "statement": clean,
                "reason": "Added during session writeback.",
                "status": "active",
                "timestamp": now,
                "last_touched": now,
            }, "session_update", now, via="writeback")
            by_statement[clean] = len(decisions)
            decisions.append(item)
        decisions_obj["decisions"] = decisions
        updated["DECISIONS"] = decisions_obj

    if update_plan.get("OPEN_UNKNOWNS"):
        unknowns_obj = dict(updated.get("OPEN_UNKNOWNS", {"items": []}))
        items = [ensure_provenance(x, now=now) for x in list(unknowns_obj.get("items", []))]
        by_question = {str(item.get("question", "")).strip(): idx for idx, item in enumerate(items)}
        for raw_entry in delta.get("unknowns", []):
            entry = _as_unknown(raw_entry)
            question = entry["question"]
            if not question:
                continue
            if question in by_question:
                idx = by_question[question]
                target = items[idx]
                target["class"] = entry["class"]
                target["status"] = entry["status"]
                target["last_touched"] = now
                items[idx] = touch_item(target, now, via="session_update")
            else:
                item = stamp_origin({
                    "id": _next_id("U", items),
                    "question": question,
                    "class": entry["class"],
                    "status": entry["status"],
                    "created_at": now,
                    "last_touched": now,
                }, "session_update", now, via="writeback")
                by_question[question] = len(items)
                items.append(item)
        unknowns_obj["items"] = items
        updated["OPEN_UNKNOWNS"] = unknowns_obj

    if update_plan.get("ERROR_LOG"):
        error_obj = dict(updated.get("ERROR_LOG", {"errors": []}))
        errors = [ensure_provenance(x, now=now) for x in list(error_obj.get("errors", []))]
        existing = {str(item.get("statement", "")).strip(): idx for idx, item in enumerate(errors)}
        for statement in delta.get("contradictions", []):
            clean = str(statement).strip()
            if not clean:
                continue
            if clean in existing:
                idx = existing[clean]
                current = errors[idx]
                current["last_touched"] = now
                errors[idx] = touch_item(current, now, via="session_update")
                continue
            item = stamp_origin({"id": _next_id("E", errors), "statement": clean, "timestamp": now, "last_touched": now}, "session_update", now, via="writeback")
            existing[clean] = len(errors)
            errors.append(item)
        error_obj["errors"] = errors
        updated["ERROR_LOG"] = error_obj

    if update_plan.get("SALIENCE"):
        salience = dict(updated.get("SALIENCE", {"priority_order": []}))
        order = [str(x).strip() for x in salience.get("priority_order", []) if str(x).strip()]
        integrity = updated.get("INTEGRITY", {}) or {}
        protected_top = [str(x).strip() for x in integrity.get("protected_priority_order", [])[:3] if str(x).strip()]
        tail = [x for x in order if x not in protected_top]
        for item in delta.get("salience_changes", []):
            clean = str(item).strip()
            if not clean or clean in protected_top:
                continue
            if clean in tail:
                tail.remove(clean)
            tail.insert(0, clean)
        salience["priority_order"] = _dedupe_keep_order(protected_top + tail)[:8] if protected_top else _dedupe_keep_order(tail)[:8]
        protected_mnf = [str(x).strip() for x in integrity.get("protected_must_not_forget", []) if str(x).strip()]
        mnf = [str(x).strip() for x in salience.get("must_not_forget", []) if str(x).strip()]
        salience["must_not_forget"] = _dedupe_keep_order(protected_mnf + mnf)[:8] if protected_mnf else _dedupe_keep_order(mnf)[:8]
        salience["last_updated"] = now
        updated["SALIENCE"] = salience

    if update_plan.get("TASK_GRAPH"):
        task_graph = dict(updated.get("TASK_GRAPH", {}))
        active_tasks = [ensure_provenance(x, now=now) for x in list(task_graph.get("active_tasks", [])) if isinstance(x, dict)]
        by_title = {str(task.get("title", "")).strip(): idx for idx, task in enumerate(active_tasks)}
        for raw_entry in delta.get("task_updates", []):
            entry = _as_task(raw_entry)
            title = entry["title"]
            if not title:
                continue
            if title in by_title:
                idx = by_title[title]
                current = active_tasks[idx]
                current["status"] = entry["status"]
                current["last_touched"] = now
                active_tasks[idx] = touch_item(current, now, via="session_update")
            else:
                task = stamp_origin({
                    "id": _next_id("T", active_tasks),
                    "title": title,
                    "status": entry["status"],
                    "output": [],
                    "created_at": now,
                    "last_touched": now,
                }, "session_update", now, via="writeback")
                by_title[title] = len(active_tasks)
                active_tasks.append(task)
        task_graph["active_tasks"] = active_tasks
        updated["TASK_GRAPH"] = task_graph

    return updated
