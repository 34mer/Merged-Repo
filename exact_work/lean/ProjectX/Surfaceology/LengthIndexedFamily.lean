import Mathlib
import ProjectX.Surfaceology.GlobalRecursion

namespace ProjectX
namespace Surfaceology

section CommRing
variable {K : Type _} [CommRing K]

/-- Word length of a global curve object. This is the most basic family grading currently carried
for surfaceology in Lean. -/
def CurveObject.length (C : CurveObject (K := K)) : Nat := C.word.length

@[simp] theorem CurveObject.length_mk (base : CurveMatrix K) (word : List (WeightedTurn K)) :
    (CurveObject.mk base word).length = word.length := rfl

@[simp] theorem CurveObject.length_snoc (C : CurveObject (K := K)) (t : WeightedTurn K) :
    (C.snoc t).length = C.length + 1 := by
  simp [CurveObject.length, CurveObject.snoc]

/-- Length-indexed surfaceology family over a fixed base matrix. -/
def SurfaceologyFamily (base : CurveMatrix K) (n : Nat) : Type :=
  { C : CurveObject (K := K) // C.base = base ∧ C.length = n }

/-- Insert a curve object into the length-indexed family determined by its base and length. -/
def CurveObject.asFamilyMember (C : CurveObject (K := K)) : SurfaceologyFamily C.base C.length :=
  ⟨C, rfl, rfl⟩

/-- One-step generation law: extending by one weighted turn moves the curve object from level `n`
to level `n+1`. -/
def SurfaceologyFamily.snoc {base : CurveMatrix K} {n : Nat}
    (C : SurfaceologyFamily (K := K) base n) (t : WeightedTurn K) :
    SurfaceologyFamily base (n + 1) := by
  rcases C with ⟨C, hbase, hlen⟩
  refine ⟨C.snoc t, ?_, ?_⟩
  · simp [CurveObject.snoc, hbase]
  · simpa [hlen] using CurveObject.length_snoc C t

/-- Determinant formula transported to the length-indexed family. -/
theorem SurfaceologyFamily.det_formula {base : CurveMatrix K} {n : Nat}
    (C : SurfaceologyFamily (K := K) base n) :
    (C.1).det = (C.1).totalWeight * det base := by
  rcases C with ⟨C, hbase, hlen⟩
  simpa [hbase] using CurveObject.det_formula C

end CommRing

end Surfaceology
end ProjectX
