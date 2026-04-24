# Completion Status

## Complete

- Phase 1: forensic inventory and import matrix.
- Phase 2: canonical repo shape.
- Phase 3: curated ProjectX import.
- Phase 4: canonical typed record spine.
- Phase 5: source-backed exact-work authority import from the ledger/Lean files present in the second zip.
- Phase 6: first live vertical slice.
- Phase 7: ProjectX outer-kernel binding through state, eval, control, and review.
- Phase 8: handoff, authority, archive, and blocker docs.

## Implemented Live Path

Entry points:

- Inner pipeline: `python -m pg_pipeline.scripts.run_batch`
- ProjectX supervised run: `projectx.control.pipeline_runner.run_research_pipeline(...)`

Live outputs:

- `weekly_summary.json`
- typed JSON records
- `records.sqlite`
- `projectx_eval.json`
- `ReviewDecisionRecord`
- typed exact-work authority records from `exact_work/authority_catalog.yaml`
- `projectx/kernel/state/state.json`

## Source Scope

The nested `final_repo_bundle` reference and any separate GitHub/final-repo source are intentionally ignored. They are not inputs to this merge.

Current source-backed behavior:

- The live vertical slice uses the `grassmannian_small` MVP from `555.txt`.
- The research ledger zip contributes handoff and Lean authority files.
- The ledger/Lean authority is imported into typed `GeometryRecord` records.
- No nested bundle or external GitHub repository is treated as required.

## Verification

Last verification completed:

- `pytest -q`: 2 passed
- `python -m compileall -q projectx pg_pipeline tests`: passed
- supervised ProjectX pipeline run: passed
- exact-work authority import: 4 typed records
- no zip files inside `merged_repo`
- no `__pycache__` directories left inside `merged_repo`
