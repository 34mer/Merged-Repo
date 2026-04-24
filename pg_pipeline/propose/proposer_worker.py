from __future__ import annotations

from pg_pipeline.pgcore.ids import stable_id
from pg_pipeline.pgcore.schemas.common import ProducerInfo, Provenance, Scope, TrustInfo
from pg_pipeline.pgcore.schemas.geometry import GeometryRecord
from pg_pipeline.pgcore.schemas.proposal import ProposalPayload, ProposalRecord


CATALAN_RECURRENCE = "C[n] = sum(C[i] * C[n - 1 - i] for i in range(0, n))"


def propose_recurrence(records: list[GeometryRecord], run_id: str) -> ProposalRecord:
    values = [
        {
            "n": record.scope.parameters["n"],
            "boundary_count": record.payload.derived_features["boundary_count"],
        }
        for record in records
    ]
    payload = {
        "proposal_type": "recurrence",
        "dsl": CATALAN_RECURRENCE,
        "values": values,
    }
    return ProposalRecord(
        id=stable_id("proposal_record", payload),
        producer=ProducerInfo(producer_type="proposer", name="deterministic_recurrence", version="0.1.0"),
        provenance=Provenance(
            source_type="conjectural",
            input_artifact_ids=[record.id for record in records],
            run_id=run_id,
            notes="Deterministic stand-in for DSL-constrained local proposer.",
        ),
        trust=TrustInfo(level="medium", reason="Proposal requires checker and stress confirmation."),
        scope=Scope(
            family="grassmannian_small",
            parameters={"observed_n": [item["n"] for item in values]},
            representation="recurrence_dsl_v1",
        ),
        payload=ProposalPayload(
            proposal_type="recurrence",
            dsl=CATALAN_RECURRENCE,
            normalized_expression="catalan_convolution_recurrence",
            supporting_record_ids=[record.id for record in records],
            diagnostics={"observed_values": values},
        ),
    )

