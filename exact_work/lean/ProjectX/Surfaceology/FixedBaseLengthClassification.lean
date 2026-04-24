import Mathlib
import ProjectX.Surfaceology.ProfileClassification

namespace ProjectX
namespace Surfaceology

section CommRing
variable {K : Type _} [CommRing K]

/-- For fixed base and fixed word length, the currently formalized conservative classification
collapses to equality of total edge-weight product. -/
def SameTotalWeight {base : CurveMatrix K} {n : Nat}
    (C₁ C₂ : SurfaceologyFamily (K := K) base n) : Prop :=
  C₁.1.totalWeight = C₂.1.totalWeight

@[refl] theorem SameTotalWeight.refl {base : CurveMatrix K} {n : Nat}
    (C : SurfaceologyFamily (K := K) base n) : SameTotalWeight C C := rfl

@[symm] theorem SameTotalWeight.symm {base : CurveMatrix K} {n : Nat}
    {C₁ C₂ : SurfaceologyFamily (K := K) base n} :
    SameTotalWeight C₁ C₂ → SameTotalWeight C₂ C₁ := by
  intro h
  simpa [SameTotalWeight] using h.symm

@[trans] theorem SameTotalWeight.trans {base : CurveMatrix K} {n : Nat}
    {C₁ C₂ C₃ : SurfaceologyFamily (K := K) base n} :
    SameTotalWeight C₁ C₂ → SameTotalWeight C₂ C₃ → SameTotalWeight C₁ C₃ := by
  intro h12 h23
  simpa [SameTotalWeight] using h12.trans h23

/-- On a fixed-base fixed-length family, extracted signature equivalence is exactly total-weight
 equivalence. -/
theorem sameSignature_iff_sameTotalWeight {base : CurveMatrix K} {n : Nat}
    (C₁ C₂ : SurfaceologyFamily (K := K) base n) :
    SameSignature C₁.1 C₂.1 ↔ SameTotalWeight C₁ C₂ := by
  constructor
  · intro h
    simpa [SameTotalWeight] using congrArg FamilySignature.totalWeight h
  · intro h
    rcases C₁ with ⟨C₁, hbase₁, hlen₁⟩
    rcases C₂ with ⟨C₂, hbase₂, hlen₂⟩
    apply by
      ext <;> simp [SameTotalWeight, CurveObject.signature, hbase₁, hbase₂, hlen₁, hlen₂, h]

/-- Setoid on a fixed-base fixed-length family induced by equality of total weight. -/
def sameTotalWeightSetoid (base : CurveMatrix K) (n : Nat) :
    Setoid (SurfaceologyFamily (K := K) base n) where
  r := SameTotalWeight
  iseqv := ⟨SameTotalWeight.refl, SameTotalWeight.symm, SameTotalWeight.trans⟩

/-- Quotient class for a fixed-base fixed-length family under total-weight equivalence. -/
abbrev FixedBaseLengthClass (base : CurveMatrix K) (n : Nat) :=
  Quotient (sameTotalWeightSetoid (K := K) base n)

/-- Class of a family member modulo fixed-base fixed-length total-weight equivalence. -/
def SurfaceologyFamily.fixedClass {base : CurveMatrix K} {n : Nat}
    (C : SurfaceologyFamily (K := K) base n) : FixedBaseLengthClass (K := K) base n :=
  Quotient.mk _ C

/-- Total weight is constant on a fixed-base fixed-length class. -/
def FixedBaseLengthClass.totalWeight {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) : K := by
  refine Quotient.liftOn Q (fun C => C.1.totalWeight) ?_
  intro C₁ C₂ h
  exact h

/-- One-step extension induces evolution on fixed-base fixed-length classes. -/
def FixedBaseLengthClass.snoc {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) (t : WeightedTurn K) :
    FixedBaseLengthClass (K := K) base (n + 1) := by
  refine Quotient.liftOn Q (fun C => (SurfaceologyFamily.snoc C t).fixedClass) ?_
  intro C₁ C₂ h
  apply Quotient.sound
  have hs : SameSignature C₁.1 C₂.1 := (sameSignature_iff_sameTotalWeight C₁ C₂).2 h
  have hs' : SameSignature (SurfaceologyFamily.snoc C₁ t).1 (SurfaceologyFamily.snoc C₂ t).1 :=
    SameSignature.snoc hs t
  exact (sameSignature_iff_sameTotalWeight (SurfaceologyFamily.snoc C₁ t)
    (SurfaceologyFamily.snoc C₂ t)).1 hs'

/-- On fixed-base fixed-length classes, one-step extension multiplies total weight by the new edge
weight. -/
theorem FixedBaseLengthClass.totalWeight_snoc {base : CurveMatrix K} {n : Nat}
    (Q : FixedBaseLengthClass (K := K) base n) (t : WeightedTurn K) :
    (Q.snoc t).totalWeight = t.weight * Q.totalWeight := by
  refine Quotient.inductionOn Q ?_
  intro C
  simp [FixedBaseLengthClass.snoc, FixedBaseLengthClass.totalWeight, SurfaceologyFamily.fixedClass,
    SurfaceologyFamily.snoc, CurveObject.signature_snoc, CurveObject.signature_totalWeight]

end CommRing

end Surfaceology
end ProjectX
