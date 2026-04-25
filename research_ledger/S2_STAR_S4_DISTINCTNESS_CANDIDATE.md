# S2* + S4 Distinctness Candidate

STATUS: GENERATED / OPEN / CANDIDATE  
ARGUMENT_STATUS: THREAD_SUPPORTED / GENERATED  
CHECK_STATUS: NOT_CHECKED  
SOURCE_STATUS: PARTIAL / SOURCE_GAP  
PROMOTION_STATUS: BLOCKED  
TARGET_LOCATION: research_ledger/  
DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json

## 0. Non-Promotion Notice

This artifact is not a source-extracted claim, not a formal theorem, not a validator result, and not a checked repo claim.

It is a generated candidate artifact prepared for repo integration under existing Formation repo conventions.

The labels `S1`, `S2*`, `S3`, and `S4` are not repo-native terms. They are candidate/operator labels used only to organize the present argument. They must not be promoted without later source binding, checker/formal support, or an explicit repo-native vocabulary decision.

## 1. Candidate Thesis

A formation-medium specification may need to distinguish between:

1. **Intrinsic canonical boundary/readout semantics**: a structure whose observable/readout content is determined by boundary stratification, canonical form, or recursive residue/readout behavior.
2. **Bulk non-faithfulness relative to readout**: the possibility that distinct bulk geometric realizations can share the same boundary structure and logarithmic/canonical form, so that the readout does not uniquely determine the bulk geometry.

In provisional S-label language:

- `S2*` refers to intrinsic canonical boundary semantics with unique recursive readout.
- `S4` refers to bulk non-faithfulness relative to that readout.

Candidate distinction:

> A formation medium may have a stable, intrinsic readout semantics while still admitting multiple non-equivalent bulk realizations that are indistinguishable at the level of the readout.

This is a generated candidate, not a checked theorem.

## 2. Candidate Labels

### S1 — Candidate Only

Candidate reading: exact carrier plus admissibility rule.

Repo status:

- Not repo-native.
- Closest equivalents are family carrier definitions across `A`, `C`, `M1`, and `S`.
- No single confirmed repo-native term currently matches S1.

Allowed use: candidate label only.

### S2* — Candidate Only

Candidate reading: intrinsic canonical boundary semantics with unique recursive readout.

Repo status:

- Not repo-native.
- Partially supported by source-extracted/corpus material on canonical forms, cuts/faces, residue recursion, and the R8 root-bundle / local transport layer.
- Full source authority requires the 2017 Positive Geometry paper, which is not currently in the source corpus.

Allowed use: generated shorthand for the B1-B3 package below, marked PARTIAL / SOURCE_GAP until 2017 Positive Geometry intake is complete.

### S3 — Candidate Only

Candidate reading: local native operations with polymorphic operation class.

Repo status:

- Not repo-native.
- Closest repo support appears to be R1 unit codimension descent and R2 local move multiplicity.
- Partial coverage only.

Allowed use: not central to this artifact; do not promote.

### S4 — Candidate Only

Candidate reading: bulk non-faithfulness relative to readout.

Repo status:

- Not repo-native.
- Directly anchored by `EXT-AMP-PRIME-001`, which reports same boundary structure and logarithmic form with different bulk geometry.
- Related check target exists: `CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION`.
- That check target is currently `DEFINED_NOT_RUN` / `NOT_IMPLEMENTED` in the repo check-target layer.

Allowed use: generated candidate label anchored to `EXT-AMP-PRIME-001`; must not be promoted beyond the source-supported statement.

## 3. Source / Repo Anchors

### 3.1 Direct Anchor for S4

Primary anchor:

```text
EXT-AMP-PRIME-001
```

Reported source content:

> Same boundary structure and logarithmic form, but different bulk geometry.

Candidate relevance:

This supports the possibility that readout-level structure can be preserved while the bulk positive space differs. This is the strongest current repo anchor for S4.

Support status:

```text
SOURCE_EXTRACTED anchor exists.
Candidate interpretation remains GENERATED / OPEN.
Related check target is DEFINED_NOT_RUN / NOT_IMPLEMENTED.
```

Required caution:

Do not generalize from this source to all positive geometries, all formation media, or all pre-spacetime structures without further support.

### 3.2 Partial Anchors for S2*

Reported partial anchors:

```text
EXT-SCAT-FORMS-001
EXT-INTO-AMP-2013-001
R7
R8
```

Reported support:

- `EXT-SCAT-FORMS-001`: amplitude as canonical form / kinematic associahedron canonical structure.
- `EXT-INTO-AMP-2013-001`: cuts and faces as primary readout mechanism.
- `R7`: parabolic residue recursion, source-backed/exact-work for a solved finite branch.
- `R8`: root-bundle / local transport layer, THREAD-SUPPORTED / EXACT-WORK, relevant as a possible intrinsic boundary/readout transport layer.

Candidate relevance:

These support pieces of intrinsic boundary/readout semantics, especially where canonical forms, cuts/faces, recursive residue/readout behavior, and local transport across residue-family data are involved.

Support status:

```text
PARTIAL
```

Required source gap:

The general positive-geometry principle that canonical forms are recursively characterized by logarithmic singularities on all boundaries and residues equal canonical forms on boundaries requires the 2017 Positive Geometry paper:

```text
Arkani-Hamed, Bai, He, Yan — Positive Geometries and Canonical Forms
```

Current repo corpus status:

```text
NOT IN CORPUS
SOURCE_NEEDED / SOURCE_GAP
```

## 4. Proposed B-Level Decomposition

The S2* + S4 distinction should be represented through B-level subclaims rather than promoted as native S-labels.

### B1 — Intrinsic Boundary Semantics

Candidate statement:

> The relevant readout semantics are carried by boundary structure rather than by an externally imposed computational interpretation.

Support status:

```text
PARTIAL / SOURCE_GAP
```

Current support:

- Partial support from scattering forms / canonical form material.
- R8 may provide a future binding for intrinsic local transport/readout structure, but is not enough by itself to promote B1.
- Stronger authority requires 2017 Positive Geometry intake.

Blocker:

```text
2017 Positive Geometry source not ingested.
```

### B2 — Unique Recursive Readout

Candidate statement:

> The readout is recursively constrained by canonical boundary behavior, for example by residues or restrictions on boundaries.

Support status:

```text
PARTIAL / SOURCE_GAP
```

Current support:

- Partial support from R7 parabolic residue recursion for a solved finite branch.
- Possible future local-transport support from R8.
- General positive-geometry canonical-form recursion requires 2017 Positive Geometry intake.

Blocker:

```text
2017 Positive Geometry source not ingested.
No general validator for S2* readout uniqueness.
```

### B3 — Boundary / Face / Cut Primacy

Candidate statement:

> Faces, cuts, and boundaries can function as primary readout structures for the amplitude/geometry.

Support status:

```text
PARTIAL / SOURCE_ANCHORED
```

Current support:

```text
EXT-INTO-AMP-2013-001
EXT-SCAT-FORMS-001
```

Allowed formulation:

B3 may be stated as source-anchored where tied directly to existing claims about cuts/faces/canonical forms.

Blocked formulation:

Do not state that all physical meaning is exhausted by boundaries unless a source/check explicitly supports that stronger claim.

### B4 — Same Readout, Different Bulk

Candidate statement:

> Two positive spaces may share boundary structure and logarithmic/canonical form while differing as bulk geometries.

Support status:

```text
SOURCE_ANCHORED / GENERATED_INTERPRETATION
```

Current support:

```text
EXT-AMP-PRIME-001
```

Related check target:

```text
CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION
Status: DEFINED_NOT_RUN / NOT_IMPLEMENTED
```

Allowed formulation:

B4 may be used as the strongest anchor for S4, provided the statement remains limited to the Amplituhedron / Amplituhedron-Prime context or explicitly marked as analogy/candidate when generalized.

## 5. Candidate Distinction

Given B1-B4, the proposed distinction is:

```text
S2* concerns the stability or uniqueness of the canonical readout.
S4 concerns the non-uniqueness of the bulk realization relative to that readout.
```

Equivalently:

```text
S2*: the readout is intrinsic and recursively constrained.
S4: the bulk realizing that readout need not be uniquely determined by it.
```

This prevents conflating:

1. having a well-defined canonical readout, with
2. having a unique faithful bulk geometry behind that readout.

The distinction is important for the Formation Medium project because the medium is not being modeled as a computer that calculates a positive geometry. The medium is being specified as a substrate whose settled state has positive-geometric / pre-spacetime readout structure. If S4 holds as a design caution, then the same readout may be realized by multiple bulk substrates or internal configurations.

## 6. Formation-Medium Interpretation

Formation replaces computation.

The substrate does not compute the answer. Its settled state is the answer.

Under the S2* + S4 candidate distinction:

- S2* supplies a condition on the settled state's readout: it must expose intrinsic canonical boundary/readout semantics.
- S4 supplies a caution on substrate inference: the internal bulk realization of the medium may not be faithfully reconstructible from the readout alone.

Therefore, the formation-medium specification should avoid requiring that the substrate's internal bulk degrees of freedom be uniquely reconstructible from the positive-geometric readout.

Safe candidate formulation:

> A formation medium should be specified by native settling behavior that exposes canonical boundary/readout semantics, while allowing that multiple inequivalent internal bulk realizations may produce the same readout-level structure.

Status:

```text
GENERATED / OPEN / CANDIDATE
```

Caution:

This interpretation is consistent with the repo caution that substrate interpretation must not be inferred from positive-geometry rows alone. It remains a generated formation-medium design interpretation, not a repo-supported physical realization claim.

## 7. Framework Comparisons

The following comparisons currently have no repo checker, comparator, or formal support:

- classical state machines
- SAT / SMT systems
- quantum circuits
- open compositional substrates
- formation media

Required status:

```text
ARGUMENT_STATUS: THREAD_SUPPORTED / GENERATED
CHECK_STATUS: NOT_CHECKED
```

Allowed use:

These comparisons may appear only as informal/generated motivation.

Blocked use:

They must not be represented as checked separations, formal impossibility results, or repo-supported framework theorems.

## 8. Promotion Blockers

This candidate may not be promoted beyond `GENERATED / OPEN / CANDIDATE` until the following are resolved.

### PB1 — S-Labels Not Repo-Native

S1, S2*, S3, and S4 are not repo-native terms.

Required action:

- Either register them explicitly as candidate labels in a repo-native vocabulary file, or replace them with repo-native terms.

### PB2 — 2017 Positive Geometry Source Gap

The 2017 Positive Geometry paper is not in the current source corpus.

Required action:

- Add source record for Arkani-Hamed, Bai, He, Yan.
- Bind source metadata.
- Extract claims relevant to positive geometries, canonical forms, boundary recursion, and residues.
- Only then upgrade B1/B2 from SOURCE_GAP/PARTIAL.

### PB3 — No Checked Separation Theorem

No formal theorem currently separates S2* from S4.

Required action:

- Define a formal/semi-formal separation target.
- Possibly encode a finite witness: same canonical readout / different bulk realization.
- Run validator or formal check.

### PB4 — No S2* + S4 Validator

No repo validator currently checks the S2* + S4 distinction.

Required action:

- Create validator target if the distinction becomes structurally important.
- Alternatively keep artifact as generated design caution only.

### PB5 — Same-Boundary/Different-Bulk Check Not Run

Relevant target:

```text
CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION
```

Current status:

```text
DEFINED_NOT_RUN / NOT_IMPLEMENTED
```

Required action:

- Implement/run the check if promotion depends on it.
- Until then, use only source-anchored cautionary language.

### PB6 — Generated Math Not Independently Available to GPT

Some generated mathematical material from earlier discussion is not independently accessible or checked.

Required action:

- Recover generated math artifacts.
- Place them in intake queue.
- Mark as GENERATED / OPEN until independently checked.

### PB7 — Framework Comparisons Not Checked

No formal support exists for comparisons to classical state machines, SAT/SMT, quantum circuits, or open systems.

Required action:

- Keep comparisons THREAD_SUPPORTED / GENERATED / NOT_CHECKED.
- Do not use them as proof of formation-medium distinctness.

## 9. Kill Conditions

Reject, narrow, or rewrite this candidate if any of the following occurs:

1. `EXT-AMP-PRIME-001` does not actually support same boundary/logarithmic form with different bulk geometry.
2. The 2017 Positive Geometry intake contradicts the proposed B1/B2 reading.
3. Repo conventions disallow generated candidate artifacts in `research_ledger/`.
4. Existing ledger rows already define incompatible meanings for S1-S4.
5. A checker/comparator result contradicts the claimed S2* + S4 distinction.
6. The artifact is interpreted as SOURCE_EXTRACTED rather than GENERATED.
7. The formation-medium interpretation implies physical realization rather than specification criteria.
8. The candidate blurs readout-level equivalence with full bulk equivalence.
9. The candidate claims framework separation without formal/checker support.

## 10. Required Next Checks

### NC1 — Source Intake

Add and extract the 2017 Positive Geometry source.

Expected target:

```text
SOURCE_NEEDED:
Arkani-Hamed, Bai, He, Yan — Positive Geometries and Canonical Forms
```

### NC2 — Source Verification for EXT-AMP-PRIME-001

Verify exact wording and scope of:

```text
same boundary structure
same logarithmic form
different bulk geometry
```

Confirm whether this supports:

```text
B4 only in Amplituhedron-Prime context
```

or can safely support a broader candidate principle.

### NC3 — Candidate Vocabulary Registration

Decide whether S1-S4 should remain local labels in this file or be added to a candidate vocabulary registry.

### NC4 — Checker Target Review

Review whether `CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION` should be implemented before any promotion.

### NC5 — Formal Witness Design

Design a minimal witness schema:

```text
same_readout(x, y)
different_bulk(x, y)
```

Possible finite witness:

```text
Amplituhedron / Amplituhedron-Prime
```

Status:

```text
FORMAL_CANDIDATE only after source and checker review.
```

### NC6 — R8 Binding Review

Review whether R8 root-bundle / local transport should become an explicit support binding for S2* or remain a future contextual note.

Status:

```text
THREAD_SUPPORTED / EXACT-WORK context only.
Do not promote S2* on R8 alone.
```

## 11. Suggested Metadata Block

If this artifact later receives machine-readable registration, use repo-native spelling for all status values and preserve the generated/candidate boundary.

```yaml
id: S2-STAR-S4-DISTINCTNESS-CANDIDATE
title: S2* and S4 Distinctness Candidate
status:
  - GENERATED
  - OPEN
  - CANDIDATE
argument_status:
  - THREAD_SUPPORTED
  - GENERATED
check_status:
  - NOT_CHECKED
source_status:
  - PARTIAL
  - SOURCE_GAP
claim_type: formation_medium_candidate
families:
  - A
  - C
  - M1
  - S
source_anchors:
  - EXT-AMP-PRIME-001
  - EXT-INTO-AMP-2013-001
  - EXT-SCAT-FORMS-001
ledger_refs:
  - R7
  - R8
check_targets:
  - CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION
source_gaps:
  - POSITIVE_GEOMETRY_2017
promotion_status: BLOCKED
```

## 12. Final Candidate Statement

```text
The S2* + S4 distinction is a generated formation-medium design caution:

A substrate may expose intrinsic canonical boundary/readout semantics while its internal bulk realization remains non-faithful relative to that readout. Existing repo anchors partially support this distinction through canonical form / cuts / faces / recursion / local-transport material, and directly support the same-boundary/same-form/different-bulk caution through EXT-AMP-PRIME-001. However, the distinction is not checked, not formalized, and not source-complete. It remains GENERATED / OPEN / CANDIDATE pending 2017 Positive Geometry intake, source verification, and checker/formal development.
```

## 13. Non-Promotion Footer

This artifact is a generated candidate for future repo integration. It does not create a source-extracted claim, does not modify `SOURCE_EXTRACTED_CLAIMS.json`, does not assert a theorem, and does not certify a formation-medium specification. It records a candidate distinction and the exact blockers that must be resolved before promotion.
