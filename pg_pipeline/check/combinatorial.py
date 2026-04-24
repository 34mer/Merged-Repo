from __future__ import annotations

from pg_pipeline.pgcore.ids import stable_id
from pg_pipeline.pgcore.schemas.check_result import CheckResultPayload, CheckResultRecord
from pg_pipeline.pgcore.schemas.common import ProducerInfo, Provenance, Scope, TrustInfo
from pg_pipeline.pgcore.schemas.geometry import GeometryRecord
from pg_pipeline.pgcore.schemas.proposal import ProposalRecord


def check_combinatorial(
    proposal: ProposalRecord, records: list[GeometryRecord], run_id: str
) -> CheckResultRecord:
    ordered = sorted(records, key=lambda record: int(record.scope.parameters["n"]))
    counts = [int(record.payload.derived_features["boundary_count"]) for record in ordered]
    passed = all(left < right for left, right in zip(counts, counts[1:]))
    payload = {"proposal_id": proposal.id, "checker": "combinatorial", "passed": passed, "counts": counts}
    return CheckResultRecord(
        id=stable_id("check_result_record", payload),
        producer=ProducerInfo(producer_type="checker", name="monotone_boundary_checker", version="0.1.0"),
        provenance=Provenance(
            source_type="exact_computation",
            input_artifact_ids=[proposal.id, *[record.id for record in records]],
            run_id=run_id,
        ),
        trust=TrustInfo(level="medium", reason="Structural monotonicity check for MVP family."),
        scope=Scope(family="grassmannian_small", parameters={}, representation="check_result_v1"),
        payload=CheckResultPayload(
            proposal_id=proposal.id,
            checker="combinatorial",
            passed=passed,
            checked_record_ids=[record.id for record in records],
            diagnostics={"counts": counts},
        ),
    )

