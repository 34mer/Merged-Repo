import Mathlib
import ProjectX.Surfaceology.LocalUpdate

namespace ProjectX
namespace Surfaceology

/-- Direction of a primitive turn in the first exact surfaceology object. -/
inductive TurnDir where
  | left
  | right
  deriving DecidableEq, Repr

/-- A weighted primitive turn. -/
structure WeightedTurn (K : Type _) where
  dir : TurnDir
  weight : K
  deriving Repr

/-- Apply one weighted primitive turn to a curve matrix. -/
def applyTurn {K : Type _} [CommRing K] (t : WeightedTurn K) (M : CurveMatrix K) : CurveMatrix K :=
  match t.dir with
  | .left => prependLeft t.weight M
  | .right => prependRight t.weight M

/-- Evaluate a word of weighted turns from left to right on a base matrix. -/
def evalWord {K : Type _} [CommRing K] (w : List (WeightedTurn K)) (M : CurveMatrix K) : CurveMatrix K :=
  List.foldl (fun acc t => applyTurn t acc) M w

/-- Product of all edge weights appearing in a word. -/
def totalWeight {K : Type _} [Monoid K] (w : List (WeightedTurn K)) : K :=
  (w.map fun t => t.weight).prod

@[simp] theorem evalWord_nil {K : Type _} [CommRing K] (M : CurveMatrix K) :
    evalWord ([] : List (WeightedTurn K)) M = M := rfl

@[simp] theorem totalWeight_nil {K : Type _} [Monoid K] :
    totalWeight ([] : List (WeightedTurn K)) = 1 := rfl

@[simp] theorem evalWord_cons {K : Type _} [CommRing K] (t : WeightedTurn K)
    (w : List (WeightedTurn K)) (M : CurveMatrix K) :
    evalWord (t :: w) M = evalWord w (applyTurn t M) := by
  simp [evalWord]

@[simp] theorem totalWeight_cons {K : Type _} [Monoid K] (t : WeightedTurn K)
    (w : List (WeightedTurn K)) :
    totalWeight (t :: w) = t.weight * totalWeight w := by
  simp [totalWeight]

section CommRing
variable {K : Type _} [CommRing K]

/-- Determinant scaling for one primitive weighted turn. -/
theorem det_applyTurn (t : WeightedTurn K) (M : CurveMatrix K) :
    det (applyTurn t M) = t.weight * det M := by
  cases t with
  | mk dir weight =>
      cases dir <;>
      simp [applyTurn, det_prependLeft, det_prependRight]

/-- Determinant scaling across a whole word depends only on the product of edge weights. -/
theorem det_evalWord (w : List (WeightedTurn K)) (M : CurveMatrix K) :
    det (evalWord w M) = totalWeight w * det M := by
  induction w generalizing M with
  | nil =>
      simp [evalWord, totalWeight]
  | cons t w ih =>
      rw [evalWord_cons, det_evalWord]
      rw [det_applyTurn]
      simp [totalWeight_cons, mul_assoc]

/-- The determinant scaling across a word is independent of the left/right turn pattern once the
weight sequence is fixed. -/
theorem det_evalWord_depends_only_on_weights
    (w1 w2 : List (WeightedTurn K)) (M : CurveMatrix K)
    (hwt : totalWeight w1 = totalWeight w2) :
    det (evalWord w1 M) = det (evalWord w2 M) := by
  rw [det_evalWord, det_evalWord, hwt]

end CommRing

end Surfaceology
end ProjectX
