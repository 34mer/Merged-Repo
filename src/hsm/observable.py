from __future__ import annotations

from typing import Any


def midpoint(bounds: list[float]) -> float:
    return (float(bounds[0]) + float(bounds[1])) / 2.0


def features_from_construction_packet(construction: dict[str, Any]) -> dict[str, float]:
    """Build numeric observable features from construction constraints only."""
    return {
        row["feature"]: midpoint(row["range"])
        for row in construction.get("constraints", [])
    }


def extract_observables(substrate_or_state: dict[str, Any]) -> dict[str, float]:
    """Extract post-migration observables used by the independent oracle.

    The verifier uses these values, not merely the constraint hash. The object can
    therefore fail even when checkpoint/hash migration succeeds.
    """
    if "observable_features" in substrate_or_state:
        values = substrate_or_state["observable_features"]
    elif "post_migration_observables" in substrate_or_state:
        values = substrate_or_state["post_migration_observables"]
    else:
        values = substrate_or_state.get("state", {}).get("observable_features", {})
    return {str(k): float(v) for k, v in values.items()}


def evaluate_against_oracle(observables: dict[str, float], oracle: dict[str, Any]) -> dict[str, Any]:
    rows = []
    for constraint in oracle.get("constraints", []):
        feature = constraint["feature"]
        value = observables.get(feature)
        lo, hi = [float(x) for x in constraint["range"]]
        passed = value is not None and lo <= float(value) <= hi
        rows.append({
            "id": constraint["id"],
            "feature": feature,
            "value": value,
            "oracle_range": [lo, hi],
            "passed": bool(passed),
        })
    return {
        "status": "PASS" if rows and all(row["passed"] for row in rows) else "FAIL",
        "rows": rows,
        "passed_count": sum(1 for row in rows if row["passed"]),
        "total_count": len(rows),
    }
