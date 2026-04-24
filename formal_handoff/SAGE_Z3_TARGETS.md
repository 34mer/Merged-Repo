# Sage / Z3 / Python Targets

Purpose: finite and constraint-based checks before theorem certification.

## Target S1: Cosmohedron move-class finite check

Queue id: `Q2-COSMO-MOVE-CLASSES`

Check target: `CHK-COSMO-MOVE-CLASSES`

Goal:

Generate finite Matryoshka/cosmohedron cover data and compare primitive move classes against associahedron and m=1 sign-family baselines.

Suggested finite output:

```json
{
  "target_id": "CHK-COSMO-MOVE-CLASSES",
  "n_range": [4, 8],
  "families": ["C", "A", "M1"],
  "move_equivalence": "explicit relation name",
  "results": {
    "C": {"primitive_move_classes": []},
    "A": {"primitive_move_classes": []},
    "M1": {"primitive_move_classes": []}
  },
  "counterexamples": []
}
```

Failure condition:

- Cosmohedron move classes collapse to one class under the declared equivalence.
- A/M1 show the same move multiplicity under the same equivalence.
- The equivalence relation is not explicit.

## Target S2: Associahedron unit descent

Queue id: `Q3-ASSOCIAHEDRON-UNIT-DESCENT`

Check target: `CHK-ASSOCIAHEDRON-UNIT-DESCENT`

Goal:

Generate noncrossing chord collections for n-gons, build the face poset by inclusion/refinement, and verify covers change rank by one.

Failure condition:

- A cover relation changes more than one chord/rank unit.
- The poset grading is not explicit.

## Target Z1: R13 equality-layer status

Queue id: `Q1-R13-EQUALITY-LAYER`

Check target: `CHK-R13-EQUALITY-LAYER`

Goal:

Encode a minimal predicate model distinguishing:

- intrinsic/native equality,
- degenerative/saturation equality,
- ordinary inequality.

Suggested logical predicates:

```text
has_inequality(F, law)
has_equality(F, law)
native_to_definition(F, law)
requires_extra_constraint(F, law)
status(F, law) ∈ {inequality, degenerate, intrinsic}
```

Classification rule candidate:

```text
intrinsic(F, law)  := has_equality(F, law) ∧ native_to_definition(F, law)
degenerate(F, law) := has_equality(F, law) ∧ requires_extra_constraint(F, law)
```

Failure condition:

- `intrinsic` and `degenerate` overlap without an explicit resolution rule.
- Source claims do not determine `native_to_definition` vs `requires_extra_constraint`.
- The classification is representation-dependent.

## Target Z2: Surfaceology u-equation / binary behavior

Queue id: `Q4-SURF-U-EQUATION`

Check targets:

- `CHK-SURF-U-EQUATION`
- `CHK-SURF-BINARY-BOUNDARY`

Goal:

For small curve-intersection examples, encode:

```text
u_C + product_D u_D^(int(C,D)) = 1
u_C >= 0
```

and test whether the declared binary behavior follows in the modeled scope.

Failure condition:

- There exists a satisfying assignment with some u outside `[0,1]` under declared assumptions.
- Boundary behavior `u_C -> 0` does not force incompatible variables toward `1` in the modeled limit.

## Result placement

Write actual outputs to:

```text
formal_handoff/results/<target_id>.json
```

and summarize them in:

```text
research_ledger/FORMAL_CHECK_RESULTS.json
```
