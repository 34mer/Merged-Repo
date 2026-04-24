# Formal Verifier Handoff

This directory is the bridge from source extraction ledgers to external formal/checking tools.

It does not implement Aristotle, Lean, Sage, Z3, or any solver. It gives those tools exact work packets.

## Purpose

Use the model as an extraction/formalization front-end and use external verifiers/checkers as the truth filter.

Workflow:

1. Read `research_ledger/SOURCE_EXTRACTED_CLAIMS.json`.
2. Read `research_ledger/FORMAL_CHECK_TARGETS.json`.
3. Pick a target from `FORMALIZATION_QUEUE.json`.
4. Send the matching packet to Aristotle / Lean / Sage / Z3.
5. Write results back into `research_ledger/FORMAL_CHECK_RESULTS.json` or a checker-specific result artifact.

## Tool roles

- Aristotle / Ax-Prover / Lean: proof search and theorem checking.
- Sage / polymake: finite combinatorics, face posets, polytope/fan checks.
- Z3: finite logical/constraint consistency checks.
- Python/SymPy: glue code and symbolic sanity checks.

## Non-promotion rule

A target being listed here is not evidence. Only checked outputs can promote status.

`SOURCE_EXTRACTED` is not `CHECKED`.

`DEFINED_NOT_RUN` is not mathematical support.
