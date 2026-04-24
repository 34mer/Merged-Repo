# ProjectX / 111 Merge Import Matrix

Generated: 2026-04-23

## Import Rule

ProjectX is the outer operating kernel. The positive-geometry pipeline from the `111-555` planning files becomes the inner typed research subsystem. The research ledger / exact-work bundle becomes the mathematical authority and artifact pack. Raw imports are preserved only where they carry provenance or irreplaceable evidence.

Tags:

- `keep as canonical`: promote directly into the merged canonical tree.
- `adapt`: reuse the substance, but wrap, rename, split, or translate into the canonical layout.
- `archive`: preserve with provenance, but do not make it an operational dependency.
- `discard`: exclude from the merged repo.

## Source Inventory

| Source | Observed status | Merge role |
| --- | --- | --- |
| `ProjectX_extracted.zip` | Valid archive. Contains ProjectX runtime tree plus duplicated `live_exec_temp`, logs, experiments, kernel state, harnesses, schemas, scripts. | Outer kernel source. Curated import only. |
| `research-ledger-v1-clean-main.zip` | Valid archive. Contains Lean scaffold, ProjectX theorem spine, and handoff package. Nested bundle references are ignored. | Exact-work authority source and Lean secondary scaffold. |
| Nested `final_repo_bundle` / separate GitHub repo | Ignored by user instruction. | Not an input to this merge. |
| `111.txt` | Planning spec for mission, Layer 0 memory, generator/checker boundaries, failure controls. | Governing doctrine for `pg_pipeline`. |
| `222.txt` | Service topology, stack, `pgcore` package, module boundaries. | Adapt into canonical monorepo boundaries. |
| `333.txt` | Concrete Pydantic schema/interface spec, records, API boundaries, recurrence DSL, controller state machine. | Adapt into canonical record spine. |
| `444.txt` | Final merged architecture: one Python monorepo, typed records, logical service boundaries, proposal/check/stress/substrate flow. | Canonical repo shape authority. |
| `555.txt` | MVP starter tree and first runnable vertical slice. | First implementation target. |

## Canonical Destination Shape

```text
repo_root/
  projectx/
    kernel/
    system/
    eval/
    review/
    control/
    schemas_runtime/
  pg_pipeline/
    pgcore/
    kb/
    generators/
    normalize/
    propose/
    check/
    search/
    stress/
    substrate/
    configs/
    scripts/
  exact_work/
    scripts/
    outputs/
    notes/
    handoff/
    lean/
  archive/
    imported_raw/
    deprecated/
```

## ProjectX Import Matrix

| Source path | Tag | Destination | Decision |
| --- | --- | --- | --- |
| `ProjectX_extracted/system/kernel_store.py` | keep as canonical | `projectx/system/kernel_store.py` | Runtime store is core outer-kernel infrastructure. |
| `ProjectX_extracted/system/provenance.py` | keep as canonical | `projectx/system/provenance.py` | Provenance behavior belongs to ProjectX runtime, later bridged to `pgcore` provenance records. |
| `ProjectX_extracted/system/session_runner.py` | adapt | `projectx/control/session_runner.py` | Keep scheduling/session behavior but move under control surface and decouple from old paths. |
| `ProjectX_extracted/system/state_extractor.py` | adapt | `projectx/system/state_extractor.py` | Useful state extraction; adapt to distinguish runtime state from scientific truth records. |
| `ProjectX_extracted/system/memory_abstraction.py` | adapt | `projectx/system/memory_abstraction.py` | Keep as outer memory abstraction, not as the scientific KB. |
| `ProjectX_extracted/system/memory_controller.py` | adapt | `projectx/control/memory_controller.py` | Control-layer component; bridge to `pg_pipeline/kb` only through typed adapters. |
| `ProjectX_extracted/system/context_composer.py` | adapt | `projectx/control/context_composer.py` | Useful for continuity/control context; must not produce untyped scientific claims. |
| `ProjectX_extracted/system/integrity_guard.py` | keep as canonical | `projectx/system/integrity_guard.py` | Outer integrity guard remains canonical. |
| `ProjectX_extracted/system/writeback.py` | adapt | `projectx/system/writeback.py` | Keep writeback mechanics, add canonical destination constraints. |
| `ProjectX_extracted/system/workspace_roots.py` | adapt | `projectx/system/workspace_roots.py` | Replace hard-coded/import-era paths with merged repo roots. |
| `ProjectX_extracted/system/world_contact_*.py` | archive | `archive/imported_raw/projectx/system/` | Preserve as prior operational surface; not part of first scientific vertical slice. |
| `ProjectX_extracted/system/constitutional_*.py` | adapt | `projectx/control/` and `projectx/review/` | Promote only modules needed for control, review, rollback, lineage, and execution policy. Archive the rest. |
| `ProjectX_extracted/system/causal_*.py` | adapt | `projectx/eval/` or `projectx/control/` | Keep selected dependency/impact/outcome logic after direct code review. Archive unneeded harness-specific variants. |
| `ProjectX_extracted/system/*_harness.py` | adapt | `projectx/control/harnesses/` | Reusable harness runners become indexed harnesses, not root scripts. |
| `ProjectX_extracted/eval/*.py` | keep as canonical | `projectx/eval/` | Drift, coherence, burden, and report modules are outer-kernel eval surfaces. |
| `ProjectX_extracted/schemas/*.schema.json` | adapt | `projectx/schemas_runtime/` | Runtime schemas only; do not mix with `pgcore` scientific Pydantic schemas. |
| `ProjectX_extracted/kernel/state.json` | archive | `archive/imported_raw/projectx/kernel/state.json` | Preserve old runtime state as provenance. New state must be initialized cleanly. |
| `ProjectX_extracted/kernel/anchor.json` | archive | `archive/imported_raw/projectx/kernel/anchor.json` | Preserve as continuity evidence, not canonical live state. |
| `ProjectX_extracted/kernel/integrity.json` | archive | `archive/imported_raw/projectx/kernel/integrity.json` | Preserve as import-era integrity state. |
| `ProjectX_extracted/kernel/provenance.json` | archive | `archive/imported_raw/projectx/kernel/provenance.json` | Preserve source identity. Runtime provenance should be regenerated in merged layout. |
| `ProjectX_extracted/kernel/decisions.json` | archive | `archive/imported_raw/projectx/kernel/decisions.json` | Old decision ledger is evidence, not live review state. |
| `ProjectX_extracted/kernel/task_graph.json` | archive | `archive/imported_raw/projectx/kernel/task_graph.json` | Old task graph should not drive new scheduler directly. |
| `ProjectX_extracted/kernel/*.md` | adapt | `projectx/kernel/notes/` and `exact_work/notes/` | Promote only operating doctrine and substrate notes that survive review. |
| `ProjectX_extracted/kernel/constitutional_*.json` | archive | `archive/imported_raw/projectx/kernel/` | Preserve as previous harness outputs/state. Do not import as live truth. |
| `ProjectX_extracted/experiments/*` | archive | `archive/imported_raw/projectx/experiments/` | Archive raw experiment forest. Surface only an index and selected reusable harnesses. |
| `ProjectX_extracted/examples/*` | archive | `archive/imported_raw/projectx/examples/` | Examples are provenance/test fixtures, not canonical runtime. |
| `ProjectX_extracted/operational_targets/*` | archive | `archive/imported_raw/projectx/operational_targets/` | Preserve; reconsider after first vertical slice works. |
| `ProjectX_extracted/world_contact_fixture/*` | archive | `archive/imported_raw/projectx/world_contact_fixture/` | Out of scope for first scientific pipeline. |
| `ProjectX_extracted/scripts/run_*.py` | adapt | `projectx/control/harnesses/` or `projectx/scripts/` | Thin wrappers only if they invoke promoted harnesses. |
| `ProjectX_extracted/live_exec_temp/*` | discard | none | Duplicate extracted runtime/temp tree. Do not import. |
| `ProjectX_extracted/logs/*` | discard by default | none | Runtime logs are bloat. Preserve only if a specific run is needed as evidence. |
| `ProjectX_extracted/__pycache__`, nested `__pycache__` | discard | none | Generated cache. |
| `ProjectX_extracted/benchmark_profile.prof` | discard | none | Old profile output, not canonical. |

## Research Ledger / Exact Work Import Matrix

| Source path | Tag | Destination | Decision |
| --- | --- | --- | --- |
| `research-ledger-v1-clean-main/handoff/00_READ_THIS_FIRST.md` | keep as canonical | `exact_work/handoff/00_READ_THIS_FIRST.md` | Cold-start authority and non-negotiable stance. |
| `research-ledger-v1-clean-main/handoff/10_MACHINE_STATE.json` | archive | `exact_work/handoff/10_MACHINE_STATE.json` | Preserve machine-state snapshot, but do not use as live state. |
| `research-ledger-v1-clean-main/handoff/16_MATH_AUTHORITY_APPENDIX.md` | keep as canonical | `exact_work/handoff/16_MATH_AUTHORITY_APPENDIX.md` | Math authority boundary. |
| `research-ledger-v1-clean-main/handoff/19_THEOREM_DEPENDENCY_GRAPH.md` | keep as canonical | `exact_work/handoff/19_THEOREM_DEPENDENCY_GRAPH.md` | Dependency map for exact/theorem surfaces. |
| `research-ledger-v1-clean-main/handoff/20_CONTINUITY_BEARING_NOTES.md` | keep as canonical | `exact_work/handoff/20_CONTINUITY_BEARING_NOTES.md` | Continuity notes for restart. |
| `research-ledger-v1-clean-main/FORMALIZATION_STATUS.md` | keep as canonical | `exact_work/lean/FORMALIZATION_STATUS.md` | Lean status is secondary but authoritative for formalized claims. |
| `research-ledger-v1-clean-main/PROJECT_X_REPO_MAP.md` | archive | `exact_work/notes/PROJECT_X_REPO_MAP.md` | Useful snapshot map, but not canonical after merge. |
| `research-ledger-v1-clean-main/ProjectX.lean` | keep as canonical | `exact_work/lean/ProjectX.lean` | Lean entrypoint retained under exact-work authority. |
| `research-ledger-v1-clean-main/ProjectXCheck.lean` | keep as canonical | `exact_work/lean/ProjectXCheck.lean` | Lean check entrypoint retained. |
| `research-ledger-v1-clean-main/ProjectX/Spine/*` | keep as canonical | `exact_work/lean/ProjectX/Spine/` | Formal theorem spine. |
| `research-ledger-v1-clean-main/ProjectX/Surfaceology/*` | keep as canonical | `exact_work/lean/ProjectX/Surfaceology/` | Surfaceology formal baseline. |
| `research-ledger-v1-clean-main/ProjectX/CrossFamily/*` | keep as canonical | `exact_work/lean/ProjectX/CrossFamily/` | Cross-family comparison formal baseline. |
| `research-ledger-v1-clean-main/lakefile.lean` | keep as canonical | `exact_work/lean/lakefile.lean` | Lean build scaffold. |
| `research-ledger-v1-clean-main/lean-toolchain` | keep as canonical | `exact_work/lean/lean-toolchain` | Toolchain pin. |
| `research-ledger-v1-clean-main/artifacts/README_uploaded_repo_bundle.md` | discard | none | Refers to ignored nested bundle. |
| `research-ledger-v1-clean-main/artifacts/final_repo_bundle.zip` | discard | none | Nested bundle is explicitly out of scope. |
| `research-ledger-v1-clean-main/README.md` | archive | `archive/imported_raw/research-ledger/README.md` | README prose is not authority. |

## Planning Files Import Matrix

| Source path | Tag | Destination | Decision |
| --- | --- | --- | --- |
| `111.txt` | adapt | `docs/architecture/111_pipeline_mission.md` | Convert into concise doctrine: mission, Layer 0 records, allowed model/tool/human boundaries. |
| `222.txt` | adapt | `docs/architecture/service_boundaries.md` | Convert service topology into monorepo logical boundaries. |
| `333.txt` | adapt | `pg_pipeline/pgcore/schemas/` and `docs/architecture/record_spine.md` | Implement Pydantic schemas; preserve interface spec as documentation. |
| `444.txt` | adapt | `docs/architecture/merged_architecture.md` | Canonical architecture map. |
| `555.txt` | adapt | `pg_pipeline/` starter tree and `docs/architecture/mvp_vertical_slice.md` | First runnable vertical slice specification. |
| Raw `111.txt` through `555.txt` | archive | `archive/imported_raw/planning/` | Preserve original planning provenance. |

## Canonical Record Spine

The following records become canonical in `pg_pipeline/pgcore/schemas/`:

- `GeometryRecord`
- `RepresentationMapRecord`
- `FailedConjectureRecord`
- `ProposalRecord`
- `CheckResultRecord`
- `StressResultRecord`
- `SubstrateSchemaRecord`
- `ReviewDecisionRecord`
- `JobRecord`

Boundary rule:

- ProjectX runtime state is stored under `projectx/`.
- Scientific truth records are stored under `pg_pipeline/pgcore` and `pg_pipeline/kb`.
- Imported scripts/outputs/handoff/Lean files are stored under `exact_work/`.
- Raw source snapshots and deprecated material are stored under `archive/`.

## First Live Slice Decision

Use the `555.txt` MVP unless later inspection of exact scripts changes the family choice:

- family: `grassmannian_small`
- proposal type: recurrence
- checks: symbolic and combinatorial
- stress: held-out larger `n` plus symmetry-breaking mutation
- output: one `SubstrateSchemaRecord`

This is intentionally narrower than the final target family list. The merge is not considered alive until this slice runs under ProjectX control and produces a typed substrate draft with provenance.

## Blockers / Follow-up

1. ProjectX contains many overlapping `constitutional_*`, `causal_*`, and recovery/surgery harness variants. Before copying code, inspect imports and call graphs and promote only the modules required by the first vertical slice.
2. The old ProjectX `kernel/*.json` files must not become live state. They are continuity/provenance snapshots only.
3. Lean remains secondary in v1. Keep it buildable and authority-bearing, but do not expand Lean until the Python record lifecycle runs end to end.

## Immediate Next Import Order

1. Create merged root skeleton.
2. Copy/adapt `projectx/eval`, selected `projectx/system`, and selected `projectx/control` modules.
3. Create `pg_pipeline` starter tree from `555.txt`.
4. Implement `pgcore` record spine from `333.txt`.
5. Copy exact-work handoff and Lean scaffold under `exact_work/`.
6. Archive raw planning files, raw ProjectX experiment forest, old kernel state, and unreadable nested bundle.
7. Build the first live vertical slice.
