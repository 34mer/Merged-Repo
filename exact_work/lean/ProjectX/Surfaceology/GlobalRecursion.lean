import Mathlib
import ProjectX.Surfaceology.GlobalObject

namespace ProjectX
namespace Surfaceology

section CommRing
variable {K : Type _} [CommRing K]

theorem CurveObject.F_snoc_left (C : CurveObject (K := K)) (y : K) :
    (C.snoc { dir := TurnDir.left, weight := y }).F = C.matrix.a + C.matrix.b + y * C.F := by
  rw [CurveObject.F, CurveObject.matrix_snoc, F_prependLeft, CurveObject.F]

theorem CurveObject.F_snoc_right (C : CurveObject (K := K)) (y : K) :
    (C.snoc { dir := TurnDir.right, weight := y }).F = C.F + y * (C.matrix.c + C.matrix.d) := by
  rw [CurveObject.F, CurveObject.matrix_snoc, F_prependRight, CurveObject.F]

end CommRing

section Field
variable {K : Type _} [Field K]

theorem CurveObject.u_snoc_left (C : CurveObject (K := K)) (y : K)
    (hy : y ≠ 0) (ha : C.matrix.a ≠ 0) (hbd : C.matrix.b + C.matrix.d ≠ 0) :
    (C.snoc { dir := TurnDir.left, weight := y }).u =
      (C.matrix.b * (C.matrix.a + C.matrix.c)) / (C.matrix.a * (C.matrix.b + C.matrix.d)) := by
  rw [CurveObject.u, CurveObject.matrix_snoc]
  exact u_prependLeft y C.matrix hy ha hbd

theorem CurveObject.u_snoc_right (C : CurveObject (K := K)) (y : K)
    (hy : y ≠ 0) (hd : C.matrix.d ≠ 0) (hac : C.matrix.a + C.matrix.c ≠ 0) :
    (C.snoc { dir := TurnDir.right, weight := y }).u =
      (C.matrix.c * (C.matrix.b + C.matrix.d)) / (C.matrix.d * (C.matrix.a + C.matrix.c)) := by
  rw [CurveObject.u, CurveObject.matrix_snoc]
  exact u_prependRight y C.matrix hy hd hac

end Field

end Surfaceology
end ProjectX
