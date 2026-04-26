# Prime Local Carrier Candidate

STATUS: GENERATED / OPEN / CANDIDATE  
ARGUMENT_STATUS: SOURCE_RECHECK / GENERATED  
CHECK_STATUS: NOT_CHECKED  
SOURCE_STATUS: SOURCE_RECHECKED / NOT_SOURCE_EXTRACTED  
PROMOTION_STATUS: BLOCKED  
TARGET_LOCATION: research_ledger/  
DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json

## 0. Non-Promotion Notice

This artifact is a generated candidate derived from a direct source recheck of the Amplituhedron-Prime source and prior GPT equation mining.

It is not a source-extracted claim, not a theorem, not a validator result, not a Formation Medium substrate claim, not engineering evidence, and not a corporate/investor claim.

Machine-readable source recheck:

```text
research_ledger/PRIME_LOCAL_CARRIER_SOURCE_RECHECK_001.json
```

Primary source file rechecked:

```text
sources/Markdowns/_MConverter.eu_Herrmann_2020_Amplituhedron-Prime-Positive-Geometry_arXiv-2009.05607.pdf.md
```

Related existing source anchor:

```text
EXT-AMP-PRIME-001
```

## 1. Purpose

Prior GPT mining repeatedly suggested a possible Prime-side local carrier signature based on:

```text
sign-flip regions
bounded flip depth
chiral components
finite one-loop octagons
pentagon/hexagon degenerations
pentagon gluing into Amplituhedron-Prime
```

This artifact records what the source recheck currently supports as a generated candidate carrier layer, while blocking promotion to source-extracted status.

## 2. Source-Rechecked Support

The source recheck found:

```text
sign-flip hits:          127
octagon hits:            11
pentagon/hexagon hits:   129
chirality hits:          158
Prime/boundary/bulk hits: 74
gluing hits:             48
```

Selected source-recheck passages support the following limited statements.

### SR1 — Local Positive Spaces Characterized by Sign-Flip Conditions

Rechecked support:

The source abstract and introduction state that local positive spaces relevant for one-loop MHV amplitudes are characterized by sign-flip conditions.

Candidate use:

```text
Prime local spaces may be treated as sign-flip-defined positive spaces for candidate carrier analysis.
```

Status:

```text
SOURCE_RECHECKED / CANDIDATE / NOT_SOURCE_EXTRACTED
```

### SR2 — Maximal Sign-Flip Case Gives Finite One-Loop Octagons

Rechecked support:

The source states that in the maximal sign-flip case the relevant local positive spaces are finite one-loop octagons, and elsewhere links sign-flip-four spaces to chiral octagons.

Candidate use:

```text
The maximal local sign-flip sectors can be used as candidate finite local carrier blocks.
```

Status:

```text
SOURCE_RECHECKED / CANDIDATE / NOT_SOURCE_EXTRACTED
```

### SR3 — Chiral Octagons and Degenerations

Rechecked support:

The source recheck found direct passages stating that sign-flip-four spaces have logarithmic forms given by chiral octagons, and that chiral octagons degenerate to simpler spaces when labels become adjacent, matching pentagon/hexagon boundary cases.

Candidate use:

```text
Prime local carrier candidates may include generic chiral octagon blocks and degenerate pentagon/hexagon boundary cases.
```

Status:

```text
SOURCE_RECHECKED / CANDIDATE / NOT_SOURCE_EXTRACTED
```

### SR4 — Chiral Pentagon Gluing into Amplituhedron-Prime

Rechecked support:

The source recheck found direct passages stating that chiral pentagons externally triangulate a new Amplituhedron-Prime space, and that consistent gluing cancels spurious boundaries in the final space.

Candidate use:

```text
Prime carrier analysis should treat pentagon gluing as a global consistency layer, not as a single local-descent operation.
```

Status:

```text
SOURCE_RECHECKED / CANDIDATE / NOT_SOURCE_EXTRACTED
```

### SR5 — Same Boundary / Same Logarithmic Form / Different Bulk

Rechecked support:

The source recheck confirms the existing anchor: Amplituhedron-Prime has the same boundary structure and logarithmic form as the original amplituhedron while differing in the bulk as a geometric space.

Candidate use:

```text
Prime remains the main positive-geometry witness source for the bulk/readout caution.
```

Status:

```text
SOURCE_RECHECKED / EXISTING_ANCHOR / NOT_GENERAL_THEOREM
```

## 3. Conservative Candidate Carrier Signature

The prior GPT mined signature was:

```text
O_Prime,local = { S^{(2),chi}_{ij}, S^{(4),chi}_{ikellj} }
```

The source recheck supports a more conservative schema at this stage:

```text
PrimeLocalCarrierCandidate = (
  SignFlipRegion,
  ChiralComponent,
  LocalPositiveSpace,
  BoundaryAdjacencyData,
  GluingConsistencyData
)
```

with possible block types:

```text
maximal sign-flip finite one-loop octagon
chiral octagon
pentagon / hexagon degeneration
chiral pentagon building block
Amplituhedron-Prime gluing combination
```

Reason for conservatism:

The first regex pass did not reliably recover the exact notation `S^{(2),chi}_{ij}` / `S^{(4),chi}_{ikellj}` directly from the Markdown extraction. The source does support sign-flip-zero/two/four hierarchy language and sign-flip-four/chiral-octagon language, but this artifact should not pretend the mined notation has been source-extracted unless a focused equation-level source extraction verifies it.

## 4. Formation Medium Relevance

### 4.1 Carrier Shape Is Presentation-Bound

The Prime recheck supports the existing warning from prior mining:

```text
Do not claim that a single carrier shape, such as sign vectors, is substrate-level.
```

Prime uses sign-flip-defined local spaces, chiral components, octagons, pentagon gluing, and a twin geometry relation. This reinforces the idea that the surviving substrate-level requirement is not a specific carrier type, but the existence of a native carrier/admissibility/readout structure.

Related FM constraint:

```text
FM1-C1
```

Status:

```text
GENERATED / OPEN
```

### 4.2 Local Operation Type Is Not Universal

Prime gluing appears as overlap/spurious-boundary management among local positive spaces, not as a one-step local descent primitive.

Candidate implication:

```text
FM1 should not require a universal local operation type across positive-geometry families.
```

Related FM constraints:

```text
FM1-C2
FM1-C3
```

Status:

```text
GENERATED / OPEN
```

### 4.3 Bulk/Readout Schema Is Strengthened

Prime remains the strongest anchor for:

```text
same_readout(x, y)
different_bulk(x, y)
```

where readout is scoped to boundary/logarithmic-form data and bulk is scoped to positive-geometric realization.

Related artifact:

```text
research_ledger/FORMATION_MEDIUM_BULK_READOUT_WITNESS_SCHEMA.md
```

Status:

```text
SOURCE_ANCHORED_CAUTION / GENERATED_FORMAL_TEMPLATE
```

## 5. Candidate Rows for Future Extraction

Do not add these to `SOURCE_EXTRACTED_CLAIMS.json` yet. They are extraction candidates only.

### PC-EXT-001 — Sign-Flip Local Positive Spaces

Candidate claim:

```text
One-loop MHV local positive spaces are characterized by sign-flip conditions.
```

Extraction requirement:

Directly extract exact wording from abstract/introduction/sections 3-4.

### PC-EXT-002 — Maximal Sign-Flip Octagons

Candidate claim:

```text
In the maximal sign-flip case, the spaces are finite one-loop octagons / sign-flip-four spaces have logarithmic forms linked to chiral octagons.
```

Extraction requirement:

Directly extract exact wording around sign-flip-four spaces and equation 4.28 context.

### PC-EXT-003 — Chiral Octagon Degenerations

Candidate claim:

```text
Chiral octagons degenerate to simpler pentagon/hexagon spaces when labels become adjacent.
```

Extraction requirement:

Directly extract exact wording around the degeneration passage.

### PC-EXT-004 — Gluing into Amplituhedron-Prime

Candidate claim:

```text
Particular combinations of chiral pentagon/box/sign-flip spaces glue into Amplituhedron-Prime with only physical boundaries and no spurious boundaries under the stated assumptions.
```

Extraction requirement:

Directly extract exact wording around section 5.3 and equation 5.32.

## 6. Blockers

This candidate may not be promoted until:

1. Direct source-extracted claims are created for the specific local-carrier claims.
2. The exact notation for two/four sign-flip regions is recovered from source and not only prior GPT memory.
3. A formal/check target is defined if the carrier layer affects Formation Medium claims.
4. The distinction between local positive-geometry carrier and physical substrate carrier remains explicit.
5. The Prime-specific scope is preserved.

## 7. Kill Conditions

Reject or rewrite this candidate if:

1. The Prime source does not support the claimed sign-flip/local-space hierarchy under direct extraction.
2. The exact two/four/chiral notation cannot be recovered or is misremembered.
3. Octagon/pentagon/hexagon language is being inferred beyond source scope.
4. Gluing into Prime is treated as a universal operation type.
5. Prime local carrier language is used as physical substrate evidence.
6. Same boundary/log-form/different bulk is generalized beyond the positive-geometry context without support.
7. This artifact is treated as SOURCE_EXTRACTED.

## 8. Recommended Next Work

### N1 — Source-Extract Prime Local Carrier Claims

Add exact source-extracted claims only after a focused direct extraction around:

```text
sign-flip local positive spaces
maximal sign-flip finite one-loop octagons
sign-flip-four / chiral octagons
pentagon/hexagon degenerations
Amplituhedron-Prime gluing / equation 5.32
```

### N2 — Add Formal Check Target

Possible future target:

```text
CHK-PRIME-LOCAL-CARRIER-SOURCE-COVERAGE
```

Purpose:

Guard against promoting Prime local-carrier language into Formation Medium substrate claims.

### N3 — Update Bulk/Readout Witness Schema

If source extraction succeeds, update:

```text
FORMATION_MEDIUM_BULK_READOUT_WITNESS_SCHEMA.md
```

with a Prime-scoped witness profile.

## 9. Non-Promotion Footer

This artifact converts a prior-GPT mined carrier idea into a conservative source-rechecked candidate. It does not create source-extracted claims, prove a carrier theorem, define a physical substrate, or certify engineering feasibility.
