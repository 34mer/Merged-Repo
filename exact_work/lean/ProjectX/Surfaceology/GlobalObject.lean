import Mathlib
import ProjectX.Surfaceology.WordSemantics

namespace ProjectX
namespace Surfaceology

section CommRing
variable {K : Type _} [CommRing K]

/-- Global curve object carrying a base matrix and a weighted turn word.
This packages the chain `C -> M_C -> F_C` at the object level. -/
structure CurveObject where
  base : CurveMatrix K
  word : List (WeightedTurn K)

/-- Global matrix associated to a curve object. -/
def CurveObject.matrix (C : CurveObject (K := K)) : CurveMatrix K :=
  evalWord C.word C.base

/-- Global entry sum `F_C`. -/
def CurveObject.F (C : CurveObject (K := K)) : K :=
  F C.matrix

/-- Global determinant. -/
def CurveObject.det (C : CurveObject (K := K)) : K :=
  det C.matrix

/-- Product of all edge weights in the curve word. -/
def CurveObject.totalWeight (C : CurveObject (K := K)) : K :=
  totalWeight C.word

@[simp] theorem CurveObject.matrix_mk (base : CurveMatrix K) (word : List (WeightedTurn K)) :
    (CurveObject.mk base word).matrix = evalWord word base := rfl

@[simp] theorem CurveObject.F_mk (base : CurveMatrix K) (word : List (WeightedTurn K)) :
    (CurveObject.mk base word).F = F (evalWord word base) := rfl

@[simp] theorem CurveObject.det_mk (base : CurveMatrix K) (word : List (WeightedTurn K)) :
    (CurveObject.mk base word).det = det (evalWord word base) := rfl

@[simp] theorem CurveObject.totalWeight_mk (base : CurveMatrix K) (word : List (WeightedTurn K)) :
    (CurveObject.mk base word).totalWeight = totalWeight word := rfl

/-- Determinant scaling across a global curve object. -/
theorem CurveObject.det_formula (C : CurveObject (K := K)) :
    C.det = C.totalWeight * det C.base := by
  simp [CurveObject.det, CurveObject.totalWeight, CurveObject.matrix, det_evalWord]

/-- Extend a curve object by one weighted primitive turn. -/
def CurveObject.snoc (C : CurveObject (K := K)) (t : WeightedTurn K) : CurveObject :=
  { base := C.base, word := C.word ++ [t] }

@[simp] theorem CurveObject.matrix_snoc (C : CurveObject (K := K)) (t : WeightedTurn K) :
    (C.snoc t).matrix = applyTurn t C.matrix := by
  simp [CurveObject.snoc, CurveObject.matrix, evalWord, List.foldl_append]

/-- Determinant update under global object extension. -/
theorem CurveObject.det_snoc (C : CurveObject (K := K)) (t : WeightedTurn K) :
    (C.snoc t).det = t.weight * C.det := by
  rw [CurveObject.det, CurveObject.matrix_snoc, det_applyTurn, CurveObject.det]

end CommRing

section Field
variable {K : Type _} [Field K]

/-- Global rational invariant `u_C` carried by a curve object. -/
def CurveObject.u (C : CurveObject (K := K)) : K :=
  u C.matrix

@[simp] theorem CurveObject.u_mk (base : CurveMatrix K) (word : List (WeightedTurn K)) :
    (CurveObject.mk base word).u = u (evalWord word base) := rfl

end Field

end Surfaceology
end ProjectX
