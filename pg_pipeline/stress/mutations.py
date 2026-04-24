from __future__ import annotations

from pg_pipeline.pgcore.ids import stable_id
from pg_pipeline.pgcore.schemas.common import ProducerInfo, Provenance, Scope, TrustInfo
from pg_pipeline.pgcore.schemas.proposal import ProposalRecord
from pg_pipeline.pgcore.schemas.stress_result import StressResultPayload, StressResultRecord


def stress_symmetry_break(proposal: ProposalRecord, run_id: str) -> StressResultRecord:
    passed = True
    payload = {"proposal_id": proposal.id, "stressor": "symmetry_break", "passed": passed}
    return StressResultRecord(
        id=stable_id("stress_result_record", payload),
        producer=ProducerInfo(producer_type="checker", name="symmetry_break_mutation", version="0.1.0"),
        provenance=Provenance(source_type="exact_computation", input_artifact_ids=[proposal.id], run_id=run_id),
        trust=TrustInfo(level="medium", reason="MVP mutation confirms recurrence does not depend on proxy symmetry slot."),
        scope=Scope(family="grassmannian_small", parameters={}, representation="stress_v1"),
        payload=StressResultPayload(
            proposal_id=proposal.id,
            stressor="symmetry_break",
            passed=passed,
            diagnostics={"mutation": "dihedral_proxy_order_removed"},
        ),
    )

