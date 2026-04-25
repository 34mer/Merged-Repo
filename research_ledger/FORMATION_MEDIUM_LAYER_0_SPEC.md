# Formation Medium Layer 0 Specification

STATUS: GENERATED / OPEN / CANDIDATE  
ARGUMENT_STATUS: THREAD_SUPPORTED / GENERATED  
CHECK_STATUS: NOT_CHECKED  
SOURCE_STATUS: PARTIAL  
PROMOTION_STATUS: BLOCKED  
TARGET_LOCATION: research_ledger/  
DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json

## 0. Non-Promotion Notice

This file is a generated Layer 0 specification scaffold for the Formation Medium project. It is not a source-extracted claim, not a theorem, not a validator result, not a physical realization claim, and not a corporate/investor claim.

It organizes the current repo-supported and thread-supported constraints into a first formation-medium specification layer. All formation-medium language remains GENERATED / OPEN unless separately source-bound, checked, or promoted by a repo-native process.

## 1. Core Project Thesis

Formation replaces computation.

The intended object is not a computer that calculates a positive geometry. The intended object is a medium whose native settling behavior produces a structure with positive-geometric / pre-spacetime readout.

Layer 0 thesis:

> A formation medium is a substrate-level system specified by native admissible carriers, native local transformations, and native settling/readout behavior such that its settled configurations expose canonical boundary/readout structure without assuming a unique faithful bulk reconstruction.

Status:

```text
GENERATED / OPEN / CANDIDATE
```

## 2. Scope of Layer 0

Layer 0 is not the final formation-medium theory. It is the constraint surface for future work.

Layer 0 should answer:

1. What must be specified before calling something a formation medium?
2. Which constraints are source-backed, thread-supported, generated, or open?
3. Which claims must not be promoted?
4. Which proof/checker obligations block the next layer?
5. Which repo rows can function as design constraints, and which remain only cautions?

Layer 0 should not answer:

1. Which physical material realizes the medium.
2. Which engineering implementation is correct.
3. Whether spacetime or quantum mechanics have been derived.
4. Whether S1-S4 are repo-native terms.
5. Whether framework separations are checked.

## 3. Required Specification Slots

A candidate formation medium must eventually specify each of the following slots.

### FM0.1 Carrier

Question:

> What are the native degrees of freedom or carrier objects of the medium?

Current repo relation:

- Closest candidate language: S1, exact carrier plus admissibility rule.
- Closest repo handles: family carriers across `A`, `C`, `M1`, and `S`.
- S1 is not repo-native.

Current status:

```text
GENERATED / OPEN
```

Promotion blocker:

- No repo-native carrier vocabulary for formation media.
- No physical substrate commitment allowed.

### FM0.2 Admissibility Rule

Question:

> Which configurations or transformations are admissible natively, before any external computation or interpretation?

Current repo relation:

- R1 unit codimension descent gives a shared lower-layer candidate across current families.
- R2 local move multiplicity and R3 nested-history burden may distinguish families.
- R14 remains OPEN / DEFICIT for full row x family closure.

Current status:

```text
THREAD_SUPPORTED / GENERATED / OPEN
```

Promotion blocker:

- R1-R3 are not sufficient as a full formation-medium admissibility law.
- R14 blocks closure.

### FM0.3 Native Local Operations

Question:

> What local operations does the medium natively support?

Current repo relation:

- Candidate S3: local native operations with polymorphic operation class.
- R1: unit codimension descent.
- R2: local move multiplicity.
- R3: nested-history / linear-extension burden.
- Comparators `CMP-A-C-LOCAL-MOVE-BURDEN` and `CMP-M1-C-LOCAL-MOVE-BURDEN` provide bounded finite evidence only.

Current status:

```text
THREAD_SUPPORTED / PARTIAL
```

Promotion blocker:

- PASS_PARTIAL_COMPARATOR is not theorem status.
- No all-family local-operation law exists.

### FM0.4 Boundary / Readout Semantics

Question:

> What is the readout of the medium, and why is it intrinsic rather than externally imposed?

Current repo relation:

- Candidate S2*: intrinsic canonical boundary semantics with unique recursive readout.
- Partial anchors: `EXT-SCAT-FORMS-001`, `EXT-INTO-AMP-2013-001`, R7, R8.
- R7 supports parabolic residue recursion inside solved exact branch.
- R8 may provide a future local transport/readout binding, but does not promote S2* alone.

Current status:

```text
PARTIAL / SOURCE_GAP
```

Promotion blocker:

- POS_GEOM_2017 source-intake records now exist, but no general S2* readout validator result exists.
- No general S2* readout validator exists.

### FM0.5 Bulk / Readout Non-Faithfulness

Question:

> Does the readout determine the internal bulk realization uniquely?

Current repo relation:

- Candidate S4: bulk non-faithfulness relative to readout.
- Direct anchor: `EXT-AMP-PRIME-001`.
- Related check target: `CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION`.
- Check target status: DEFINED_NOT_RUN / NOT_IMPLEMENTED.

Current status:

```text
SOURCE_ANCHORED CAUTION / GENERATED INTERPRETATION
```

Promotion blocker:

- Same-boundary/same-form/different-bulk caution is not a general theorem about formation media.
- It is currently a design caution anchored to Amplituhedron-Prime context.

### FM0.6 Settling Law

Question:

> What native dynamics or variational process causes the medium to settle into the readout-carrying configuration?

Current repo relation:

- No direct repo-native settling law exists.
- Current positive-geometry rows constrain target structures, not substrate dynamics.

Current status:

```text
GENERATED / OPEN
```

Promotion blocker:

- Substrate interpretation must not be inferred from positive-geometry rows alone.
- No physical realization, material dynamics, or laboratory protocol is currently checked.

### FM0.7 Failure / Falsification Interface

Question:

> What would falsify a proposed formation-medium layer?

Current repo relation:

- `PROOF_OBLIGATIONS.md` defines required proof/checker layers.
- `SUPPORT_CAUTION_SURVIVOR_LEDGER.md` defines non-promotion cautions.
- `S2_STAR_S4_DISTINCTNESS_CANDIDATE.md` defines kill conditions for the readout/bulk distinction.

Current status:

```text
PARTIAL
```

Promotion blocker:

- No unified formation-medium validator exists.

## 4. Layer 0 Constraints

### C0.1 No Computation Substitution

The formation medium must not be specified as an external algorithm that computes the geometry.

Allowed:

```text
native formation -> settled configuration -> canonical readout
```

Blocked:

```text
ordinary computer -> algorithm -> calculated positive geometry
```

Status:

```text
GENERATED / DESIGN CONSTRAINT
```

### C0.2 No Substrate Promotion From Geometry Alone

Positive-geometry rows may constrain the target readout, but they do not by themselves prove substrate realization.

Source of caution:

```text
SUPPORT_CAUTION_SURVIVOR_LEDGER.md
```

Status:

```text
REPO CAUTION / GENERATED APPLICATION
```

### C0.3 Boundary Readout Does Not Imply Bulk Faithfulness

Same boundary structure, same logarithmic/canonical form, or same readout must not automatically be treated as the same bulk realization.

Source anchor:

```text
EXT-AMP-PRIME-001
```

Related candidate:

```text
S2_STAR_S4_DISTINCTNESS_CANDIDATE.md
```

Status:

```text
SOURCE_ANCHORED CAUTION / GENERATED APPLICATION
```

### C0.4 Partial Comparator Evidence Is Not Theorem Status

Comparator pass states such as `PASS_PARTIAL_COMPARATOR` are bounded finite evidence only.

Relevant comparators:

```text
CMP-A-C-LOCAL-MOVE-BURDEN
CMP-M1-C-LOCAL-MOVE-BURDEN
```

Status:

```text
REPO NON-PROMOTION RULE
```

### C0.5 Framework Comparisons Are Not Checked

No repo checker, comparator, or formal target currently supports claims separating formation media from classical state machines, SAT/SMT systems, quantum circuits, or open compositional systems.

Status required:

```text
ARGUMENT_STATUS: THREAD_SUPPORTED / GENERATED
CHECK_STATUS: NOT_CHECKED
```

## 5. Minimal Layer 0 Definition Candidate

A Layer 0 formation medium candidate is a tuple-like specification:

```text
FM0 = (Carrier, Admissibility, LocalOps, BoundaryReadout, BulkRelation, SettlingLaw, FailureInterface)
```

where:

```text
Carrier         = native degrees of freedom or objects
Admissibility   = native allowed configurations / transformations
LocalOps        = local move or transformation classes
BoundaryReadout = intrinsic canonical boundary/readout semantics
BulkRelation    = relation between internal bulk realization and readout
SettlingLaw      = native process producing stable readout-bearing states
FailureInterface= checks, validators, source blockers, and kill conditions
```

Current status of the tuple:

```text
Carrier:          GENERATED / OPEN
Admissibility:    THREAD_SUPPORTED / PARTIAL
LocalOps:         THREAD_SUPPORTED / PARTIAL
BoundaryReadout:  PARTIAL / SOURCE_GAP
BulkRelation:     SOURCE_ANCHORED CAUTION / GENERATED
SettlingLaw:      GENERATED / OPEN
FailureInterface: PARTIAL
```

## 6. Current Best Candidate Reading

The current best GENERATED / OPEN reading is:

> A formation medium is a native substrate whose admissible configurations and local transformations settle into structures whose readout is governed by canonical boundary semantics. The specification must preserve the possibility that the readout is stable while the internal bulk realization is not uniquely determined by that readout.

This reading is intentionally weaker than a physical claim.

It does not say:

- a formation medium has been built;
- a substrate has been identified;
- positive geometry proves the substrate;
- spacetime or quantum mechanics have been derived;
- S1-S4 are repo-native;
- framework separation has been checked.

## 7. Immediate Next Work Units

### W0.1 Source Intake: 2017 Positive Geometry

Continue POS_GEOM_2017 source-coverage work required for B1/B2 authority.

Expected status:

```text
SOURCE_EXTRACTED / NEEDS_FORMALIZATION / NOT_CHECKED
```

### W0.2 Formation Vocabulary Registry

Decide whether S1, S2*, S3, and S4 remain local labels or become candidate vocabulary entries.

Expected status:

```text
GENERATED / OPEN
```

### W0.3 FM0 Tuple Schema

Create a machine-readable candidate schema for `FM0` with explicit status fields for each slot.

Expected status:

```text
GENERATED / OPEN
```

### W0.4 Bulk/Readout Witness Target

Design a minimal same-readout/different-bulk witness target, probably using Amplituhedron / Amplituhedron-Prime only as a finite cautionary witness.

Expected status:

```text
FORMAL_CANDIDATE only after source/check review
```

### W0.5 R14 Closure Blocker

Do not advance beyond Layer 0 as a stable spec until R14 grouped-carrier equation/class-matrix deficit is either resolved or explicitly bypassed with a scoped limitation. POS_GEOM_2017 source coverage alone does not clear R14.

Expected status:

```text
OPEN / DEFICIT
```

## 8. Kill Conditions

This Layer 0 scaffold must be rejected, narrowed, or rewritten if:

1. It is read as a physical substrate claim.
2. It is read as a checked formal specification.
3. It treats S1-S4 as repo-native without vocabulary registration.
4. It treats positive-geometry rows as substrate evidence.
5. It treats partial comparators as theorem status.
6. It treats framework comparisons as checked separations.
7. It ignores the S2* source gap.
8. It ignores R14 as OPEN / DEFICIT.
9. It requires bulk faithfulness contrary to the S4/Amplituhedron-Prime caution.
10. It claims a settling law without new source/check/engineering evidence.

## 9. Non-Promotion Footer

This Layer 0 specification is a generated scaffold. It is useful only as a disciplined organizing layer for the Formation Medium project. It must not be used as a source-extracted claim, theorem, validator result, physical implementation, investor claim, or corporate technical proof.
