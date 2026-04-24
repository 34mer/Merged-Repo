import ProjectX.Basic

namespace ProjectX

/-- The terminal residue atom has two oriented boundary poles. -/
inductive Pole where
  | zero
  | infinity
  deriving DecidableEq, Repr

/-- Signed residue readout on the two boundary poles. -/
def residueSign : Pole → Int
  | .zero => 1
  | .infinity => -1

@[simp] theorem residueSign_zero : residueSign Pole.zero = 1 := rfl
@[simp] theorem residueSign_infinity : residueSign Pole.infinity = -1 := rfl

/-- Support nodes contributing to top interaction coefficients are either fixed or paired
under the diagram involution induced by `w₀`. -/
inductive SupportNodeType where
  | fixed
  | paired
  deriving DecidableEq, Repr

/-- Orbit-support coefficient law at the top-interaction layer. -/
def supportCoefficient (h : Nat) : SupportNodeType → Nat
  | .fixed => (h + 2) / 2
  | .paired => h + 2

@[simp] theorem supportCoefficient_fixed (h : Nat) :
    supportCoefficient h .fixed = (h + 2) / 2 := rfl

@[simp] theorem supportCoefficient_paired (h : Nat) :
    supportCoefficient h .paired = h + 2 := rfl

/-- `Gr_+(2,n)` / `Gr_+(n-2,n)` coefficient extracted from the paired support law.
The theorem below requires the natural domain hypothesis `2 ≤ n`. -/
def gr2Coeff (n : Nat) : Nat := supportCoefficient (n - 2) .paired

theorem gr2Coeff_formula {n : Nat} (h : 2 ≤ n) : gr2Coeff n = n := by
  simp [gr2Coeff, supportCoefficient, Nat.sub_add_cancel h]

/-- `Gr_+(3,6)` (type `D₄`) coefficient extracted from the fixed support law. -/
def gr36Coeff : Nat := supportCoefficient 6 .fixed

theorem gr36Coeff_formula : gr36Coeff = 4 := by
  native_decide

/-- Fixed-node coefficient in the `E₆` branch (`Gr_+(3,7)` / `Gr_+(4,7)`). -/
def gr37FixedCoeff : Nat := supportCoefficient 12 .fixed

theorem gr37FixedCoeff_formula : gr37FixedCoeff = 7 := by
  native_decide

/-- Paired-node coefficient in the `E₆` branch (`Gr_+(3,7)` / `Gr_+(4,7)`). -/
def gr37PairedCoeff : Nat := supportCoefficient 12 .paired

theorem gr37PairedCoeff_formula : gr37PairedCoeff = 14 := by
  native_decide

end ProjectX
