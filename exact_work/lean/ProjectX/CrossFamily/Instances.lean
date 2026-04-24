import ProjectX.CrossFamily.Schema
import ProjectX.Spine.ExactFiniteAmbientUnified
import ProjectX.Surfaceology.ExtractedFamilyClassification

namespace ProjectX
namespace CrossFamily

/-- Conservative comparison profile for the currently formalized exact finite branch. -/
def exactFiniteProfile : ExactFiniteAmbient → ConservativeFamilyProfile
  | .gr2 n _ =>
      { grading := n - 4
        invariantSlots := 1
        oneStepDelta := -1
        hasCanonicalFamilyObject := true
        hasCanonicalClassifier := true
        hasExactOneStepLaw := true }
  | .gr36 =>
      { grading := 3
        invariantSlots := 1
        oneStepDelta := -1
        hasCanonicalFamilyObject := true
        hasCanonicalClassifier := true
        hasExactOneStepLaw := true }
  | .gr37 =>
      { grading := 5
        invariantSlots := 2
        oneStepDelta := -1
        hasCanonicalFamilyObject := true
        hasCanonicalClassifier := true
        hasExactOneStepLaw := true }

/-- Conservative comparison profile for the current surfaceology extracted family datum. -/
def surfaceologyProfile {K : Type _} [CommRing K]
    (D : Surfaceology.ExtractedFamilyDatum K) : ConservativeFamilyProfile :=
  { grading := D.length
    invariantSlots := 1
    oneStepDelta := 1
    hasCanonicalFamilyObject := true
    hasCanonicalClassifier := true
    hasExactOneStepLaw := true }

/-- Surfaceology comparison profile attached directly to a fixed-base fixed-length class. -/
def fixedBaseLengthSurfaceologyProfile {K : Type _} [CommRing K]
    {base : Surfaceology.CurveMatrix K} {n : Nat}
    (Q : Surfaceology.FixedBaseLengthClass (K := K) base n) : ConservativeFamilyProfile :=
  surfaceologyProfile Q.extractedFamilyDatum

@[simp] theorem exactFiniteProfile_ready (b : ExactFiniteAmbient) :
    ComparisonReady (exactFiniteProfile b) := by
  cases b <;> simp [exactFiniteProfile, ComparisonReady]

@[simp] theorem surfaceologyProfile_ready {K : Type _} [CommRing K]
    (D : Surfaceology.ExtractedFamilyDatum K) :
    ComparisonReady (surfaceologyProfile D) := by
  simp [surfaceologyProfile, ComparisonReady]

@[simp] theorem fixedBaseLengthSurfaceologyProfile_ready {K : Type _} [CommRing K]
    {base : Surfaceology.CurveMatrix K} {n : Nat}
    (Q : Surfaceology.FixedBaseLengthClass (K := K) base n) :
    ComparisonReady (fixedBaseLengthSurfaceologyProfile Q) := by
  simpa [fixedBaseLengthSurfaceologyProfile] using surfaceologyProfile_ready Q.extractedFamilyDatum

@[simp] theorem exactFiniteProfile_invariantSlots_gr2 (n : Nat) (hn : 3 ≤ n) :
    (exactFiniteProfile (.gr2 n hn)).invariantSlots = 1 := rfl

@[simp] theorem exactFiniteProfile_invariantSlots_gr36 :
    (exactFiniteProfile ExactFiniteAmbient.gr36).invariantSlots = 1 := rfl

@[simp] theorem exactFiniteProfile_invariantSlots_gr37 :
    (exactFiniteProfile ExactFiniteAmbient.gr37).invariantSlots = 2 := rfl

@[simp] theorem surfaceologyProfile_invariantSlots {K : Type _} [CommRing K]
    (D : Surfaceology.ExtractedFamilyDatum K) :
    (surfaceologyProfile D).invariantSlots = 1 := rfl

@[simp] theorem exactFiniteProfile_oneStepDelta (b : ExactFiniteAmbient) :
    (exactFiniteProfile b).oneStepDelta = -1 := by
  cases b <;> rfl

@[simp] theorem surfaceologyProfile_oneStepDelta {K : Type _} [CommRing K]
    (D : Surfaceology.ExtractedFamilyDatum K) :
    (surfaceologyProfile D).oneStepDelta = 1 := rfl

end CrossFamily
end ProjectX
