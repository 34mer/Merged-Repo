from __future__ import annotations

from pg_pipeline.pgcore.ids import stable_id
from pg_pipeline.pgcore.schemas.common import ProducerInfo, Provenance, Scope, TrustInfo
from pg_pipeline.pgcore.schemas.review_decision import ReviewDecisionPayload, ReviewDecisionRecord
from pg_pipeline.pgcore.schemas.substrate_schema import SubstrateSchemaRecord


def decide_substrate_draft(substrate: SubstrateSchemaRecord, run_id: str) -> ReviewDecisionRecord:
    decision = "accept" if substrate.trust.level in {"medium", "high"} else "revise"
    payload = {
        "subject_record_id": substrate.id,
        "decision": decision,
        "domain": substrate.payload.domain_of_validity,
    }
    return ReviewDecisionRecord(
        id=stable_id("review_decision_record", payload),
        producer=ProducerInfo(producer_type="controller", name="projectx_review", version="0.1.0"),
        provenance=Provenance(
            source_type="conjectural",
            input_artifact_ids=[substrate.id],
            run_id=run_id,
            notes="Outer ProjectX review decision over inner pipeline substrate draft.",
        ),
        trust=TrustInfo(level="medium", reason="Automated review for MVP slice; human review remains authoritative."),
        scope=Scope(
            family=substrate.scope.family,
            parameters={"subject": substrate.id},
            representation="review_decision_v1",
        ),
        payload=ReviewDecisionPayload(
            subject_record_id=substrate.id,
            decision=decision,
            rationale="Accepted as a typed MVP draft, not as theorem-level math authority.",
            diagnostics={"domain_of_validity": substrate.payload.domain_of_validity},
        ),
    )

