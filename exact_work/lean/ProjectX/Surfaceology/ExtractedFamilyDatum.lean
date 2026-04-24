import Mathlib
import ProjectX.Surfaceology.ClassificationTheorems

namespace ProjectX
namespace Surfaceology

section CommRing
variable {K : Type _} [CommRing K]

/-- The current extracted family datum carried by the surfaceology side.

This packages the strongest global family data currently formalized in Lean:
- base matrix
- word length
- total edge-weight invariant
- determinant value, together with the exact relation tying it to the invariant
-/
structure ExtractedFamilyDatum where
  base : CurveMatrix K
  length : Nat
  totalWeight : K
  detValue : K
  det_relation : detValue = totalWeight * det base

/-- Extract the current family datum from a curve object. -/
def CurveObject.extractedFamilyDatum (C : CurveObject (K := K)) : ExtractedFamilyDatum (K := K) :=
  { base := C.base
    length := C.length
    totalWeight := C.totalWeight
    detValue := C.det
    det_relation := by simpa [CurveObject.det_formula] }

/-- Extract the current family datum from a fixed-base fixed-length class. -/
def FixedBaseLengthClass.extractedFamilyDatum {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) : ExtractedFamilyDatum (K := K) :=
  { base := base
    length := n
    totalWeight := Q.totalWeight
    detValue := Q.detValue
    det_relation := by simp [FixedBaseLengthClass.detValue] }

@[simp] theorem CurveObject.extractedFamilyDatum_base (C : CurveObject (K := K)) :
    C.extractedFamilyDatum.base = C.base := rfl

@[simp] theorem CurveObject.extractedFamilyDatum_length (C : CurveObject (K := K)) :
    C.extractedFamilyDatum.length = C.length := rfl

@[simp] theorem CurveObject.extractedFamilyDatum_totalWeight (C : CurveObject (K := K)) :
    C.extractedFamilyDatum.totalWeight = C.totalWeight := rfl

@[simp] theorem CurveObject.extractedFamilyDatum_detValue (C : CurveObject (K := K)) :
    C.extractedFamilyDatum.detValue = C.det := rfl

@[simp] theorem FixedBaseLengthClass.extractedFamilyDatum_base {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) :
    Q.extractedFamilyDatum.base = base := rfl

@[simp] theorem FixedBaseLengthClass.extractedFamilyDatum_length {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) :
    Q.extractedFamilyDatum.length = n := rfl

@[simp] theorem FixedBaseLengthClass.extractedFamilyDatum_totalWeight {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) :
    Q.extractedFamilyDatum.totalWeight = Q.totalWeight := rfl

@[simp] theorem FixedBaseLengthClass.extractedFamilyDatum_detValue {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) :
    Q.extractedFamilyDatum.detValue = Q.detValue := rfl

/-- Recover the current global signature from an extracted family datum. -/
def ExtractedFamilyDatum.signature (D : ExtractedFamilyDatum (K := K)) : FamilySignature K :=
  { base := D.base
    length := D.length
    totalWeight := D.totalWeight }

/-- Recover the current conservative constraint profile from an extracted family datum. -/
def ExtractedFamilyDatum.constraintProfile (D : ExtractedFamilyDatum (K := K)) : ConstraintProfile K :=
  { signature := D.signature
    detValue := D.detValue }

@[simp] theorem CurveObject.signature_eq_extractedFamilyDatum_signature (C : CurveObject (K := K)) :
    C.signature = C.extractedFamilyDatum.signature := rfl

@[simp] theorem CurveObject.constraintProfile_eq_extractedFamilyDatum_constraintProfile
    (C : CurveObject (K := K)) :
    C.constraintProfile = C.extractedFamilyDatum.constraintProfile := rfl

@[simp] theorem FixedBaseLengthClass.signature_eq_extractedFamilyDatum_signature {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) :
    Q.signature = Q.extractedFamilyDatum.signature := rfl

@[simp] theorem FixedBaseLengthClass.constraintProfile_eq_extractedFamilyDatum_constraintProfile
    {base : CurveMatrix K} {n : Nat} (Q : FixedBaseLengthClass (K := K) base n) :
    Q.constraintProfile = Q.extractedFamilyDatum.constraintProfile := rfl

/-- One-step update law on extracted family data. -/
def ExtractedFamilyDatum.snoc (D : ExtractedFamilyDatum (K := K)) (t : WeightedTurn K) :
    ExtractedFamilyDatum (K := K) :=
  { base := D.base
    length := D.length + 1
    totalWeight := t.weight * D.totalWeight
    detValue := t.weight * D.detValue
    det_relation := by
      rw [D.det_relation]
      ring }

@[simp] theorem CurveObject.extractedFamilyDatum_snoc (C : CurveObject (K := K)) (t : WeightedTurn K) :
    (C.snoc t).extractedFamilyDatum = C.extractedFamilyDatum.snoc t := by
  ext <;>
    simp [CurveObject.extractedFamilyDatum, ExtractedFamilyDatum.snoc,
      CurveObject.length_snoc, CurveObject.det_snoc, CurveObject.signature_snoc,
      CurveObject.signature_totalWeight, mul_assoc]

@[simp] theorem FixedBaseLengthClass.extractedFamilyDatum_snoc {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) (t : WeightedTurn K) :
    (Q.snoc t).extractedFamilyDatum = Q.extractedFamilyDatum.snoc t := by
  ext <;>
    simp [FixedBaseLengthClass.extractedFamilyDatum, ExtractedFamilyDatum.snoc,
      FixedBaseLengthClass.totalWeight_snoc, FixedBaseLengthClass.detValue_snoc, mul_assoc]

/-- Equality of extracted family data implies equality of all current conservative classifier
objects attached to a curve object. -/
theorem sameExtractedFamilyDatum_implies_sameCurrentClassifiers (C₁ C₂ : CurveObject (K := K))
    (hD : C₁.extractedFamilyDatum = C₂.extractedFamilyDatum) :
    C₁.signature = C₂.signature ∧ C₁.constraintProfile = C₂.constraintProfile := by
  constructor <;>
  simpa using congrArg (fun D => D.signature) hD
  simpa using congrArg (fun D => D.constraintProfile) hD

end CommRing

end Surfaceology
end ProjectX
