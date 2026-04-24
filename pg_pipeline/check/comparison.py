from __future__ import annotations

from pg_pipeline.pgcore.ids import stable_id
from pg_pipeline.pgcore.schemas.check_result import CheckResultPayload, CheckResultRecord
from pg_pipeline.pgcore.schemas.common import ProducerInfo, Provenance, Scope, TrustInfo
from pg_pipeline.pgcore.schemas.comparison import ComparisonRecord


def check_r2_r3_comparison(record: ComparisonRecord, run_id: str) -> CheckResultRecord:
    """Conservative structural checker for the typed R2↔R3 comparison record."""
    required_shared = {
        "grouped carriers",
        "grouped weights / parameters",
        "grouped factorization",
        "overlap/submodular inequality layer",
    }
    required_distinguishers = {
        "R2 equalities appear as special saturated degeneration data",
        "R3 equalities are intrinsic to the primitive grouped compatibility law",
    }
    shared = set(record.payload.shared_layers)
    distinguishers = set(record.payload.distinguishing_layers)
    diagnostics = {
        "relation": record.payload.relation,
        "verdict": record.payload.verdict,
        "has_required_shared_layers": required_shared.issubset(shared),
        "has_required_distinguishers": required_distinguishers.issubset(distinguishers),
        "has_direction": bool(record.payload.specialization_direction),
        "authority_record_count": len(record.payload.authority_record_ids),
        "unresolved_deficits": record.payload.unresolved_deficits,
    }
    passed = (
        record.payload.relation == "ordered_specialization"
        and record.payload.verdict == "supported"
        and diagnostics["has_required_shared_layers"]
        and diagnostics["has_required_distinguishers"]
        and diagnostics["has_direction"]
        and diagnostics["authority_record_count"] >= 1
    )
    payload = {
        "proposal_id": record.id,
        "checker": "combinatorial",
        "passed": passed,
        "diagnostics": diagnostics,
    }
    return CheckResultRecord(
        id=stable_id("check_result_record", payload),
        producer=ProducerInfo(
            producer_type="checker",
            name="r2_r3_comparison_checker",
            version="0.1.0",
        ),
        provenance=Provenance(
            source_type="conjectural",
            input_artifact_ids=[record.id, *record.payload.authority_record_ids],
            run_id=run_id,
            notes="Checks the typed carrier shape of the R2↔R3 discriminator, not the full theorem.",
        ),
        trust=TrustInfo(
            level="medium",
            reason="Shape-level checker over a typed comparison record with authority linkage.",
        ),
        scope=Scope(
            family="realization_class_comparison",
            parameters={"comparison_id": record.payload.comparison_id},
            representation="check_result_v1",
            applicability_domain="Typed ledger-shape validation only.",
        ),
        payload=CheckResultPayload(
            proposal_id=record.id,
            checker="combinatorial",
            passed=passed,
            checked_record_ids=[record.id],
            diagnostics=diagnostics,
        ),
    )
