# 2017 Positive Geometry Intake Plan

STATUS: GENERATED / OPEN / SOURCE_NEEDED  
ARGUMENT_STATUS: GENERATED  
CHECK_STATUS: NOT_CHECKED  
PROMOTION_STATUS: BLOCKED  
TARGET_LOCATION: research_ledger/  
DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json

## 0. Non-Promotion Notice

This is an intake plan, not a source-extracted claim. It does not certify any S2*, B1, B2, or formation-medium statement.

The 2017 Positive Geometry source is currently a required source gap for the S2* + S4 distinction and Formation Medium Layer 0/1 readout constraints.

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
NOT IN CURRENT SOURCE_CORPUS
SOURCE_NEEDED
SOURCE_GAP
```

## 2. Why This Source Matters

This source is required before promoting the following generated/partial claims:

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

Status before extraction:

```text
SOURCE_NEEDED
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

Status before extraction:

```text
SOURCE_NEEDED
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

Status before extraction:

```text
SOURCE_NEEDED
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

Status before extraction:

```text
SOURCE_NEEDED
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

Status before extraction:

```text
SOURCE_NEEDED
```

## 4. Expected Repo Updates After Source Is Available

Do not perform these until the source file is actually present and inspected.

### 4.1 Source Corpus Update

Add a new source record to `SOURCE_CORPUS.json` or the repo-native equivalent.

Candidate paper id:

```text
POS_GEOM_2017
```

Do not finalize id until checked against repo naming conventions.

### 4.2 Source Binding Update

Bind the checked-in source file in the source binding manifest.

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

Only after source inspection, add claims with ids matching repo convention:

```text
EXT-POS-GEOM-2017-001
EXT-POS-GEOM-2017-002
...
```

Do not use these exact ids until actual repo convention/paper_id is finalized.

### 4.4 Formal Check Targets

Possible later check targets:

```text
CHK-POS-GEOM-CANONICAL-BOUNDARY-RECURSION
CHK-S2STAR-READOUT-SOURCE-COVERAGE
CHK-FM1-C4-SOURCE-GAP-CLOSURE
```

Status at intake-plan stage:

```text
NOT_IMPLEMENTED
```

## 5. Promotion Effects If Intake Succeeds

Only if source extraction succeeds:

```text
B1: may move from SOURCE_GAP to PARTIAL/SOURCE_ANCHORED
B2: may move from SOURCE_GAP to PARTIAL/SOURCE_ANCHORED
S2*: may remain CANDIDATE but with stronger source anchor
FM0.4: may update source_status from SOURCE_GAP to PARTIAL/SOURCE_ANCHORED
FM1-C4: may update source_status from SOURCE_GAP to PARTIAL/SOURCE_ANCHORED
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

Acquire or locate the source in the local repo, preferably as Markdown source text. Then run a source-intake update that:

1. registers the source,
2. binds the source file,
3. extracts exact claims,
4. updates validators,
5. leaves all formation-medium statements GENERATED / OPEN until separately checked.
