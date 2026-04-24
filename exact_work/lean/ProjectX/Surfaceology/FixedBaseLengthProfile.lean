import Mathlib
import ProjectX.Surfaceology.FixedBaseLengthClassification

namespace ProjectX
namespace Surfaceology

section CommRing
variable {K : Type _} [CommRing K]

/-- Canonical extracted signature attached to a fixed-base fixed-length class. -/
def FixedBaseLengthClass.signature {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) : FamilySignature K :=
  { base := base
    length := n
    totalWeight := Q.totalWeight }

@[simp] theorem FixedBaseLengthClass.signature_base {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) :
    Q.signature.base = base := rfl

@[simp] theorem FixedBaseLengthClass.signature_length {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) :
    Q.signature.length = n := rfl

@[simp] theorem FixedBaseLengthClass.signature_totalWeight {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) :
    Q.signature.totalWeight = Q.totalWeight := rfl

/-- Canonical determinant value attached to a fixed-base fixed-length class. -/
def FixedBaseLengthClass.detValue {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) : K :=
  Q.totalWeight * det base

/-- Canonical conservative constraint profile attached to a fixed-base fixed-length class. -/
def FixedBaseLengthClass.constraintProfile {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) : ConstraintProfile K :=
  { signature := Q.signature
    detValue := Q.detValue }

/-- A family member's extracted signature agrees with the canonical signature of its class. -/
theorem SurfaceologyFamily.signature_eq_fixedClass_signature {base : CurveMatrix K} {n : Nat}
    (C : SurfaceologyFamily (K := K) base n) :
    C.1.signature = C.fixedClass.signature := by
  ext <;>
    simp [FixedBaseLengthClass.signature, SurfaceologyFamily.fixedClass, FixedBaseLengthClass.totalWeight,
      SurfaceologyFamily.signature_base, SurfaceologyFamily.signature_length]

/-- A family member's determinant agrees with the canonical determinant value of its class. -/
theorem SurfaceologyFamily.det_eq_fixedClass_detValue {base : CurveMatrix K} {n : Nat}
    (C : SurfaceologyFamily (K := K) base n) :
    C.1.det = C.fixedClass.detValue := by
  simp [FixedBaseLengthClass.detValue, SurfaceologyFamily.det_formula]

/-- A family member's conservative constraint profile agrees with the canonical profile of its
fixed-base fixed-length class. -/
theorem SurfaceologyFamily.constraintProfile_eq_fixedClass_constraintProfile
    {base : CurveMatrix K} {n : Nat} (C : SurfaceologyFamily (K := K) base n) :
    C.1.constraintProfile = C.fixedClass.constraintProfile := by
  ext <;>
    simp [FixedBaseLengthClass.constraintProfile,
      SurfaceologyFamily.signature_eq_fixedClass_signature,
      SurfaceologyFamily.det_eq_fixedClass_detValue]

/-- One-step extension updates the canonical signature of a fixed-base fixed-length class by the
same signature snoc law as on objects. -/
theorem FixedBaseLengthClass.signature_snoc {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) (t : WeightedTurn K) :
    (Q.snoc t).signature = Q.signature.snoc t := by
  ext <;>
    simp [FixedBaseLengthClass.signature, FixedBaseLengthClass.totalWeight_snoc,
      FamilySignature.snoc, mul_assoc]

/-- One-step extension updates the canonical determinant value of a fixed-base fixed-length class by
multiplication with the new edge weight. -/
theorem FixedBaseLengthClass.detValue_snoc {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) (t : WeightedTurn K) :
    (Q.snoc t).detValue = t.weight * Q.detValue := by
  simp [FixedBaseLengthClass.detValue, FixedBaseLengthClass.totalWeight_snoc, mul_assoc]

/-- One-step extension updates the canonical conservative constraint profile of a fixed-base
fixed-length class by the profile snoc law. -/
theorem FixedBaseLengthClass.constraintProfile_snoc {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) (t : WeightedTurn K) :
    (Q.snoc t).constraintProfile = (Q.constraintProfile).snoc t := by
  ext <;>
    simp [FixedBaseLengthClass.constraintProfile,
      FixedBaseLengthClass.signature_snoc,
      FixedBaseLengthClass.detValue_snoc,
      ConstraintProfile.snoc]

end CommRing

end Surfaceology
end ProjectX
