import Mathlib
import ProjectX.Surfaceology.LengthIndexedFamily

namespace ProjectX
namespace Surfaceology

section CommRing
variable {K : Type _} [CommRing K]

/-- A conservative global signature for a surfaceology curve object.

This is not yet a full extracted family classification. It is the strongest global signature the repo
can currently carry honestly from the formalized word/object infrastructure:
- fixed base matrix
- word length
- total edge-weight product
-/
structure FamilySignature where
  base : CurveMatrix K
  length : Nat
  totalWeight : K

/-- Extract the current global signature from a curve object. -/
def CurveObject.signature (C : CurveObject (K := K)) : FamilySignature :=
  { base := C.base
    length := C.length
    totalWeight := C.totalWeight }

@[simp] theorem CurveObject.signature_base (C : CurveObject (K := K)) :
    C.signature.base = C.base := rfl

@[simp] theorem CurveObject.signature_length (C : CurveObject (K := K)) :
    C.signature.length = C.length := rfl

@[simp] theorem CurveObject.signature_totalWeight (C : CurveObject (K := K)) :
    C.signature.totalWeight = C.totalWeight := rfl

/-- Signature update under one-step extension. -/
def FamilySignature.snoc (σ : FamilySignature (K := K)) (t : WeightedTurn K) : FamilySignature :=
  { base := σ.base
    length := σ.length + 1
    totalWeight := t.weight * σ.totalWeight }

@[simp] theorem CurveObject.signature_snoc (C : CurveObject (K := K)) (t : WeightedTurn K) :
    (C.snoc t).signature = C.signature.snoc t := by
  cases C
  cases t
  simp [CurveObject.signature, FamilySignature.snoc, CurveObject.snoc, CurveObject.length,
    CurveObject.totalWeight, totalWeight, List.map_append, List.prod_append, mul_assoc]

/-- Signature equality forces equality of the determinant scaling factor relative to the common
base matrix. -/
theorem signature_eq_implies_det_eq (C₁ C₂ : CurveObject (K := K))
    (hσ : C₁.signature = C₂.signature) :
    C₁.det = C₂.det := by
  have hbase : C₁.base = C₂.base := by simpa [CurveObject.signature] using congrArg FamilySignature.base hσ
  have hwt : C₁.totalWeight = C₂.totalWeight := by
    simpa [CurveObject.signature] using congrArg FamilySignature.totalWeight hσ
  rw [CurveObject.det_formula, CurveObject.det_formula, hwt, hbase]

/-- Signature-level determinant law. -/
theorem CurveObject.det_depends_only_on_signature (C : CurveObject (K := K)) :
    C.det = C.signature.totalWeight * det C.signature.base := by
  simp [CurveObject.signature, CurveObject.det_formula]

/-- Extract the signature of a member of the length-indexed family.
This makes the grading visible at the family level. -/
def SurfaceologyFamily.signature {base : CurveMatrix K} {n : Nat}
    (C : SurfaceologyFamily (K := K) base n) : FamilySignature :=
  C.1.signature

@[simp] theorem SurfaceologyFamily.signature_base {base : CurveMatrix K} {n : Nat}
    (C : SurfaceologyFamily (K := K) base n) :
    C.signature.base = base := by
  rcases C with ⟨C, hbase, hlen⟩
  simp [SurfaceologyFamily.signature, CurveObject.signature, hbase]

@[simp] theorem SurfaceologyFamily.signature_length {base : CurveMatrix K} {n : Nat}
    (C : SurfaceologyFamily (K := K) base n) :
    C.signature.length = n := by
  rcases C with ⟨C, hbase, hlen⟩
  simp [SurfaceologyFamily.signature, CurveObject.signature, hlen]

@[simp] theorem SurfaceologyFamily.signature_snoc {base : CurveMatrix K} {n : Nat}
    (C : SurfaceologyFamily (K := K) base n) (t : WeightedTurn K) :
    (SurfaceologyFamily.snoc C t).signature = C.signature.snoc t := by
  rcases C with ⟨C, hbase, hlen⟩
  simp [SurfaceologyFamily.signature, SurfaceologyFamily.snoc, CurveObject.signature_snoc]

end CommRing

end Surfaceology
end ProjectX
