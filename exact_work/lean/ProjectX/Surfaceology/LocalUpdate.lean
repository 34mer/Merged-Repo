import Mathlib

namespace ProjectX
namespace Surfaceology

/-- The local 2×2 curve matrix used in the first exact surfaceology object. -/
structure CurveMatrix (K : Type _) where
  a : K
  b : K
  c : K
  d : K
  deriving Repr

section CommRing
variable {K : Type _} [CommRing K]

/-- Sum of entries. -/
def F (M : CurveMatrix K) : K := M.a + M.b + M.c + M.d

/-- Determinant of the local curve matrix. -/
def det (M : CurveMatrix K) : K := M.a * M.d - M.b * M.c

/-- Prepend an edge of weight `y` and a left turn. -/
def prependLeft (y : K) (M : CurveMatrix K) : CurveMatrix K :=
  { a := M.a
    b := M.b
    c := y * (M.a + M.c)
    d := y * (M.b + M.d) }

/-- Prepend an edge of weight `y` and a right turn. -/
def prependRight (y : K) (M : CurveMatrix K) : CurveMatrix K :=
  { a := M.a + M.c
    b := M.b + M.d
    c := y * M.c
    d := y * M.d }

@[simp] theorem prependLeft_a (y : K) (M : CurveMatrix K) : (prependLeft y M).a = M.a := rfl
@[simp] theorem prependLeft_b (y : K) (M : CurveMatrix K) : (prependLeft y M).b = M.b := rfl
@[simp] theorem prependLeft_c (y : K) (M : CurveMatrix K) : (prependLeft y M).c = y * (M.a + M.c) := rfl
@[simp] theorem prependLeft_d (y : K) (M : CurveMatrix K) : (prependLeft y M).d = y * (M.b + M.d) := rfl

@[simp] theorem prependRight_a (y : K) (M : CurveMatrix K) : (prependRight y M).a = M.a + M.c := rfl
@[simp] theorem prependRight_b (y : K) (M : CurveMatrix K) : (prependRight y M).b = M.b + M.d := rfl
@[simp] theorem prependRight_c (y : K) (M : CurveMatrix K) : (prependRight y M).c = y * M.c := rfl
@[simp] theorem prependRight_d (y : K) (M : CurveMatrix K) : (prependRight y M).d = y * M.d := rfl

theorem F_prependLeft (y : K) (M : CurveMatrix K) :
    F (prependLeft y M) = M.a + M.b + y * F M := by
  simp [F, prependLeft]
  ring

theorem F_prependRight (y : K) (M : CurveMatrix K) :
    F (prependRight y M) = F M + y * (M.c + M.d) := by
  simp [F, prependRight]
  ring

theorem det_prependLeft (y : K) (M : CurveMatrix K) :
    det (prependLeft y M) = y * det M := by
  simp [det, prependLeft]
  ring

theorem det_prependRight (y : K) (M : CurveMatrix K) :
    det (prependRight y M) = y * det M := by
  simp [det, prependRight]
  ring

end CommRing

section Field
variable {K : Type _} [Field K]

/-- Rational update invariant used in the first exact surfaceology object. -/
def u (M : CurveMatrix K) : K := (M.b * M.c) / (M.a * M.d)

theorem u_prependLeft (y : K) (M : CurveMatrix K)
    (hy : y ≠ 0) (ha : M.a ≠ 0) (hbd : M.b + M.d ≠ 0) :
    u (prependLeft y M) = (M.b * (M.a + M.c)) / (M.a * (M.b + M.d)) := by
  rw [u, prependLeft]
  field_simp [hy, ha, hbd]
  ring

theorem u_prependRight (y : K) (M : CurveMatrix K)
    (hy : y ≠ 0) (hd : M.d ≠ 0) (hac : M.a + M.c ≠ 0) :
    u (prependRight y M) = (M.c * (M.b + M.d)) / (M.d * (M.a + M.c)) := by
  rw [u, prependRight]
  field_simp [hy, hd, hac]
  ring

end Field

end Surfaceology
end ProjectX
