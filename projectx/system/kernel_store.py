
from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import load_json, load_text, save_json, save_text

JSON_MAP = {
    "STATE": "state.json",
    "DECISIONS": "decisions.json",
    "SALIENCE": "salience.json",
    "OPEN_UNKNOWNS": "unknowns.json",
    "ERROR_LOG": "error_log.json",
    "TASK_GRAPH": "task_graph.json",
    "INTEGRITY": "integrity.json",
    "ANCHOR": "anchor.json",
    "RESILIENCE": "resilience.json",
    "PROVENANCE": "provenance.json",
    "CONSTRAINT_LOCK": "constraint_lock.json",
    "CONSTRAINT_AUDIT": "constraint_audit.json",
    "BEHAVIOR_AUDIT": "behavior_audit.json",
    "META_CONFLICT": "meta_conflict.json",
    "CONSTITUTIONAL_REVISION": "constitutional_revision.json",
    "CONSTITUTIONAL_REVIEW": "constitutional_review.json",
    "CONSTITUTIONAL_WORLD_MODEL_REVIEW": "constitutional_world_model_review.json",
    "CONSTITUTIONAL_EVIDENCE": "constitutional_evidence.json",
    "CONSTITUTIONAL_ROLLBACK": "constitutional_rollback.json",
    "CONSTITUTIONAL_PREVIEW": "constitutional_preview.json",
    "CONSTITUTIONAL_PLAN_PREVIEW": "constitutional_plan_preview.json",
    "CONSTITUTIONAL_PLAN_COMPARE": "constitutional_plan_compare.json",
    "CONSTITUTIONAL_PLAN_SCORE": "constitutional_plan_score.json",
    "CONSTITUTIONAL_PORTFOLIO": "constitutional_portfolio.json",
    "CONSTITUTIONAL_SEQUENCE": "constitutional_sequence.json",
    "CONSTITUTIONAL_REPLAN": "constitutional_replan.json",
    "CONSTITUTIONAL_WORLD_CONTACT_INTERVENTION": "constitutional_world_contact_intervention.json",
    "CONSTITUTIONAL_WORLD_CONTACT_OBSERVATION": "constitutional_world_contact_observation.json",
    "CONSTITUTIONAL_WORLD_CONTACT_ATTRIBUTION": "constitutional_world_contact_attribution.json",
    "CONSTITUTIONAL_WORLD_CONTACT_UPDATE": "constitutional_world_contact_update.json",
    "CONSTITUTIONAL_CAUSAL_WORLD_BELIEF": "constitutional_causal_world_belief.json",
    "CONSTITUTIONAL_CAUSAL_DEPENDENCY_VALIDATION": "constitutional_causal_dependency_validation.json",
    "CONSTITUTIONAL_CAUSAL_DEPENDENCY": "constitutional_causal_dependency.json",
    "CONSTITUTIONAL_CAUSAL_DEPENDENCY_IMPACT": "constitutional_causal_dependency_impact.json",
    "CONSTITUTIONAL_CAUSAL_SALIENCE": "constitutional_causal_salience.json",
    "CONSTITUTIONAL_CAUSAL_METHOD_CHOICE": "constitutional_causal_method_choice.json",
    "CONSTITUTIONAL_CAUSAL_ACTION": "constitutional_causal_action.json",
    "CONSTITUTIONAL_CAUSAL_VALUATION": "constitutional_causal_valuation.json",
    "CONSTITUTIONAL_CAUSAL_ARBITRATION": "constitutional_causal_arbitration.json",
    "CONSTITUTIONAL_CAUSAL_COMMITMENT": "constitutional_causal_commitment.json",
    "CONSTITUTIONAL_CAUSAL_ACTION_EXECUTION": "constitutional_causal_action_execution.json",
    "CONSTITUTIONAL_CAUSAL_OUTCOME_EVALUATION": "constitutional_causal_outcome_evaluation.json",
    "CONSTITUTIONAL_EXECUTION_COUPLING": "constitutional_execution_coupling.json",
    "CONSTITUTIONAL_EXECUTION_CONTROL": "constitutional_execution_control.json",
    "CONSTITUTIONAL_EXECUTION_POLICY": "constitutional_execution_policy.json",
    "CONSTITUTIONAL_EXECUTION_LONGITUDINAL": "constitutional_execution_longitudinal.json",
    "CONSTITUTIONAL_EXECUTION_GENEALOGY": "constitutional_execution_genealogy.json",
    "CONSTITUTIONAL_EXECUTION_SURGERY": "constitutional_execution_surgery.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY": "constitutional_execution_recovery.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_FAMILY_BIRTH": "constitutional_execution_recovery_family_birth.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_EXECUTION": "constitutional_execution_recovery_execution.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_FEEDBACK": "constitutional_execution_recovery_feedback.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_LIFECYCLE": "constitutional_execution_recovery_lifecycle.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_LONGITUDINAL": "constitutional_execution_recovery_longitudinal.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_GENEALOGY": "constitutional_execution_recovery_genealogy.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_SURGERY": "constitutional_execution_recovery_surgery.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_SURGERY_EXECUTION": "constitutional_execution_recovery_surgery_execution.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_SURGERY_FEEDBACK": "constitutional_execution_recovery_surgery_feedback.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_SURGERY_LIFECYCLE": "constitutional_execution_recovery_surgery_lifecycle.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_SURGERY_LONGITUDINAL": "constitutional_execution_recovery_surgery_longitudinal.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_SURGERY_GENEALOGY": "constitutional_execution_recovery_surgery_genealogy.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_SURGERY_LINEAGE_SURGERY": "constitutional_execution_recovery_surgery_lineage_surgery.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_SURGERY_LINEAGE_SURGERY_EXECUTION": "constitutional_execution_recovery_surgery_lineage_surgery_execution.json",
    "CONSTITUTIONAL_EXECUTION_RECOVERY_SURGERY_LINEAGE_SURGERY_FEEDBACK": "constitutional_execution_recovery_surgery_lineage_surgery_feedback.json",
}

TEXT_MAP = {
    "INVARIANT": "INVARIANT.md",
    "WORLD_MODEL": "WORLD_MODEL.md",
    "METHODS_ALLOWED": "METHODS_ALLOWED.md",
    "METHODS_REJECTED": "METHODS_REJECTED.md",
    "EVAL_CRITERIA": "EVAL_CRITERIA.md",
    "RESOURCE_MAP": "RESOURCE_MAP.md",
    "PEOPLE_MAP": "PEOPLE_MAP.md",
    "SESSION_PROTOCOL": "SESSION_PROTOCOL.md",
}


def load_kernel(kernel_dir: Path) -> dict[str, Any]:
    state: dict[str, Any] = {}
    for key, filename in JSON_MAP.items():
        state[key] = load_json(kernel_dir / filename)
    for key, filename in TEXT_MAP.items():
        state[key] = load_text(kernel_dir / filename)
    return state


def save_kernel(kernel_dir: Path, kernel_state: dict[str, Any]) -> None:
    for key, filename in JSON_MAP.items():
        if key in kernel_state:
            save_json(kernel_dir / filename, kernel_state[key])
    for key, filename in TEXT_MAP.items():
        if key in kernel_state:
            save_text(kernel_dir / filename, str(kernel_state[key] or ''))
