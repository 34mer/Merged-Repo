from __future__ import annotations

import re
from typing import Any

# Canonical bucket names used throughout the repo.
SECTION_TO_BUCKET = {
    "DECISION": "decisions",
    "DECISIONS": "decisions",
    "HYPOTHESIS": "hypotheses",
    "HYPOTHESES": "hypotheses",
    "UNKNOWN": "unknowns",
    "UNKNOWNS": "unknowns",
    "PRIORITY": "salience_changes",
    "PRIORITIES": "salience_changes",
    "TASK": "task_updates",
    "TASKS": "task_updates",
    "CONTRADICTION": "contradictions",
    "CONTRADICTIONS": "contradictions",
    "NOTE": "notes",
    "NOTES": "notes",
    "CONSTITUTIONAL_REVISION": "constitutional_revisions",
    "CONSTITUTIONAL_REVISIONS": "constitutional_revisions",
    "CONSTITUTIONAL_REVIEW": "constitutional_reviews",
    "CONSTITUTIONAL_REVIEWS": "constitutional_reviews",
    "CONSTITUTIONAL_ROLLBACK": "constitutional_rollbacks",
    "CONSTITUTIONAL_ROLLBACKS": "constitutional_rollbacks",
    "CONSTITUTIONAL_PREVIEW": "constitutional_previews",
    "CONSTITUTIONAL_PREVIEWS": "constitutional_previews",
    "CONSTITUTIONAL_PREVIEW_ROLLBACK": "constitutional_previews",
    "CONSTITUTIONAL_PREVIEW_ROLLBACKS": "constitutional_previews",
    "CONSTITUTIONAL_PLAN": "constitutional_plan_previews",
    "CONSTITUTIONAL_PLANS": "constitutional_plan_previews",
    "CONSTITUTIONAL_PLAN_BRANCH": "constitutional_plan_branches",
    "CONSTITUTIONAL_PLAN_BRANCHES": "constitutional_plan_branches",
    "CONSTITUTIONAL_PLAN_COMPARE": "constitutional_plan_comparisons",
    "CONSTITUTIONAL_PLAN_COMPARES": "constitutional_plan_comparisons",
    "CONSTITUTIONAL_PORTFOLIO": "constitutional_portfolios",
    "CONSTITUTIONAL_PORTFOLIOS": "constitutional_portfolios",
    "CONSTITUTIONAL_SEQUENCE": "constitutional_sequences",
    "CONSTITUTIONAL_SEQUENCES": "constitutional_sequences",
    "CONSTITUTIONAL_REPLAN": "constitutional_replans",
    "CONSTITUTIONAL_REPLANS": "constitutional_replans",
    "WORLD_CONTACT": "world_contact_interventions",
    "WORLD_CONTACTS": "world_contact_interventions",
    "CAUSAL_ACTION_EXECUTE": "causal_action_executes",
    "CAUSAL_ACTION_EXECUTES": "causal_action_executes",
}

INLINE_TAG_RE = re.compile(
    r"^\s*(?:\[(?P<bracket>[A-Z_]+)(?:\((?P<bracket_meta>[^\]]+)\))?\]|(?P<plain>[A-Z_]+)(?:\((?P<plain_meta>[^\)]+)\))?):\s*(?P<body>.+?)\s*$"
)
SECTION_HEADER_RE = re.compile(r"^\s*(?P<header>[A-Z_]+):\s*$")
BULLET_RE = re.compile(r"^\s*(?:[-*]|\d+[.)])\s+(?P<body>.+?)\s*$")
KV_RE = re.compile(r"^(?P<key>[a-zA-Z_]+)\s*=\s*(?P<value>.+)$")
WS_RE = re.compile(r"\s+")

ALLOW_DUPLICATE_BUCKETS = {
    "constitutional_revisions",
    "constitutional_plan_previews",
    "constitutional_plan_branches",
    "constitutional_sequences",
    "constitutional_replans",
}



def _normalize_line(line: str) -> str:
    return WS_RE.sub(" ", line.strip())


def _empty_delta() -> dict[str, list[Any]]:
    return {
        "decisions": [],
        "hypotheses": [],
        "unknowns": [],
        "salience_changes": [],
        "task_updates": [],
        "contradictions": [],
        "notes": [],
        "constitutional_revisions": [],
        "constitutional_reviews": [],
        "constitutional_rollbacks": [],
        "constitutional_previews": [],
        "constitutional_plan_previews": [],
        "constitutional_plan_branches": [],
        "constitutional_plan_comparisons": [],
        "constitutional_portfolios": [],
        "constitutional_sequences": [],
        "constitutional_replans": [],
        "world_contact_interventions": [],
        "causal_action_executes": [],
    }


def _parse_unknown(body: str, meta: str | None = None) -> dict[str, str]:
    item: dict[str, str] = {
        "question": body,
        "class": "engineering",
        "status": "open",
    }
    if meta:
        tokens = [token.strip().lower() for token in re.split(r"[,|]", meta) if token.strip()]
        for token in tokens:
            if token in {"principled", "engineering", "organizational"}:
                item["class"] = token
            elif token in {"open", "working", "resolved"}:
                item["status"] = token
    return item


def _parse_task(body: str, meta: str | None = None) -> dict[str, str]:
    item: dict[str, str] = {
        "title": body,
        "status": "active",
    }
    if meta:
        tokens = [token.strip().lower() for token in re.split(r"[,|]", meta) if token.strip()]
        for token in tokens:
            if token in {"next", "active", "done", "parked", "blocked"}:
                item["status"] = token
    return item


def _parse_constitutional_revision(body: str, meta: str | None = None) -> dict[str, str]:
    item: dict[str, str] = {
        "proposal": body,
        "scope": "general",
        "stance": "revise",
    }
    if meta:
        tokens = [token.strip().lower() for token in re.split(r"[,|]", meta) if token.strip()]
        for token in tokens:
            if token in {"general", "terminal_object", "core_decision", "core_distinction", "methods", "world_model", "constraint_lock"}:
                item["scope"] = token
            elif token in {"revise", "amend", "revoke", "lock"}:
                item["stance"] = token
    return item



def _parse_constitutional_rollback(body: str, meta: str | None = None) -> dict[str, str]:
    item: dict[str, str] = {
        "bundle_id": body,
        "action": "rollback",
    }
    if meta:
        tokens = [token.strip().lower() for token in re.split(r"[,|]", meta) if token.strip()]
        for token in tokens:
            if token in {"rollback", "rollback_locked"}:
                item["action"] = token
    return item





def _parse_constitutional_review(body: str, meta: str | None = None) -> dict[str, str]:
    item: dict[str, str] = {
        "proposal": body,
        "scope": "general",
        "action": "approve",
    }
    if meta:
        tokens = [token.strip().lower() for token in re.split(r"[,|]", meta) if token.strip()]
        for token in tokens:
            if token in {"general", "terminal_object", "core_decision", "core_distinction", "methods", "world_model", "constraint_lock"}:
                item["scope"] = token
            elif token in {"approve", "reject", "approve_locked"}:
                item["action"] = token
    return item







def _parse_constitutional_plan(body: str, meta: str | None = None) -> dict[str, str]:
    item: dict[str, str] = {
        "kind": "review",
        "scope": "general",
        "action": "approve",
        "stance": "revise",
        "proposal": body,
    }
    if meta:
        tokens = [token.strip().lower() for token in re.split(r"[,|]", meta) if token.strip()]
        if tokens:
            head = tokens[0]
            if head in {"review", "rollback", "revise", "revision"}:
                item["kind"] = "revise" if head == "revision" else head
            for token in tokens[1:] if head in {"review", "rollback", "revise", "revision"} else tokens:
                if item.get("kind") == "review":
                    if token in {"general", "terminal_object", "core_decision", "core_distinction", "methods", "world_model", "constraint_lock"}:
                        item["scope"] = token
                    elif token in {"approve", "reject", "approve_locked"}:
                        item["action"] = token
                elif item.get("kind") == "revise":
                    if token in {"general", "terminal_object", "core_decision", "core_distinction", "methods", "world_model", "constraint_lock"}:
                        item["scope"] = token
                    elif token in {"revise", "amend", "revoke", "lock"}:
                        item["stance"] = token
                else:
                    if token in {"rollback", "rollback_locked"}:
                        item["action"] = token
        if item.get("kind") == "rollback":
            item = {
                "kind": "rollback",
                "bundle_id": body,
                "action": item.get("action", "rollback"),
            }
        elif item.get("kind") == "revise":
            item = {
                "kind": "revise",
                "scope": item.get("scope", "general"),
                "stance": item.get("stance", "revise"),
                "proposal": body,
            }
    return item



def _parse_constitutional_plan_branch(body: str, meta: str | None = None) -> dict[str, str]:
    item: dict[str, str] = {
        "plan": "default",
        "kind": "review",
        "scope": "general",
        "action": "approve",
        "stance": "revise",
        "proposal": body,
    }
    if meta:
        tokens = [token.strip().lower() for token in re.split(r"[,|]", meta) if token.strip()]
        if tokens:
            item["plan"] = tokens[0]
            rest = tokens[1:]
            if rest:
                head = rest[0]
                if head in {"review", "rollback", "revise", "revision"}:
                    item["kind"] = "revise" if head == "revision" else head
                    rest = rest[1:]
            for token in rest:
                if item.get("kind") == "review":
                    if token in {"general", "terminal_object", "core_decision", "core_distinction", "methods", "world_model", "constraint_lock"}:
                        item["scope"] = token
                    elif token in {"approve", "reject", "approve_locked"}:
                        item["action"] = token
                elif item.get("kind") == "revise":
                    if token in {"general", "terminal_object", "core_decision", "core_distinction", "methods", "world_model", "constraint_lock"}:
                        item["scope"] = token
                    elif token in {"revise", "amend", "revoke", "lock"}:
                        item["stance"] = token
                else:
                    if token in {"rollback", "rollback_locked"}:
                        item["action"] = token
            if item.get("kind") == "rollback":
                item = {
                    "plan": item.get("plan", "default"),
                    "kind": "rollback",
                    "bundle_id": body,
                    "action": item.get("action", "rollback"),
                }
            elif item.get("kind") == "revise":
                item = {
                    "plan": item.get("plan", "default"),
                    "kind": "revise",
                    "scope": item.get("scope", "general"),
                    "stance": item.get("stance", "revise"),
                    "proposal": body,
                }
    return item


def _parse_constitutional_plan_compare(body: str, meta: str | None = None) -> dict[str, Any]:
    plans = [part.strip() for part in re.split(r"[,|]", body) if part.strip()]
    item: dict[str, Any] = {"plans": plans}
    if meta:
        tokens = [token.strip().lower() for token in re.split(r"[,|]", meta) if token.strip()]
        if tokens:
            item["label"] = tokens[0]
    return item


def _parse_constitutional_portfolio(body: str, meta: str | None = None) -> dict[str, Any]:
    plans = [part.strip() for part in re.split(r"[,|]", body) if part.strip()]
    item: dict[str, Any] = {"plans": plans, "label": "", "comparison": ""}
    if meta:
        tokens = [token.strip() for token in re.split(r"[,|]", meta) if token.strip()]
        for idx, token in enumerate(tokens):
            m = KV_RE.match(token)
            if m:
                key = m.group("key").strip().lower()
                value = m.group("value").strip()
                if key in {"comparison", "comparison_id", "compare"}:
                    item["comparison"] = value
                elif key in {"max_branches"}:
                    item["max_branches"] = value
                elif key in {"max_total_cost", "max_cost", "budget"}:
                    item["max_total_cost"] = value
                elif key in {"max_total_locked_exposure", "max_locked_exposure", "max_locked"}:
                    item["max_total_locked_exposure"] = value
                elif key in {"max_total_rollback_burden", "max_rollback_burden"}:
                    item["max_total_rollback_burden"] = value
                elif key in {"min_branch_value"}:
                    item["min_branch_value"] = value
                elif key in {"min_total_value"}:
                    item["min_total_value"] = value
            elif idx == 0 and not item.get("label"):
                item["label"] = token
    return item


def _parse_constitutional_sequence(body: str, meta: str | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {
        "plans": [part.strip() for part in re.split(r"[,|]", body) if part.strip()],
        "label": "",
        "portfolio": "",
        "comparison": "",
        "strategy": "dependency_first",
        "max_steps": "",
    }
    if meta:
        tokens = [token.strip() for token in re.split(r"[,|]", meta) if token.strip()]
        for idx, token in enumerate(tokens):
            m = KV_RE.match(token)
            if m:
                key = m.group("key").strip().lower()
                value = m.group("value").strip()
                if key in {"portfolio", "portfolio_id"}:
                    item["portfolio"] = value
                elif key in {"comparison", "comparison_id", "compare"}:
                    item["comparison"] = value
                elif key in {"strategy", "order"}:
                    item["strategy"] = value
                elif key in {"max_steps", "limit"}:
                    item["max_steps"] = value
            elif idx == 0 and not item.get("label"):
                item["label"] = token
    return item



def _parse_constitutional_replan(body: str, meta: str | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {
        "label": "",
        "sequence": "",
        "completed": [part.strip() for part in re.split(r"[,|]", body) if part.strip()],
        "invalidated": [],
        "recheck": [],
        "portfolio": "",
        "comparison": "",
        "max_steps": "",
        "reason": "execution_feedback",
    }
    if meta:
        tokens = [token.strip() for token in re.split(r"[,|]", meta) if token.strip()]
        for idx, token in enumerate(tokens):
            m = KV_RE.match(token)
            if m:
                key = m.group("key").strip().lower()
                value = m.group("value").strip()
                if key in {"label"}:
                    item["label"] = value
                elif key in {"sequence", "sequence_id"}:
                    item["sequence"] = value
                elif key in {"portfolio", "portfolio_id"}:
                    item["portfolio"] = value
                elif key in {"comparison", "comparison_id", "compare"}:
                    item["comparison"] = value
                elif key in {"max_steps", "limit"}:
                    item["max_steps"] = value
                elif key in {"reason", "feedback"}:
                    item["reason"] = value
                elif key in {"completed", "done", "executed"}:
                    item["completed"] = [part.strip() for part in re.split(r"[;|,]", value) if part.strip()]
                elif key in {"invalidated", "blocked"}:
                    item["invalidated"] = [part.strip() for part in re.split(r"[;|,]", value) if part.strip()]
                elif key in {"recheck", "delay"}:
                    item["recheck"] = [part.strip() for part in re.split(r"[;|,]", value) if part.strip()]
            elif idx == 0 and not item.get("label"):
                item["label"] = token
    return item


def _parse_world_contact(body: str, meta: str | None = None) -> dict[str, str]:
    item: dict[str, str] = {
        "adapter": "filesystem",
        "target_ref": "world_contact_fixture/target.json",
        "intent": "append_fact",
        "expected_effect": body,
        "actual_effect": "",
        "world_model_note": f"Observed external effect: {body}",
        "salience_priority": "Prioritize confirmed world-contact updates over proposal-only world-model shifts.",
        "task_title": f"Review confirmed external effect: {body}",
    }
    if meta:
        tokens = [token.strip() for token in re.split(r"[,|]", meta) if token.strip()]
        for token in tokens:
            m = KV_RE.match(token)
            if m:
                key = m.group("key").strip().lower()
                value = m.group("value").strip()
                if key in {"adapter"}:
                    item["adapter"] = value.lower()
                elif key in {"target", "target_ref"}:
                    item["target_ref"] = value
                elif key in {"intent"}:
                    item["intent"] = value.lower()
                elif key in {"actual_effect", "observed_effect", "actual", "observed"}:
                    item["actual_effect"] = value
                elif key in {"world_model", "world_model_note"}:
                    item["world_model_note"] = value
                elif key in {"salience", "salience_priority"}:
                    item["salience_priority"] = value
                elif key in {"task", "task_title"}:
                    item["task_title"] = value
            else:
                low = token.lower()
                if low == "filesystem":
                    item["adapter"] = low
    return item


def _parse_causal_action_execute(body: str, meta: str | None = None) -> dict[str, str]:
    item: dict[str, str] = {
        "action_id": "",
        "selection": body.strip() or "execute",
    }
    if meta:
        tokens = [token.strip() for token in re.split(r"[,|]", meta) if token.strip()]
        for token in tokens:
            m = KV_RE.match(token)
            if not m:
                continue
            key = m.group("key").strip().lower()
            value = m.group("value").strip()
            if key in {"action_id", "id"}:
                item["action_id"] = value
            elif key in {"target", "target_ref"}:
                item["target_ref"] = value
    return item

def _parse_constitutional_preview(body: str, meta: str | None = None, tag: str | None = None) -> dict[str, str]:
    item: dict[str, str] = {
        "kind": "review",
        "proposal": body,
        "scope": "general",
        "action": "approve",
    }
    if str(tag or '').upper() in {"CONSTITUTIONAL_PREVIEW_ROLLBACK", "CONSTITUTIONAL_PREVIEW_ROLLBACKS"}:
        item = {
            "kind": "rollback",
            "bundle_id": body,
            "action": "rollback",
        }
    if meta:
        tokens = [token.strip().lower() for token in re.split(r"[,|]", meta) if token.strip()]
        for token in tokens:
            if item.get("kind") == "review":
                if token in {"general", "terminal_object", "core_decision", "core_distinction", "methods", "world_model", "constraint_lock"}:
                    item["scope"] = token
                elif token in {"approve", "reject", "approve_locked"}:
                    item["action"] = token
            else:
                if token in {"rollback", "rollback_locked"}:
                    item["action"] = token
    return item

def _parse_entry(bucket: str, body: str, meta: str | None = None, tag: str | None = None) -> Any:
    if bucket == "unknowns":
        return _parse_unknown(body, meta)
    if bucket == "task_updates":
        return _parse_task(body, meta)
    if bucket == "constitutional_revisions":
        return _parse_constitutional_revision(body, meta)
    if bucket == "constitutional_reviews":
        return _parse_constitutional_review(body, meta)
    if bucket == "constitutional_rollbacks":
        return _parse_constitutional_rollback(body, meta)
    if bucket == "constitutional_previews":
        return _parse_constitutional_preview(body, meta, tag=tag)
    if bucket == "constitutional_plan_previews":
        return _parse_constitutional_plan(body, meta)
    if bucket == "constitutional_plan_branches":
        return _parse_constitutional_plan_branch(body, meta)
    if bucket == "constitutional_plan_comparisons":
        return _parse_constitutional_plan_compare(body, meta)
    if bucket == "constitutional_portfolios":
        return _parse_constitutional_portfolio(body, meta)
    if bucket == "constitutional_sequences":
        return _parse_constitutional_sequence(body, meta)
    if bucket == "constitutional_replans":
        return _parse_constitutional_replan(body, meta)
    if bucket == "world_contact_interventions":
        return _parse_world_contact(body, meta)
    if bucket == "causal_action_executes":
        return _parse_causal_action_execute(body, meta)
    return body


def _append_entry(delta: dict[str, list[Any]], bucket: str, entry: Any) -> None:
    if bucket not in delta:
        return
    if bucket not in ALLOW_DUPLICATE_BUCKETS and entry in delta[bucket]:
        return
    delta[bucket].append(entry)


def extract_state_delta(raw_text: str) -> dict[str, list[Any]]:
    """
    Conservative but more expressive extractor for v0.

    Supported forms:
      DECISION: ...
      [DECISION]: ...
      UNKNOWN(principled,working): ...
      TASK(done): ...

    Also supports plural block sections:
      DECISIONS:
      - ...
      - ...

      TASKS:
      - active :: tighten extractor
      - done :: instantiate repo

    Free text remains ignored unless explicitly tagged or placed under a tagged block.
    """
    delta = _empty_delta()
    current_block_bucket: str | None = None
    current_block_meta: str | None = None

    for raw_line in raw_text.splitlines():
        line = _normalize_line(raw_line)
        if not line:
            current_block_bucket = None
            current_block_meta = None
            continue

        inline_match = INLINE_TAG_RE.match(line)
        if inline_match:
            tag = inline_match.group("bracket") or inline_match.group("plain") or ""
            meta = inline_match.group("bracket_meta") or inline_match.group("plain_meta")
            body = inline_match.group("body").strip()
            bucket = SECTION_TO_BUCKET.get(tag.upper())
            if bucket:
                entry = _parse_entry(bucket, body, meta, tag)
                _append_entry(delta, bucket, entry)
                current_block_bucket = None
                current_block_meta = None
                continue

        section_match = SECTION_HEADER_RE.match(line)
        if section_match:
            header = section_match.group("header").upper()
            bucket = SECTION_TO_BUCKET.get(header)
            if bucket:
                current_block_bucket = bucket
                current_block_meta = None
                continue

        bullet_match = BULLET_RE.match(line)
        if bullet_match and current_block_bucket:
            body = bullet_match.group("body").strip()
            meta = current_block_meta

            # Optional inline metadata inside bullets.
            # Examples:
            #   active :: tighten extractor
            #   principled|working :: what is constitutive burden?
            if "::" in body and current_block_bucket in {"unknowns", "task_updates"}:
                left, right = [part.strip() for part in body.split("::", 1)]
                if KV_RE.match(left):
                    # Allow future structured kv prefixes without acting on them yet.
                    pass
                else:
                    meta = left
                    body = right

            entry = _parse_entry(current_block_bucket, body, meta, tag=current_block_bucket)
            _append_entry(delta, current_block_bucket, entry)
            continue

        # Free text does not mutate state in v0.

    return delta


def summarize_delta(delta: dict[str, list[Any]]) -> dict[str, int]:
    return {key: len(values) for key, values in delta.items()}
