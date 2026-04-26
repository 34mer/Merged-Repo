# Formation Medium Bulk / Readout Witness Schema

STATUS: GENERATED / OPEN / FORMAL_CANDIDATE  
ARGUMENT_STATUS: GENERATED / PRIOR_CONVERSATION_ORE  
CHECK_STATUS: NOT_CHECKED  
SOURCE_STATUS: PARTIAL / SOURCE_ANCHORED_CAUTION  
PROMOTION_STATUS: BLOCKED  
TARGET_LOCATION: research_ledger/  
DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json

## 0. Non-Promotion Notice

This artifact defines a generated candidate schema for reasoning about bulk/readout non-faithfulness in the Formation Medium project.

It is not a source-extracted claim, not a theorem, not a validator result, not a physical substrate claim, not engineering feasibility evidence, and not an investor/corporate proof.

It is a formal-candidate interface for future checks. It must not be used to promote S4, Formation Medium substrate claims, or physical implementation claims.

Inputs:

```text
research_ledger/S2_STAR_S4_DISTINCTNESS_CANDIDATE.md
research_ledger/FORMATION_MEDIUM_LAYER_1_SPEC.md
research_ledger/PREVIOUS_GPT_EQUATION_MINING_SYNTHESIS_001.md
EXT-AMP-PRIME-001
CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION
```

## 1. Purpose

The purpose of this schema is to separate three ideas that are easy to conflate:

1. A stable or canonical readout exists.
2. The readout is shared by two realizations.
3. The underlying bulk realization is the same.

The S2* + S4 distinction requires that (1) and (2) do not imply (3).

Layer 1 relation:

```text
FM1-C5 — Bulk/Readout Non-Faithfulness Constraint
```

## 2. Minimal Predicate Vocabulary

### 2.1 Readout Predicate

Candidate predicate:

```text
readout(x) = r
```

Meaning:

`x` is a candidate realization and `r` is the readout-level object exposed by `x`.

Allowed readings of `r` may include, depending on source/check context:

```text
canonical form
boundary structure
logarithmic form
cut/face/factorization data
observable readout channel
scattering/amplitude data
```

Status:

```text
GENERATED / OPEN
```

### 2.2 Same-Readout Predicate

Candidate predicate:

```text
same_readout(x, y) := readout(x) = readout(y)
```

Meaning:

Two realizations expose the same readout-level object under the chosen readout map.

Required caution:

The readout map must be specified. Without a specified readout map, `same_readout` is meaningless.

Status:

```text
GENERATED / OPEN / FORMAL_CANDIDATE
```

### 2.3 Bulk Predicate

Candidate predicate:

```text
bulk(x) = b
```

Meaning:

`x` has an internal or geometric realization `b` at the bulk level.

Allowed readings of `b` may include, depending on source/check context:

```text
bulk positive geometry
internal substrate configuration
geometric realization class
representation class
physical state-space realization
```

Required caution:

The bulk notion must be scoped. Positive-geometric bulk, representation bulk, and physical substrate bulk are not automatically the same.

Status:

```text
GENERATED / OPEN
```

### 2.4 Different-Bulk Predicate

Candidate predicate:

```text
different_bulk(x, y) := bulk(x) != bulk(y)
```

Meaning:

Two realizations differ at the chosen bulk level.

Required caution:

`different_bulk` must identify the level of difference: geometric, representational, physical, or substrate-level.

Status:

```text
GENERATED / OPEN / FORMAL_CANDIDATE
```

## 3. Non-Faithful Readout Witness

Minimal witness schema:

```text
exists x, y such that:
  same_readout(x, y)
  and different_bulk(x, y)
```

Interpretation:

The readout map is non-faithful with respect to the chosen bulk equivalence relation.

Equivalent statement:

```text
readout(x) = readout(y)
not imply bulk(x) = bulk(y)
```

Status:

```text
GENERATED / OPEN / FORMAL_CANDIDATE
```

Current source contact:

```text
EXT-AMP-PRIME-001
```

Current support limitation:

The strongest current anchor is the Amplituhedron / Amplituhedron-Prime caution: same boundary structure and logarithmic form, different bulk geometry. This does not automatically generalize to physical substrates or all positive geometries.

## 4. Boundary-Determined vs Bulk-Sensitive Classification

The equation mining pass identified the following discriminator as central:

```text
boundary_determined_vs_bulk_sensitive
```

This schema refines it into two candidate classifiers.

### 4.1 Boundary-Determined Constraint

Candidate classifier:

```text
boundary_determined(C) :=
  for all x, y,
    same_readout(x, y) -> (C(x) iff C(y))
```

Meaning:

A candidate constraint `C` is boundary-determined if it depends only on readout-level data. If two realizations have the same readout, `C` gives the same answer for both.

Example reading:

If a constraint survives replacement of the amplituhedron by Amplituhedron-Prime while boundary/log-form data are held fixed, that constraint is a candidate boundary-determined constraint.

Status:

```text
GENERATED / OPEN / FORMAL_CANDIDATE
```

### 4.2 Bulk-Sensitive Constraint

Candidate classifier:

```text
bulk_sensitive(C) :=
  exists x, y such that:
    same_readout(x, y)
    and different_bulk(x, y)
    and C(x) != C(y)
```

Meaning:

A candidate constraint `C` is bulk-sensitive if it can distinguish two realizations with the same readout but different bulk.

Example reading:

If a constraint fails when moving from the amplituhedron to Amplituhedron-Prime even though boundary/log-form data are preserved, that constraint is a candidate bulk-sensitive constraint.

Status:

```text
GENERATED / OPEN / FORMAL_CANDIDATE
```

### 4.3 Unknown / Under-Scoped Constraint

Candidate classifier:

```text
classification_unknown(C)
```

Use when:

1. the readout map is not specified;
2. the bulk equivalence relation is not specified;
3. no same-readout/different-bulk witness exists;
4. the source only gives analogy-level support;
5. the constraint mixes readout-level and bulk-level language.

Status:

```text
GENERATED / OPEN
```

## 5. Application to Formation Medium Constraints

### FM1-C4 — Canonical Boundary Readout

Candidate classification:

```text
boundary_determined(FM1-C4) = plausible but not checked
```

Reason:

FM1-C4 concerns the readout itself: boundary/canonical-form-like and recursively constrained.

Blocker:

This is source-covered only; no formal readout theorem exists.

Status:

```text
GENERATED / OPEN / SOURCE_COVERAGE_ONLY
```

### FM1-C5 — Bulk / Readout Non-Faithfulness

Candidate classification:

```text
bulk_sensitive(FM1-C5) = plausible design role
```

Reason:

FM1-C5 is explicitly about whether readout determines bulk. It should become the place where same-readout/different-bulk witnesses are registered.

Blocker:

No general Formation Medium witness exists. The current source anchor is Amplituhedron-Prime only.

Status:

```text
GENERATED / OPEN / SOURCE_ANCHORED_CAUTION
```

### FM1-C1 — Native Carrier

Candidate classification:

```text
classification_unknown(FM1-C1)
```

Reason:

Carrier constraints may be bulk-sensitive, because carrier shape can change across representations while readout survives. Prior mining repeatedly warns that fixed carrier shape is presentation-bound.

Status:

```text
GENERATED / OPEN
```

### FM1-C2 / FM1-C3 — Native Operations and Settling

Candidate classification:

```text
classification_unknown(FM1-C2)
classification_unknown(FM1-C3)
```

Reason:

Operations and settling laws are likely bulk/substrate-sensitive, but the repo has no witness or physical substrate model.

Status:

```text
GENERATED / OPEN
```

## 6. Prime-Scoped Witness Template

Candidate finite witness template:

```text
x = amplituhedron_like_object
y = amplituhedron_prime_like_object
readout(x) = boundary_structure_and_logarithmic_form(x)
readout(y) = boundary_structure_and_logarithmic_form(y)

same_readout(x, y)
different_bulk(x, y)
```

Source contact:

```text
EXT-AMP-PRIME-001
```

Allowed use:

This may be used as a cautionary witness template for positive-geometry readout non-faithfulness.

Blocked use:

It may not be used as proof that physical substrates, all positive geometries, or all formation media exhibit non-faithful readout.

Status:

```text
SOURCE_ANCHORED_CAUTION / GENERATED_FORMAL_TEMPLATE
```

## 7. Engineering Interpretation Gate

For engineering triage, the schema imposes a gate:

```text
An engineering route must say whether its readout is expected to be faithful or non-faithful relative to internal substrate state.
```

Three allowed statuses:

```text
READOUT_FAITHFUL
READOUT_NONFAITHFUL
READOUT_FAITHFULNESS_UNKNOWN
```

Current instruction:

All engineering routes in `FORMATION_MEDIUM_ENGINEERING_TRIAGE_001.md` should remain:

```text
READOUT_FAITHFULNESS_UNKNOWN
```

unless external source review or experiment supports stronger classification.

## 8. Future Checker Path

A future checker could be added only after source recheck and formal scoping.

Candidate future target:

```text
CHK-FM-BULK-READOUT-WITNESS-SCHEMA
```

Candidate checker duties:

1. Verify every witness declares a readout map.
2. Verify every witness declares a bulk equivalence relation.
3. Verify every witness distinguishes source-level, representation-level, and physical-substrate-level bulk.
4. Prevent generalization beyond source scope.
5. Prevent engineering routes from claiming readout non-faithfulness without evidence.

Status:

```text
NOT_CREATED / FUTURE_TARGET
```

No formal check target is created by this artifact.

## 9. Kill Conditions

Reject or rewrite this schema if:

1. `same_readout` is used without specifying the readout map.
2. `different_bulk` is used without specifying the bulk equivalence relation.
3. Amplituhedron-Prime caution is generalized beyond its source scope.
4. Physical substrate non-faithfulness is inferred from positive-geometry bulk non-faithfulness.
5. Engineering routes use this schema as feasibility evidence.
6. FM1-C5 is promoted to theorem status without a checker/formal witness.
7. S4 is treated as repo-native vocabulary without registration.
8. Boundary-determined constraints are confused with substrate-invariant constraints.

## 10. Non-Promotion Footer

This schema is a generated formal candidate. It is useful for structuring future checks and engineering gates. It does not establish a theorem, prove non-faithful readout, select a substrate, or certify a company-facing technical claim.
