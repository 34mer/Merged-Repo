# Formation Medium Layer 1 Specification

STATUS: GENERATED / OPEN / CANDIDATE  
ARGUMENT_STATUS: THREAD_SUPPORTED / GENERATED  
CHECK_STATUS: NOT_CHECKED  
SOURCE_STATUS: PARTIAL / LOCAL_SOURCE_INTAKE  
PROMOTION_STATUS: BLOCKED  
TARGET_LOCATION: research_ledger/  
DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json

## 0. Non-Promotion Notice

This Layer 1 specification is a generated candidate derived from:

- `research_ledger/FORMATION_MEDIUM_LAYER_0_SPEC.md`
- `research_ledger/FORMATION_MEDIUM_LAYER_1_CANDIDATE_CONSTRAINTS.json`
- `research_ledger/PREVIOUS_GPT_CONVERSATION_INTAKE.json`
- `research_ledger/PREVIOUS_GPT_CANDIDATE_EXTRACTIONS.json`
- repo caution/proof-obligation ledgers

It is not a source-extracted claim, not a theorem, not a validator result, not a physical realization, and not an investor/corporate proof.

Prior GPT conversation exports are treated as local thread-source intake only. They may contain important equations and design constraints, but their contents remain GENERATED / OPEN until separately source-bound, repo-bound, or checked.

## 1. Layer 1 Purpose

Layer 0 defined the minimal formation-medium slots:

```text
FM0 = (Carrier, Admissibility, LocalOps, BoundaryReadout, BulkRelation, SettlingLaw, FailureInterface)
```

Layer 1 turns those slots into candidate constraints that can guide later source intake, formalization, physical-regime triage, and corporate technical planning.

Layer 1 does not identify a final substrate. It defines what a candidate substrate must eventually satisfy.

## 2. Layer 1 Candidate Constraint Set

### FM1-C1 — Native Carrier Constraint

Candidate constraint:

> A formation-medium carrier must be specified as native substrate degrees of freedom, not as an external data structure manipulated by an ordinary computer.

Slot:

```text
Carrier
```

Status:

```text
GENERATED / OPEN
```

Source leads:

- prior GPT conversation intake
- Layer 0 carrier slot
- S1 candidate language

Promotion blockers:

- no repo-native carrier vocabulary
- no physical substrate evidence
- S1 is not repo-native

Failure mode:

A candidate fails this constraint if its carrier is merely a user-imposed encoding on a conventional computational substrate rather than a native state space of the medium.

---

### FM1-C2 — Native Admissibility Constraint

Candidate constraint:

> Admissibility must be native to the medium: allowed configurations and local transformations must be defined before readout, not retrofitted from a solved geometry.

Slot:

```text
Admissibility
```

Status:

```text
GENERATED / OPEN / PARTIAL
```

Source leads:

- R1 unit codimension descent
- R2 local move multiplicity
- R3 nested-history / linear-extension burden
- prior GPT conversation intake

Promotion blockers:

- R14 remains OPEN / DEFICIT
- current comparator results are PASS_PARTIAL_COMPARATOR only
- no all-family admissibility law exists

Failure mode:

A candidate fails this constraint if the allowed moves are defined only after the target geometry is known, or if admissibility is implemented as an external solver rule rather than native medium behavior.

---

### FM1-C3 — Settling Law Constraint

Candidate constraint:

> The medium must include a settling law or variational/native formation process; positive-geometry target rows alone do not supply substrate dynamics.

Slot:

```text
SettlingLaw
```

Status:

```text
GENERATED / OPEN
```

Source leads:

- `SUPPORT_CAUTION_SURVIVOR_LEDGER.md`
- prior GPT conversation intake
- Layer 0 settling-law slot

Promotion blockers:

- no checked settling law
- no physical realization claim allowed
- substrate interpretation must not be inferred from positive-geometry rows alone

Failure mode:

A candidate fails this constraint if it only describes a target mathematical object and never specifies how the medium naturally reaches a stable readout-bearing state.

---

### FM1-C4 — Canonical Boundary Readout Constraint

Candidate constraint:

> Readout should be boundary/canonical-form-like and recursively constrained, but S2* remains partial/source-gap until 2017 Positive Geometry intake and readout validators exist.

Slot:

```text
BoundaryReadout
```

Status:

```text
GENERATED / OPEN / SOURCE_GAP
```

Source leads:

- `S2_STAR_S4_DISTINCTNESS_CANDIDATE.md`
- R7 parabolic residue recursion
- R8 root-bundle / local transport layer
- `EXT-SCAT-FORMS-001`
- `EXT-INTO-AMP-2013-001`

Promotion blockers:

- 2017 Positive Geometry source missing
- no S2* validator
- S2* is not repo-native
- R8 cannot promote S2* alone

Failure mode:

A candidate fails this constraint if its readout is chosen by an observer, an output register, or an external computational convention rather than by intrinsic boundary/canonical structure.

---

### FM1-C5 — Bulk/Readout Non-Faithfulness Constraint

Candidate constraint:

> The specification must not require unique faithful bulk reconstruction from readout; same-boundary/same-log-form/different-bulk remains a design caution anchored by EXT-AMP-PRIME-001.

Slot:

```text
BulkRelation
```

Status:

```text
GENERATED / OPEN / SOURCE_ANCHORED_CAUTION
```

Source leads:

- `EXT-AMP-PRIME-001`
- `S2_STAR_S4_DISTINCTNESS_CANDIDATE.md`
- `CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION`

Promotion blockers:

- `CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION` is not implemented
- same-boundary/different-bulk is not yet a general formation-medium theorem
- S4 is not repo-native

Failure mode:

A candidate fails this constraint if it assumes readout-level equivalence automatically implies bulk equivalence, or if it requires the internal substrate state to be uniquely reconstructible from the canonical readout.

---

### FM1-C6 — Anti-Computation Constraint

Candidate constraint:

> Formation replaces computation: the settled configuration is the answer; the medium must not be reduced to an algorithm computing a positive geometry.

Slot:

```text
AntiComputation / Project Ontology
```

Status:

```text
GENERATED / OPEN
```

Source leads:

- `FORMATION_MEDIUM_LAYER_0_SPEC.md`
- prior GPT conversation intake

Promotion blockers:

- project ontology is not a source-extracted physics claim
- no formal framework-separation checker exists
- no repo support for comparisons against classical state machines, SAT/SMT, quantum circuits, or open compositional systems

Failure mode:

A candidate fails this constraint if the medium is only a conventional computing substrate running an algorithm, even if that algorithm outputs positive-geometric data.

---

### FM1-C7 — Failure Interface Constraint

Candidate constraint:

> Every formation-medium claim must carry a failure interface: source gap, checker target, proof obligation, or kill condition.

Slot:

```text
FailureInterface
```

Status:

```text
GENERATED / OPEN / PARTIAL
```

Source leads:

- `PROOF_OBLIGATIONS.md`
- `SUPPORT_CAUTION_SURVIVOR_LEDGER.md`
- `S2_STAR_S4_DISTINCTNESS_CANDIDATE.md`
- `FORMATION_MEDIUM_LAYER_0_SPEC.md`

Promotion blockers:

- no unified formation-medium validator
- no machine-readable FM1 validation schema yet

Failure mode:

A candidate fails this constraint if it cannot state what evidence would demote, reject, or narrow it.

## 3. Combined Layer 1 Candidate Definition

A Layer 1 formation-medium candidate is a Layer 0 tuple satisfying FM1-C1 through FM1-C7:

```text
FM1 = FM0 + {C1, C2, C3, C4, C5, C6, C7}
```

Expanded:

```text
FM1 = (
  NativeCarrier,
  NativeAdmissibility,
  NativeLocalOps,
  CanonicalBoundaryReadout,
  NonFaithfulBulkRelation,
  NativeSettlingLaw,
  ExplicitFailureInterface,
  AntiComputationConstraint
)
```

Current support profile:

```text
NativeCarrier:             GENERATED / OPEN
NativeAdmissibility:       THREAD_SUPPORTED / PARTIAL
NativeLocalOps:            THREAD_SUPPORTED / PARTIAL
CanonicalBoundaryReadout:  PARTIAL / SOURCE_GAP
NonFaithfulBulkRelation:   SOURCE_ANCHORED_CAUTION / GENERATED
NativeSettlingLaw:         GENERATED / OPEN
ExplicitFailureInterface:  PARTIAL
AntiComputationConstraint: GENERATED / OPEN
```

## 4. Physical-Regime Triage Implications

The prior GPT conversation intake suggests several physical-regime leads. These are not repo-supported conclusions. They are triage targets.

### 4.1 Leading Candidate Direction: Scattering Systems

Generated lead:

> Asymptotic scattering systems may be the strongest current mathematics-first fit because their native readout is scattering/amplitude data organized by poles, cuts, factorization, unitarity, and boundary/asymptotic channels.

Status:

```text
GENERATED / OPEN / NEEDS_SOURCE_REVIEW
```

Reason it remains live:

- plausible native carrier: legal asymptotic states
- plausible readout: scattering map / amplitude
- plausible S2* relation: poles/cuts/factorization recursively constrain readout
- plausible S4 relation: different bulk descriptions may share readout data

Blockers:

- field-redefinition / S-matrix equivalence claims need source intake
- physical realization is not proven
- no formation-medium settling law is specified

### 4.2 Near-Hit: Integrable Coherent Media

Generated lead:

> Integrable coherent media may satisfy carrier/admissibility/readout constraints but may fail S4 because inverse scattering can be too faithful to bulk reconstruction.

Status:

```text
GENERATED / OPEN / NEAR_HIT
```

Reason it remains useful:

- clarifies the difference between canonical readout and non-faithful readout
- may inform test cases for FM1-C5

Blockers:

- source intake needed
- S4 failure/success conditions unclear

### 4.3 Near-Hit: 2D Topological Order With Boundaries

Generated lead:

> Topological orders with gapped boundaries may satisfy exact carrier, admissibility, and boundary semantics, but may fail S4 if boundary data reconstructs the bulk too faithfully.

Status:

```text
GENERATED / OPEN / NEAR_HIT
```

Reason it remains useful:

- strong native carrier/admissibility example
- useful negative control for bulk/readout faithfulness

Blockers:

- source intake needed
- relation to positive-geometry readout unclear

### 4.4 Exploratory: Classical Topological Continua

Generated lead:

> Classical topological continua, such as magnetized plasmas or diffusive media with bulk-edge structure, may show that boundary-structured semantics is broader than quantum hardware.

Status:

```text
GENERATED / OPEN / EXPLORATORY
```

Reason it remains useful:

- broadens search space beyond quantum computing hardware
- may support corporate/lab triage later

Blockers:

- no source-backed S2* readout
- no Prime-style S4 witness
- no formation-medium settling law

## 5. What Layer 1 Rules Out

Layer 1 currently rules out only weakly and provisionally.

It rules out candidates that:

1. use an ordinary algorithm as the actual formation process;
2. define boundary/readout externally rather than intrinsically;
3. lack a native carrier or admissibility law;
4. require unique faithful bulk reconstruction from readout;
5. lack any failure interface;
6. infer substrate realization from positive-geometry rows alone.

Status:

```text
GENERATED / OPEN / DESIGN TRIAGE ONLY
```

This is not a theorem-level exclusion.

## 6. Required Next Formal/Repo Work

### FM1-W1 — Machine-Readable FM1 Schema

Create a JSON schema for FM1 constraints with fields:

```text
id
slot
constraint
status
source_leads
repo_rows
source_anchors
check_targets
promotion_blockers
failure_mode
```

Current partial precursor:

```text
research_ledger/FORMATION_MEDIUM_LAYER_1_CANDIDATE_CONSTRAINTS.json
```

### FM1-W2 — Source Intake for Scattering-System Lead

Create a separate source-intake plan for:

- field-redefinition equivalence / same S-matrix with different bulk descriptions
- amplitudes determined by poles/cuts/unitarity/factorization
- asymptotic state spaces as intrinsic boundary/readout carriers

Status:

```text
SOURCE_NEEDED / GENERATED / OPEN
```

### FM1-W3 — 2017 Positive Geometry Intake

Still required for B1/B2 and S2* authority.

Status:

```text
SOURCE_GAP
```

### FM1-W4 — Bulk/Readout Witness Checker

Define a minimal witness target:

```text
same_readout(x, y)
different_bulk(x, y)
```

Initial cautionary source:

```text
EXT-AMP-PRIME-001
```

Status:

```text
FORMAL_CANDIDATE only after source/check review
```

### FM1-W5 — Formation-Medium Validator Skeleton

Create a validator that checks only ledger discipline, not physics truth:

- every FM claim has status;
- every FM claim has blocker/failure mode;
- no FM claim appears in SOURCE_EXTRACTED_CLAIMS;
- no FM claim uses CHECKED without a check result;
- no substrate claim is promoted from positive geometry alone.

Status:

```text
NOT_IMPLEMENTED
```

## 7. Kill Conditions

Reject or narrow this Layer 1 spec if:

1. prior GPT conversation intake is treated as source authority;
2. FM1 constraints are used as checked physics;
3. physical-regime leads are presented as selected substrates;
4. the 2017 Positive Geometry gap is ignored;
5. S1-S4 are treated as repo-native;
6. S2* is promoted without source/check support;
7. S4 is generalized beyond Amplituhedron-Prime caution without support;
8. framework comparisons are treated as formal separations;
9. any candidate lacks a failure interface;
10. corporate/investor materials use this as proof rather than roadmap.

## 8. Non-Promotion Footer

This Layer 1 specification converts current generated/thread-source intake into a disciplined candidate constraint set. It is useful for roadmap, triage, source-intake planning, and future validator design. It is not a proof, not a source-extracted claim, not a substrate realization, and not a final corporate technical claim.
