import Mathlib
import ProjectX.Spine.ClassLevel

namespace ProjectX

/-- Ambient exact branch object for the `Gr_+(2,n)` / `Gr_+(n-2,n)` family, with the natural
residue domain hypothesis needed to descend to `n-1`. -/
structure Gr2Ambient where
  n : Nat
  hn : 3 ≤ n

/-- Named supporting facet for the ambient `Gr_+(2,n)` exact branch.
At the current level of formalization this records the fact that a supporting short facet is the
relevant residue locus, without distinguishing the `n` different geometric instances. -/
inductive Gr2SupportingFacet where
  | short
  deriving DecidableEq, Repr

/-- Ambient top-interaction representative attached to the `Gr_+(2,n)` exact branch. -/
def gr2AmbientRep (G : Gr2Ambient) : TopClassRep Gr2Support :=
  muGr2Rep G.n

/-- Target representative attached to a supporting short facet.
This is the exact lower branch representative `Gr_+(2,n-1)`. -/
def gr2FacetTargetRep (G : Gr2Ambient) (_ : Gr2SupportingFacet) : TopClassRep Gr2Support :=
  muGr2Rep (G.n - 1)

/-- Ambient residue along a supporting short facet in the `Gr_+(2,n)` exact branch.

Important: this is a family-specific ambient residue law. It is **not** generated from the current
finite-support residue interface, because that interface preserves coefficients and therefore does
not yet capture the `n ↦ n-1` descent visible in the exact `A`-family branch. -/
def gr2ResidueAlongFacet (G : Gr2Ambient) (_ : Gr2SupportingFacet) : TopClassRep Gr2Support :=
  muGr2Rep (G.n - 1)

/-- Ambient `Gr_+(2,n)` residue theorem: residue along a supporting short facet lands on the exact
lower branch representative. -/
theorem gr2ResidueAlongFacet_eq_target (G : Gr2Ambient) (f : Gr2SupportingFacet) :
    gr2ResidueAlongFacet G f = gr2FacetTargetRep G f := by
  cases f <;> rfl

/-- Degree-lowering form of the ambient `Gr_+(2,n)` residue theorem. -/
theorem gr2ResidueAlongFacet_degree (G : Gr2Ambient) (f : Gr2SupportingFacet) :
    (gr2ResidueAlongFacet G f).degree = (gr2AmbientRep G).degree - 1 := by
  cases f
  simp [gr2ResidueAlongFacet, gr2FacetTargetRep, gr2AmbientRep, muGr2Rep]
  omega

/-- Explicit coefficient form of the ambient `Gr_+(2,n)` residue theorem. -/
theorem gr2ResidueAlongFacet_coeff (G : Gr2Ambient) :
    TopClassRep.coefficient (gr2ResidueAlongFacet G .short) Gr2Support.paired = Int.ofNat (G.n - 1) := by
  simp [gr2ResidueAlongFacet, muGr2Rep]

/-- Exact lower representative identification for the ambient `Gr_+(2,n)` branch. -/
theorem gr2ResidueAlongFacet_eq_prev (G : Gr2Ambient) :
    gr2ResidueAlongFacet G .short = muGr2Rep (G.n - 1) := rfl

end ProjectX
