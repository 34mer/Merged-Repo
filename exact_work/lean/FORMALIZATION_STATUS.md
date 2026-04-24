# Theorem Spine Formalization Status

This file records the current status of Lean formalization inside this reconstructed Project X baseline.

## Formalized now in Lean

### 1. Static residue atom (core portion)
Implemented in `ProjectX/Spine/Support.lean`:
- `Pole`
- `residueSign`
- simp theorems for the two boundary poles

This covers the most reduced formal core of the static residue base.

### 2. Support-node coefficient law
Implemented in `ProjectX/Spine/Support.lean`:
- `SupportNodeType`
- `supportCoefficient`
- concrete derived coefficient formulas for:
  - `Gr_+(2,n)` coefficient `n` (under the domain hypothesis `2 ≤ n`)
  - `Gr_+(3,6)` coefficient `4`
  - `Gr_+(3,7)` / `Gr_+(4,7)` fixed/paired split `7 : 14`

### 3. Local `A_2` quarter-turn transport
Implemented in `ProjectX/Spine/QuarterTurn.lean`:
- active adjacent pair indices
- `quarterTurn`
- pointwise formulas on left/right/off-pair coordinates
- square action on the active pair

### 4. Exact finite-branch coefficient layer
Implemented in `ProjectX/Spine/FiniteClosure.lean`:
- coefficient-level representatives for the exact finite positive-Grassmannian top-cell closure
- explicit coefficient formulas for `A`, `D4`, `E6`
- a formal marker that the exact finite closure currently safe in this repository is `A`, `D4`, `E6`

### 5. Class-level coefficient representatives
Implemented in `ProjectX/Spine/ClassLevel.lean`:
- `TopClassRep`
- named support types for the current exact branch
- representative objects `muGr2Rep`, `muGr36Rep`, `muGr37Rep`
- explicit coefficient theorems at representative-object level

This is stronger than bare coefficient scalars, but still weaker than full ambient cohomology classes.

### 6. Geometric residue interface
Implemented in `ProjectX/Spine/GeometryInterface.lean`:
- `OrientationSign`
- `ResidueData`
- a genuine residue operator on finite support types
- finite support instances for the exact support families currently formalized

This is the first honest geometric interface layer beyond coefficient summaries.

### 7. Unified affine residue core
Implemented in `ProjectX/Spine/AffineResidueCore.lean`:
- `AffineResidueData`
- `affineResidue`
- theorem reducing affine residue to the earlier residue interface under zero correction
- zero-correction helper constructor

This is the key unification layer that lets the exact `A`-family branch and the solved `D4/E6` side live in one residue framework.

### 8. Class-representative residue recursion
Implemented in `ProjectX/Spine/ResidueRecursion.lean`:
- actual class-representative residue computations for solved branches:
  - `D4 -> A3`
  - `E6 -> A5`
  - `E6 -> D5` shadow support carry

This is stronger than a scalar carry: the repo now carries residue as an operator on representative objects, not only a handoff-level statement.

### 9. Named parabolic target objects and recursion theorems
Implemented in:
- `ProjectX/Spine/ParabolicTargets.lean`
- `ProjectX/Spine/ParabolicRecursion.lean`

The repo now contains:
- named parabolic target representatives (`A₃`, `A₅`, `D₅` shadow)
- object-equality theorems matching solved residue outputs to those targets
- named parabolic-recursion theorems packaging the solved branch recursion as theorem objects

This is the strongest formalization of the solved residue branch currently carried here.

### 10. Minimal ambient solved-branch geometry (`D4` / `E6` side)
Implemented in `ProjectX/Spine/SolvedAmbientGeometry.lean`:
- named solved exact branches (`Gr_+(3,6)` and `Gr_+(3,7)` representatives)
- named supporting facets for those branches
- support types, target objects, and residue data attached to those facets
- ambient residue-along-facet theorem and degree-lowering theorem

This is the first ambient solved-branch geometry carried in Lean for the exact solved `D4/E6` branch.

### 11. Ambient `Gr_+(2,n)` exact branch geometry
Implemented in `ProjectX/Spine/Gr2AmbientGeometry.lean`:
- ambient exact branch object for `Gr_+(2,n)` / `Gr_+(n-2,n)`
- named supporting short facet
- ambient residue theorem landing on the exact lower representative `Gr_+(2,n-1)`
- degree-lowering theorem and explicit coefficient theorem

### 12. Unified exact finite ambient residue interface
Implemented in `ProjectX/Spine/UnifiedExactFiniteResidue.lean` and `ProjectX/Spine/ExactFiniteAmbientUnified.lean`:
- a single affine residue interface instantiated across the full exact finite branch
- `A`-family via nonzero correction
- `D4/E6` via zero-correction specialization
- one unified ambient exact-finite branch/facet type
- one unified theorem:
  - residue along any currently formalized exact finite supporting facet lands on the named target representative for that facet

At the representative/ambient level, this closes the exact finite branch under one residue framework.

### 13. Surfaceology local exact baseline
Implemented in `ProjectX/Surfaceology/LocalUpdate.lean`:
- local curve matrix `M_C`
- entry sum `F_C`
- determinant `det M_C`
- rational invariant `u_C`
- primitive local updates `eL` and `eR`
- exact formulas for updated matrix entries
- exact formulas for updated `F`
- exact determinant scaling by the new edge weight under both primitive moves
- exact `u`-update formulas under the necessary nonzero hypotheses

This opens the surfaceology front inside Lean rather than leaving it only in the handoff.

### 14. Surfaceology word semantics
Implemented in `ProjectX/Surfaceology/WordSemantics.lean`:
- turn directions and weighted turns
- global word evaluation on curve matrices
- total edge-weight product
- determinant scaling across an arbitrary word
- theorem that determinant scaling depends only on total weight, not left/right pattern

This moves surfaceology beyond one-step updates into global word-level semantics.

### 15. Surfaceology global object and recursion
Implemented in:
- `ProjectX/Surfaceology/GlobalObject.lean`
- `ProjectX/Surfaceology/GlobalRecursion.lean`

The repo now carries:
- a global curve object formalizing the chain `C -> M_C -> F_C -> u_C`
- determinant formula at the object level
- one-step extension `snoc`
- global `F` recursion theorems under left/right extension
- global `u` recursion theorems under left/right extension and the necessary nonzero hypotheses

This is the strongest surfaceology dynamics formalization currently carried here.

### 16. Surfaceology family signature and conservative constraint profile
Implemented in:
- `ProjectX/Surfaceology/FamilySignature.lean`
- `ProjectX/Surfaceology/ConstraintProfile.lean`

The repo now carries:
- a conservative global signature extractor by base / length / total weight
- signature update under one-step extension
- determinant dependence on signature
- a conservative constraint profile packaging signature plus determinant value
- one-step update law for the constraint profile
- theorem that equal signatures force equal conservative constraint profiles

This is the first classifier-style surfaceology layer available for future cross-family comparison.

### 17. Surfaceology quotient classification by extracted signature
Implemented in `ProjectX/Surfaceology/Classification.lean`:
- signature-equivalence relation
- quotient signature classes
- induced one-step evolution on signature classes
- equivalence between same-signature and same conservative-constraint-profile
- class-level conservative constraint profile
- theorem that class evolution respects the profile snoc law

This is the first actual quotient/classification layer on the surfaceology side.

### 18. Surfaceology quotient classification by conservative constraint profile
Implemented in `ProjectX/Surfaceology/ProfileClassification.lean`:
- profile-equivalence setoid
- quotient profile classes
- equivalence between signature classes and profile classes
- class-level profile extraction
- induced one-step evolution on profile classes
- theorem that profile-class evolution respects the profile snoc law

This tightens the classifier side and makes explicit that, at the current conservative level, profile classes and signature classes carry the same information.

### 19. Fixed-base fixed-length surfaceology classification
Implemented in:
- `ProjectX/Surfaceology/FixedBaseLengthClassification.lean`
- `ProjectX/Surfaceology/FixedBaseLengthProfile.lean`
- `ProjectX/Surfaceology/FixedBaseLengthBridge.lean`
- `ProjectX/Surfaceology/ClassificationTheorems.lean`

The repo now carries:
- the theorem that for fixed base and fixed length, the current conservative classification collapses to total-weight equality
- fixed-base fixed-length quotient classes
- canonical class-level signature, determinant value, and conservative constraint profile
- bridge maps from fixed-base/length classes into the global signature/profile quotient layers
- injectivity and commuting snoc laws for those bridge maps
- packaged classification theorems restated at the levels of fixed classes, global signature classes, and global profile classes
- a canonical current invariant object for fixed-base fixed-length classes together with its snoc law

This is the strongest current family-classification statement available on the surfaceology side.

### 20. Surfaceology extracted family datum and factorization
Implemented in:
- `ProjectX/Surfaceology/ExtractedFamilyDatum.lean`
- `ProjectX/Surfaceology/ExtractedFamilyFactorization.lean`
- `ProjectX/Surfaceology/ExtractedFamilyClassification.lean`

The repo now carries:
- an explicit extracted family datum packaging base, length, total weight, determinant value, and their exact relation
- extraction of that datum from curve objects and fixed-base fixed-length classes
- factorization of the current signature/profile stack through the extracted family datum
- the theorem that, at the current conservative level, equality of extracted family data is equivalent to equality of global signature classes and to equality of global profile classes
- injectivity of the extracted-family-datum map on the global quotient classifiers
- commuting snoc laws for extracted family data on objects, fixed classes, and the global quotient classifiers
- the theorem that on fixed-base fixed-length families, equality of extracted family data is exactly total-weight equality and exactly fixed-class equality

This makes the extracted family datum the clearest current conservative family object on the surfaceology side.

### 21. Conservative cross-family comparison schema
Implemented in:
- `ProjectX/CrossFamily/Schema.lean`
- `ProjectX/CrossFamily/Instances.lean`
- `ProjectX/CrossFamily/ComparisonTheorems.lean`

The repo now carries:
- one shared conservative comparison profile schema for both the exact finite Grassmannian side and the current surfaceology extracted-family side
- exact-finite and surfaceology instances of that schema
- readiness theorems showing both sides satisfy the current conservative comparison requirements
- theorems showing that surfaceology currently matches the single-slot exact finite branches (`A` and `D4`) in invariant-slot count, but differs from the two-slot `E6` branch
- the theorem that the current surfaceology family object and the exact finite branch have opposite one-step recursion directions in the shared schema
- the theorem that the fixed-base fixed-length surfaceology comparison profile is determined by extracted family datum

This is the first explicit formal cross-family comparison interface carried in Lean.

## Not yet formalized in Lean

### A. Full cohomology-class objects
The following remain carried by the handoff and are not yet formalized as genuine cohomology objects in Lean:
- `[μ_{Gr_+(2,n)}] = n·u_{n-4}` as an actual class-level object
- `[μ_{Gr_+(3,6)}] = 4·u_3·Ω_D` as an actual class-level object
- `[μ_{Gr_+(3,7)}] = u_5(7·ω_A + 14·ω_D)` as an actual class-level object

Current Lean files formalize representative/coefficient data, not the full ambient geometry.

### B. Full positive-geometry/cohomology infrastructure
The exact statement

`Res_Y(μ_Γ) = ± μ_{Γ'}`

is still not encoded against a concrete full Lean model of facets, residues, and positive-geometry/cohomology objects. The repo currently carries the exact finite branch at the representative/ambient level, not the full positive-geometry ambient infrastructure.

### C. Surfaceology equal global footing
Surfaceology is no longer only handoff-carried: the local baseline, word semantics, global object, global recursion, family grading, signature, conservative constraint profile, quotient classifications, fixed-base/length classification theorem layers, extracted family datum, and a conservative cross-family comparison schema are formalized. But it is still not yet on equal exact-family footing with associahedron / cosmohedron / amplituhedron in the sense of a globally extracted family classification with surviving substrate-constraint comparison.

### D. Generated continuations
The following remain outside exact Lean authority here:
- additive/formal generated branches (ACBM / RCSS / etc.)
- abstract `D_n` continuation beyond exact `D4`
- CRBSM and all realization-class generation

## Reading rule
Use Lean files for the formalized coefficient/transport core plus representative, residue-interface, ambient exact-branch, unified exact-finite residue, surfaceology local/word/global/classifier/extracted-family layers, and the conservative cross-family comparison schema.
Use the handoff for the broader exact/generated/provisional boundary until the remaining geometry is formalized.
