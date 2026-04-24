# Proof / Checker Obligations

This file lists the required formal/checker work implied by the R1-R14 discriminator ledger.

Nothing in this file is automatically solved. These are explicit obligations that prevent thread-state claims from being silently promoted into theorem authority.

## Global obligations

| Obligation | Scope | Required tool layer | Status |
|---|---|---|---|
| O1 | Source-bind every row R1-R14 to exact paper excerpts, exact-work files, or explicit generated status | source/PDF retrieval + artifact ledger | OPEN |
| O2 | Convert each row predicate into a typed predicate object | Python/Pydantic or Lean structure | OPEN |
| O3 | Produce full row × class matrix | Python ledger generator | OPEN |
| O4 | Separate source-backed, generated, bridge, and open claims | schema/status checker | PARTIAL |
| O5 | Add formal failure conditions for each discriminator | checker/proof obligation records | OPEN |
| O6 | Preserve no-substrate-commitment invariant | ledger invariant checker | PARTIAL |
| O7 | Keep `CRBSM` generated-only unless explicitly proven otherwise | ledger invariant checker | PARTIAL |

## Row-specific obligations

| Row | Required next check | Tool layer | Status |
|---|---|---|---|
| R1 | Formalize unit codimension descent uniformly across `A`, `C`, `M1`; verify no hidden non-unit descent in current baselines. | Python/Sage finite enumerators; later Lean predicates | OPEN |
| R2 | Define equivalence relation on local move classes; prove/count primitive move multiplicity per family. | Python/Sage graph/poset enumeration | OPEN |
| R3 | Formalize nested-history / linear-extension burden and compare against ordinary deletion descent. | Python/Sage combinatorics; possible Z3 obstruction | OPEN |
| R4 | Bind exact finite `A,D4,E6` closure to Lean/exact-work authority and block generated `D_n` promotion. | Lean/exact-work audit | PARTIAL |
| R5 | Preserve explicit top-interaction representative formulas in machine-readable record. | JSON + Lean mirror | OPEN |
| R6 | Check support-node orbit coefficient law inside solved branch only. | Lean/exact-work audit | PARTIAL |
| R7 | Check parabolic residue recursion statement and scope. | Lean/exact-work audit | PARTIAL |
| R8 | Define root-bundle/local transport predicate and scope. | Lean/Python formalization | OPEN |
| R9 | Define grouped-carrier predicate per family and populate full matrix. | source extraction + schema | OPEN |
| R10 | Define grouped-parameter dictionary per family. | source extraction + schema | OPEN |
| R11 | Define grouped-factorization predicate and checker. | SymPy/Sage/Python | OPEN |
| R12 | Formalize overlap/submodular law and source-bind inequality/equality cases. | Z3/SymPy finite predicate + source ledger | OPEN |
| R13 | Formalize equality-layer status values: absent / inequality / degenerate equality / intrinsic equality. | Z3/Sage predicate model; later Lean | OPEN |
| R14 | Complete grouped-carrier equation layer and full class-matrix closure. | all layers | OPEN / DEFICIT |

## Mandatory non-promotion rule

A row may not be promoted to `CHECKED` unless the repo contains:

1. a machine-readable row record,
2. a source/provenance binding,
3. a predicate definition,
4. a checker/proof obligation result,
5. a failure mode or counterexample policy.

## Current uploaded state

The uploaded state is now:

- R1-R14 human-readable ledger
- R1-R14 machine-readable JSON ledger
- realization-class matrix
- R2/R3 typed comparison slice
- this proof/checker obligation file

This is still not theorem certification.
