# Import Manifest

## Promoted

- ProjectX eval modules into `projectx/eval`.
- Selected ProjectX system modules into `projectx/system`.
- ProjectX runtime schemas into `projectx/schemas_runtime`.
- ProjectX kernel notes into `projectx/kernel/notes`.
- Research-ledger handoff files into `exact_work/handoff`.
- Research-ledger Lean scaffold into `exact_work/lean`.
- `111-555` planning logic into architecture docs and `pg_pipeline`.

## Adapted

- ProjectX control became `projectx/control/pipeline_runner.py`, a thin supervisor over the typed pipeline.
- ProjectX review became `projectx/review/decisions.py`.
- ProjectX continuity state became `projectx/kernel/state_store.py`.
- Ledger/Lean family authority became `exact_work/authority_catalog.yaml` plus typed authority records.

## Archived

- Original planning files.
- Old ProjectX kernel JSON snapshots.
- Raw ProjectX experiment forest.
- Historical ProjectX control graph that pulled in too many old dependencies.

## Discarded

- caches
- logs
- temp execution trees
- nested bundle references

