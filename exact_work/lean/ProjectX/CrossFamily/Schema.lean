import Mathlib

namespace ProjectX
namespace CrossFamily

/-- Conservative cross-family profile carrying only features that are actually formalized on both
sides of the current project state. -/
structure ConservativeFamilyProfile where
  grading : Nat
  invariantSlots : Nat
  oneStepDelta : Int
  hasCanonicalFamilyObject : Bool
  hasCanonicalClassifier : Bool
  hasExactOneStepLaw : Bool

/-- A family profile is comparison-ready when all currently required conservative structural fields
are present. -/
def ComparisonReady (P : ConservativeFamilyProfile) : Prop :=
  P.hasCanonicalFamilyObject = true ∧
  P.hasCanonicalClassifier = true ∧
  P.hasExactOneStepLaw = true

@[simp] theorem comparisonReady_iff (P : ConservativeFamilyProfile) :
    ComparisonReady P ↔
      P.hasCanonicalFamilyObject = true ∧
      P.hasCanonicalClassifier = true ∧
      P.hasExactOneStepLaw = true := by
  rfl

end CrossFamily
end ProjectX
