# Repo Hygiene Policy

## Scope

This policy is path-based, reversible, and non-destructive.

It classifies current repo mass into:
- `keep_canonical`
- `keep_evidence`
- `ignore_noncanonical`
- `archive_candidate`
- `maybe_review`

No deletion or move is authorized by this document alone.

## Canonical Rule

Unless future evidence proves otherwise, treat `d:\Project X\extracted` as the canonical bounded external harness/bridge line.

Do **not** treat clone exhaust, temp probes, caches, or generated run mass as canonical by default.

## Keep Canonical

- `d:\Project X\extracted\system\**`
- `d:\Project X\extracted\kernel\**`
- `d:\Project X\extracted\schemas\**`
- `d:\Project X\extracted\scripts\**`
- `d:\Project X\extracted\world_contact_fixture\**`
- `d:\Project X\extracted\operational_targets\**`
- `d:\Project X\extracted\run_*.py`
- `d:\Project X\extracted\README.md`

These paths are load-bearing source / state / runner mass.

## Keep Evidence

- `d:\Project X\extracted\experiments\**`
- `d:\Project X\experiments\**`
- `d:\Project X\extracted\logs\**`

These paths are non-canonical as source, but preserve proof artifacts, rerun evidence, and historical run outputs.

Keep them until a separate archive pass is explicitly authorized.

## Ignore Noncanonical

- `d:\Project X\codex_tmp\**`
- `d:\Project X\kernel_zero_*\**`
- `d:\Project X\probe_*\**`
- `d:\Project X\extracted\__pycache__\**`

Treat these as:
- temp clone mass
- probe branches
- cache artifacts
- non-load-bearing by default

Do not use them as proof authority or source of truth.

## Archive Candidates

- `d:\Project X\extracted\live_exec_temp\**`
- `d:\Project X\kernel-zero-recovery-surgery-lineage-feedback-coupled.zip`

These are obvious candidates for later archive / quarantine because they are large, generated, and not canonical source.

Do not delete or move them in this turn.

## Maybe Review

- `d:\Project X\extracted\examples\**`
- `d:\Project X\extracted\eval\**`

These may remain useful as fixtures or benchmark inputs, but they are not assumed canonical source by default.

Review them only when a new proof lane explicitly needs them.

## Reversibility Rule

Any future cleanup action must be:
- path-specific
- reversible
- recorded
- justified against this policy

## Operational Rule

When citing authoritative repo state:
- cite canonical source from `d:\Project X\extracted\system\**` or `d:\Project X\extracted\kernel\**`
- cite proof artifacts from `d:\Project X\extracted\experiments\**`
- do not cite `codex_tmp`, `kernel_zero_*`, or `probe_*` mass as canonical evidence
