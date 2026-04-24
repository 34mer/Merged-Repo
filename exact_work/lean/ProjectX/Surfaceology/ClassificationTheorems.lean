import Mathlib
import ProjectX.Surfaceology.FixedBaseLengthBridge

namespace ProjectX
namespace Surfaceology

section CommRing
variable {K : Type _} [CommRing K]

/-- Strongest current fixed-base fixed-length classification statement:
for a fixed base matrix and fixed word length, the present conservative surfaceology classification
is exactly total-weight classification. -/
theorem fixedBaseLength_classification_theorem {base : CurveMatrix K} {n : Nat}
    (C₁ C₂ : SurfaceologyFamily (K := K) base n) :
    C₁.fixedClass = C₂.fixedClass ↔ C₁.1.totalWeight = C₂.1.totalWeight := by
  constructor
  · intro h
    exact Quotient.exact h
  · intro h
    exact Quotient.sound h

/-- Same theorem restated at the level of global signature classes: within a fixed-base fixed-length
family, equality of global signature classes is exactly total-weight equality. -/
theorem fixedBaseLength_signatureClass_theorem {base : CurveMatrix K} {n : Nat}
    (C₁ C₂ : SurfaceologyFamily (K := K) base n) :
    C₁.1.signatureClass = C₂.1.signatureClass ↔ C₁.1.totalWeight = C₂.1.totalWeight := by
  rw [← fixedBaseLength_classification_theorem (C₁ := C₁) (C₂ := C₂)]
  constructor
  · intro h
    apply FixedBaseLengthClass.toSignatureClass_injective (K := K) (base := base) (n := n)
    simpa using h
  · intro h
    have hclass : C₁.fixedClass = C₂.fixedClass :=
      (fixedBaseLength_classification_theorem (C₁ := C₁) (C₂ := C₂)).2 h
    simpa using congrArg (FixedBaseLengthClass.toSignatureClass (K := K) (base := base) (n := n)) hclass

/-- Same theorem restated at the level of global conservative-profile classes: within a fixed-base
fixed-length family, equality of global profile classes is exactly total-weight equality. -/
theorem fixedBaseLength_profileClass_theorem {base : CurveMatrix K} {n : Nat}
    (C₁ C₂ : SurfaceologyFamily (K := K) base n) :
    C₁.1.constraintProfileClass = C₂.1.constraintProfileClass ↔ C₁.1.totalWeight = C₂.1.totalWeight := by
  rw [← fixedBaseLength_classification_theorem (C₁ := C₁) (C₂ := C₂)]
  constructor
  · intro h
    apply FixedBaseLengthClass.toConstraintProfileClass_injective (K := K) (base := base) (n := n)
    simpa using h
  · intro h
    have hclass : C₁.fixedClass = C₂.fixedClass :=
      (fixedBaseLength_classification_theorem (C₁ := C₁) (C₂ := C₂)).2 h
    simpa using congrArg (FixedBaseLengthClass.toConstraintProfileClass (K := K) (base := base) (n := n)) hclass

/-- Canonical family invariant object for the current fixed-base fixed-length classification. -/
structure FixedBaseLengthInvariant where
  totalWeight : K

/-- Extract the canonical current invariant from a fixed-base fixed-length class. -/
def FixedBaseLengthClass.invariant {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) : FixedBaseLengthInvariant (K := K) :=
  { totalWeight := Q.totalWeight }

@[simp] theorem FixedBaseLengthClass.invariant_totalWeight {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) :
    Q.invariant.totalWeight = Q.totalWeight := rfl

/-- One-step extension updates the canonical current invariant by multiplication with the new edge
weight. -/
theorem FixedBaseLengthClass.invariant_snoc {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) (t : WeightedTurn K) :
    (Q.snoc t).invariant.totalWeight = t.weight * Q.invariant.totalWeight := by
  simp [FixedBaseLengthClass.invariant, FixedBaseLengthClass.totalWeight_snoc]

/-- Every canonical class-level object currently carried by the fixed-base fixed-length
classification is determined by the same total-weight invariant. -/
theorem fixedBaseLength_all_current_classifiers_determined_by_totalWeight {base : CurveMatrix K} {n : Nat}
    (Q₁ Q₂ : FixedBaseLengthClass (K := K) base n)
    (hwt : Q₁.invariant.totalWeight = Q₂.invariant.totalWeight) :
    Q₁.signature = Q₂.signature ∧
    Q₁.constraintProfile = Q₂.constraintProfile ∧
    Q₁.toSignatureClass = Q₂.toSignatureClass ∧
    Q₁.toConstraintProfileClass = Q₂.toConstraintProfileClass := by
  refine Quotient.inductionOn₂ Q₁ Q₂ ?_ hwt
  intro C₁ C₂ hwt
  have hsigEq : C₁.1.signature = C₂.1.signature := by
    exact (sameSignature_iff_sameTotalWeight C₁ C₂).2 hwt
  have hprofEq : C₁.1.constraintProfile = C₂.1.constraintProfile :=
    (sameSignature_iff_sameConstraintProfile C₁.1 C₂.1).1 hsigEq
  have hsigClass : C₁.1.signatureClass = C₂.1.signatureClass := Quotient.sound hsigEq
  have hprofClass : C₁.1.constraintProfileClass = C₂.1.constraintProfileClass := Quotient.sound hprofEq
  constructor
  · simpa [FixedBaseLengthClass.signature, SurfaceologyFamily.fixedClass, FixedBaseLengthClass.totalWeight] using hsigEq
  constructor
  · simpa [FixedBaseLengthClass.constraintProfile, SurfaceologyFamily.fixedClass,
      FixedBaseLengthClass.totalWeight, FixedBaseLengthClass.detValue] using hprofEq
  constructor
  · simpa [FixedBaseLengthClass.toSignatureClass, SurfaceologyFamily.fixedClass] using hsigClass
  · simpa [FixedBaseLengthClass.toConstraintProfileClass, SurfaceologyFamily.fixedClass] using hprofClass

end CommRing

end Surfaceology
end ProjectX
