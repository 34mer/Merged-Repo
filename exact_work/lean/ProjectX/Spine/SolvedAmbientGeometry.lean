import ProjectX.Spine.ParabolicRecursion

namespace ProjectX

/-- The solved exact branches currently carried as ambient objects in the Lean formalization. -/
inductive SolvedExactBranch where
  | gr36
  | gr37
  deriving DecidableEq, Repr

/-- Support type attached to each solved exact branch. -/
def BranchSupport : SolvedExactBranch → Type
  | .gr36 => Gr36Support
  | .gr37 => Gr37Support

/-- Ambient top-interaction representative attached to each solved exact branch. -/
def branchRep : (b : SolvedExactBranch) → TopClassRep (BranchSupport b)
  | .gr36 => muGr36Rep
  | .gr37 => muGr37Rep

/-- Named supporting facets for the solved exact branches. -/
inductive SupportingFacet : SolvedExactBranch → Type where
  | gr36_to_A3 : SupportingFacet .gr36
  | gr37_to_A5 : SupportingFacet .gr37
  | gr37_to_D5Shadow : SupportingFacet .gr37
  deriving DecidableEq, Repr

/-- Target support type selected by each supporting facet. -/
def FacetTargetSupport : {b : SolvedExactBranch} → SupportingFacet b → Type
  | .gr36, .gr36_to_A3 => Gr2Support
  | .gr37, .gr37_to_A5 => Gr2Support
  | .gr37, .gr37_to_D5Shadow => SingleSupport

/-- Target representative object selected by each supporting facet. -/
def facetTargetRep : {b : SolvedExactBranch} (f : SupportingFacet b) → TopClassRep (FacetTargetSupport f)
  | .gr36, .gr36_to_A3 => muA3ParabolicRep
  | .gr37, .gr37_to_A5 => muA5ParabolicRep
  | .gr37, .gr37_to_D5Shadow => muD5ShadowRep

/-- Residue data attached to each supporting facet. -/
def facetResidueData : {b : SolvedExactBranch} (f : SupportingFacet b) → ResidueData (BranchSupport b) (FacetTargetSupport f)
  | .gr36, .gr36_to_A3 => residueData_Gr36_to_A3
  | .gr37, .gr37_to_A5 => residueData_Gr37_to_A5
  | .gr37, .gr37_to_D5Shadow => residueData_Gr37_to_D5Shadow

/-- Residue representative along a named supporting facet. -/
def residueAlongFacet : {b : SolvedExactBranch} (f : SupportingFacet b) → TopClassRep (FacetTargetSupport f)
  | b, f => residue (facetResidueData f) (branchRep b)

/-- Ambient solved-branch residue theorem: residue along a named supporting facet lands on the
named target representative for that facet. -/
theorem residueAlongFacet_eq_target : {b : SolvedExactBranch} (f : SupportingFacet b) →
    residueAlongFacet f = facetTargetRep f
  | .gr36, .gr36_to_A3 => by
      simpa [residueAlongFacet, branchRep, facetTargetRep, facetResidueData] using parabolicRecursion_Gr36_to_A3
  | .gr37, .gr37_to_A5 => by
      simpa [residueAlongFacet, branchRep, facetTargetRep, facetResidueData] using parabolicRecursion_Gr37_to_A5
  | .gr37, .gr37_to_D5Shadow => by
      simpa [residueAlongFacet, branchRep, facetTargetRep, facetResidueData] using parabolicRecursion_Gr37_to_D5Shadow

/-- Degree-lowering form of the ambient solved-branch residue theorem. -/
theorem residueAlongFacet_degree : {b : SolvedExactBranch} (f : SupportingFacet b) →
    (residueAlongFacet f).degree = (branchRep b).degree - 1
  | .gr36, .gr36_to_A3 => by
      simpa [residueAlongFacet, branchRep, facetResidueData] using parabolicRecursion_Gr36_to_A3_degree
  | .gr37, .gr37_to_A5 => by
      simpa [residueAlongFacet, branchRep, facetResidueData] using parabolicRecursion_Gr37_to_A5_degree
  | .gr37, .gr37_to_D5Shadow => by
      simpa [residueAlongFacet, branchRep, facetResidueData] using parabolicRecursion_Gr37_to_D5Shadow_degree

end ProjectX
