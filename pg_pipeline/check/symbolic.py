from __future__ import annotations

from pg_pipeline.generators.families.grassmannian import catalan
from pg_pipeline.pgcore.ids import stable_id
from pg_pipeline.pgcore.schemas.check_result import CheckResultPayload, CheckResultRecord
from pg_pipeline.pgcore.schemas.common import ProducerInfo, Provenance, Scope, TrustInfo
from pg_pipeline.pgcore.schemas.geometry import GeometryRecord
from pg_pipeline.pgcore.schemas.proposal import ProposalRecord


def check_symbolic(proposal: ProposalRecord, records: list[GeometryRecord], run_id: str) -> CheckResultRecord:
    diagnostics = {}
    passed = True
    for record in records:
        n = int(record.scope.parameters["n"])
        expected = catalan(n - 3)
        observed = int(record.payload.derived_features["boundary_count"])
        diagnostics[str(n)] = {"expected": expected, "observed": observed}
        passed = passed and expected == observed
    payload = {"proposal_id": proposal.id, "checker": "symbolic", "passed": passed, "records": diagnostics}
    return CheckResultRecord(
        id=stable_id("check_result_record", payload),
        producer=ProducerInfo(producer_type="checker", name="symbolic_catalan_checker", version="0.1.0"),
        provenance=Provenance(
            source_type="exact_computation",
            input_artifact_ids=[proposal.id, *[record.id for record in records]],
            run_id=run_id,
        ),
        trust=TrustInfo(level="high", reason="Closed-form integer equality check."),
        scope=Scope(family="grassmannian_small", parameters={}, representation="check_result_v1"),
        payload=CheckResultPayload(
            proposal_id=proposal.id,
            checker="symbolic",
            passed=passed,
            checked_record_ids=[record.id for record in records],
            diagnostics=diagnostics,
        ),
    )

