import Mathlib
import ProjectX.Surfaceology.ExtractedFamilyFactorization

namespace ProjectX
namespace Surfaceology

section CommRing
variable {K : Type _} [CommRing K]

/-- At the current conservative level, equality of global signature classes is exactly equality of
extracted family data. -/
theorem signatureClass_eq_iff_sameExtractedFamilyDatum (C₁ C₂ : CurveObject (K := K)) :
    C₁.signatureClass = C₂.signatureClass ↔ C₁.extractedFamilyDatum = C₂.extractedFamilyDatum := by
  rw [← sameSignature_iff_sameExtractedFamilyDatum]
  constructor
  · intro h
    exact Quotient.exact h
  · intro h
    exact Quotient.sound h

/-- At the current conservative level, equality of global conservative-profile classes is exactly
equality of extracted family data. -/
theorem constraintProfileClass_eq_iff_sameExtractedFamilyDatum (C₁ C₂ : CurveObject (K := K)) :
    C₁.constraintProfileClass = C₂.constraintProfileClass ↔ C₁.extractedFamilyDatum = C₂.extractedFamilyDatum := by
  rw [← sameConstraintProfile_iff_sameExtractedFamilyDatum]
  constructor
  · intro h
    exact Quotient.exact h
  · intro h
    exact Quotient.sound h

/-- The extracted family datum map on the global signature quotient is injective. -/
theorem SignatureClass.extractedFamilyDatum_injective :
    Function.Injective (SignatureClass.extractedFamilyDatum (K := K)) := by
  intro Q₁ Q₂ hQ
  refine Quotient.inductionOn₂ Q₁ Q₂ ?_ hQ
  intro C₁ C₂ h
  apply Quotient.sound
  exact (sameSignature_iff_sameExtractedFamilyDatum C₁ C₂).2 h

/-- The extracted family datum map on the global conservative-profile quotient is injective. -/
theorem ConstraintProfileClass.extractedFamilyDatum_injective :
    Function.Injective (ConstraintProfileClass.extractedFamilyDatum (K := K)) := by
  intro Q₁ Q₂ hQ
  refine Quotient.inductionOn₂ Q₁ Q₂ ?_ hQ
  intro C₁ C₂ h
  apply Quotient.sound
  exact (sameConstraintProfile_iff_sameExtractedFamilyDatum C₁ C₂).2 h

/-- On a fixed-base fixed-length family, equality of extracted family data is exactly total-weight
equality. -/
theorem fixedBaseLength_sameExtractedFamilyDatum_theorem {base : CurveMatrix K} {n : Nat}
    (C₁ C₂ : SurfaceologyFamily (K := K) base n) :
    C₁.1.extractedFamilyDatum = C₂.1.extractedFamilyDatum ↔ C₁.1.totalWeight = C₂.1.totalWeight := by
  rw [← fixedBaseLength_signatureClass_theorem (C₁ := C₁) (C₂ := C₂),
      signatureClass_eq_iff_sameExtractedFamilyDatum]

/-- On a fixed-base fixed-length family, equality of fixed classes is exactly equality of extracted
family data. -/
theorem fixedBaseLength_class_eq_iff_sameExtractedFamilyDatum {base : CurveMatrix K} {n : Nat}
    (C₁ C₂ : SurfaceologyFamily (K := K) base n) :
    C₁.fixedClass = C₂.fixedClass ↔ C₁.1.extractedFamilyDatum = C₂.1.extractedFamilyDatum := by
  rw [fixedBaseLength_classification_theorem (C₁ := C₁) (C₂ := C₂),
      ← fixedBaseLength_sameExtractedFamilyDatum_theorem (C₁ := C₁) (C₂ := C₂)]

/-- The fixed-base fixed-length class is completely determined by the extracted family datum of any
representative. -/
theorem fixedBaseLength_class_determined_by_extractedFamilyDatum {base : CurveMatrix K} {n : Nat}
    (C₁ C₂ : SurfaceologyFamily (K := K) base n)
    (hD : C₁.1.extractedFamilyDatum = C₂.1.extractedFamilyDatum) :
    C₁.fixedClass = C₂.fixedClass :=
  (fixedBaseLength_class_eq_iff_sameExtractedFamilyDatum (C₁ := C₁) (C₂ := C₂)).2 hD

end CommRing

end Surfaceology
end ProjectX
