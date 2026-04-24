import Mathlib
import ProjectX.Surfaceology.ConstraintProfile

namespace ProjectX
namespace Surfaceology

section CommRing
variable {K : Type _} [CommRing K]

/-- Two curve objects are signature-equivalent if they have the same extracted conservative global
signature. -/
def SameSignature (C₁ C₂ : CurveObject (K := K)) : Prop :=
  C₁.signature = C₂.signature

@[refl] theorem SameSignature.refl (C : CurveObject (K := K)) : SameSignature C C := rfl
@[symm] theorem SameSignature.symm {C₁ C₂ : CurveObject (K := K)} :
    SameSignature C₁ C₂ → SameSignature C₂ C₁ := by
  intro h
  simpa [SameSignature] using h.symm
@[trans] theorem SameSignature.trans {C₁ C₂ C₃ : CurveObject (K := K)} :
    SameSignature C₁ C₂ → SameSignature C₂ C₃ → SameSignature C₁ C₃ := by
  intro h12 h23
  simpa [SameSignature] using h12.trans h23

/-- Setoid induced by the extracted signature. -/
def signatureSetoid (K : Type _) [CommRing K] : Setoid (CurveObject (K := K)) where
  r := SameSignature
  iseqv := ⟨SameSignature.refl, SameSignature.symm, SameSignature.trans⟩

/-- Quotient of curve objects by the extracted conservative signature. -/
abbrev SignatureClass (K : Type _) [CommRing K] := Quotient (signatureSetoid K)

/-- Class of a curve object modulo extracted signature. -/
def CurveObject.signatureClass (C : CurveObject (K := K)) : SignatureClass K :=
  Quotient.mk _ C

/-- Extending by one weighted turn respects signature-equivalence. -/
theorem SameSignature.snoc {C₁ C₂ : CurveObject (K := K)}
    (h : SameSignature C₁ C₂) (t : WeightedTurn K) :
    SameSignature (C₁.snoc t) (C₂.snoc t) := by
  simpa [SameSignature] using congrArg (fun σ => σ.snoc t) h

/-- One-step evolution induced on signature classes. -/
def SignatureClass.snoc (Q : SignatureClass K) (t : WeightedTurn K) : SignatureClass K := by
  refine Quotient.liftOn Q (fun C => C.signatureClass |> fun _ => (C.snoc t).signatureClass) ?_
  intro C₁ C₂ h
  exact Quotient.sound (SameSignature.snoc h t)

/-- Two curve objects with the same signature have the same conservative constraint profile. -/
theorem SameSignature.sameConstraintProfile {C₁ C₂ : CurveObject (K := K)}
    (h : SameSignature C₁ C₂) : C₁.constraintProfile = C₂.constraintProfile :=
  sameSignature_sameConstraintProfile C₁ C₂ h

/-- Conservative-constraint-profile equivalence. -/
def SameConstraintProfile (C₁ C₂ : CurveObject (K := K)) : Prop :=
  C₁.constraintProfile = C₂.constraintProfile

theorem sameSignature_iff_sameConstraintProfile (C₁ C₂ : CurveObject (K := K)) :
    SameSignature C₁ C₂ ↔ SameConstraintProfile C₁ C₂ := by
  constructor
  · intro h
    exact SameSignature.sameConstraintProfile h
  · intro h
    simpa [SameConstraintProfile, SameSignature] using congrArg ConstraintProfile.signature h

/-- The conservative constraint profile is constant on a signature class. -/
def SignatureClass.constraintProfile (Q : SignatureClass K) : ConstraintProfile K := by
  refine Quotient.liftOn Q (fun C => C.constraintProfile) ?_
  intro C₁ C₂ h
  exact SameSignature.sameConstraintProfile h

/-- Extending a signature class updates its conservative constraint profile by the profile snoc law. -/
theorem SignatureClass.constraintProfile_snoc (Q : SignatureClass K) (t : WeightedTurn K) :
    (SignatureClass.snoc Q t).constraintProfile = (Q.constraintProfile).snoc t := by
  refine Quotient.inductionOn Q ?_
  intro C
  simp [SignatureClass.snoc, SignatureClass.constraintProfile, CurveObject.constraintProfile_snoc]

end CommRing

end Surfaceology
end ProjectX
