from __future__ import annotations

from pg_pipeline.pgcore.schemas.check_result import CheckResultRecord
from pg_pipeline.pgcore.schemas.geometry import GeometryRecord
from pg_pipeline.pgcore.schemas.proposal import ProposalRecord
from pg_pipeline.pgcore.schemas.stress_result import StressResultRecord
from pg_pipeline.pgcore.schemas.substrate_schema import SubstrateSchemaRecord


def build_weekly_summary(
    records: list[GeometryRecord],
    proposal: ProposalRecord,
    checks: list[CheckResultRecord],
    stresses: list[StressResultRecord],
    substrate: SubstrateSchemaRecord,
) -> dict[str, object]:
    return {
        "status": "passed" if all(c.payload.passed for c in checks) and all(s.payload.passed for s in stresses) else "failed",
        "family": "grassmannian_small",
        "geometry_records": len(records),
        "proposal_id": proposal.id,
        "check_results": {check.payload.checker: check.payload.passed for check in checks},
        "stress_results": {stress.payload.stressor: stress.payload.passed for stress in stresses},
        "substrate_schema_id": substrate.id,
        "substrate_domain": substrate.payload.domain_of_validity,
    }

