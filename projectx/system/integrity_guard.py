from __future__ import annotations

from copy import deepcopy
from typing import Any

from .utils import utc_now_iso
from .regenerator import regenerate_protection, protection_is_trustworthy
from .provenance import normalize_kernel_provenance, choose_stronger, item_trust, stamp_origin


CONFLICT_TOKENS = {
    'cosmetic', 'polish', 'unrelated', 'general usability', 'interface polish',
    'product usability', 'cleanup backlog', 'docs cosmetically', 'cosmetic cleanup'
}


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


def _restore_by_key(existing: list[dict[str, Any]], protected: list[dict[str, Any]], key: str, restore_origin: str = "anchor_restore", now: str | None = None) -> tuple[list[dict[str, Any]], int]:
    index = {str(item.get(key, '')).strip(): i for i, item in enumerate(existing) if str(item.get(key, '')).strip()}
    restored = 0
    merged = list(existing)
    for item in protected:
        target = str(item.get(key, '')).strip()
        if not target:
            continue
        candidate = stamp_origin(item, restore_origin, now or utc_now_iso(), via="integrity_guard")
        if target in index:
            i = index[target]
            stronger = choose_stronger(merged[i], candidate)
            if stronger != merged[i]:
                merged[i] = stronger
                restored += 1
        else:
            index[target] = len(merged)
            merged.append(candidate)
            restored += 1
    return merged, restored


def _enforce_priority_band(order: list[str], protected_top: list[str], max_len: int = 8) -> list[str]:
    tail = [str(x).strip() for x in order if str(x).strip() and str(x).strip() not in protected_top]
    return _dedupe_keep_order(list(protected_top) + tail)[:max_len]


def _conflict_phrase(s: str) -> bool:
    raw = str(s).strip().lower()
    return any(tok in raw for tok in CONFLICT_TOKENS)


def _anchor_from_state(kernel_state: dict[str, Any]) -> dict[str, Any]:
    return deepcopy(kernel_state.get('ANCHOR') or kernel_state.get('INTEGRITY') or {})


def _resilience_from_state(kernel_state: dict[str, Any]) -> dict[str, Any]:
    return deepcopy(kernel_state.get('RESILIENCE') or {})


def _blocked_exact_set(resilience: dict[str, Any], key: str) -> set[str]:
    return {str(x).strip().lower() for x in resilience.get(key, []) if str(x).strip()}


def _repair_integrity_from_anchor(state: dict[str, Any], anchor: dict[str, Any], now: str) -> tuple[list[str], bool]:
    actions: list[str] = []
    repaired = False
    integrity = deepcopy(state.get('INTEGRITY') or {})
    if not anchor:
        return actions, repaired

    protected_keys = [
        'protected_objective', 'protected_phase', 'root_objective', 'protected_priority_order',
        'protected_must_not_forget', 'minimum_counts', 'protected_decisions',
        'protected_unknowns', 'protected_tasks'
    ]
    for key in protected_keys:
        if integrity.get(key) != anchor.get(key):
            integrity[key] = deepcopy(anchor.get(key))
            repaired = True
    if repaired:
        integrity['last_reanchored'] = now
        state['INTEGRITY'] = integrity
        actions.append('integrity_reanchored_from_anchor')
    return actions, repaired


def _clean_conflicting_salience(
    salience: dict[str, Any],
    protected_top: list[str],
    protected_mnf: list[str],
    resilience: dict[str, Any],
) -> tuple[dict[str, Any], list[str]]:
    actions: list[str] = []
    order = [str(x).strip() for x in salience.get('priority_order', []) if str(x).strip()]
    mnf = [str(x).strip() for x in salience.get('must_not_forget', []) if str(x).strip()]
    blocked_order = _blocked_exact_set(resilience, 'blocked_priority_order')
    blocked_mnf = _blocked_exact_set(resilience, 'blocked_must_not_forget')

    def allow_order(x: str) -> bool:
        low = x.strip().lower()
        return low not in blocked_order and not _conflict_phrase(x)

    def allow_mnf(x: str) -> bool:
        low = x.strip().lower()
        return low not in blocked_mnf and not _conflict_phrase(x)

    filtered_order = [x for x in order if allow_order(x)]
    filtered_mnf = [x for x in mnf if allow_mnf(x)]
    if len(filtered_order) != len(order) or len(filtered_mnf) != len(mnf):
        actions.append('recurrent_pressure_quarantined')
    salience['priority_order'] = _dedupe_keep_order(protected_top + filtered_order)[:8]
    salience['must_not_forget'] = _dedupe_keep_order(protected_mnf + filtered_mnf)[:8]
    return salience, actions


def _dedupe_tasks(tasks: list[dict[str, Any]], resilience: dict[str, Any]) -> tuple[list[dict[str, Any]], int]:
    out: list[dict[str, Any]] = []
    best_index: dict[str, int] = {}
    removed = 0
    blocked_titles = _blocked_exact_set(resilience, 'blocked_task_titles')
    for task in tasks:
        title = str(task.get('title', '')).strip()
        if not title:
            continue
        key = title.lower()
        if key in blocked_titles or _conflict_phrase(title):
            removed += 1
            continue
        if key in best_index:
            idx = best_index[key]
            stronger = choose_stronger(out[idx], task)
            if stronger != out[idx]:
                out[idx] = stronger
            removed += 1
            continue
        best_index[key] = len(out)
        out.append(task)
    return out, removed


def preflight_reanchor(kernel_state: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    state = normalize_kernel_provenance(deepcopy(kernel_state), utc_now_iso())
    actions: list[str] = []
    alerts: list[str] = []
    repaired_keys: list[str] = []
    restored_counts: dict[str, int] = {}
    now = utc_now_iso()

    if not protection_is_trustworthy(state):
        state, regen_actions = regenerate_protection(state)
        actions.extend(regen_actions)
        alerts.extend(regen_actions)
        repaired_keys.extend(['ANCHOR', 'INTEGRITY'])

    anchor = _anchor_from_state(state)
    resilience = _resilience_from_state(state)
    integrity_actions, integrity_repaired = _repair_integrity_from_anchor(state, anchor, now)
    if integrity_actions:
        actions.extend(integrity_actions)
        alerts.extend(integrity_actions)
        repaired_keys.append('INTEGRITY')

    integrity = state.get('INTEGRITY') or anchor
    if not integrity:
        return state, {
            'pre_run_alerts': alerts,
            'pre_run_actions': actions,
            'repaired_state_keys': sorted(set(repaired_keys)),
            'restored_counts': restored_counts,
        }

    protected_objective = str(integrity.get('protected_objective', '')).strip()
    current_objective = str(state.get('STATE', {}).get('current_objective', '')).strip()
    if protected_objective and current_objective != protected_objective:
        state.setdefault('STATE', {})['current_objective'] = protected_objective
        state['STATE']['last_updated'] = now
        actions.append('objective_reanchored')
        repaired_keys.append('STATE')
        alerts.append('objective_reanchored')

    protected_phase = str(integrity.get('protected_phase', '')).strip()
    if protected_phase and str(state.get('STATE', {}).get('phase', '')).strip() != protected_phase:
        state.setdefault('STATE', {})['phase'] = protected_phase
        state['STATE']['last_updated'] = now
        actions.append('phase_reanchored')
        repaired_keys.append('STATE')

    root_objective = str(integrity.get('root_objective', '')).strip()
    if root_objective and str(state.get('TASK_GRAPH', {}).get('root_objective', '')).strip() != root_objective:
        state.setdefault('TASK_GRAPH', {})['root_objective'] = root_objective
        actions.append('root_objective_reanchored')
        repaired_keys.append('TASK_GRAPH')

    salience = deepcopy(state.get('SALIENCE', {}) or {})
    protected_order = list(integrity.get('protected_priority_order', []))
    protected_top = [str(x).strip() for x in protected_order[:3] if str(x).strip()]
    protected_mnf = [str(x).strip() for x in integrity.get('protected_must_not_forget', []) if str(x).strip()]
    salience, salience_actions = _clean_conflicting_salience(salience, protected_top, protected_mnf, resilience)
    if salience_actions:
        actions.extend(salience_actions)
        repaired_keys.append('SALIENCE')
        if 'recurrent_pressure_quarantined' not in alerts:
            alerts.append('recurrent_pressure_quarantined')

    current_top = [str(x).strip() for x in salience.get('priority_order', [])[:3] if str(x).strip()]
    exact_top = current_top == protected_top[:len(current_top)] if protected_top else True
    overlap = len(set(current_top) & set(protected_top)) if protected_top else 1
    required_overlap = len(protected_top) if protected_top else 1
    if protected_top and (overlap < required_overlap or not exact_top):
        salience['priority_order'] = _enforce_priority_band(list(salience.get('priority_order', [])), protected_top, 8)
        actions.append('salience_reanchored')
        repaired_keys.append('SALIENCE')
        if 'salience_reanchored' not in alerts:
            alerts.append('salience_reanchored')
    salience['must_not_forget'] = _dedupe_keep_order(protected_mnf + list(salience.get('must_not_forget', [])))[:8]
    salience['last_updated'] = now
    state['SALIENCE'] = salience

    minimums = integrity.get('minimum_counts', {}) or {}
    restored_any = False

    decisions_obj = deepcopy(state.get('DECISIONS', {}) or {'decisions': []})
    decisions = list(decisions_obj.get('decisions', []))
    protected_decisions = list(integrity.get('protected_decisions', []))
    decisions, backbone_restored = _restore_by_key(decisions, protected_decisions, 'statement', restore_origin='anchor_restore', now=now)
    if backbone_restored:
        decisions_obj['decisions'] = decisions
        state['DECISIONS'] = decisions_obj
        actions.append('decision_backbone_restored')
        repaired_keys.append('DECISIONS')
        restored_counts['decisions'] = backbone_restored
        restored_any = True
    elif len(decisions) < int(minimums.get('decisions', 0)):
        decisions, restored = _restore_by_key(decisions, protected_decisions, 'statement', restore_origin='anchor_restore', now=now)
        if restored:
            decisions_obj['decisions'] = decisions
            state['DECISIONS'] = decisions_obj
            actions.append('decisions_restored')
            repaired_keys.append('DECISIONS')
            restored_counts['decisions'] = restored
            restored_any = True

    unknowns_obj = deepcopy(state.get('OPEN_UNKNOWNS', {}) or {'items': []})
    unknowns = list(unknowns_obj.get('items', []))
    protected_unknowns = list(integrity.get('protected_unknowns', []))
    unknowns, backbone_unknowns = _restore_by_key(unknowns, protected_unknowns, 'question', restore_origin='anchor_restore', now=now)
    if backbone_unknowns:
        unknowns_obj['items'] = unknowns
        state['OPEN_UNKNOWNS'] = unknowns_obj
        actions.append('unknown_backbone_restored')
        repaired_keys.append('OPEN_UNKNOWNS')
        restored_counts['unknowns'] = backbone_unknowns
        restored_any = True
    elif len(unknowns) < int(minimums.get('unknowns', 0)):
        unknowns, restored = _restore_by_key(unknowns, protected_unknowns, 'question', restore_origin='anchor_restore', now=now)
        if restored:
            unknowns_obj['items'] = unknowns
            state['OPEN_UNKNOWNS'] = unknowns_obj
            actions.append('unknowns_restored')
            repaired_keys.append('OPEN_UNKNOWNS')
            restored_counts['unknowns'] = restored
            restored_any = True

    task_graph = deepcopy(state.get('TASK_GRAPH', {}) or {'active_tasks': []})
    tasks = list(task_graph.get('active_tasks', []))
    tasks, removed = _dedupe_tasks(tasks, resilience)
    if removed:
        task_graph['active_tasks'] = tasks
        actions.append('conflicting_or_duplicate_tasks_removed')
        repaired_keys.append('TASK_GRAPH')
        restored_counts['task_conflicts_removed'] = removed
        if 'recurrent_pressure_quarantined' not in alerts:
            alerts.append('recurrent_pressure_quarantined')
    protected_tasks = list(integrity.get('protected_tasks', []))
    tasks, backbone_tasks = _restore_by_key(tasks, protected_tasks, 'title', restore_origin='anchor_restore', now=now)
    if backbone_tasks:
        task_graph['active_tasks'] = tasks
        actions.append('task_backbone_restored')
        repaired_keys.append('TASK_GRAPH')
        restored_counts['tasks'] = backbone_tasks
        restored_any = True
    elif len(tasks) < int(minimums.get('tasks', 0)):
        tasks, restored = _restore_by_key(tasks, protected_tasks, 'title', restore_origin='anchor_restore', now=now)
        if restored:
            task_graph['active_tasks'] = tasks
            actions.append('tasks_restored')
            repaired_keys.append('TASK_GRAPH')
            restored_counts['tasks'] = restored
            restored_any = True

    protected_titles = [str(t.get('title', '')).strip() for t in integrity.get('protected_tasks', []) if str(t.get('title', '')).strip()]
    if protected_titles:
        current_titles = {str(t.get('title', '')).strip() for t in task_graph.get('active_tasks', []) if isinstance(t, dict)}
        preferred = protected_titles[0]
        if preferred and preferred not in current_titles:
            task_graph.setdefault('active_tasks', []).insert(0, stamp_origin({'id': 'T-PROTECTED', 'title': preferred, 'status': 'active', 'output': [], 'created_at': now, 'last_touched': now}, 'anchor_restore', now, via='integrity_guard'))
            actions.append('protected_task_restored')
            repaired_keys.append('TASK_GRAPH')
            restored_any = True
    state['TASK_GRAPH'] = task_graph

    if restored_any and 'critical_state_restored' not in alerts:
        alerts.append('critical_state_restored')

    return state, {
        'pre_run_alerts': alerts,
        'pre_run_actions': actions,
        'repaired_state_keys': sorted(set(repaired_keys)),
        'restored_counts': restored_counts,
    }
