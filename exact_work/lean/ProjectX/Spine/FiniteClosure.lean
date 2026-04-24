import ProjectX.Spine.Support

namespace ProjectX

/-- Coefficient-level formalization of the exact finite positive-Grassmannian top-cell closure.

This file formalizes the coefficient spine only:
- `Gr_+(2,n)` / `Gr_+(n-2,n)` coefficient `n`
- `Gr_+(3,6)` coefficient `4`
- `Gr_+(3,7)` / `Gr_+(4,7)` fixed/paired split `7 : 14`

It does **not** formalize the full cohomology classes yet. Those remain carried by the handoff
and must be connected to explicit geometry later.
-/

/-- Exact coefficient representative for `Gr_+(2,n)` at the top-interaction layer. -/
def topCoeff_Gr2 (n : Nat) : Nat := gr2Coeff n

theorem topCoeff_Gr2_formula {n : Nat} (h : 2 ≤ n) : topCoeff_Gr2 n = n := by
  simpa [topCoeff_Gr2] using gr2Coeff_formula h

/-- Exact coefficient representative for `Gr_+(3,6)`. -/
def topCoeff_Gr36 : Nat := gr36Coeff

theorem topCoeff_Gr36_formula : topCoeff_Gr36 = 4 := by
  simpa [topCoeff_Gr36] using gr36Coeff_formula

/-- Exact fixed-node coefficient representative for `Gr_+(3,7)` / `Gr_+(4,7)`. -/
def topCoeff_Gr37_fixed : Nat := gr37FixedCoeff

theorem topCoeff_Gr37_fixed_formula : topCoeff_Gr37_fixed = 7 := by
  simpa [topCoeff_Gr37_fixed] using gr37FixedCoeff_formula

/-- Exact paired-node coefficient representative for `Gr_+(3,7)` / `Gr_+(4,7)`. -/
def topCoeff_Gr37_paired : Nat := gr37PairedCoeff

theorem topCoeff_Gr37_paired_formula : topCoeff_Gr37_paired = 14 := by
  simpa [topCoeff_Gr37_paired] using gr37PairedCoeff_formula

/-- Formal reminder of the exact closure currently safe in the project state. -/
inductive ExactFinitePositiveGrassmannianTopCell where
  | A_branch
  | D4_branch
  | E6_branch
  deriving DecidableEq, Repr

/-- Any continuation outside `A`, `D₄`, `E₆` is not yet part of the exact positive-Grassmannian
finite top-cell closure in this repository. -/
def isInExactFiniteClosure : ExactFinitePositiveGrassmannianTopCell → Prop
  | .A_branch => True
  | .D4_branch => True
  | .E6_branch => True

end ProjectX
