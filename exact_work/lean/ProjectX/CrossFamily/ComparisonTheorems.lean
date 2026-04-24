import ProjectX.CrossFamily.Instances

namespace ProjectX
namespace CrossFamily

/-- Current conservative comparison theorem: the surfaceology extracted-family classifier has the
same invariant-slot count as the single-slot exact finite branches (`A` family and `D₄` branch). -/
theorem surfaceology_matches_singleSlot_exactFinite {K : Type _} [CommRing K]
    (D : Surfaceology.ExtractedFamilyDatum K) (n : Nat) (hn : 3 ≤ n) :
    (surfaceologyProfile D).invariantSlots = (exactFiniteProfile (.gr2 n hn)).invariantSlots ∧
    (surfaceologyProfile D).invariantSlots = (exactFiniteProfile ExactFiniteAmbient.gr36).invariantSlots := by
  simp

/-- Current conservative comparison theorem: the surfaceology extracted-family classifier differs in
invariant-slot count from the two-slot exact finite `E₆` branch. -/
theorem surfaceology_differs_from_gr37_invariantSlots {K : Type _} [CommRing K]
    (D : Surfaceology.ExtractedFamilyDatum K) :
    (surfaceologyProfile D).invariantSlots ≠ (exactFiniteProfile ExactFiniteAmbient.gr37).invariantSlots := by
  simp

/-- Current conservative comparison theorem: the exact finite branch and the current surfaceology
family object are both comparison-ready under the shared schema. -/
theorem exactFinite_and_surfaceology_are_comparisonReady {K : Type _} [CommRing K]
    (b : ExactFiniteAmbient) (D : Surfaceology.ExtractedFamilyDatum K) :
    ComparisonReady (exactFiniteProfile b) ∧ ComparisonReady (surfaceologyProfile D) := by
  constructor <;> simp

/-- Current conservative comparison theorem: the exact finite branch and the current surfaceology
family object have opposite one-step recursion directions in the shared schema. -/
theorem exactFinite_and_surfaceology_have_opposite_oneStepDirections {K : Type _} [CommRing K]
    (b : ExactFiniteAmbient) (D : Surfaceology.ExtractedFamilyDatum K) :
    (exactFiniteProfile b).oneStepDelta = - (surfaceologyProfile D).oneStepDelta := by
  simp

/-- Current conservative comparison theorem specialized to fixed-base fixed-length surfaceology
classes. -/
theorem fixedBaseLengthSurfaceology_matches_singleSlot_exactFinite {K : Type _} [CommRing K]
    {base : Surfaceology.CurveMatrix K} {n : Nat}
    (Q : Surfaceology.FixedBaseLengthClass (K := K) base n)
    (m : Nat) (hm : 3 ≤ m) :
    (fixedBaseLengthSurfaceologyProfile Q).invariantSlots = (exactFiniteProfile (.gr2 m hm)).invariantSlots ∧
    (fixedBaseLengthSurfaceologyProfile Q).invariantSlots = (exactFiniteProfile ExactFiniteAmbient.gr36).invariantSlots := by
  simpa [fixedBaseLengthSurfaceologyProfile] using
    surfaceology_matches_singleSlot_exactFinite (D := Q.extractedFamilyDatum) m hm

/-- The current conservative cross-family profile of a fixed-base fixed-length surfaceology class is
entirely determined by its extracted family datum. -/
theorem fixedBaseLengthSurfaceologyProfile_eq_of_sameExtractedFamilyDatum {K : Type _} [CommRing K]
    {base : Surfaceology.CurveMatrix K} {n : Nat}
    (Q₁ Q₂ : Surfaceology.FixedBaseLengthClass (K := K) base n)
    (hD : Q₁.extractedFamilyDatum = Q₂.extractedFamilyDatum) :
    fixedBaseLengthSurfaceologyProfile Q₁ = fixedBaseLengthSurfaceologyProfile Q₂ := by
  cases hD
  rfl

end CrossFamily
end ProjectX
