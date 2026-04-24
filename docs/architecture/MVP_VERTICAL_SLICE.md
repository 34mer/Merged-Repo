# MVP Vertical Slice

Run:

```powershell
python -m pg_pipeline.scripts.run_batch
```

Outer supervised run:

```powershell
@'
from pathlib import Path
from projectx.control.pipeline_runner import run_research_pipeline
print(run_research_pipeline(Path("runs/projectx_supervised")).summary)
'@ | python -
```

Expected lifecycle:

1. Generate `GeometryRecord` objects.
2. Normalize geometry records.
3. Emit one recurrence `ProposalRecord`.
4. Run symbolic and combinatorial `CheckResultRecord` checks.
5. Run held-out and symmetry-break `StressResultRecord` stresses.
6. Emit one `SubstrateSchemaRecord`.
7. ProjectX emits one `ReviewDecisionRecord`.
8. ProjectX records run continuity in `projectx/kernel/state/state.json`.

