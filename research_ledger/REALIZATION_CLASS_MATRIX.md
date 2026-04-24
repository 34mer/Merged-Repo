# Realization-Class Matrix

This matrix records current thread-state comparisons. It is intentionally conservative: unknown cells stay `OPEN` rather than being silently inferred.

## Class handles

- `A`: associahedron / noncrossing diagonal family
- `M1`: amplituhedron `m=1` sign-vector family
- `C`: cosmohedron / Matryoshka family
- `GAssoc`: graph-associahedral / cosmological-polytope vicinity
- `S`: surfaceology curve-word family
- `PGfinite`: exact finite positive-Grassmannian top-cell closure `A,D4,E6`

## Pairwise comparison status

| Pair | Status | Shared rows | Separating rows | Verdict |
|---|---|---|---|---|
| `GAssoc` vs `C` | THREAD-SUPPORTED | R9, R10, R11, R12 | R13 | Distinct but ordered: `C <= GAssoc` as equality-saturated specialization/refinement. |
| `A` vs `C` | PARTIAL | R1 | R2, R3 candidate | Cosmohedron carries additional local move multiplicity and nested-history burden in current finite baseline. Needs source-bound formalization. |
| `M1` vs `C` | PARTIAL | R1 | R2, R3 candidate | Cosmohedron carries additional local move multiplicity and nested-history burden. `M1` sign descent has one basic primitive in current baseline. |
| `A` vs `M1` | OPEN/PARTIAL | R1 | none currently finalized | Both share unit descent but have different native representations; no finalized realization-class verdict uploaded. |
| `S` vs `A` | OPEN | unknown | unknown | Surfaceology not yet on equal global footing. |
| `S` vs `M1` | OPEN | unknown | unknown | Surfaceology not yet on equal global footing. |
| `S` vs `C` | OPEN | local update/factorization motifs possible | unknown | Surfaceology exact local baseline exists, but global family footing incomplete. |
| `PGfinite` vs `S` | PARTIAL | coefficient/family classifier comparison exists in exact-work | invariant-slot difference/one-step direction in conservative schema | Existing Lean scaffold compares conservative profiles only; not full realization-class verdict. |

## Matrix rule

Do not convert `PARTIAL` into `SUPPORTED` without:

1. explicit row predicate,
2. family coverage,
3. source/provenance binding,
4. checker/proof obligation,
5. failure condition.

## Current completed upload

The previous PR uploaded only the `GAssoc` vs `C` / R13 slice. This file uploads the remaining pairwise continuity state and marks unresolved cells explicitly.
