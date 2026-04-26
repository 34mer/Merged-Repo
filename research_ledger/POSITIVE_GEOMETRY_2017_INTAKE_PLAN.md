# 2017 Positive Geometry Intake Plan

STATUS: GENERATED / OPEN / SOURCE_INTAKE_STARTED  
ARGUMENT_STATUS: GENERATED  
CHECK_STATUS: NOT_CHECKED  
PROMOTION_STATUS: BLOCKED  
TARGET_LOCATION: research_ledger/  
DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json

## 0. Non-Promotion Notice

This is an intake plan, not a source-extracted claim. It does not certify any S2*, B1, B2, or formation-medium statement.

The 2017 Positive Geometry source now has initial POS_GEOM_2017 source-intake records, but remains a required source-coverage and formalization gap for the S2* + S4 distinction and Formation Medium Layer 0/1 readout constraints.

## 1. Target Source

Working target:

```text
Arkani-Hamed, Bai, He, Yan — Positive Geometries and Canonical Forms
```

Expected role:

```text
Primary source for general positive geometry definitions, canonical forms, logarithmic singularities, boundary recursion, and residues-as-boundary-canonical-forms.
```

Current repo status:

```text
POS_GEOM_2017 present in SOURCE_CORPUS / SOURCE_PDF_BINDINGS
SOURCE_EXTRACTED / NEEDS_FORMALIZATION
CHECKED status blocked
```

## 2. Why This Source Matters

Checked source coverage and formalization of this source are required before promoting the following generated/partial claims:

```text
B1 — Intrinsic Boundary Semantics
B2 — Unique Recursive Readout
S2* — intrinsic canonical boundary semantics with unique recursive readout
FM0.4 — Boundary / Readout Semantics
FM1-C4 — Canonical Boundary Readout Constraint
```

Current support for these is partial only:

```text
EXT-SCAT-FORMS-001
EXT-INTO-AMP-2013-001
R7
R8
```

Those anchors are not enough to promote a general S2* readout criterion.

## 3. Extraction Targets

When the source is ingested, extract only precise claims into source-extracted form.

### PG2017-T1 — Positive Geometry Definition

Question:

> What exactly is a positive geometry in the source's terminology?

Required extraction:

- carrier/space definition
- boundary stratification requirement
- positivity/admissibility requirements, if stated
- dimensional recursion, if stated

Potential target rows:

```text
S2*
FM0.4
FM1-C4
```

Status after initial extraction:

```text
SOURCE_EXTRACTED / NEEDS_FORMALIZATION / NOT_CHECKED
```

### PG2017-T2 — Canonical Form Definition

Question:

> How does the source define the canonical form associated to a positive geometry?

Required extraction:

- uniqueness conditions
- singularity/logarithmic behavior
- residue constraints
- normalization/sign conventions if present

Potential target rows:

```text
B1
B2
S2*
FM0.4
```

Status after initial extraction:

```text
SOURCE_EXTRACTED / NEEDS_FORMALIZATION / NOT_CHECKED
```

### PG2017-T3 — Boundary Recursion / Residue Semantics

Question:

> Does the source state that residues on boundaries equal canonical forms of boundary positive geometries?

Required extraction:

- exact statement
- scope of recursion
- limitations / assumptions
- examples, if necessary

Potential target rows:

```text
B2
R7 comparison context
FM1-C4
```

Status after initial extraction:

```text
SOURCE_EXTRACTED / NEEDS_FORMALIZATION / NOT_CHECKED
```

### PG2017-T4 — Triangulation / Pushforward Readout

Question:

> Does the source explain canonical forms through triangulations, pushforforwards, or additive decomposition of forms?

Required extraction:

- triangulation conditions
- pushforward statement
- whether readout is independent of triangulation

Potential target rows:

```text
S2*
FM0.4
FM1-C4
```

Status after initial extraction:

```text
SOURCE_EXTRACTED / NEEDS_FORMALIZATION / NOT_CHECKED
```

### PG2017-T5 — Limits of Generalization

Question:

> What does the source not say, especially regarding physical substrates or formation media?

Required extraction:

- no-substrate caveats
- geometry-only scope
- any limitations on canonical-form uniqueness

Potential target rows:

```text
SUPPORT_CAUTION_SURVIVOR_LEDGER
FORMATION_MEDIUM_LAYER_0_SPEC
FORMATION_MEDIUM_LAYER_1_SPEC
```

Status after initial extraction:

```text
SOURCE_EXTRACTED / NEEDS_FORMALIZATION / NOT_CHECKED
```

## 4. Expected Repo Updates After Source Is Available

Initial source registration and extraction are present. Continue to preserve non-promotion discipline and do not treat source intake as formal proof.

### 4.1 Source Corpus Update

Preserve the `POS_GEOM_2017` source record in `SOURCE_CORPUS.json`.

Current paper id:

```text
POS_GEOM_2017
```

### 4.2 Source Binding Update

Preserve the checked-in source file binding in the source binding manifest.

Because the repo has migrated to Markdown-aware source bindings, preferred storage is:

```text
sources/Markdowns/<canonical-positive-geometry-2017-name>.md
```

Allowed storage kinds:

```text
markdown_text
git_lfs_pointer
binary_pdf
```

### 4.3 Source-Extracted Claims

Initial source-extracted claims now exist:

```text
EXT-POS-GEOM-2017-001
EXT-POS-GEOM-2017-002
EXT-POS-GEOM-2017-003
```

They remain SOURCE_EXTRACTED / NEEDS_FORMALIZATION and are not proof results.

### 4.4 Formal Check Targets

Possible later check targets:

```text
CHK-POS-GEOM-CANONICAL-BOUNDARY-RECURSION
CHK-S2STAR-READOUT-SOURCE-COVERAGE
CHK-FM1-C4-SOURCE-GAP-CLOSURE
```

Current status:

```text
CHK-S2STAR-READOUT-SOURCE-COVERAGE: PASS_SOURCE_COVERAGE
CHK-POS-GEOM-CANONICAL-BOUNDARY-RECURSION: PASS_SOURCE_COVERAGE
CHK-POS-GEOM-TRIANGULATION-PUSHFORWARD: PASS_SOURCE_COVERAGE
```

## 5. Promotion Effects If Intake Succeeds

After initial source extraction:

```text
B1: moved past SOURCE_GAP to SOURCE_COVERAGE_IMPLEMENTED / PARTIAL, but remains NOT_THEOREM
B2: moved past SOURCE_GAP to SOURCE_COVERAGE_IMPLEMENTED / PARTIAL, but remains NOT_THEOREM
S2*: may remain CANDIDATE but with stronger source anchor
FM0.4: source_status updated from SOURCE_GAP to PARTIAL / SOURCE_COVERAGE_IMPLEMENTED, but remains not theorem/substrate status
FM1-C4: source_status updated from SOURCE_GAP to PARTIAL / SOURCE_COVERAGE_IMPLEMENTED, but remains not theorem/substrate status
```

No automatic promotion to CHECKED occurs.

## 6. Kill Conditions

This intake plan must be revised if:

1. The source is already present under a different name/id.
2. The source does not state the expected canonical-form recursion strongly enough.
3. The source's scope is narrower than the S2* candidate needs.
4. The source supports positive geometry but not formation-medium substrate interpretation.
5. Extraction would blur SOURCE_EXTRACTED with GENERATED formation-medium language.

## 7. Immediate Next Action

Continue from the existing POS_GEOM_2017 source-intake update by implementing the remaining formal/source-coverage validators. Formation-medium statements must remain GENERATED / OPEN until separately checked.
