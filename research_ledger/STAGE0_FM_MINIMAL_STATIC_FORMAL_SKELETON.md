# Stage 0 Formation Medium Minimal Static Formal Skeleton

STATUS: GENERATED / OPEN / MATH_FIRST / FINITE_STATIC_MODEL / NOT_SOURCE_EXTRACTED / NOT_THEOREM / NOT_PHYSICS  
TARGET: STAGE0-FM-MINIMAL-STATIC-FORMAL-SKELETON  
ARTIFACT ROLES: STAGE0 / STATIC_GEOMETRY / FORMAL_SKELETON / RED_TEAM / NEGATIVE_CONTROL  
DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json

## 0. Non-Promotion Notice

This Stage 0 skeleton is a minimal formal attack artifact. It is not a theorem, not source extraction, not a final object definition, not a physical substrate, not engineering readiness, and not proof that Formation Medium exists.

It is intentionally pre-physics.

It exists to stop the project from continuing by source shopping, physics analogy, validator-first work, or tool-driven motion.

## 1. Actual Mathematical Object

The current object is:

```text
a finite static support/residue surrogate for the Gr_+(1,n) positive simplex tower
plus a Gr_+(0,n) terminal atom convention
```

It models:

```text
terminal atom
simplex faces
residue deletion
ordered deletion signs
minimal readout
non-faithful bulk/readout cover
pre-physics settling as residue descent
```

It does not model:

```text
full positive Grassmannian geometry
canonical forms as source-extracted theorem
amplitudes
physical substrate
native dynamics
engineering implementation
```

## 2. Definitions Fixed Before Computation

### OBJ_LABEL_SET

```text
[n] = {1,...,n}
```

Finite ordered label set. Current Stage 0 finite range:

```text
2 <= n <= 8
```

### OBJ_TERMINAL_ATOM

```text
A_n ~ Gr_+(0,n)
```

A unique terminal atom with scalar readout:

```text
Omega(A_n) = 1
```

This is a convention in this skeleton, not theorem status.

### OBJ_STATIC_SIMPLEX_FACE

For every nonempty support subset:

```text
S subset [n], S != empty
```

define:

```text
F_S
```

Interpretation:

```text
coordinate face/support object of the Gr_+(1,n) simplex tower
```

Dimension:

```text
dim(F_S) = |S| - 1
```

### OBJ_RESIDUE_DELETION

If `i in S` and `|S| > 1`:

```text
Res_i(F_S) = F_{S \ {i}}
```

If `S = {i}`:

```text
Res_i(F_S) = A_n
```

Undefined if:

```text
i notin S
```

### OBJ_ORDERED_ROUTE_SIGN

For a deletion route:

```text
D = (d_1,...,d_m)
```

where `D` is an ordering of the deleted label set, define:

```text
sign(D) = (-1)^{inv(D)}
```

relative to ascending order on the deleted label set.

Adjacent swaps flip sign.

This is a finite orientation surrogate, not source-extracted canonical-form theorem status.

### OBJ_READOUT_MAP

Minimal readout:

```text
rho(F_S) = S
rho(A_n) = terminal
```

The readout records support/terminal structure, not coordinates or measurement values.

### OBJ_BULK_COVER

Let `D_bulk` be a finite decoration set with `|D_bulk| >= 2`.

Define bulk states:

```text
B_{S,a}
```

with map:

```text
pi(B_{S,a}) = F_S
```

This creates intentional non-faithfulness:

```text
B_{S,a} and B_{S,b} have the same readout when a != b
```

This is not physical bulk. It is only a typed toy cover.

### OBJ_SETTLING_RELATION

Before physics, settling is only:

```text
directed residue descent
```

Each step deletes one support label and strictly decreases support size:

```text
F_S -> F_{S \ {i}}
```

or reaches terminal atom:

```text
F_{ {i} } -> A_n
```

This is not native dynamics.

## 3. Smallest Literal Finite Object

The smallest object is `n=2`:

```text
F_{1,2}
F_{1}
F_{2}
A_2
```

Residues:

```text
Res_1(F_{1,2}) = F_2
Res_2(F_{1,2}) = F_1
Res_1(F_1) = A_2
Res_2(F_2) = A_2
```

The first nontrivial ordered-route parity comparison appears at `n=3`, where two deletion orders can reach the same target singleton.

## 4. First Finite Check Targets

### FC1 — Face Counts

Range:

```text
2 <= n <= 8
```

Expected:

```text
number of nonterminal faces = 2^n - 1
number of d-dimensional faces = binomial(n, d+1)
```

Falsifier:

```text
Any count mismatch invalidates the support-subset simplex model.
```

### FC2 — Residue Closure and Acyclicity

Expected:

```text
Every defined residue step lands in a smaller support face or terminal atom.
No directed cycles exist.
```

Falsifier:

```text
A residue step that does not reduce support size destroys settling-as-residue-descent.
```

### FC3 — Route Parity Coherence

Expected:

```text
Adjacent swaps of deletion routes flip sign.
Route signs match permutation parity relative to ascending deleted labels.
```

Falsifier:

```text
If adjacent swaps do not flip sign, SG2 ordered residue sign/coherence is not represented.
```

### FC4 — Non-Faithful Bulk Cover

Expected with decoration count `>=2`:

```text
Each nonterminal readout face has at least two bulk preimages under pi.
```

Falsifier:

```text
If fibers are singleton, the skeleton has no non-faithfulness even as a toy model.
```

### FC5 — Terminal Route Count

Expected:

```text
from full support [n] to terminal A_n there are n! deletion routes
for n >= 2, even_count = odd_count = n!/2
```

Falsifier:

```text
Parity imbalance for n>=2 indicates route-sign implementation error.
```

## 5. Computed Stage 0 Result

Range checked:

```text
2 <= n <= 8
```

Method:

```text
exact Python enumeration of finite support subsets and deletion-route permutations
```

Result:

```text
PASS_FINITE_STATIC_MODEL_CHECKS
```

This means only:

```text
the support-subset static skeleton is internally coherent for these finite checks
```

It does not mean:

```text
all-n theorem
source-extracted geometry
definitive Formation Medium object
physical substrate
```

## 6. Tool Plan

### Python

Use now for:

```text
exact finite enumeration for n <= 8
witness table generation
```

### polymake

Use next for:

```text
simplex face-lattice confirmation
comparison against support-subset model
```

Status:

```text
available: polymake 4.11 through D-backed WSL distro Ubuntu-24.04-D
```

### Sage

Use next for:

```text
symbolic/log-form sanity checks
oriented simplex residue experiments after sign conventions stabilize
```

Status:

```text
available: SageMath 9.5 through D-backed WSL distro Ubuntu-22.04-D
```

### Lean/Lake

Use after Stage 1 statement extraction for:

```text
typed definitions
route parity theorem skeleton
residue decreases rank theorem skeleton
```

### Z3

Optional use for:

```text
bounded predicate consistency / counterexample search
```

### Ax-Prover / Aristotle

Use only after Lean theorem statements exist.

Output remains candidate until local Lean validation.

## 7. Stage 1 Formal Targets

### STAGE1-STATIC-FACE-TYPE

```text
Define a finite type of nonempty support faces F_S over Fin n plus terminal atom A_n.
```

### STAGE1-RESIDUE-DECREASES-RANK

```text
For every defined residue deletion Res_i(F_S), support size strictly decreases or reaches terminal.
```

### STAGE1-ADJACENT-SWAP-FLIPS-SIGN

```text
For deletion routes differing by one adjacent transposition, route parity signs differ by -1.
```

### STAGE1-BULK-READOUT-NONFAITHFUL

```text
For decoration_count >= 2, pi(B_{S,a}) = F_S has fiber size decoration_count for each nonterminal face.
```

## 8. Red-Team Falsifiers

```text
The terminal atom convention may be mathematically wrong or too coarse compared with source-backed canonical residue semantics.
The support-subset model may capture only face combinatorics and not canonical forms, positivity, or amplitudes.
Route parity may be a bookkeeping sign rather than SG2 ordered residue sign/coherence.
The non-faithful bulk cover is artificial; it proves only that non-faithfulness can be typed, not that Formation Medium has a natural bulk.
Settling as residue descent may be the wrong pre-physics abstraction if native formation should settle to nonterminal readout rather than terminal residues.
If mutation transport SG4 cannot be added as a nontrivial atlas operation, this Stage 0 skeleton remains static-only and insufficient.
```

## 9. Blocked Promotions

```text
finite support-subset checks are not source-extracted claims
route parity is not yet canonical form orientation theorem
bulk cover is not physical bulk
settling relation is not native dynamics
Stage 0 skeleton is not final Formation Medium definition
Stage 0 skeleton does not resume physical-regime winner claims
```

## 10. Recommended Next

Move to Stage 1 typed formal target extraction for:

```text
support faces
residue deletion
route parity
bulk/readout non-faithfulness
```

Then run polymake simplex face-lattice confirmation as a Stage 2 cross-check.

Do not resume SN-C3 / Ising / high-resonance physical comparison until Stage 1 targets are at least stated.

## 11. Non-Promotion Footer

This Stage 0 skeleton is a minimal formal attack artifact. It is not a theorem, not source extraction, not a final object definition, not a physical substrate, not engineering readiness, and not proof that Formation Medium exists.
