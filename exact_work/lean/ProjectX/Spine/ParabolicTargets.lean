import ProjectX.Spine.ResidueRecursion

namespace ProjectX

/-- Named representative for the `A₃` parabolic target appearing in the solved `D₄ -> A₃`
residue recursion. -/
def muA3ParabolicRep : TopClassRep Gr2Support :=
  { degree := 2
    coeff := fun
      | .paired => 4 }

@[simp] theorem muA3ParabolicRep_degree : muA3ParabolicRep.degree = 2 := rfl
@[simp] theorem muA3ParabolicRep_coeff :
    TopClassRep.coefficient muA3ParabolicRep Gr2Support.paired = 4 := rfl

/-- Named representative for the `A₅` parabolic target appearing in the solved `E₆ -> A₅`
residue recursion. -/
def muA5ParabolicRep : TopClassRep Gr2Support :=
  { degree := 4
    coeff := fun
      | .paired => 7 }

@[simp] theorem muA5ParabolicRep_degree : muA5ParabolicRep.degree = 4 := rfl
@[simp] theorem muA5ParabolicRep_coeff :
    TopClassRep.coefficient muA5ParabolicRep Gr2Support.paired = 7 := rfl

/-- Named representative for the `D₅` shadow target carried by the solved `E₆ -> D₅` residue
shadow in the current formalization. -/
def muD5ShadowRep : TopClassRep SingleSupport :=
  { degree := 4
    coeff := fun
      | .carrier => 14 }

@[simp] theorem muD5ShadowRep_degree : muD5ShadowRep.degree = 4 := rfl
@[simp] theorem muD5ShadowRep_coeff :
    TopClassRep.coefficient muD5ShadowRep SingleSupport.carrier = 14 := rfl

/-- Object-level match for the solved `D₄ -> A₃` residue recursion. -/
theorem residueRep_Gr36_to_A3_eq_muA3ParabolicRep :
    residueRep_Gr36_to_A3 = muA3ParabolicRep := by
  apply TopClassRep.ext
  · simp [residueRep_Gr36_to_A3, muA3ParabolicRep]
  · intro s
    cases s <;> simp [residueRep_Gr36_to_A3, muA3ParabolicRep]

/-- Object-level match for the solved `E₆ -> A₅` residue recursion. -/
theorem residueRep_Gr37_to_A5_eq_muA5ParabolicRep :
    residueRep_Gr37_to_A5 = muA5ParabolicRep := by
  apply TopClassRep.ext
  · simp [residueRep_Gr37_to_A5, muA5ParabolicRep]
  · intro s
    cases s <;> simp [residueRep_Gr37_to_A5, muA5ParabolicRep]

/-- Object-level match for the carried `E₆ -> D₅` residue shadow. -/
theorem residueRep_Gr37_to_D5Shadow_eq_muD5ShadowRep :
    residueRep_Gr37_to_D5Shadow = muD5ShadowRep := by
  apply TopClassRep.ext
  · simp [residueRep_Gr37_to_D5Shadow, muD5ShadowRep]
  · intro s
    cases s <;> simp [residueRep_Gr37_to_D5Shadow, muD5ShadowRep]

end ProjectX
