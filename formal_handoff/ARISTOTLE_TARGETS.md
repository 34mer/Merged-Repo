# Aristotle / Lean Targets

Purpose: give Aristotle / Lean-style provers exact packets, not chat residue.

These are not proof claims. They are formalization tasks.

## Target A: R13 equality-layer status

Queue id: `Q1-R13-EQUALITY-LAYER`

Check target: `CHK-R13-EQUALITY-LAYER`

Source claim ids:

- `EXT-COSMO-002`
- `EXT-COSMO-COMB-001`

Informal problem:

Classify whether the equality layer for a family is native/intrinsic or only appears by degenerating/saturating a more generic inequality layer.

Desired formal objects:

```lean
inductive EqualityLayerStatus
| absent
| inequality
| degenerate
| intrinsic
```

Desired predicate shape:

```lean
structure EqualityLayerWitness (Family : Type) where
  has_layer : Prop
  native_to_definition : Prop
  obtained_by_extra_constraints : Prop
```

Desired theorem shape:

```lean
-- Do not assert until definitions are source-bound.
theorem cosmohedron_equality_layer_intrinsic :
  equalityLayerStatus Cosmohedron = EqualityLayerStatus.intrinsic := by
  sorry

theorem graph_assoc_equality_layer_degenerate :
  equalityLayerStatus GraphAssocVicinity = EqualityLayerStatus.degenerate := by
  sorry
```

Required output from Aristotle/Lean:

- either a compiling formalization/proof,
- or a precise failure report: missing definitions, underdetermined assumptions, or counterexample.

## Target B: Same-boundary / different-bulk caution

Queue id: `Q5-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION`

Check target: `CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION`

Source claim id:

- `EXT-AMP-PRIME-001`

Formal guard:

A comparator must not infer realization equivalence from equal boundary structure or equal logarithmic form unless a separate bulk-equivalence witness is supplied.

Desired theorem/schema shape:

```lean
structure RealizationEvidence (A B : Type) where
  boundary_equiv : Prop
  canonical_form_equiv : Prop
  bulk_equiv : Prop

axiom no_equiv_without_bulk
  (e : RealizationEvidence A B) :
  e.boundary_equiv -> e.canonical_form_equiv -> ¬ e.bulk_equiv -> ¬ realizationEquivalent A B
```

Required output:

- accepted schema/guard,
- or rejection explaining which assumptions are too strong or incorrectly posed.

## Non-promotion rule

Do not change any project row to `CHECKED` from these targets unless Aristotle/Lean returns an actual verified artifact.
