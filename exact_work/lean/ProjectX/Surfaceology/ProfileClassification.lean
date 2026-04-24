import Mathlib
import ProjectX.Surfaceology.Classification

namespace ProjectX
namespace Surfaceology

section CommRing
variable {K : Type _} [CommRing K]

/-- Setoid induced by equality of the conservative constraint profile. -/
def constraintProfileSetoid (K : Type _) [CommRing K] : Setoid (CurveObject (K := K)) where
  r := SameConstraintProfile
  iseqv := by
    refine ⟨?_, ?_, ?_⟩
    · intro C
      rfl
    · intro C₁ C₂ h
      simpa [SameConstraintProfile] using h.symm
    · intro C₁ C₂ C₃ h12 h23
      simpa [SameConstraintProfile] using h12.trans h23

/-- Quotient of curve objects by the conservative constraint profile. -/
abbrev ConstraintProfileClass (K : Type _) [CommRing K] := Quotient (constraintProfileSetoid K)

/-- Class of a curve object modulo conservative constraint profile. -/
def CurveObject.constraintProfileClass (C : CurveObject (K := K)) : ConstraintProfileClass K :=
  Quotient.mk _ C

/-- Profile classes and signature classes carry the same information at the current conservative
classification level. -/
theorem sameSignature_iff_sameProfileClass (C₁ C₂ : CurveObject (K := K)) :
    C₁.signatureClass = C₂.signatureClass ↔ C₁.constraintProfileClass = C₂.constraintProfileClass := by
  constructor
  · intro h
    exact Quotient.sound ((sameSignature_iff_sameConstraintProfile C₁ C₂).mp (Quotient.exact h))
  · intro h
    exact Quotient.sound ((sameSignature_iff_sameConstraintProfile C₁ C₂).mpr (Quotient.exact h))

/-- Extract the conservative constraint profile from a profile class. -/
def ConstraintProfileClass.profile (Q : ConstraintProfileClass K) : ConstraintProfile K := by
  refine Quotient.liftOn Q (fun C => C.constraintProfile) ?_
  intro C₁ C₂ h
  simpa [SameConstraintProfile] using h

/-- One-step evolution induced on profile classes. -/
def ConstraintProfileClass.snoc (Q : ConstraintProfileClass K) (t : WeightedTurn K) : ConstraintProfileClass K := by
  refine Quotient.liftOn Q (fun C => (C.snoc t).constraintProfileClass) ?_
  intro C₁ C₂ h
  apply Quotient.sound
  simpa [SameConstraintProfile] using congrArg (fun P => P.snoc t) h

/-- The class-level profile update law survives quotienting by conservative constraint profile. -/
theorem ConstraintProfileClass.profile_snoc (Q : ConstraintProfileClass K) (t : WeightedTurn K) :
    (ConstraintProfileClass.snoc Q t).profile = (Q.profile).snoc t := by
  refine Quotient.inductionOn Q ?_
  intro C
  simp [ConstraintProfileClass.snoc, ConstraintProfileClass.profile, CurveObject.constraintProfile_snoc]

end CommRing

end Surfaceology
end ProjectX
