# Previous GPT Equation Mining Synthesis 001

STATUS: GENERATED / OPEN / LOCAL_SOURCE_INTAKE  
CHECK_STATUS: NOT_CHECKED  
SOURCE_STATUS: PRIOR_CONVERSATION_ORE  
PROMOTION_STATUS: BLOCKED  
TARGET_LOCATION: research_ledger/  
DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json

## 0. Non-Promotion Notice

This artifact summarizes an equation/formal-object mining pass over `Previous Conversations with GPT/`.

It is not a source-extracted claim, not a theorem, not a formal proof, not an engineering result, not IP, and not an investor/corporate claim.

Machine-readable companion:

```text
research_ledger/PREVIOUS_GPT_EQUATION_MINING_PASS_001.json
```

## 1. Mining Result

The pass found substantial formal ore:

```text
raw formal/math records:      4362
deduplicated formal records:  4362
selected high-value records:  48
```

Selected role coverage:

```text
carrier:        36
admissibility:  35
readout:        34
bulk_relation:  26
transport:      33
engineering:    25
corporate:      36
checker:        25
```

Interpretation:

The prior-conversation folder contains a large amount of mathematical and formal scaffolding. Most of it is not directly importable, but it is not fluff. The useful layer is a small set of recurring formal signatures.

## 2. Candidate Equation Families

### EQF-001 — FM0/FM1 Tuple Signatures

Candidate form:

```text
FM0 = (Carrier, Admissibility, LocalOps, BoundaryReadout, BulkRelation, SettlingLaw, FailureInterface)

FM1 = FM0 + {C1, C2, C3, C4, C5, C6, C7}
```

Meaning:

This is the main specification skeleton. It is already partially reflected in Layer 0 and Layer 1 artifacts.

Repo contacts:

```text
research_ledger/FORMATION_MEDIUM_LAYER_0_SPEC.md
research_ledger/FORMATION_MEDIUM_LAYER_1_SPEC.md
research_ledger/FORMATION_MEDIUM_LAYER_1_CANDIDATE_CONSTRAINTS.json
```

Status:

```text
GENERATED / OPEN / ALREADY_PARTIAL_LEDGER_CONTACT
```

Next action:

Convert this into a machine-readable FM schema only if it improves validation. Do not treat the tuple as a theorem.

---

### EQF-002 — S1-S4 Candidate Constraint Tuple

Candidate form:

```text
S1  = exact carrier + admissibility rule
S2* = intrinsic boundary stratification / canonical recursive readout
S3  = local native operations, operation-class polymorphic
S4  = bulk non-faithfulness relative to readout
```

Meaning:

This is the compact candidate vocabulary driving much of the Formation Medium work. The equation mining confirms it appears repeatedly and functions as a design handle.

Repo contacts:

```text
research_ledger/S2_STAR_S4_DISTINCTNESS_CANDIDATE.md
research_ledger/FORMATION_MEDIUM_LAYER_1_SPEC.md
```

Status:

```text
GENERATED / OPEN / CANDIDATE_VOCABULARY
```

Next action:

Create a candidate vocabulary registry only after deciding whether S1-S4 should become repo-native candidate terms.

---

### EQF-003 — Bulk/Readout Witness Predicates

Candidate form:

```text
same_readout(x, y)
different_bulk(x, y)
```

Meaning:

This is the minimal formal witness schema for S4-style non-faithful readout. It captures the idea that two internal/bulk realizations can share the same readout while differing in bulk.

Repo contacts:

```text
research_ledger/S2_STAR_S4_DISTINCTNESS_CANDIDATE.md
research_ledger/FORMATION_MEDIUM_LAYER_0_SPEC.md
EXT-AMP-PRIME-001
CHK-SAME-BOUNDARY-DIFFERENT-BULK-CAUTION
```

Status:

```text
GENERATED / OPEN / FORMAL_CANDIDATE
```

Next action:

Design a formal/check target only after Prime source recheck. Do not generalize beyond Amplituhedron-Prime evidence.

---

### EQF-004 — Prime Local Carrier Signature

Candidate form:

```text
O_Prime,local = { S^{(2),chi}_{ij}, S^{(4),chi}_{ikellj} }
```

with:

```text
bounded flip depth
flip-position labels
chirality bit
octagon generic sectors
pentagon/hexagon degenerations
```

Meaning:

This is a candidate local positive-geometry carrier signature mined from prior discussion around Amplituhedron-Prime.

Repo contacts:

```text
research_ledger/PREVIOUS_GPT_TARGETED_MINING_SYNTHESIS_001.md
EXT-AMP-PRIME-001
```

Status:

```text
GENERATED / OPEN / NEEDS_SOURCE_RECHECK
```

Next action:

Create `PRIME_LOCAL_CARRIER_CANDIDATE.md` only after direct source recheck against the Prime paper.

---

### EQF-005 — Boundary-Determined vs Bulk-Sensitive Discriminator

Candidate form:

```text
boundary_determined_vs_bulk_sensitive
```

Operational reading:

```text
If a candidate constraint survives fixed boundary/log-form data under bulk change, mark it boundary-determined.
If it fails under fixed boundary/log-form data when bulk changes, mark it bulk-sensitive.
```

Meaning:

This is the most important mined discriminator for the Formation Medium ontology. It sharpens the S2*+S4 distinction into an audit rule.

Repo contacts:

```text
EXT-AMP-PRIME-001
research_ledger/S2_STAR_S4_DISTINCTNESS_CANDIDATE.md
research_ledger/FORMATION_MEDIUM_LAYER_1_SPEC.md
```

Status:

```text
GENERATED / OPEN / PARTIALLY_REPO_ANCHORED
```

Next action:

Use this to refine FM1-C5 and the bulk/readout witness checker. Do not promote to general theorem.

---

### EQF-006 — Root-Bundle / Local Transport Symbols

Candidate form:

```text
V_m root-bundle layer
J_i adjacent quarter-turn transport
```

Meaning:

The mining pass found repeated transport symbols and engineering analogies around a root-bundle/local-transport layer. This appears to connect R8-style local transport, candidate readout structure, and engineering route A from the engineering triage.

Repo contacts:

```text
R8
research_ledger/FORMATION_MEDIUM_ENGINEERING_TRIAGE_001.md
```

Status:

```text
GENERATED / OPEN / NEEDS_REVIEW
```

Next action:

Run a focused transport-symbol mining pass around `V_m`, `J_i`, `root-bundle`, and `quarter-turn`. This should happen before using these symbols in engineering language.

---

### EQF-007 — Quiver Source-Side Carrier / Admissibility Chain

Candidate form:

```text
subobjects / closure
  -> inclusion / refinement order
  -> admissibility / validity
  -> downward-closed / antichain closure
  -> F-polynomial or Hall/Euler readout
```

Meaning:

This is a separate mathematical vein from the engineering triage. It suggests a source-side carrier/admissibility/readout progression for quiver/grouped-object structures.

Repo contacts:

```text
research_ledger/PREVIOUS_GPT_CANDIDATE_EXTRACTIONS.json
```

Status:

```text
GENERATED / OPEN / NEEDS_SOURCE_REVIEW
```

Next action:

Create a quiver/grouped-carrier mining pass. Keep it separate from physical engineering triage.

## 3. Best Current Judgment

The equation mining pass confirms that the prior GPT folder contains three especially valuable formal veins:

```text
1. Formation specification signatures:
   FM0/FM1 and S1-S4.

2. Bulk/readout formalization:
   same_readout / different_bulk and boundary_determined_vs_bulk_sensitive.

3. Carrier/transport candidates:
   Prime local carrier and root-bundle/quarter-turn transport.
```

The most strategically useful next formal artifact is likely not another broad extraction. It is either:

```text
A. PRIME_LOCAL_CARRIER_CANDIDATE.md
```

or:

```text
B. FORMATION_MEDIUM_BULK_READOUT_WITNESS_SCHEMA.md
```

Given the corporate/engineering goal, `B` is probably more central because it clarifies what the substrate must preserve or fail to preserve before picking hardware.

## 4. What This Pass Did Not Do

This pass did not:

1. Prove any equation.
2. Source-extract any prior GPT content.
3. Validate any mathematical object.
4. Select a physical substrate.
5. Commit to S1-S4 as repo-native vocabulary.
6. Convert transport symbols into engineering requirements.

## 5. Recommended Next Work

### N1 — Bulk/Readout Witness Schema

Candidate path:

```text
research_ledger/FORMATION_MEDIUM_BULK_READOUT_WITNESS_SCHEMA.md
```

Purpose:

Define a generated/open formal candidate schema around:

```text
same_readout(x, y)
different_bulk(x, y)
boundary_determined(candidate_constraint)
bulk_sensitive(candidate_constraint)
```

Use it to refine FM1-C5 and future Prime checks.

### N2 — Prime Local Carrier Source Recheck

Candidate path:

```text
research_ledger/PRIME_LOCAL_CARRIER_CANDIDATE.md
```

Purpose:

Recheck direct source support for:

```text
O_Prime,local
S^{(2),chi}_{ij}
S^{(4),chi}_{ikellj}
bounded flip depth
chirality bit
octagon/pentagon/hexagon degeneration
```

### N3 — Transport Symbol Mining

Candidate path:

```text
research_ledger/PREVIOUS_GPT_TRANSPORT_SYMBOL_MINING_PASS_001.json
```

Purpose:

Mine and isolate:

```text
V_m
J_i
root-bundle
quarter-turn transport
local channel motion
```

## 6. Non-Promotion Footer

This synthesis is a map of formal ore. It does not create repo-native definitions, source-extracted claims, proof obligations, engineering requirements, or corporate claims. All formal objects here remain generated candidate material pending source/check review.
