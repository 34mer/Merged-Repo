import ProjectX.Spine.FiniteClosure

namespace ProjectX

/-- A coefficient-bearing representative for a top interaction class.

This is intentionally weaker than a full cohomology-class formalization:
it stores the degree and the coefficient data attached to named support directions.
-/
structure TopClassRep (Support : Type) where
  degree : Nat
  coeff : Support → Int

namespace TopClassRep

/-- Read off the coefficient of a named support direction. -/
def coefficient {Support : Type} (μ : TopClassRep Support) (s : Support) : Int := μ.coeff s

@[simp] theorem coefficient_mk {Support : Type} (d : Nat) (f : Support → Int) (s : Support) :
    coefficient ⟨d, f⟩ s = f s := rfl

@[ext] theorem ext {Support : Type} {μ ν : TopClassRep Support}
    (hdeg : μ.degree = ν.degree)
    (hcoeff : ∀ s, coefficient μ s = coefficient ν s) : μ = ν := by
  cases μ
  cases ν
  simp at hdeg
  subst hdeg
  have hfun : coeff = coeff_1 := funext hcoeff
  subst hfun
  rfl

end TopClassRep

/-- `Gr_+(2,n)` has one coefficient direction at the current exact top-interaction layer. -/
inductive Gr2Support where
  | paired
  deriving DecidableEq, Repr

/-- `Gr_+(3,6)` has one named coefficient direction at the current exact top-interaction layer. -/
inductive Gr36Support where
  | omegaD
  deriving DecidableEq, Repr

/-- `Gr_+(3,7)` / `Gr_+(4,7)` has two named coefficient directions at the current exact layer. -/
inductive Gr37Support where
  | omegaA
  | omegaD
  deriving DecidableEq, Repr

/-- Class-level coefficient representative for `Gr_+(2,n)` / `Gr_+(n-2,n)`. -/
def muGr2Rep (n : Nat) : TopClassRep Gr2Support :=
  { degree := n - 4
    coeff := fun
      | .paired => Int.ofNat (topCoeff_Gr2 n) }

@[simp] theorem muGr2Rep_degree (n : Nat) : (muGr2Rep n).degree = n - 4 := rfl

@[simp] theorem muGr2Rep_coeff (n : Nat) :
    TopClassRep.coefficient (muGr2Rep n) Gr2Support.paired = Int.ofNat (topCoeff_Gr2 n) := rfl

/-- Class-level coefficient representative for `Gr_+(3,6)`. -/
def muGr36Rep : TopClassRep Gr36Support :=
  { degree := 3
    coeff := fun
      | .omegaD => Int.ofNat topCoeff_Gr36 }

@[simp] theorem muGr36Rep_degree : muGr36Rep.degree = 3 := rfl

@[simp] theorem muGr36Rep_coeff :
    TopClassRep.coefficient muGr36Rep Gr36Support.omegaD = Int.ofNat topCoeff_Gr36 := rfl

/-- Class-level coefficient representative for `Gr_+(3,7)` / `Gr_+(4,7)`. -/
def muGr37Rep : TopClassRep Gr37Support :=
  { degree := 5
    coeff := fun
      | .omegaA => Int.ofNat topCoeff_Gr37_fixed
      | .omegaD => Int.ofNat topCoeff_Gr37_paired }

@[simp] theorem muGr37Rep_degree : muGr37Rep.degree = 5 := rfl

@[simp] theorem muGr37Rep_coeff_A :
    TopClassRep.coefficient muGr37Rep Gr37Support.omegaA = Int.ofNat topCoeff_Gr37_fixed := rfl

@[simp] theorem muGr37Rep_coeff_D :
    TopClassRep.coefficient muGr37Rep Gr37Support.omegaD = Int.ofNat topCoeff_Gr37_paired := rfl

/-- Explicit coefficient formulas carried at the representative-object level for `Gr_+(2,n)`. -/
theorem muGr2Rep_formula {n : Nat} (h : 2 ≤ n) :
    TopClassRep.coefficient (muGr2Rep n) Gr2Support.paired = Int.ofNat n := by
  rw [muGr2Rep_coeff, topCoeff_Gr2_formula h]

/-- Explicit coefficient formula carried at the representative-object level for `Gr_+(3,6)`. -/
theorem muGr36Rep_formula :
    TopClassRep.coefficient muGr36Rep Gr36Support.omegaD = 4 := by
  rw [muGr36Rep_coeff, topCoeff_Gr36_formula]

/-- Explicit fixed-node coefficient formula carried at the representative-object level for
`Gr_+(3,7)` / `Gr_+(4,7)`. -/
theorem muGr37Rep_formula_A :
    TopClassRep.coefficient muGr37Rep Gr37Support.omegaA = 7 := by
  rw [muGr37Rep_coeff_A, topCoeff_Gr37_fixed_formula]

/-- Explicit paired-node coefficient formula carried at the representative-object level for
`Gr_+(3,7)` / `Gr_+(4,7)`. -/
theorem muGr37Rep_formula_D :
    TopClassRep.coefficient muGr37Rep Gr37Support.omegaD = 14 := by
  rw [muGr37Rep_coeff_D, topCoeff_Gr37_paired_formula]

end ProjectX
