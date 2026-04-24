import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Data.Finset.Basic
import ProjectX.Spine.ClassLevel

open scoped BigOperators

namespace ProjectX

/-- Orientation sign carried by a residue operation. -/
inductive OrientationSign where
  | plus
  | minus
  deriving DecidableEq, Repr

/-- Integer multiplier associated to a residue sign. -/
def OrientationSign.multiplier : OrientationSign → Int
  | .plus => 1
  | .minus => -1

@[simp] theorem multiplier_plus : OrientationSign.multiplier .plus = 1 := rfl
@[simp] theorem multiplier_minus : OrientationSign.multiplier .minus = -1 := rfl

/-- Finite support instances for the exact support types currently formalized. -/
instance : Fintype Gr2Support where
  elems := {Gr2Support.paired}
  complete x := by
    cases x <;> simp

instance : Fintype Gr36Support where
  elems := {Gr36Support.omegaD}
  complete x := by
    cases x <;> simp

instance : Fintype Gr37Support where
  elems := {Gr37Support.omegaA, Gr37Support.omegaD}
  complete x := by
    cases x <;> simp

/-- Data for a residue from a larger support system to a smaller one.

`keep l = some s` means that the large support direction `l` survives as the smaller support
direction `s` under the residue. `keep l = none` means that `l` vanishes under the residue. -/
structure ResidueData (Large Small : Type) where
  sign : OrientationSign
  keep : Large → Option Small

/-- Residue of a coefficient-bearing representative across finite support types.

This is an honest class-level representative residue operator: it lowers the degree by one and
transfers support coefficients according to the surviving support map, with the specified sign. -/
def residue {Large Small : Type} [Fintype Large] [DecidableEq Large] [DecidableEq Small]
    (r : ResidueData Large Small) (μ : TopClassRep Large) : TopClassRep Small :=
  { degree := μ.degree - 1
    coeff := fun s =>
      r.sign.multiplier *
        ∑ l in Finset.univ.filter (fun l => r.keep l = some s), TopClassRep.coefficient μ l }

@[simp] theorem residue_degree {Large Small : Type} [Fintype Large] [DecidableEq Large]
    [DecidableEq Small] (r : ResidueData Large Small) (μ : TopClassRep Large) :
    (residue r μ).degree = μ.degree - 1 := rfl

/-- A one-direction support type used only to carry coefficient-level residue data into a lower
branch that has not yet been formalized as an exact class family. -/
inductive SingleSupport where
  | carrier
  deriving DecidableEq, Repr

instance : Fintype SingleSupport where
  elems := {SingleSupport.carrier}
  complete x := by
    cases x <;> simp

end ProjectX
