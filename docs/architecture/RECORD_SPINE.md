# Canonical Record Spine

All scientific lifecycle objects move through typed records in `pg_pipeline/pgcore/schemas`.

Canonical records:

- `GeometryRecord`: source-backed or generated family/object datum.
- `RepresentationMapRecord`: validated mapping between representations.
- `FailedConjectureRecord`: normalized failed proposal with counterexamples.
- `ProposalRecord`: DSL-constrained candidate emitted by proposer/controller.
- `CheckResultRecord`: symbolic, combinatorial, numeric, SMT, or formal check result.
- `StressResultRecord`: held-out, mutation, adversarial, or robustness result.
- `SubstrateSchemaRecord`: draft substrate constraint summary emitted after checks and stress.
- `ReviewDecisionRecord`: review action over substrate/proposal/result records.
- `JobRecord`: lifecycle state for scheduled work.

Boundaries:

- ProjectX runtime state is not scientific truth.
- Scientific truth records are immutable record objects and SQLite rows.
- Artifact files become scientific inputs only after record ingestion with provenance.
- Review decisions do not mutate proposal records; they reference them.

