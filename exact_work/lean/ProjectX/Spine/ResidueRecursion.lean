import ProjectX.Spine.GeometryInterface

namespace ProjectX

/-- Residue from the exact `D₄` branch to the exact `A₃`-type support system.
The unique `D₄` support direction survives as the unique lower direction. -/
def residueData_Gr36_to_A3 : ResidueData Gr36Support Gr2Support where
  sign := .plus
  keep
    | .omegaD => some .paired

/-- Class-level representative residue on the solved `D₄ -> A₃` branch. -/
def residueRep_Gr36_to_A3 : TopClassRep Gr2Support :=
  residue residueData_Gr36_to_A3 muGr36Rep

@[simp] theorem residueRep_Gr36_to_A3_degree : residueRep_Gr36_to_A3.degree = 2 := by
  native_decide

@[simp] theorem residueRep_Gr36_to_A3_coeff :
    TopClassRep.coefficient residueRep_Gr36_to_A3 Gr2Support.paired = 4 := by
  native_decide

/-- Residue from the exact `E₆` branch to its `A₅` supporting facet.
The fixed-node support direction survives and the paired-node direction vanishes. -/
def residueData_Gr37_to_A5 : ResidueData Gr37Support Gr2Support where
  sign := .plus
  keep
    | .omegaA => some .paired
    | .omegaD => none

/-- Class-level representative residue on the solved `E₆ -> A₅` branch. -/
def residueRep_Gr37_to_A5 : TopClassRep Gr2Support :=
  residue residueData_Gr37_to_A5 muGr37Rep

@[simp] theorem residueRep_Gr37_to_A5_degree : residueRep_Gr37_to_A5.degree = 4 := by
  native_decide

@[simp] theorem residueRep_Gr37_to_A5_coeff :
    TopClassRep.coefficient residueRep_Gr37_to_A5 Gr2Support.paired = 7 := by
  native_decide

/-- Residue from the exact `E₆` branch to its `D₅`-supporting facet.
This carries the paired-node support coefficient into a one-direction shadow support type.
It is stronger than a bare scalar, but still weaker than a full exact `D₅` branch formalization. -/
def residueData_Gr37_to_D5Shadow : ResidueData Gr37Support SingleSupport where
  sign := .plus
  keep
    | .omegaA => none
    | .omegaD => some .carrier

/-- Class-level representative residue shadow on the `E₆ -> D₅` branch. -/
def residueRep_Gr37_to_D5Shadow : TopClassRep SingleSupport :=
  residue residueData_Gr37_to_D5Shadow muGr37Rep

@[simp] theorem residueRep_Gr37_to_D5Shadow_degree : residueRep_Gr37_to_D5Shadow.degree = 4 := by
  native_decide

@[simp] theorem residueRep_Gr37_to_D5Shadow_coeff :
    TopClassRep.coefficient residueRep_Gr37_to_D5Shadow SingleSupport.carrier = 14 := by
  native_decide

/-- Formal status marker for the currently exact class-representative residue recursion carried in
the repo. -/
inductive ExactRepresentativeResidueRecursion where
  | D4_to_A3
  | E6_to_A5
  | E6_to_D5_shadow
  deriving DecidableEq, Repr

end ProjectX
