from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .provenance import item_trust


def _parse_iso(raw: str) -> datetime:
    if not raw:
        return datetime(1970, 1, 1, tzinfo=timezone.utc)
    try:
        dt = datetime.fromisoformat(raw.replace('Z', '+00:00'))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError:
        return datetime(1970, 1, 1, tzinfo=timezone.utc)


def _hours_since(raw: str, now: datetime) -> float:
    dt = _parse_iso(raw)
    return max(0.0, (now - dt).total_seconds() / 3600.0)


def _recency_score(raw: str, now: datetime, horizon_hours: float = 168.0) -> float:
    hours = _hours_since(raw, now)
    if hours <= 1.0:
        return 25.0
    if hours >= horizon_hours:
        return 0.0
    return 25.0 * (1.0 - (hours / horizon_hours))


def _text_match_score(text: str, anchors: list[str]) -> float:
    hay = str(text).strip().lower()
    if not hay:
        return 0.0
    score = 0.0
    for anchor in anchors:
        a = str(anchor).strip().lower()
        if a and (a in hay or hay in a):
            score += 18.0
    return score


def _parse_invariant(text: str) -> dict[str, Any]:
    terminal = ''
    distinction: list[str] = []
    doctrine = ''
    top_non_substitutions: list[str] = []
    current = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith('## '):
            current = line[3:].strip().lower()
            continue
        if current == 'terminal object' and not terminal:
            terminal = line
        elif current == 'core distinction':
            distinction.append(line)
        elif current == 'current doctrine' and not doctrine:
            doctrine = line
        elif current == 'non-substitutable rule' and line.startswith('-'):
            top_non_substitutions.append(line[1:].strip())
    return {
        'terminal_object': terminal,
        'core_distinction': ' '.join(distinction),
        'current_doctrine': doctrine,
        'top_non_substitutions': top_non_substitutions[:6],
    }


def _focus_task_titles(task_graph: dict[str, Any], delta: dict[str, Any] | None = None, limit: int = 6) -> list[str]:
    delta = delta or {}
    explicit = [str(t.get('title', '')).strip() for t in delta.get('task_updates', []) if isinstance(t, dict) and str(t.get('title', '')).strip()]
    if explicit:
        return explicit[:limit]
    tasks = [t for t in task_graph.get('active_tasks', []) if isinstance(t, dict)]
    active = [str(t.get('title', '')).strip() for t in tasks if str(t.get('status', '')).strip().lower() == 'active' and str(t.get('title', '')).strip()]
    return active[:limit]


def build_canonical_state(kernel_state: dict[str, Any], delta: dict[str, Any] | None = None) -> dict[str, Any]:
    delta = delta or {}
    state = kernel_state.get('STATE', {}) or {}
    salience = kernel_state.get('SALIENCE', {}) or {}
    task_graph = kernel_state.get('TASK_GRAPH', {}) or {}
    return {
        'invariant': _parse_invariant(str(kernel_state.get('INVARIANT', ''))),
        'phase': state.get('phase', ''),
        'current_objective': state.get('current_objective', ''),
        'active_tasks': state.get('active_tasks', []),
        'bottlenecks': state.get('bottlenecks', []),
        'focus_task_titles': _focus_task_titles(task_graph, delta=delta),
        'top_priorities': salience.get('priority_order', [])[:6],
        'must_not_forget': salience.get('must_not_forget', [])[:5],
        'parked_items': salience.get('parked_items', [])[:4],
        'decisions': kernel_state.get('DECISIONS', {}).get('decisions', []),
        'unknowns': kernel_state.get('OPEN_UNKNOWNS', {}).get('items', []),
        'errors': kernel_state.get('ERROR_LOG', {}).get('errors', []),
        'task_graph_items': task_graph.get('active_tasks', []),
        'root_objective': task_graph.get('root_objective', ''),
        'delta_task_titles': [str(t.get('title', '')).strip() for t in delta.get('task_updates', []) if isinstance(t, dict)],
        'delta_unknown_questions': [str(u.get('question', '')).strip() for u in delta.get('unknowns', []) if isinstance(u, dict)],
        'delta_decisions': [str(d).strip() for d in delta.get('decisions', []) if str(d).strip()],
        'delta_contradictions': [str(c).strip() for c in delta.get('contradictions', []) if str(c).strip()],
        'delta_has_contradictions': bool(delta.get('contradictions')),
        'delta_has_decisions': bool(delta.get('decisions')),
        'delta_has_unknowns': bool(delta.get('unknowns')),
    }


VIEW_ORDER = [
    'core_loop',
    'continuity_guard',
    'active_work',
    'decision_backbone',
    'open_threads',
    'error_pressure',
]


def _rank_tasks(tasks: list[dict[str, Any]], canonical_state: dict[str, Any], now: datetime, limit: int = 4) -> list[dict[str, Any]]:
    anchors = canonical_state.get('focus_task_titles', []) + canonical_state.get('top_priorities', [])
    scored: list[dict[str, Any]] = []
    for task in tasks:
        title = str(task.get('title', '')).strip()
        if not title:
            continue
        reasons: list[str] = []
        score = 0.0
        status = str(task.get('status', '')).strip().lower()
        if status == 'active':
            score += 35.0; reasons.append('active_status')
        elif status == 'blocked':
            score += 28.0; reasons.append('blocked_status')
        elif status == 'next':
            score += 22.0; reasons.append('next_status')
        elif status == 'done':
            score -= 12.0; reasons.append('done_penalty')
        recency = _recency_score(str(task.get('last_touched') or task.get('created_at') or ''), now)
        if recency > 0:
            score += recency; reasons.append('recently_touched')
        relevance = _text_match_score(title, anchors)
        if relevance > 0:
            score += relevance; reasons.append('task_relevant')
        if title in canonical_state.get('delta_task_titles', []):
            score += 30.0; reasons.append('delta_task')
        trust = item_trust(task) * 20.0
        score += trust
        reasons.append(f'provenance_trust={item_trust(task):.2f}')
        scored.append({'text': f'[{status}] {title}' if status else title, 'score': round(score,2), 'reasons': reasons, 'trust': round(item_trust(task),2)})
    scored.sort(key=lambda x: (-x['score'], x['text']))
    return scored[:limit]


def _rank_decisions(decisions: list[dict[str, Any]], canonical_state: dict[str, Any], now: datetime, limit: int = 4) -> list[dict[str, Any]]:
    anchors = canonical_state.get('focus_task_titles', []) + canonical_state.get('delta_decisions', []) + canonical_state.get('top_priorities', [])
    scored: list[dict[str, Any]] = []
    for item in decisions:
        statement = str(item.get('statement', '')).strip()
        if not statement:
            continue
        reasons: list[str] = []
        score = 0.0
        if str(item.get('status', '')).strip().lower() == 'active':
            score += 20.0; reasons.append('active_status')
        recency = _recency_score(str(item.get('last_touched') or item.get('timestamp') or ''), now)
        if recency > 0:
            score += recency; reasons.append('recently_touched')
        relevance = _text_match_score(statement, anchors)
        if relevance > 0:
            score += relevance; reasons.append('task_relevant')
        if statement in canonical_state.get('delta_decisions', []):
            score += 35.0; reasons.append('delta_decision')
        trust = item_trust(item) * 20.0
        score += trust
        reasons.append(f'provenance_trust={item_trust(item):.2f}')
        scored.append({'text': statement, 'score': round(score,2), 'reasons': reasons, 'trust': round(item_trust(item),2)})
    scored.sort(key=lambda x: (-x['score'], x['text']))
    return scored[:limit]


def _rank_unknowns(unknowns: list[dict[str, Any]], canonical_state: dict[str, Any], now: datetime, limit: int = 5) -> list[dict[str, Any]]:
    anchors = canonical_state.get('focus_task_titles', []) + canonical_state.get('top_priorities', []) + canonical_state.get('delta_unknown_questions', [])
    scored: list[dict[str, Any]] = []
    for item in unknowns:
        q = str(item.get('question', '')).strip()
        if not q:
            continue
        reasons: list[str] = []
        score = 0.0
        status = str(item.get('status', '')).strip().lower()
        cls = str(item.get('class', '')).strip().lower()
        if status == 'working':
            score += 35.0; reasons.append('working_status')
        elif status == 'open':
            score += 22.0; reasons.append('open_status')
        elif status == 'resolved':
            score -= 20.0; reasons.append('resolved_penalty')
        if cls == 'principled':
            score += 10.0; reasons.append('principled_weight')
        recency = _recency_score(str(item.get('last_touched') or item.get('created_at') or ''), now)
        if recency > 0:
            score += recency; reasons.append('recently_touched')
        relevance = _text_match_score(q, anchors)
        if relevance > 0:
            score += relevance; reasons.append('task_relevant')
        if q in canonical_state.get('delta_unknown_questions', []):
            score += 35.0; reasons.append('delta_unknown')
        trust = item_trust(item) * 20.0
        score += trust
        reasons.append(f'provenance_trust={item_trust(item):.2f}')
        scored.append({'text': f'[{cls}/{status}] {q}' if (cls or status) else q, 'score': round(score,2), 'reasons': reasons, 'trust': round(item_trust(item),2)})
    scored.sort(key=lambda x: (-x['score'], x['text']))
    return scored[:limit]


def _rank_errors(errors: list[dict[str, Any]], canonical_state: dict[str, Any], now: datetime, limit: int = 4) -> list[dict[str, Any]]:
    anchors = canonical_state.get('focus_task_titles', []) + canonical_state.get('top_priorities', []) + canonical_state.get('delta_contradictions', [])
    scored: list[dict[str, Any]] = []
    for item in errors:
        statement = str(item.get('statement', '')).strip()
        if not statement:
            continue
        reasons: list[str] = ['error_pressure']
        score = 15.0
        recency = _recency_score(str(item.get('last_touched') or item.get('timestamp') or ''), now)
        if recency > 0:
            score += recency; reasons.append('recently_touched')
        relevance = _text_match_score(statement, anchors)
        if relevance > 0:
            score += relevance; reasons.append('task_relevant')
        if statement in canonical_state.get('delta_contradictions', []):
            score += 40.0; reasons.append('delta_contradiction')
        trust = item_trust(item) * 15.0
        score += trust
        reasons.append(f'provenance_trust={item_trust(item):.2f}')
        scored.append({'text': statement, 'score': round(score,2), 'reasons': reasons, 'trust': round(item_trust(item),2)})
    scored.sort(key=lambda x: (-x['score'], x['text']))
    return scored[:limit]


def _rank_priorities(priorities: list[str], focus_task_titles: list[str], limit: int = 4) -> list[dict[str, Any]]:
    anchors = focus_task_titles + priorities[:4]
    scored: list[dict[str, Any]] = []
    for idx, item in enumerate(priorities):
        clean = str(item).strip()
        if not clean:
            continue
        reasons: list[str] = []
        score = max(0.0, 22.0 - idx * 4.0)
        if idx < 2:
            reasons.append('top_priority')
        relevance = _text_match_score(clean, anchors)
        if relevance > 0:
            score += relevance; reasons.append('task_relevant')
        scored.append({'text': clean, 'score': round(score,2), 'reasons': reasons})
    scored.sort(key=lambda x: (-x['score'], x['text']))
    return scored[:limit]


def build_view_library(canonical_state: dict[str, Any]) -> dict[str, dict[str, Any]]:
    now = datetime.now(timezone.utc)
    invariant = canonical_state.get('invariant', {}) or {}
    ranked_tasks = _rank_tasks(canonical_state.get('task_graph_items', []), canonical_state, now)
    ranked_decisions = _rank_decisions(canonical_state.get('decisions', []), canonical_state, now)
    ranked_unknowns = _rank_unknowns(canonical_state.get('unknowns', []), canonical_state, now)
    ranked_errors = _rank_errors(canonical_state.get('errors', []), canonical_state, now)
    ranked_priorities = _rank_priorities(canonical_state.get('top_priorities', []), canonical_state.get('focus_task_titles', []))
    sticky = canonical_state.get('must_not_forget', [])[:4]

    return {
        'core_loop': {
            'title': 'CORE_LOOP',
            'payload': {
                'terminal_object': invariant.get('terminal_object', ''),
                'phase': canonical_state.get('phase', ''),
                'current_objective': canonical_state.get('current_objective', ''),
                'root_objective': canonical_state.get('root_objective', ''),
            },
        },
        'continuity_guard': {
            'title': 'CONTINUITY_GUARD',
            'payload': {
                'core_distinction': invariant.get('core_distinction', ''),
                'current_doctrine': invariant.get('current_doctrine', ''),
                'top_non_substitutions': invariant.get('top_non_substitutions', [])[:3],
                'must_not_forget': sticky,
            },
        },
        'active_work': {
            'title': 'ACTIVE_WORK',
            'payload': {
                'focus_tasks': [x['text'] for x in ranked_tasks],
                'focus_task_trace': ranked_tasks,
                'bottlenecks': canonical_state.get('bottlenecks', [])[:3],
                'top_priorities': [x['text'] for x in ranked_priorities],
                'priority_trace': ranked_priorities,
                'parked_items': canonical_state.get('parked_items', [])[:2],
            },
        },
        'decision_backbone': {
            'title': 'DECISION_BACKBONE',
            'payload': {
                'recent_active_decisions': [x['text'] for x in ranked_decisions],
                'decision_trace': ranked_decisions,
            },
        },
        'open_threads': {
            'title': 'OPEN_THREADS',
            'payload': {
                'active_unknowns': [x['text'] for x in ranked_unknowns],
                'unknown_trace': ranked_unknowns,
            },
        },
        'error_pressure': {
            'title': 'ERROR_PRESSURE',
            'payload': {
                'recent_errors': [x['text'] for x in ranked_errors],
                'error_trace': ranked_errors,
                'delta_has_contradictions': canonical_state.get('delta_has_contradictions', False),
            },
        },
    }


def _view_score(name: str, view: dict[str, Any], canonical_state: dict[str, Any]) -> int:
    score = 0
    payload = view.get('payload', {})
    if name in {'core_loop', 'continuity_guard'}:
        score += 100
    if name == 'active_work':
        score += 60
        score += 6 * len(payload.get('focus_tasks', []))
        score += 3 * len(payload.get('top_priorities', []))
    if name == 'decision_backbone':
        score += 8 * len(payload.get('recent_active_decisions', []))
        if canonical_state.get('delta_has_decisions'):
            score += 30
    if name == 'open_threads':
        score += 8 * len(payload.get('active_unknowns', []))
        if canonical_state.get('delta_has_unknowns'):
            score += 30
    if name == 'error_pressure':
        score += 8 * len(payload.get('recent_errors', []))
        if canonical_state.get('delta_has_contradictions'):
            score += 35
    return score


def select_working_slice(view_library: dict[str, dict[str, Any]], canonical_state: dict[str, Any], max_views: int = 5) -> list[dict[str, Any]]:
    scored: list[tuple[int, str, dict[str, Any]]] = []
    for name in VIEW_ORDER:
        view = view_library.get(name)
        if not view:
            continue
        scored.append((_view_score(name, view, canonical_state), name, view))
    scored.sort(key=lambda item: (-item[0], VIEW_ORDER.index(item[1]) if item[1] in VIEW_ORDER else 999))
    return [view for _, _, view in scored[:max_views]]
