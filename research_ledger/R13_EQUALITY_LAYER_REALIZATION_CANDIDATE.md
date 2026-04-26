# R13 Equality-Layer Realization Candidate

STATUS: GENERATED / OPEN / CANDIDATE  
ARGUMENT_STATUS: ROW_BINDING_SUPPORTED / GENERATED  
CHECK_STATUS: NOT_CHECKED  
SOURCE_STATUS: SOURCE_COVERAGE_GUARDED / NOT_THEOREM  
PROMOTION_STATUS: BLOCKED  
TARGET_LOCATION: research_ledger/  
DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json

## 0. Non-Promotion Notice

This artifact develops R13 as a candidate realization-class discriminator for Formation Medium work.

It is not a source-extracted claim, not a theorem, not a validator result, not a Lean/Z3 proof, not a substrate claim, not engineering evidence, and not a corporate/investor claim.

Authority reference:

```text
research_ledger/R1_R14_DISCRIMINATOR_LEDGER.md
```

Existing check target and result:

```text
CHK-R13-EQUALITY-LAYER
Result: PASS_SOURCE_COVERAGE only
```

That result is source-coverage discipline, not theorem status.

## 1. Purpose

R13 is currently described as:

```text
Equality-layer status:
Equality layer is typed as absent / generic inequality / degenerate equality / intrinsic equality.
```

The purpose of this artifact is to make that useful for Formation Medium work without promoting it.

Core candidate idea:

> A realization class is partly characterized by how its equality layer appears: intrinsically as part of its native definition, generically as inequality, by saturation/degeneration, or absent from the relevant structure.

## 2. Candidate Equality-Layer Types

### EL0 — Absent Equality Layer

Candidate meaning:

```text
No relevant equality layer is present in the scoped object.
```

Use when:

- the family/object has no equality constraints of the relevant kind;
- equality is not part of the row being compared;
- no source/check contact exists.

Status:

```text
GENERATED / OPEN
```

### EL1 — Generic Inequality Layer

Candidate meaning:

```text
The object is governed by inequalities in generic position.
```

Use when:

- equality appears only as boundary/saturation of inequality;
- the default object is inequality-governed;
- equality is not native to the family definition.

Status:

```text
GENERATED / OPEN
```

### EL2 — Degenerative / Saturated Equality Layer

Candidate meaning:

```text
Equality appears by imposing extra constraints, specialization, degeneration, or saturation on a more generic inequality layer.
```

Use when:

- equality is obtained by tuning parameters;
- equality is not generic;
- equality is a limit or specialization of a broader class.

Candidate example from current ledger:

```text
GAssoc: equality layer appears by special saturation / degeneration
```

Status:

```text
THREAD-SUPPORTED / GENERATED / NOT_THEOREM
```

### EL3 — Intrinsic Equality Layer

Candidate meaning:

```text
Equality is part of the native family definition or compatibility law.
```

Use when:

- equality constraints are required by the native structure;
- removing equality changes the realization class;
- equality is not merely a special point inside an inequality family.

Candidate example from current ledger:

```text
C: equality layer is intrinsic to grouped compatibility / nontransversal gluing
```

Status:

```text
THREAD-SUPPORTED / GENERATED / NOT_THEOREM
```

## 3. Candidate Realization-Class Test

A proposed realization-class comparison should record:

```text
family_or_route
carrier_type
inequality_layer
existence_of_equality_layer
equality_layer_status: EL0 | EL1 | EL2 | EL3 | UNKNOWN
source_contacts
check_contacts
promotion_blockers
```

Candidate discriminator:

```text
If two objects share grouped carriers, grouped parameters, grouped factorization, and overlap/submodular inequality structure, but differ in equality-layer status, then they should not be identified as the same realization class without an explicit equivalence proof.
```

Status:

```text
GENERATED / OPEN / CANDIDATE
```

Current thread-supported verdict from R1-R14 ledger:

```text
GAssoc != C as realization classes
C <= GAssoc as equality-saturated specialization/refinement
```

Required caution:

This is thread-supported, not Lean-certified.

## 4. Formation Medium Relevance

### 4.1 Relation to S4

S4 says:

```text
bulk non-faithfulness relative to readout
```

R13 adds a more precise comparison handle:

```text
same or similar readout/factorization layer
but different equality-layer realization status
```

This helps avoid collapsing distinct realization classes just because they share some readout-level structure.

### 4.2 Relation to Bulk/Readout Witness Schema

R13 can refine:

```text
same_readout(x, y)
different_bulk(x, y)
```

by adding:

```text
equality_status(x) != equality_status(y)
```

Possible future predicate:

```text
different_realization_class(x, y) :=
  different_bulk(x, y)
  or equality_status(x) != equality_status(y)
  or representation_equivalence_unproven(x, y)
```

Status:

```text
GENERATED / OPEN / FORMAL_CANDIDATE
```

### 4.3 Relation to Engineering Routes

Engineering routes should eventually answer:

```text
Are constraints intrinsic to the medium,
or imposed by tuning/saturation/degeneration?
```

This gives a new gate for physical-regime triage:

```text
G9 equality-layer intrinsicness
```

Allowed route statuses:

```text
EQUALITY_INTRINSIC
EQUALITY_DEGENERATIVE
EQUALITY_ABSENT
EQUALITY_UNKNOWN
```

Current instruction:

All engineering routes should remain:

```text
EQUALITY_UNKNOWN
```

until external source review or experiment supports stronger classification.

## 5. Relation to Corporate Goal

R13 is important because it turns the company story away from vague “we can reproduce the output” language.

Safe corporate framing:

```text
The technical program distinguishes readout reproduction from realization-class equivalence. One current discriminator is whether equality constraints are intrinsic to a candidate class or arise only by degeneration/saturation.
```

Unsafe corporate framing:

```text
If two routes produce the same readout, they are the same substrate.
```

R13 is a guardrail against that unsafe framing.

## 6. Proposed Matrix Fields

If R14 is converted into a machine-readable class matrix, include:

```text
row: R13
family_or_route
carrier_layer
grouped_carrier_status
grouped_parameter_status
inequality_layer_status
equality_layer_status
source_contacts
check_contacts
result_status
promotion_blockers
notes
```

Allowed `equality_layer_status` values:

```text
ABSENT
GENERIC_INEQUALITY
DEGENERATIVE_EQUALITY
INTRINSIC_EQUALITY
UNKNOWN
```

## 7. Required Next Checks

### R13-NC1 — Preserve Source-Coverage Scope

Do not promote `CHK-R13-EQUALITY-LAYER` beyond:

```text
PASS_SOURCE_COVERAGE
```

unless a typed predicate model / Lean-Z3 proof exists.

### R13-NC2 — Add to R14 Matrix

R13 should become a column/field in:

```text
R1_R14_CLASS_MATRIX_CANDIDATE.json
```

### R13-NC3 — Compare Physical Routes

Only after external source review, apply equality-layer statuses to:

```text
Route A topoelectrical + superconducting microwave hybrid
Route B topological photonics / microwave-photonic hybrid
Route D topological order / anyonic substrates
Route E scattering / S-matrix regimes
```

All should remain UNKNOWN until source-supported.

## 8. Kill Conditions

Reject or rewrite this candidate if:

1. R13 is treated as theorem status.
2. PASS_SOURCE_COVERAGE is treated as formal proof.
3. Equality-layer status is assigned without source/check contact.
4. Physical routes are classified without source review.
5. Degenerative equality is treated as inferior without mathematical reason.
6. Intrinsic equality is treated as physical substrate evidence.
7. Realization-class distinction is inferred from equality status alone without considering readout/bulk/context.
8. R14 class-matrix deficit is ignored.

## 9. Non-Promotion Footer

This artifact records R13 as a generated realization-class discriminator candidate. It does not solve R13, does not solve R14, does not prove realization-class separation, and does not certify engineering or corporate claims.
