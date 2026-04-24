from __future__ import annotations

from pg_pipeline.pgcore.ids import stable_id
from pg_pipeline.pgcore.schemas.check_result import CheckResultRecord
from pg_pipeline.pgcore.schemas.common import ProducerInfo, Provenance, Scope, TrustInfo
from pg_pipeline.pgcore.schemas.proposal import ProposalRecord
from pg_pipeline.pgcore.schemas.stress_result import StressResultRecord
from pg_pipeline.pgcore.schemas.substrate_schema import SubstrateSchemaPayload, SubstrateSchemaRecord


def compile_substrate_schema(
    proposal: ProposalRecord,
    checks: list[CheckResultRecord],
    stresses: list[StressResultRecord],
    run_id: str,
) -> SubstrateSchemaRecord:
    evidence_ids = [proposal.id, *[check.id for check in checks], *[stress.id for stress in stresses]]
    payload = {
        "source_proposal_id": proposal.id,
        "evidence_record_ids": evidence_ids,
        "domain": "grassmannian_small MVP proxy",
    }
    return SubstrateSchemaRecord(
        id=stable_id("substrate_schema_record", payload),
        producer=ProducerInfo(producer_type="controller", name="substrate_compiler", version="0.1.0"),
        provenance=Provenance(source_type="conjectural", input_artifact_ids=evidence_ids, run_id=run_id),
        trust=TrustInfo(level="medium", reason="Draft emitted after all MVP checks and stresses passed."),
        scope=Scope(
            family="grassmannian_small",
            parameters={"proposal_type": "recurrence"},
            representation="substrate_schema_v1",
            applicability_domain="Only the MVP proxy family until exact-work generators are available.",
        ),
        payload=SubstrateSchemaPayload(
            source_proposal_id=proposal.id,
            primitive_operations=["integer recurrence", "boundary-count readout"],
            invariants=["Catalan convolution form"],
            scaling_laws=["boundary_count follows Catalan growth for generated proxy indices"],
            readout_bottlenecks=["requires exact integer boundary summary per n"],
            domain_of_validity="grassmannian_small MVP proxy; not a theorem-level positive-geometry claim.",
            evidence_record_ids=evidence_ids,
            diagnostics={"checks": [check.payload.passed for check in checks], "stresses": [s.payload.passed for s in stresses]},
        ),
    )

