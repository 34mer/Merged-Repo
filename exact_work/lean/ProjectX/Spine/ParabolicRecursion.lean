import ProjectX.Spine.ParabolicTargets

namespace ProjectX

/-- Residue sign on the solved `D₄ -> A₃` branch. -/
@[simp] theorem residueData_Gr36_to_A3_sign : residueData_Gr36_to_A3.sign = .plus := rfl

/-- Residue sign on the solved `E₆ -> A₅` branch. -/
@[simp] theorem residueData_Gr37_to_A5_sign : residueData_Gr37_to_A5.sign = .plus := rfl

/-- Residue sign on the carried `E₆ -> D₅` shadow branch. -/
@[simp] theorem residueData_Gr37_to_D5Shadow_sign : residueData_Gr37_to_D5Shadow.sign = .plus := rfl

/-- The solved `D₄ -> A₃` residue recursion holds at the object-representative level. -/
theorem parabolicRecursion_Gr36_to_A3 :
    residueRep_Gr36_to_A3 = muA3ParabolicRep :=
  residueRep_Gr36_to_A3_eq_muA3ParabolicRep

/-- The solved `E₆ -> A₅` residue recursion holds at the object-representative level. -/
theorem parabolicRecursion_Gr37_to_A5 :
    residueRep_Gr37_to_A5 = muA5ParabolicRep :=
  residueRep_Gr37_to_A5_eq_muA5ParabolicRep

/-- The carried `E₆ -> D₅` shadow residue recursion holds at the object-representative level. -/
theorem parabolicRecursion_Gr37_to_D5Shadow :
    residueRep_Gr37_to_D5Shadow = muD5ShadowRep :=
  residueRep_Gr37_to_D5Shadow_eq_muD5ShadowRep

/-- Degree-lowering form of the solved `D₄ -> A₃` residue recursion. -/
theorem parabolicRecursion_Gr36_to_A3_degree :
    residueRep_Gr36_to_A3.degree = muGr36Rep.degree - 1 := by
  simp [residueRep_Gr36_to_A3, muGr36Rep]

/-- Degree-lowering form of the solved `E₆ -> A₅` residue recursion. -/
theorem parabolicRecursion_Gr37_to_A5_degree :
    residueRep_Gr37_to_A5.degree = muGr37Rep.degree - 1 := by
  simp [residueRep_Gr37_to_A5, muGr37Rep]

/-- Degree-lowering form of the carried `E₆ -> D₅` shadow residue recursion. -/
theorem parabolicRecursion_Gr37_to_D5Shadow_degree :
    residueRep_Gr37_to_D5Shadow.degree = muGr37Rep.degree - 1 := by
  simp [residueRep_Gr37_to_D5Shadow, muGr37Rep]

end ProjectX
