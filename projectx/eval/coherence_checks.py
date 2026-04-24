from __future__ import annotations

from typing import Any


BASE_REQUIRED = {"INVARIANT", "STATE", "TASK_GRAPH", "SALIENCE"}


def _required_retrieval_keys(session_data: dict[str, Any]) -> set[str]:
    delta = session_data.get("delta", {})
    required = set(BASE_REQUIRED)
    if delta.get("unknowns"):
        required.add("OPEN_UNKNOWNS")
    if delta.get("decisions"):
        required.add("DECISIONS")
    if delta.get("contradictions"):
        required.update({"DECISIONS", "ERROR_LOG"})
    return required


def detect_failure_signatures(session_data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    retrieval_keys = set(session_data.get("retrieval_keys", []))
    required = _required_retrieval_keys(session_data)
    delta = session_data.get("delta", {})
    raw_text_length = int(session_data.get("raw_text_length", 0))
    explicit_state_cues = int(session_data.get("explicit_state_cues", 0))
    state_changed_keys = set(session_data.get("state_changed_keys", []))
    drift_events = set(session_data.get("drift_events", []))
    pre_run_alerts = set(session_data.get('pre_run_alerts', []))
    pre_run_actions = set(session_data.get('pre_run_actions', []))

    missing_required = required - retrieval_keys
    retrieval_excess = max(0, len(retrieval_keys) - len(required))

    if retrieval_excess >= 3 or session_data.get("context_length", 0) > 8000:
        failures.append("retrieval_spam")

    decisive_mutation = any(delta.get(k) for k in ["decisions", "unknowns", "salience_changes", "task_updates", "contradictions"])
    if retrieval_keys and not decisive_mutation and not state_changed_keys:
        failures.append("archive_trap")

    if not session_data.get("writeback_complete"):
        failures.append("no_writeback")

    if missing_required:
        failures.append("user_monopoly")

    if decisive_mutation and not state_changed_keys:
        failures.append("false_continuity")

    if raw_text_length > 2000 and explicit_state_cues <= 1:
        failures.append("transcript_dependence_risk")

    if "active_tasks_reset" in drift_events or "unknowns_lost" in drift_events or "decisions_lost" in drift_events:
        failures.append("state_reset_risk")

    if 'integrity_reanchored_from_anchor' not in pre_run_alerts and 'integrity_reanchored_from_anchor' not in pre_run_actions and 'integrity_poison_detected' in pre_run_alerts:
        failures.append('integrity_anchor_failure')

    branch_removed = 'conflicting_or_duplicate_tasks_removed' in pre_run_alerts or 'conflicting_or_duplicate_tasks_removed' in pre_run_actions or 'recurrent_pressure_quarantined' in pre_run_alerts
    unresolved_branch_signals = 'active_tasks_reset' in drift_events or missing_required or 'false_continuity' in failures
    if branch_removed and unresolved_branch_signals:
        failures.append('branch_pressure_risk')

    return failures
