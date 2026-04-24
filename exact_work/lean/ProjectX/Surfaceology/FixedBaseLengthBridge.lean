import Mathlib
import ProjectX.Surfaceology.FixedBaseLengthProfile

namespace ProjectX
namespace Surfaceology

section CommRing
variable {K : Type _} [CommRing K]

/-- Map a fixed-base fixed-length class into the global signature-class quotient. -/
def FixedBaseLengthClass.toSignatureClass {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) : SignatureClass K := by
  refine Quotient.liftOn Q (fun C => C.1.signatureClass) ?_
  intro C₁ C₂ h
  exact Quotient.sound ((sameSignature_iff_sameTotalWeight C₁ C₂).2 h)

/-- Map a fixed-base fixed-length class into the global conservative-profile quotient. -/
def FixedBaseLengthClass.toConstraintProfileClass {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) : ConstraintProfileClass K := by
  refine Quotient.liftOn Q (fun C => C.1.constraintProfileClass) ?_
  intro C₁ C₂ h
  exact Quotient.sound (((sameSignature_iff_sameConstraintProfile C₁.1 C₂.1).1)
    ((sameSignature_iff_sameTotalWeight C₁ C₂).2 h))

@[simp] theorem SurfaceologyFamily.toSignatureClass_fixedClass {base : CurveMatrix K} {n : Nat}
    (C : SurfaceologyFamily (K := K) base n) :
    C.fixedClass.toSignatureClass = C.1.signatureClass := rfl

@[simp] theorem SurfaceologyFamily.toConstraintProfileClass_fixedClass {base : CurveMatrix K} {n : Nat}
    (C : SurfaceologyFamily (K := K) base n) :
    C.fixedClass.toConstraintProfileClass = C.1.constraintProfileClass := rfl

/-- The fixed-base fixed-length classification injects into the global signature quotient. -/
theorem FixedBaseLengthClass.toSignatureClass_injective {base : CurveMatrix K} {n : Nat} :
    Function.Injective (FixedBaseLengthClass.toSignatureClass (K := K) (base := base) (n := n)) := by
  intro Q₁ Q₂ hQ
  refine Quotient.inductionOn₂ Q₁ Q₂ ?_ hQ
  intro C₁ C₂ h
  apply Quotient.sound
  exact (sameSignature_iff_sameTotalWeight C₁ C₂).1 (Quotient.exact h)

/-- The fixed-base fixed-length classification injects into the global conservative-profile quotient. -/
theorem FixedBaseLengthClass.toConstraintProfileClass_injective {base : CurveMatrix K} {n : Nat} :
    Function.Injective (FixedBaseLengthClass.toConstraintProfileClass (K := K) (base := base) (n := n)) := by
  intro Q₁ Q₂ hQ
  refine Quotient.inductionOn₂ Q₁ Q₂ ?_ hQ
  intro C₁ C₂ h
  apply Quotient.sound
  exact (sameSignature_iff_sameTotalWeight C₁ C₂).1
    (((sameSignature_iff_sameConstraintProfile C₁.1 C₂.1).2) (Quotient.exact h))

/-- One-step extension on fixed-base fixed-length classes commutes with passage to the global
signature quotient. -/
theorem FixedBaseLengthClass.toSignatureClass_snoc {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) (t : WeightedTurn K) :
    (Q.snoc t).toSignatureClass = (Q.toSignatureClass).snoc t := by
  refine Quotient.inductionOn Q ?_
  intro C
  rfl

/-- One-step extension on fixed-base fixed-length classes commutes with passage to the global
conservative-profile quotient. -/
theorem FixedBaseLengthClass.toConstraintProfileClass_snoc {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) (t : WeightedTurn K) :
    (Q.snoc t).toConstraintProfileClass = (Q.toConstraintProfileClass).snoc t := by
  refine Quotient.inductionOn Q ?_
  intro C
  rfl

/-- The canonical fixed-base fixed-length class profile agrees with the global profile extracted
after passing to the global profile-class quotient. -/
theorem FixedBaseLengthClass.profileClass_profile_eq_constraintProfile {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) :
    (Q.toConstraintProfileClass).profile = Q.constraintProfile := by
  refine Quotient.inductionOn Q ?_
  intro C
  simp [FixedBaseLengthClass.toConstraintProfileClass, ConstraintProfileClass.profile,
    FixedBaseLengthClass.constraintProfile,
    SurfaceologyFamily.constraintProfile_eq_fixedClass_constraintProfile]

end CommRing

end Surfaceology
end ProjectX
