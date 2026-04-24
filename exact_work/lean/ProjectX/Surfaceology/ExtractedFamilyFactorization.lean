import Mathlib
import ProjectX.Surfaceology.ExtractedFamilyDatum

namespace ProjectX
namespace Surfaceology

section CommRing
variable {K : Type _} [CommRing K]

/-- At the current conservative level, equality of extracted family data is equivalent to equality of
extracted signatures. -/
theorem sameSignature_iff_sameExtractedFamilyDatum (C₁ C₂ : CurveObject (K := K)) :
    C₁.signature = C₂.signature ↔ C₁.extractedFamilyDatum = C₂.extractedFamilyDatum := by
  constructor
  · intro hsig
    have hbase : C₁.base = C₂.base := by
      simpa [CurveObject.signature] using congrArg FamilySignature.base hsig
    have hlen : C₁.length = C₂.length := by
      simpa [CurveObject.signature] using congrArg FamilySignature.length hsig
    have hwt : C₁.totalWeight = C₂.totalWeight := by
      simpa [CurveObject.signature] using congrArg FamilySignature.totalWeight hsig
    have hdet : C₁.det = C₂.det := signature_eq_implies_det_eq C₁ C₂ hsig
    ext <;> simp [CurveObject.extractedFamilyDatum, hbase, hlen, hwt, hdet]
  · intro hD
    simpa using congrArg (fun D => D.signature) hD

/-- Equality of extracted family data is equivalent to equality of conservative constraint profiles. -/
theorem sameConstraintProfile_iff_sameExtractedFamilyDatum (C₁ C₂ : CurveObject (K := K)) :
    C₁.constraintProfile = C₂.constraintProfile ↔ C₁.extractedFamilyDatum = C₂.extractedFamilyDatum := by
  rw [← sameSignature_iff_sameConstraintProfile, sameSignature_iff_sameExtractedFamilyDatum]

/-- The global signature quotient carries a well-defined extracted family datum. -/
def SignatureClass.extractedFamilyDatum (Q : SignatureClass K) : ExtractedFamilyDatum K := by
  refine Quotient.liftOn Q (fun C => C.extractedFamilyDatum) ?_
  intro C₁ C₂ h
  exact (sameSignature_iff_sameExtractedFamilyDatum C₁ C₂).1 h

/-- The global conservative-profile quotient carries a well-defined extracted family datum. -/
def ConstraintProfileClass.extractedFamilyDatum (Q : ConstraintProfileClass K) : ExtractedFamilyDatum K := by
  refine Quotient.liftOn Q (fun C => C.extractedFamilyDatum) ?_
  intro C₁ C₂ h
  exact (sameConstraintProfile_iff_sameExtractedFamilyDatum C₁ C₂).1 h

@[simp] theorem CurveObject.signatureClass_extractedFamilyDatum (C : CurveObject (K := K)) :
    C.signatureClass.extractedFamilyDatum = C.extractedFamilyDatum := rfl

@[simp] theorem CurveObject.constraintProfileClass_extractedFamilyDatum (C : CurveObject (K := K)) :
    C.constraintProfileClass.extractedFamilyDatum = C.extractedFamilyDatum := rfl

/-- The extracted family datum recovered from the global signature quotient coincides with the datum
recovered from the global conservative-profile quotient. -/
theorem signatureClass_extractedFamilyDatum_eq_profileClass_extractedFamilyDatum (Q : SignatureClass K) :
    Q.extractedFamilyDatum = ((Quotient.liftOn Q (fun C => C.constraintProfileClass)
      (fun C₁ C₂ h => Quotient.sound ((sameSignature_iff_sameConstraintProfile C₁ C₂).1 h))) : ConstraintProfileClass K).extractedFamilyDatum := by
  refine Quotient.inductionOn Q ?_
  intro C
  rfl

/-- One-step evolution on the global signature quotient commutes with extracted family datum snoc. -/
theorem SignatureClass.extractedFamilyDatum_snoc (Q : SignatureClass K) (t : WeightedTurn K) :
    (Q.snoc t).extractedFamilyDatum = Q.extractedFamilyDatum.snoc t := by
  refine Quotient.inductionOn Q ?_
  intro C
  simp [SignatureClass.snoc, SignatureClass.extractedFamilyDatum, CurveObject.extractedFamilyDatum_snoc]

/-- One-step evolution on the global conservative-profile quotient commutes with extracted family
datum snoc. -/
theorem ConstraintProfileClass.extractedFamilyDatum_snoc (Q : ConstraintProfileClass K) (t : WeightedTurn K) :
    (Q.snoc t).extractedFamilyDatum = Q.extractedFamilyDatum.snoc t := by
  refine Quotient.inductionOn Q ?_
  intro C
  simp [ConstraintProfileClass.snoc, ConstraintProfileClass.extractedFamilyDatum,
    CurveObject.extractedFamilyDatum_snoc]

/-- The fixed-base fixed-length bridge to the global signature quotient factors through extracted
family data. -/
theorem FixedBaseLengthClass.toSignatureClass_extractedFamilyDatum_eq {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) :
    (Q.toSignatureClass).extractedFamilyDatum = Q.extractedFamilyDatum := by
  refine Quotient.inductionOn Q ?_
  intro C
  rfl

/-- The fixed-base fixed-length bridge to the global conservative-profile quotient factors through
extracted family data. -/
theorem FixedBaseLengthClass.toConstraintProfileClass_extractedFamilyDatum_eq
    {base : CurveMatrix K} {n : Nat} (Q : FixedBaseLengthClass (K := K) base n) :
    (Q.toConstraintProfileClass).extractedFamilyDatum = Q.extractedFamilyDatum := by
  refine Quotient.inductionOn Q ?_
  intro C
  rfl

end CommRing

end Surfaceology
end ProjectX
