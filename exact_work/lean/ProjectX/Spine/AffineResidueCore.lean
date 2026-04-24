import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Data.Finset.Basic
import ProjectX.Spine.GeometryInterface

open scoped BigOperators

namespace ProjectX

/-- A unified residue interface allowing both support-selection transport and an explicit target-side
correction term.

This is the smallest honest generalization that captures:
- the `D4/E6` solved branch, where the correction is zero
- the exact `A`-family branch, where the supporting-facet residue carries the coefficient descent
  `n ↦ n - 1`
-/
structure AffineResidueData (Large Small : Type) where
  sign : OrientationSign
  keep : Large → Option Small
  correction : Small → Int

/-- Residue of a class representative across the affine residue interface. -/
def affineResidue {Large Small : Type} [Fintype Large] [DecidableEq Large] [DecidableEq Small]
    (r : AffineResidueData Large Small) (μ : TopClassRep Large) : TopClassRep Small :=
  { degree := μ.degree - 1
    coeff := fun s =>
      r.correction s +
        r.sign.multiplier *
          ∑ l in Finset.univ.filter (fun l => r.keep l = some s), TopClassRep.coefficient μ l }

@[simp] theorem affineResidue_degree {Large Small : Type} [Fintype Large] [DecidableEq Large]
    [DecidableEq Small] (r : AffineResidueData Large Small) (μ : TopClassRep Large) :
    (affineResidue r μ).degree = μ.degree - 1 := rfl

/-- The zero-correction specialization of affine residue recovers the earlier residue interface. -/
theorem affineResidue_eq_residue_of_zeroCorrection {Large Small : Type}
    [Fintype Large] [DecidableEq Large] [DecidableEq Small]
    (r : AffineResidueData Large Small) (μ : TopClassRep Large)
    (hzero : ∀ s, r.correction s = 0) :
    affineResidue r μ = residue { sign := r.sign, keep := r.keep } μ := by
  apply TopClassRep.ext
  · simp [affineResidue, residue]
  · intro s
    simp [affineResidue, residue, hzero s]

/-- Helper constructor for the common zero-correction case. -/
def zeroCorrectionAffine {Large Small : Type}
    (sign : OrientationSign) (keep : Large → Option Small) : AffineResidueData Large Small :=
  { sign := sign, keep := keep, correction := fun _ => 0 }

@[simp] theorem zeroCorrectionAffine_correction {Large Small : Type}
    (sign : OrientationSign) (keep : Large → Option Small) (s : Small) :
    (zeroCorrectionAffine sign keep).correction s = 0 := rfl

end ProjectX
