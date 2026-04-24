# R1-R14 Discriminator Ledger

This file externalizes the thread-level discriminator state that was not fully uploaded in the first R2-R3-only PR.

It is an authority/continuity ledger, not a theorem certification file.

Status tags:

- `SOURCE-BACKED`: tied to uploaded papers / exact-work handoff / Lean authority files.
- `THREAD-SUPPORTED`: established by repeated thread comparison but not yet formalized as a source-bound theorem.
- `GENERATED`: internally generated construction; not source authority.
- `OPEN`: unresolved; must not be used as assumption.
- `DEFICIT`: known missing formal/source layer.

## Current object

Extract exact computable families from positive-geometry / amplitudes / cosmological-geometry papers, compare which structures survive across families, then use stronger mathematics to distinguish realization classes before any substrate or engineering commitment.

## Class / family handles

| Handle | Meaning | Current authority |
|---|---|---|
| `A` | associahedron / noncrossing diagonal family | exact baseline |
| `M1` | amplituhedron `m=1` sign-vector family | exact baseline |
| `C` | cosmohedron / Matryoshka family | exact baseline through finite cases |
| `GAssoc` | graph-associahedral / cosmological-polytope vicinity | source-backed comparison object |
| `S` | surfaceology curve-word family | exact local baseline; global footing incomplete |
| `PGfinite` | exact finite positive-Grassmannian top-cell closure | `A`, `D4`, `E6` only |
| `CRBSM` | generated substrate/proxy candidate | generated only; not object |

## Row ledger

| Row | Name | Core predicate | Current status | Current verdict / use |
|---|---|---|---|---|
| R1 | Unit codimension descent | Boundary descent proceeds by unit codimension moves. | THREAD-SUPPORTED | Survives across associahedron, cosmohedron, amplituhedron `m=1`; useful as shared lower layer, not a class discriminator by itself. |
| R2 | Local move multiplicity | The family has more than one primitive immediate-face/local cover move. | THREAD-SUPPORTED | Cosmohedron has at least two local cover moves (`delete_nonminimal`, `collapse_children`); associahedron and `m=1` amplituhedron each have one basic descent primitive in current baseline. Candidate cosmohedron-specific discriminator. |
| R3 | Nested-history / linear-extension burden | Objects/faces carry strong nested-history or linear-extension data beyond ordinary deletion descent. | THREAD-SUPPORTED | Appears cosmohedron-specific in current finite baseline. Requires broader source/formal check before theorem-level use. |
| R4 | Exact finite positive-Grassmannian top-cell closure | Safe finite closure consists only of `A`, `D4`, `E6`. | SOURCE-BACKED / EXACT-WORK | Non-negotiable authority state. Do not extend to `D_n` beyond `D4` as exact. |
| R5 | Top-interaction coefficient representatives | Explicit top-interaction representatives: `[mu_Gr+(2,n)] = n u_{n-4}`, `[mu_Gr+(3,6)] = 4 u_3 Omega_D`, `[mu_Gr+(3,7)] = u_5(7 omega_A + 14 omega_D)`. | SOURCE-BACKED / EXACT-WORK | Must be carried explicitly; not compressed into vague coefficient language. |
| R6 | Support-node orbit law | Paired support node coefficient is `h+2`; fixed support node coefficient is `(h+2)/2`. | SOURCE-BACKED / EXACT-WORK | Coefficient law inside solved exact branch only; not arbitrary continuation. |
| R7 | Parabolic residue recursion | Fully supporting parabolic facets carry lower top-interaction class as residue, `Res_Y(mu_Gamma)=±mu_Gamma'`. | SOURCE-BACKED / EXACT-WORK | Safe recursive descent through solved branch only. |
| R8 | Root-bundle / local transport layer | Intrinsic rank-`m` residue-family bundle and local `A2` quarter-turn transport law. | THREAD-SUPPORTED / EXACT-WORK | Candidate faithful local transport layer. Does not imply literal substrate realization. |
| R9 | Grouped carriers | Family admits grouped carriers / grouped subsets supporting factorization or compatibility data. | THREAD-SUPPORTED | Shared by graph-associahedral/cosmological and cosmohedral side; not enough to distinguish R2/R3. |
| R10 | Grouped parameters / weights | Family has grouped parameters such as `delta_P` / grouped weights. | THREAD-SUPPORTED | Shared lower layer between graph-associahedral vicinity and cosmohedral construction. |
| R11 | Grouped factorization | Factorization is expressible at grouped-carrier/grouped-parameter level. | THREAD-SUPPORTED | Shared lower layer; does not separate R2/R3. |
| R12 | Overlap / submodular inequality law | Grouped parameters obey overlap/submodular inequalities of the form `delta_P + delta_P' <= delta_union + delta_intersection`. | SOURCE-BACKED / THREAD-SUPPORTED | Shared by generalized-permutahedron / graph-associahedron side and cosmohedron-related grouped laws; not the final R2/R3 discriminator. |
| R13 | Equality-layer status | Equality layer is typed as absent / generic inequality / degenerate equality / intrinsic equality. | THREAD-SUPPORTED | Current strongest R2/R3 discriminator: graph-associahedral vicinity reaches equalities by specialization/degeneration; cosmohedron requires many equalities intrinsically in its grouped compatibility law. |
| R14 | Missing grouped-carrier equation / full class-matrix deficit | The exact equation layer and class matrix must be source-bound and formalized across all surviving rows/classes. | DEFICIT / OPEN | Not solved. This is the known gap: complete R1-R14 × class matrix, source bindings, proof/check obligations, and unresolved discriminators. |

## Current solved comparison

### R2/R3 branch comparison

`GAssoc` and `C` share:

- grouped carriers
- grouped parameters / weights
- grouped factorization
- overlap/submodular inequality layer

They differ at:

- equality-layer status

Current typed verdict:

```text
GAssoc: equality layer appears by special saturation / degeneration
C:      equality layer is intrinsic to grouped compatibility / nontransversal gluing
```

Therefore current thread verdict:

```text
GAssoc != C as realization classes
C <= GAssoc as equality-saturated specialization/refinement
```

This verdict is `THREAD-SUPPORTED`, not Lean-certified.

## Missing uploads fixed by this file

The previous GitHub patch only encoded the R2/R3 comparison slice. This file uploads the broader R1-R14 discriminator ledger and explicitly marks the unresolved R14 deficit.

## Next required formal work

1. Convert this ledger into machine-readable JSON.
2. Add row/class matrix records.
3. Add source-provenance bindings per row.
4. Add check/proof-obligation records per unresolved row.
5. Do not promote `R14` to solved until the grouped-carrier equation layer and full class matrix are formalized.
