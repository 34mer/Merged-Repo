from __future__ import annotations

from pg_pipeline.pgcore.ids import stable_id
from pg_pipeline.pgcore.schemas.common import ProducerInfo, Provenance, Scope, TrustInfo
from pg_pipeline.pgcore.schemas.comparison import (
    ComparisonPayload,
    ComparisonRecord,
    RealizationClassSummary,
)
from pg_pipeline.pgcore.schemas.geometry import GeometryRecord


def _authority_ids(authority_records: list[GeometryRecord]) -> list[str]:
    wanted = {
        "exact_finite_grassmannian_A",
        "exact_finite_grassmannian_D4",
        "exact_finite_grassmannian_E6",
        "surfaceology_conservative_family",
    }
    return [record.id for record in authority_records if record.scope.family in wanted]


def generate_r2_r3_comparison(
    authority_records: list[GeometryRecord],
    run_id: str,
) -> ComparisonRecord:
    """Encode the thread-level R2↔R3 discriminator as a typed comparison record.

    R2 is the graph-associahedral / generic grouped-parameter vicinity.
    R3 is the cosmohedral / intrinsic equality-saturated grouped law.

    This record is not a new theorem. It is the repo-native carrier for the current
    thread result, so later checkers can preserve, reject, or refine it explicitly.
    """
    authority_record_ids = _authority_ids(authority_records)
    payload = ComparisonPayload(
        comparison_id="r2_graph_associahedral_vs_r3_cosmohedral_intrinsic_equalities_v1",
        left=RealizationClassSummary(
            class_id="R2_graph_associahedral_vicinity",
            label="R2 / graph-associahedral vicinity",
            role="generic grouped-parameter realization regime",
            features=[
                "grouped carriers",
                "grouped parameters",
                "grouped factorization",
                "overlap/submodular inequalities",
                "equalities by special saturation or degeneration",
            ],
        ),
        right=RealizationClassSummary(
            class_id="R3_cosmohedral",
            label="R3 / cosmohedral realization",
            role="equality-saturated grouped-law realization regime",
            features=[
                "grouped carriers",
                "grouped parameters",
                "grouped factorization",
                "overlap/submodular inequalities",
                "intrinsic equalities required by grouped compatibility law",
            ],
        ),
        relation="ordered_specialization",
        verdict="supported",
        shared_layers=[
            "grouped carriers",
            "grouped weights / parameters",
            "grouped factorization",
            "overlap/submodular inequality layer",
        ],
        distinguishing_layers=[
            "R2 equalities appear as special saturated degeneration data",
            "R3 equalities are intrinsic to the primitive grouped compatibility law",
        ],
        specialization_direction="R3 is an equality-saturated specialization/refinement of the generic R2-type grouped-parameter regime; not conversely.",
        unresolved_deficits=[
            "Formal source-level proof still required: this record carries the current checked-thread verdict, not a Lean-certified theorem.",
            "Broader R1/R2/R3 and R1..R14 matrix still needs typed completion.",
        ],
        authority_record_ids=authority_record_ids,
        thread_claim_summary=(
            "The R2↔R3 comparison is distinct but ordered: both sides share grouped carriers, "
            "parameters, factorization, and submodular overlap inequalities; R3 adds intrinsic "
            "equality constraints while R2 reaches those equalities only under specialization/degeneration."
        ),
        diagnostics={
            "source": "current_thread_extraction",
            "status": "repo_native_carrier_for_existing_thread_result",
            "authority_record_count": len(authority_record_ids),
        },
    )
    record_id = stable_id("comparison_record", payload.model_dump(mode="json"))
    return ComparisonRecord(
        id=record_id,
        producer=ProducerInfo(
            producer_type="controller",
            name="realization_comparison_generator",
            version="0.1.0",
        ),
        provenance=Provenance(
            source_type="conjectural",
            input_artifact_ids=authority_record_ids,
            run_id=run_id,
            notes="Typed carrier for the thread-level R2↔R3 discriminator; not theorem-level authority.",
        ),
        trust=TrustInfo(
            level="medium",
            reason="Supported by thread extraction and authority pack linkage, pending formal checker expansion.",
        ),
        scope=Scope(
            family="realization_class_comparison",
            parameters={"left": payload.left.class_id, "right": payload.right.class_id},
            representation="comparison_record_v1",
            applicability_domain="Finite realization-class discriminator ledger only; no substrate commitment.",
        ),
        payload=payload,
    )
