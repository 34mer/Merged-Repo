import ProjectX.Spine.UnifiedExactFiniteResidue

namespace ProjectX

/-- Unified ambient object for the exact finite branch currently formalized in Lean. -/
inductive ExactFiniteAmbient where
  | gr2 (n : Nat) (hn : 3 ≤ n)
  | gr36
  | gr37

/-- Unified supporting facets for the exact finite branch currently formalized in Lean. -/
inductive ExactFiniteFacet : ExactFiniteAmbient → Type where
  | gr2_short (n : Nat) (hn : 3 ≤ n) : ExactFiniteFacet (.gr2 n hn)
  | gr36_to_A3 : ExactFiniteFacet .gr36
  | gr37_to_A5 : ExactFiniteFacet .gr37
  | gr37_to_D5Shadow : ExactFiniteFacet .gr37

/-- Support type attached to each exact finite ambient branch. -/
def exactFiniteSupport : ExactFiniteAmbient → Type
  | .gr2 _ _ => Gr2Support
  | .gr36 => Gr36Support
  | .gr37 => Gr37Support

/-- Ambient representative attached to each exact finite ambient branch. -/
def exactFiniteRep : (b : ExactFiniteAmbient) → TopClassRep (exactFiniteSupport b)
  | .gr2 n _ => muGr2Rep n
  | .gr36 => muGr36Rep
  | .gr37 => muGr37Rep

/-- Target support type selected by each exact finite supporting facet. -/
def exactFiniteFacetTargetSupport : {b : ExactFiniteAmbient} → ExactFiniteFacet b → Type
  | .gr2 _ _, .gr2_short _ _ => Gr2Support
  | .gr36, .gr36_to_A3 => Gr2Support
  | .gr37, .gr37_to_A5 => Gr2Support
  | .gr37, .gr37_to_D5Shadow => SingleSupport

/-- Target representative attached to each exact finite supporting facet. -/
def exactFiniteFacetTargetRep : {b : ExactFiniteAmbient} (f : ExactFiniteFacet b) →
    TopClassRep (exactFiniteFacetTargetSupport f)
  | .gr2 n hn, .gr2_short _ _ => muGr2Rep (n - 1)
  | .gr36, .gr36_to_A3 => muA3ParabolicRep
  | .gr37, .gr37_to_A5 => muA5ParabolicRep
  | .gr37, .gr37_to_D5Shadow => muD5ShadowRep

/-- Unified affine residue data attached to each exact finite supporting facet. -/
def exactFiniteAffineResidueData : {b : ExactFiniteAmbient} (f : ExactFiniteFacet b) →
    AffineResidueData (exactFiniteSupport b) (exactFiniteFacetTargetSupport f)
  | .gr2 _ _, .gr2_short _ _ => affineResidueData_Gr2
  | .gr36, .gr36_to_A3 => affineResidueData_Gr36_to_A3
  | .gr37, .gr37_to_A5 => affineResidueData_Gr37_to_A5
  | .gr37, .gr37_to_D5Shadow => affineResidueData_Gr37_to_D5Shadow

/-- Unified affine residue along a supporting facet of the exact finite branch. -/
def exactFiniteResidueAlongFacet : {b : ExactFiniteAmbient} (f : ExactFiniteFacet b) →
    TopClassRep (exactFiniteFacetTargetSupport f)
  | b, f => affineResidue (exactFiniteAffineResidueData f) (exactFiniteRep b)

/-- Unified exact finite residue theorem: residue along any currently formalized exact finite
supporting facet lands on the named target representative for that facet. -/
theorem exactFiniteResidueAlongFacet_eq_target : {b : ExactFiniteAmbient} (f : ExactFiniteFacet b) →
    exactFiniteResidueAlongFacet f = exactFiniteFacetTargetRep f
  | .gr2 n hn, .gr2_short _ _ => by
      simpa [exactFiniteResidueAlongFacet, exactFiniteAffineResidueData, exactFiniteRep,
        exactFiniteFacetTargetRep] using affineResidue_Gr2_eq_prev ⟨n, hn⟩
  | .gr36, .gr36_to_A3 => by
      simpa [exactFiniteResidueAlongFacet, exactFiniteAffineResidueData, exactFiniteRep,
        exactFiniteFacetTargetRep] using affineResidue_Gr36_to_A3_eq_target
  | .gr37, .gr37_to_A5 => by
      simpa [exactFiniteResidueAlongFacet, exactFiniteAffineResidueData, exactFiniteRep,
        exactFiniteFacetTargetRep] using affineResidue_Gr37_to_A5_eq_target
  | .gr37, .gr37_to_D5Shadow => by
      simpa [exactFiniteResidueAlongFacet, exactFiniteAffineResidueData, exactFiniteRep,
        exactFiniteFacetTargetRep] using affineResidue_Gr37_to_D5Shadow_eq_target

/-- Degree-lowering form of the unified exact finite residue theorem. -/
theorem exactFiniteResidueAlongFacet_degree : {b : ExactFiniteAmbient} (f : ExactFiniteFacet b) →
    (exactFiniteResidueAlongFacet f).degree = (exactFiniteRep b).degree - 1
  | b, f => by
      simp [exactFiniteResidueAlongFacet, exactFiniteRep]

end ProjectX
