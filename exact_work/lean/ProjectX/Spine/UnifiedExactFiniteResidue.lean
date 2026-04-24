import Mathlib
import ProjectX.Spine.AffineResidueCore
import ProjectX.Spine.SolvedAmbientGeometry
import ProjectX.Spine.Gr2AmbientGeometry

namespace ProjectX

/-- Unified affine residue data for the exact `A`-family branch.
The support direction survives, and the coefficient receives the exact `-1` correction responsible
for the descent `n ↦ n - 1`. -/
def affineResidueData_Gr2 : AffineResidueData Gr2Support Gr2Support where
  sign := .plus
  keep
    | .paired => some .paired
  correction
    | .paired => -1

/-- The affine residue interface recovers the exact lower `Gr_+(2,n-1)` representative. -/
theorem affineResidue_Gr2_eq_prev (G : Gr2Ambient) :
    affineResidue affineResidueData_Gr2 (gr2AmbientRep G) = gr2FacetTargetRep G .short := by
  apply TopClassRep.ext
  · simp [affineResidue, gr2AmbientRep, gr2FacetTargetRep, muGr2Rep]
    omega
  · intro s
    cases s
    simp [affineResidue, affineResidueData_Gr2, gr2AmbientRep, gr2FacetTargetRep, muGr2Rep]

/-- Unified affine residue data for the solved `D₄ -> A₃` branch. -/
def affineResidueData_Gr36_to_A3 : AffineResidueData Gr36Support Gr2Support :=
  zeroCorrectionAffine residueData_Gr36_to_A3.sign residueData_Gr36_to_A3.keep

/-- The affine residue interface recovers the solved `D₄ -> A₃` target. -/
theorem affineResidue_Gr36_to_A3_eq_target :
    affineResidue affineResidueData_Gr36_to_A3 muGr36Rep = muA3ParabolicRep := by
  rw [affineResidue_eq_residue_of_zeroCorrection
      (r := affineResidueData_Gr36_to_A3) (μ := muGr36Rep)]
  · simpa [affineResidueData_Gr36_to_A3, residueData_Gr36_to_A3, zeroCorrectionAffine,
      residueRep_Gr36_to_A3, residueAlongFacet, branchRep, facetTargetRep, facetResidueData,
      muA3ParabolicRep] using parabolicRecursion_Gr36_to_A3
  · intro s
    cases s <;> simp [affineResidueData_Gr36_to_A3, zeroCorrectionAffine]

/-- Unified affine residue data for the solved `E₆ -> A₅` branch. -/
def affineResidueData_Gr37_to_A5 : AffineResidueData Gr37Support Gr2Support :=
  zeroCorrectionAffine residueData_Gr37_to_A5.sign residueData_Gr37_to_A5.keep

/-- The affine residue interface recovers the solved `E₆ -> A₅` target. -/
theorem affineResidue_Gr37_to_A5_eq_target :
    affineResidue affineResidueData_Gr37_to_A5 muGr37Rep = muA5ParabolicRep := by
  rw [affineResidue_eq_residue_of_zeroCorrection
      (r := affineResidueData_Gr37_to_A5) (μ := muGr37Rep)]
  · simpa [affineResidueData_Gr37_to_A5, residueData_Gr37_to_A5, zeroCorrectionAffine,
      residueRep_Gr37_to_A5, residueAlongFacet, branchRep, facetTargetRep, facetResidueData,
      muA5ParabolicRep] using parabolicRecursion_Gr37_to_A5
  · intro s
    cases s <;> simp [affineResidueData_Gr37_to_A5, zeroCorrectionAffine]

/-- Unified affine residue data for the carried `E₆ -> D₅` shadow branch. -/
def affineResidueData_Gr37_to_D5Shadow : AffineResidueData Gr37Support SingleSupport :=
  zeroCorrectionAffine residueData_Gr37_to_D5Shadow.sign residueData_Gr37_to_D5Shadow.keep

/-- The affine residue interface recovers the carried `E₆ -> D₅` shadow target. -/
theorem affineResidue_Gr37_to_D5Shadow_eq_target :
    affineResidue affineResidueData_Gr37_to_D5Shadow muGr37Rep = muD5ShadowRep := by
  rw [affineResidue_eq_residue_of_zeroCorrection
      (r := affineResidueData_Gr37_to_D5Shadow) (μ := muGr37Rep)]
  · simpa [affineResidueData_Gr37_to_D5Shadow, residueData_Gr37_to_D5Shadow,
      zeroCorrectionAffine, residueRep_Gr37_to_D5Shadow, residueAlongFacet, branchRep,
      facetTargetRep, facetResidueData, muD5ShadowRep] using parabolicRecursion_Gr37_to_D5Shadow
  · intro s
    cases s <;> simp [affineResidueData_Gr37_to_D5Shadow, zeroCorrectionAffine]

/-- The full exact finite branch now shares one affine residue interface:
- `A`-family via nonzero correction
- `D₄/E₆` solved side via zero correction
-/
inductive ExactFiniteAffineResidueCase where
  | gr2_family
  | gr36_to_A3
  | gr37_to_A5
  | gr37_to_D5Shadow
  deriving DecidableEq, Repr

end ProjectX
