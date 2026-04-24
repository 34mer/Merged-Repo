from __future__ import annotations

from typing import Any


BASE_REQUIRED = {"INVARIANT", "STATE", "TASK_GRAPH", "SALIENCE"}


def _clamp(x: float) -> float:
    return max(0.0, min(1.0, x))


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


def _retrieval_coverage(session_data: dict[str, Any]) -> float:
    required = _required_retrieval_keys(session_data)
    retrieved = set(session_data.get("retrieval_keys", []))
    if not required:
        return 1.0
    return len(required & retrieved) / len(required)


def compute_rbr(session_data: dict[str, Any]) -> float:
    """
    Reconstitution Burden Reduction.

    Interpreted for v0 as: how completely did the kernel auto-reload the state
    needed for this cycle, without the user having to restate a large amount of
    structured project state?
    """
    coverage = _retrieval_coverage(session_data)
    explicit_state_cues = int(session_data.get("explicit_state_cues", 0))
    retrieved = session_data.get("retrieval_keys", [])
    required = _required_retrieval_keys(session_data)

    # More explicit state cues generally means the user is still carrying more
    # reconstitution burden manually.
    manual_repair_pressure = min(1.0, explicit_state_cues / 8.0)
    retrieval_excess = max(0, len(retrieved) - len(required))
    excess_penalty = min(0.20, retrieval_excess * 0.04)

    score = 0.70 * coverage + 0.30 * (1.0 - manual_repair_pressure) - excess_penalty
    return _clamp(score)


def compute_mlli(session_data: dict[str, Any]) -> float:
    """
    Memory Loop Load-Bearing Index.

    Credit retrieval only when it was actually needed by the current delta and
    the session produced durable writeback.
    """
    delta = session_data.get("delta", {})
    retrieved = set(session_data.get("retrieval_keys", []))
    links: list[bool] = []

    # Base continuity links.
    links.append("INVARIANT" in retrieved)
    links.append("STATE" in retrieved)
    links.append("TASK_GRAPH" in retrieved)
    links.append("SALIENCE" in retrieved)

    # Conditional links tied to actual state mutation.
    if delta.get("unknowns"):
        links.append("OPEN_UNKNOWNS" in retrieved)
    if delta.get("decisions"):
        links.append("DECISIONS" in retrieved)
    if delta.get("contradictions"):
        links.append("ERROR_LOG" in retrieved)
        links.append("DECISIONS" in retrieved)

    if not links:
        return 0.0

    linkage_score = sum(1 for x in links if x) / len(links)
    writeback_bonus = 0.10 if session_data.get("writeback_complete") else 0.0
    state_change_bonus = 0.10 if session_data.get("state_changed_keys") else 0.0
    return _clamp(linkage_score * 0.80 + writeback_bonus + state_change_bonus)


def compute_scs(session_data: dict[str, Any]) -> float:
    """
    Session Continuity Score.

    High when the kernel supplies required state, the session writes back, and
    no major drift/reset signatures are observed.
    """
    coverage = _retrieval_coverage(session_data)
    writeback = 1.0 if session_data.get("writeback_complete") else 0.0
    drift_events = session_data.get("drift_events", [])
    drift_penalty = min(1.0, len(drift_events) / 4.0)
    explicit_state_cues = int(session_data.get("explicit_state_cues", 0))
    manual_penalty = min(0.35, explicit_state_cues * 0.04)

    score = 0.50 * coverage + 0.35 * writeback + 0.15 * (1.0 - drift_penalty) - manual_penalty
    return _clamp(score)


def compute_drift_rate(session_data: dict[str, Any]) -> float:
    """
    Higher is worse. Uses actual run-to-run state comparison rather than only
    session-local contradiction count.
    """
    drift_events = session_data.get("drift_events", [])
    contradictions = len(session_data.get("delta", {}).get("contradictions", []))
    state_reset = 1 if "active_tasks_reset" in drift_events else 0
    invariant_shift = 1 if "invariant_changed" in drift_events else 0

    severity = len(drift_events) + contradictions + 2 * state_reset + 2 * invariant_shift
    return _clamp(severity / 6.0)


def compute_cps(session_data: dict[str, Any]) -> float:
    """
    Coherence Preservation Score.

    High when the system behaves like one regime: enough state is loaded,
    retrieval is selective, writeback lands, and coherence failures stay low.
    """
    coverage = _retrieval_coverage(session_data)
    failures = set(session_data.get("failures", []))

    penalty = 0.0
    if "retrieval_spam" in failures:
        penalty += 0.15
    if "user_monopoly" in failures:
        penalty += 0.25
    if "false_continuity" in failures:
        penalty += 0.25
    if "transcript_dependence_risk" in failures:
        penalty += 0.10
    if "no_writeback" in failures:
        penalty += 0.30

    score = 0.85 * coverage + 0.15 * (1.0 if session_data.get("writeback_complete") else 0.0) - penalty
    return _clamp(score)
