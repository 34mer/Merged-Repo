from __future__ import annotations

from pg_pipeline.generators.families.grassmannian import generate_grassmannian_small
from pg_pipeline.pgcore.ids import stable_id
from pg_pipeline.pgcore.schemas.common import ProducerInfo, Provenance, Scope, TrustInfo
from pg_pipeline.pgcore.schemas.proposal import ProposalRecord
from pg_pipeline.pgcore.schemas.stress_result import StressResultPayload, StressResultRecord


def stress_heldout(proposal: ProposalRecord, run_id: str) -> StressResultRecord:
    heldout = generate_grassmannian_small(run_id=run_id, n_values=[8])
    count = heldout[0].payload.derived_features["boundary_count"]
    passed = count == 42
    payload = {"proposal_id": proposal.id, "stressor": "heldout", "passed": passed, "count": count}
    return StressResultRecord(
        id=stable_id("stress_result_record", payload),
        producer=ProducerInfo(producer_type="checker", name="heldout_large_n", version="0.1.0"),
        provenance=Provenance(source_type="exact_computation", input_artifact_ids=[proposal.id], run_id=run_id),
        trust=TrustInfo(level="high", reason="Held-out exact computation."),
        scope=Scope(family="grassmannian_small", parameters={"heldout_n": 8}, representation="stress_v1"),
        payload=StressResultPayload(
            proposal_id=proposal.id,
            stressor="heldout",
            passed=passed,
            diagnostics={"heldout_boundary_count": count},
        ),
    )

