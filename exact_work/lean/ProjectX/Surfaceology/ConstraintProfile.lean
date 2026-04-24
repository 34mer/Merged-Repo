import Mathlib
import ProjectX.Surfaceology.FamilySignature

namespace ProjectX
namespace Surfaceology

section CommRing
variable {K : Type _} [CommRing K]

/-- A conservative profile of the currently provable global surfaceology constraints.

This is not a full extracted family classification. It packages the strongest global structure the
repo currently proves on the surfaceology side:
- one-step generation by extending a word
- length grading
- determinant scaling by total weight
- signature extraction by base/length/total weight
-/
structure ConstraintProfile where
  signature : FamilySignature K
  detValue : K

/-- Extract the current conservative constraint profile from a curve object. -/
def CurveObject.constraintProfile (C : CurveObject (K := K)) : ConstraintProfile :=
  { signature := C.signature
    detValue := C.det }

@[simp] theorem CurveObject.constraintProfile_signature (C : CurveObject (K := K)) :
    C.constraintProfile.signature = C.signature := rfl

@[simp] theorem CurveObject.constraintProfile_detValue (C : CurveObject (K := K)) :
    C.constraintProfile.detValue = C.det := rfl

/-- The determinant component of the constraint profile is determined by the signature. -/
theorem CurveObject.constraintProfile_det_formula (C : CurveObject (K := K)) :
    C.constraintProfile.detValue = C.signature.totalWeight * det C.signature.base := by
  simp [CurveObject.constraintProfile, CurveObject.det_depends_only_on_signature]

/-- One-step update law for the conservative constraint profile. -/
def ConstraintProfile.snoc (P : ConstraintProfile (K := K)) (t : WeightedTurn K) : ConstraintProfile :=
  { signature := P.signature.snoc t
    detValue := t.weight * P.detValue }

@[simp] theorem CurveObject.constraintProfile_snoc (C : CurveObject (K := K)) (t : WeightedTurn K) :
    (C.snoc t).constraintProfile = C.constraintProfile.snoc t := by
  apply congrArg (fun d => { signature := (C.snoc t).signature, detValue := d })
    (CurveObject.det_snoc C t)
  -- The signature field is definitionally aligned after rewriting.
  simp [CurveObject.constraintProfile, ConstraintProfile.snoc, CurveObject.signature_snoc,
    CurveObject.det_snoc]

/-- Equality of signatures forces equality of the full conservative constraint profile. -/
theorem sameSignature_sameConstraintProfile (C₁ C₂ : CurveObject (K := K))
    (hσ : C₁.signature = C₂.signature) :
    C₁.constraintProfile = C₂.constraintProfile := by
  cases C₁
  cases C₂
  simp [CurveObject.constraintProfile, CurveObject.signature] at hσ ⊢
  subst hσ
  simp

end CommRing

end Surfaceology
end ProjectX
