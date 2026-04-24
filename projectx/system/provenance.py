from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

ORIGIN_TRUST = {
    'invariant_default': 1.0,
    'anchor_carryover': 0.97,
    'anchor_restore': 0.95,
    'integrity_restore': 0.93,
    'constraint_reconstructed': 0.94,
    'backbone_promoted': 0.95,
    'regenerated_survivor': 0.88,
    'confirmed_update': 0.82,
    'session_update': 0.66,
    'legacy_untyped': 0.60,
    'decayed_session': 0.46,
    'contradicted_update': 0.28,
    'error_pressure': 0.72,
}

WEAK_ORIGINS = {'session_update', 'legacy_untyped', 'confirmed_update', 'decayed_session', 'regenerated_survivor', 'contradicted_update'}
PROTECTED_ORIGINS = {'invariant_default', 'anchor_carryover', 'anchor_restore', 'integrity_restore', 'constraint_reconstructed', 'backbone_promoted'}
PROMOTION_TOUCH_THRESHOLD = 3
BACKBONE_TOUCH_THRESHOLD = 3
SUPPORT_PROMOTION_THRESHOLD = 2
CONFLICT_PENALTY_STEP = 0.05
MIN_CONTRADICTION_TRUST = 0.12
DECAY_DAYS = 21
CONFIRM_DAYS = 14


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


def origin_trust(origin: str) -> float:
    return float(ORIGIN_TRUST.get(str(origin or '').strip(), 0.5))


def _clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, float(value)))


def _age_days(raw: str, now: str | datetime) -> float:
    end = now if isinstance(now, datetime) else _parse_iso(str(now))
    start = _parse_iso(str(raw))
    return max(0.0, (end - start).total_seconds() / 86400.0)


def ensure_provenance(item: dict[str, Any], default_origin: str = 'legacy_untyped', now: str | None = None) -> dict[str, Any]:
    item = deepcopy(item)
    prov = deepcopy(item.get('provenance') or {})
    origin = str(prov.get('origin') or default_origin).strip() or default_origin
    created = str(prov.get('created_at') or item.get('timestamp') or item.get('created_at') or now or '').strip()
    touched = str(prov.get('last_touched') or item.get('last_touched') or created or now or '').strip()
    prov.setdefault('origin', origin)
    prov.setdefault('created_at', created)
    prov['last_touched'] = touched
    prov['trust'] = float(prov.get('trust', origin_trust(origin)))
    lineage = list(prov.get('lineage', []))
    if origin and origin not in lineage:
        lineage.append(origin)
    prov['lineage'] = lineage[-8:]
    prov['touch_count'] = int(prov.get('touch_count', 1))
    prov.setdefault('promotion_count', 0)
    prov.setdefault('decay_count', 0)
    prov.setdefault('support_count', 0)
    prov.setdefault('conflict_count', 0)
    prov.setdefault('last_evolved_at', touched or created or now or '')
    item['provenance'] = prov
    return item


def touch_item(item: dict[str, Any], now: str, via: str | None = None) -> dict[str, Any]:
    item = ensure_provenance(item, now=now)
    prov = item['provenance']
    prov['last_touched'] = now
    prov['touch_count'] = int(prov.get('touch_count', 1)) + 1
    if via:
        lineage = list(prov.get('lineage', []))
        if via not in lineage:
            lineage.append(via)
        prov['lineage'] = lineage[-8:]
    item['provenance'] = prov
    return item


def stamp_origin(item: dict[str, Any], origin: str, now: str, via: str | None = None, trust: float | None = None) -> dict[str, Any]:
    item = deepcopy(item)
    item = ensure_provenance(item, default_origin=origin, now=now)
    prov = item['provenance']
    prov['origin'] = origin
    prov['trust'] = float(origin_trust(origin) if trust is None else trust)
    prov['created_at'] = prov.get('created_at') or now
    prov['last_touched'] = now
    lineage = list(prov.get('lineage', []))
    if origin not in lineage:
        lineage.append(origin)
    if via and via not in lineage:
        lineage.append(via)
    prov['lineage'] = lineage[-8:]
    prov['touch_count'] = max(1, int(prov.get('touch_count', 1)))
    prov['last_evolved_at'] = now
    item['provenance'] = prov
    return item


def item_trust(item: dict[str, Any], default_origin: str = 'legacy_untyped') -> float:
    if not isinstance(item, dict):
        return origin_trust(default_origin)
    prov = item.get('provenance') or {}
    if 'trust' in prov:
        try:
            return float(prov['trust'])
        except (TypeError, ValueError):
            pass
    origin = str(prov.get('origin') or default_origin).strip() or default_origin
    return origin_trust(origin)


def item_recency(item: dict[str, Any]) -> datetime:
    if not isinstance(item, dict):
        return _parse_iso('')
    prov = item.get('provenance') or {}
    return _parse_iso(str(prov.get('last_touched') or item.get('last_touched') or item.get('timestamp') or item.get('created_at') or ''))


def evolve_item(item: dict[str, Any], now: str, role: str = 'generic') -> dict[str, Any]:
    item = ensure_provenance(item, now=now)
    prov = item['provenance']
    origin = str(prov.get('origin') or 'legacy_untyped').strip() or 'legacy_untyped'
    trust = float(prov.get('trust', origin_trust(origin)))
    touches = int(prov.get('touch_count', 1))
    age = _age_days(str(prov.get('last_touched') or prov.get('created_at') or ''), now)
    reasons: list[str] = []

    if role in {'protected', 'backbone'} and origin not in PROTECTED_ORIGINS and touches >= BACKBONE_TOUCH_THRESHOLD:
        origin = 'backbone_promoted'
        trust = max(trust, origin_trust(origin))
        prov['promotion_count'] = int(prov.get('promotion_count', 0)) + 1
        reasons.append('backbone_promotion')
    elif origin in {'session_update', 'legacy_untyped', 'decayed_session'} and touches >= PROMOTION_TOUCH_THRESHOLD and age <= CONFIRM_DAYS:
        origin = 'confirmed_update'
        trust = max(trust, origin_trust(origin))
        prov['promotion_count'] = int(prov.get('promotion_count', 0)) + 1
        reasons.append('repeated_confirmation')

    if role not in {'protected', 'backbone'} and origin in WEAK_ORIGINS and age >= DECAY_DAYS and touches <= 2:
        origin = 'decayed_session'
        trust = min(trust, origin_trust(origin))
        prov['decay_count'] = int(prov.get('decay_count', 0)) + 1
        reasons.append('stale_decay')

    lineage = list(prov.get('lineage', []))
    if origin not in lineage:
        lineage.append(origin)
    for tag in reasons:
        if tag not in lineage:
            lineage.append(tag)
    prov['origin'] = origin
    prov['trust'] = _clamp(trust)
    prov['lineage'] = lineage[-10:]
    prov['last_evolved_at'] = now
    prov['evolution_reason'] = reasons[-1] if reasons else prov.get('evolution_reason', '')
    item['provenance'] = prov
    return item


def _relation_to_reference(item: dict[str, Any], reference: dict[str, Any] | None, fields: tuple[str, ...]) -> str:
    if not reference:
        return 'none'
    for field in fields:
        if str(item.get(field, '')).strip() != str(reference.get(field, '')).strip():
            return 'conflict'
    return 'support'


def revise_against_reference(
    item: dict[str, Any],
    reference: dict[str, Any] | None,
    now: str,
    *,
    role: str = 'generic',
    fields: tuple[str, ...] = (),
) -> dict[str, Any]:
    item = ensure_provenance(item, now=now)
    if not reference:
        return item
    reference = ensure_provenance(reference, default_origin='invariant_default', now=now)
    prov = item['provenance']
    origin = str(prov.get('origin') or 'legacy_untyped').strip() or 'legacy_untyped'
    trust = float(prov.get('trust', origin_trust(origin)))
    relation = _relation_to_reference(item, reference, fields)
    lineage = list(prov.get('lineage', []))

    if relation == 'conflict':
        prov['conflict_count'] = int(prov.get('conflict_count', 0)) + 1
        conflict_count = int(prov['conflict_count'])
        if origin not in PROTECTED_ORIGINS:
            origin = 'contradicted_update'
            trust = min(trust, max(MIN_CONTRADICTION_TRUST, origin_trust(origin) - CONFLICT_PENALTY_STEP * max(0, conflict_count - 1)))
        tag = 'backbone_conflict'
        if tag not in lineage:
            lineage.append(tag)
        prov['evolution_reason'] = tag
    elif relation == 'support':
        prov['support_count'] = int(prov.get('support_count', 0)) + 1
        support_count = int(prov['support_count'])
        if origin in {'session_update', 'legacy_untyped', 'decayed_session', 'contradicted_update'} and support_count >= SUPPORT_PROMOTION_THRESHOLD:
            if role in {'protected', 'backbone'}:
                origin = 'backbone_promoted'
            else:
                origin = 'confirmed_update'
            trust = max(trust, origin_trust(origin))
            prov['promotion_count'] = int(prov.get('promotion_count', 0)) + 1
            tag = 'conflict_survival_confirmation' if prov.get('conflict_count', 0) else 'backbone_support_confirmation'
            if tag not in lineage:
                lineage.append(tag)
            prov['evolution_reason'] = tag
        elif origin in {'confirmed_update', 'backbone_promoted'}:
            trust = max(trust, min(1.0, origin_trust(origin) + 0.01 * min(3, support_count)))
            tag = 'backbone_support'
            if tag not in lineage:
                lineage.append(tag)
            prov['evolution_reason'] = tag

    if origin not in lineage:
        lineage.append(origin)
    prov['origin'] = origin
    prov['trust'] = _clamp(trust)
    prov['lineage'] = lineage[-12:]
    prov['last_evolved_at'] = now
    item['provenance'] = prov
    return item


def choose_stronger(existing: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    et = item_trust(existing)
    ct = item_trust(candidate)
    if ct > et + 1e-6:
        chosen = deepcopy(candidate)
        loser = existing
    elif et > ct + 1e-6:
        chosen = deepcopy(existing)
        loser = candidate
    else:
        er = item_recency(existing)
        cr = item_recency(candidate)
        if cr >= er:
            chosen = deepcopy(candidate)
            loser = existing
        else:
            chosen = deepcopy(existing)
            loser = candidate
    chosen = ensure_provenance(chosen)
    loser = ensure_provenance(loser)
    lineage = list(chosen['provenance'].get('lineage', []))
    for tag in loser['provenance'].get('lineage', []):
        if tag not in lineage:
            lineage.append(tag)
    chosen['provenance']['lineage'] = lineage[-10:]
    chosen['provenance']['trust'] = max(item_trust(chosen), item_trust(loser))
    return chosen


def normalize_kernel_provenance(state: dict[str, Any], now: str) -> dict[str, Any]:
    state = deepcopy(state)
    anchor = deepcopy(state.get('ANCHOR') or state.get('INTEGRITY') or {})
    protected_decisions = {str(x.get('statement', '')).strip(): deepcopy(x) for x in anchor.get('protected_decisions', []) if isinstance(x, dict)}
    protected_unknowns = {str(x.get('question', '')).strip(): deepcopy(x) for x in anchor.get('protected_unknowns', []) if isinstance(x, dict)}
    protected_tasks = {str(x.get('title', '')).strip(): deepcopy(x) for x in anchor.get('protected_tasks', []) if isinstance(x, dict)}

    list_specs = [
        ('DECISIONS', 'decisions', 'legacy_untyped', 'statement', protected_decisions, ('status',)),
        ('OPEN_UNKNOWNS', 'items', 'legacy_untyped', 'question', protected_unknowns, ('class', 'status')),
        ('ERROR_LOG', 'errors', 'error_pressure', 'statement', {}, ()),
        ('TASK_GRAPH', 'active_tasks', 'legacy_untyped', 'title', protected_tasks, ('status',)),
    ]
    for key, list_key, origin, identity_key, protected_map, relation_fields in list_specs:
        obj = deepcopy(state.get(key) or {})
        items = []
        for raw in obj.get(list_key, []):
            if not isinstance(raw, dict):
                continue
            evolved = ensure_provenance(raw, default_origin=origin, now=now)
            ident = str(evolved.get(identity_key, '')).strip()
            role = 'protected' if ident in protected_map else 'generic'
            evolved = evolve_item(evolved, now, role=role)
            evolved = revise_against_reference(evolved, protected_map.get(ident), now, role=role, fields=relation_fields)
            items.append(evolved)
        obj[list_key] = items
        state[key] = obj

    for pkey, origin in [('ANCHOR', 'anchor_carryover'), ('INTEGRITY', 'anchor_carryover')]:
        pobj = deepcopy(state.get(pkey) or {})
        if pobj:
            pobj.setdefault('provenance', {})
            pobj['provenance'].setdefault('origin', origin)
            pobj['provenance'].setdefault('trust', origin_trust(origin))
            pobj['provenance'].setdefault('created_at', now)
            pobj['provenance']['last_touched'] = now
            for list_key in ['protected_decisions', 'protected_unknowns', 'protected_tasks']:
                items = []
                item_origin = 'invariant_default' if pkey == 'ANCHOR' else 'anchor_carryover'
                for raw in pobj.get(list_key, []):
                    if isinstance(raw, dict):
                        evolved = ensure_provenance(raw, default_origin=item_origin, now=now)
                        items.append(evolve_item(evolved, now, role='backbone'))
                pobj[list_key] = items
            state[pkey] = pobj

    state.setdefault('PROVENANCE', {
        'origin_weights': ORIGIN_TRUST,
        'conflict_rule': 'prefer_higher_trust_then_newer',
        'protected_origins': sorted(PROTECTED_ORIGINS),
        'evolution': {
            'promotion_touch_threshold': PROMOTION_TOUCH_THRESHOLD,
            'backbone_touch_threshold': BACKBONE_TOUCH_THRESHOLD,
            'support_promotion_threshold': SUPPORT_PROMOTION_THRESHOLD,
            'confirm_days': CONFIRM_DAYS,
            'decay_days': DECAY_DAYS,
            'contradiction_penalty_step': CONFLICT_PENALTY_STEP,
        },
        'truth_revision': {
            'protected_reference_source': 'anchor_or_integrity',
            'decision_fields': ['status'],
            'unknown_fields': ['class', 'status'],
            'task_fields': ['status'],
            'contradicted_origin': 'contradicted_update',
        },
        'last_updated': now,
    })
    state['PROVENANCE']['origin_weights'] = ORIGIN_TRUST
    state['PROVENANCE']['protected_origins'] = sorted(PROTECTED_ORIGINS)
    state['PROVENANCE']['evolution'] = {
        'promotion_touch_threshold': PROMOTION_TOUCH_THRESHOLD,
        'backbone_touch_threshold': BACKBONE_TOUCH_THRESHOLD,
        'support_promotion_threshold': SUPPORT_PROMOTION_THRESHOLD,
        'confirm_days': CONFIRM_DAYS,
        'decay_days': DECAY_DAYS,
        'contradiction_penalty_step': CONFLICT_PENALTY_STEP,
    }
    state['PROVENANCE']['truth_revision'] = {
        'protected_reference_source': 'anchor_or_integrity',
        'decision_fields': ['status'],
        'unknown_fields': ['class', 'status'],
        'task_fields': ['status'],
        'contradicted_origin': 'contradicted_update',
    }
    state['PROVENANCE']['last_updated'] = now
    return state
