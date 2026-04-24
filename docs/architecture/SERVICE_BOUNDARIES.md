# Logical Service Boundaries

The first implementation is a Python monorepo, not a deployed microservice system. The boundaries are still enforced by modules and typed records.

## `pgcore`

Owns schemas, DSL parsing, canonical hashing, IDs, and storage helpers.

## `kb`

Owns typed record ingestion and retrieval. It is the Layer 0 memory surface.

## `generators`

Owns deterministic source-backed data generation/import. Current live generators:

- `grassmannian_small`: MVP proxy family from `555.txt`.
- `ledger_catalog`: source-backed authority records from Lean/handoff files.

## `normalize`

Owns deterministic canonicalization.

## `propose`

Owns DSL-constrained proposals. The current proposer is deterministic; it stands in for the local model boundary without returning free text.

## `check`

Owns truth checks. Current checks are symbolic and combinatorial for the MVP slice.

## `stress`

Owns held-out and mutation attacks.

## `substrate`

Owns substrate draft compilation after checks and stress pass.

## `review`

Owns weekly summaries inside `pg_pipeline`; ProjectX owns outer review decisions.

