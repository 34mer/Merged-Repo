# Prime Direct Source Extraction Summary 001

STATUS: SOURCE_EXTRACTION_SUMMARY / OPEN  
CHECK_STATUS: DEFINED_NOT_RUN  
SOURCE_STATUS: SOURCE_EXTRACTED  
PROMOTION_STATUS: BLOCKED  
TARGET_LOCATION: research_ledger/  
DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json

## 0. Non-Promotion Notice

This artifact summarizes direct source extraction from the Amplituhedron-Prime source.

It is not a theorem, not a validator result, not a Formation Medium substrate claim, not engineering feasibility, not IP, and not corporate/investor language.

Direct extraction context:

```text
research_ledger/PRIME_DIRECT_EXTRACTION_CONTEXT_001.json
```

Updated registries:

```text
research_ledger/SOURCE_EXTRACTED_CLAIMS.json
research_ledger/FORMAL_CHECK_TARGETS.json
research_ledger/FORMAL_CHECK_RESULTS.json
```

## 1. New Source-Extracted Claims

### EXT-AMP-PRIME-002 — Sign-Flip Local Positive Spaces

Extracted claim:

```text
Local positive spaces relevant for one-loop MHV amplitudes are characterized by sign-flip conditions; in the maximal sign-flip case the spaces are finite one-loop octagons, and the logarithmic forms of maximal sign-flip spaces are chiral octagons.
```

Source anchors:

```text
abstract and introduction
extracted Markdown lines 21 and 205-207
```

Status:

```text
SOURCE_EXTRACTED / NEEDS_FORMALIZATION
```

---

### EXT-AMP-PRIME-003 — Sign-Flip-Four / Chiral Octagon Regions

Extracted claim:

```text
The paper defines sign-flip-four regions labelled by the four sign-flip positions and states that sign-flip-four spaces have logarithmic forms linked to chiral octagon integrals, with chiral components having eight boundaries in the generic case.
```

Source anchors:

```text
section 4 sign-flip-four regions
extracted Markdown lines 2125, 2297-2299, 2445-2473, 4529
```

Status:

```text
SOURCE_EXTRACTED / NEEDS_FORMALIZATION
```

---

### EXT-AMP-PRIME-004 — Chiral Octagon Degenerations

Extracted claim:

```text
Chiral octagons naturally degenerate to simpler spaces when labels become adjacent; the paper identifies pentagon and hexagon examples as boundary cases of the generic octagon.
```

Source anchors:

```text
section 4 chiral octagons
extracted Markdown lines 2493-2497
```

Status:

```text
SOURCE_EXTRACTED / NEEDS_FORMALIZATION
```

---

### EXT-AMP-PRIME-005 — Pentagon Gluing / Same Log Form / Different Bulk

Extracted claim:

```text
Chiral pentagons externally triangulate a new Amplituhedron-Prime space, a non-overlapping twin of the original Amplituhedron with only physical boundaries and the same logarithmic form; the source also states that the Amplituhedron-Prime has the same boundary structure/logarithmic form as the Amplituhedron but differs in the bulk as a geometric space.
```

Source anchors:

```text
abstract, introduction, and conclusion
extracted Markdown lines 21-23, 217-221, 3901-3903
```

Status:

```text
SOURCE_EXTRACTED / NEEDS_FORMALIZATION
```

## 2. New Check Target

Created target:

```text
CHK-PRIME-LOCAL-CARRIER-SOURCE-COVERAGE
```

Purpose:

Guard against promoting Prime local-carrier source claims into Formation Medium substrate, engineering feasibility, or universal carrier theorem claims.

Result status:

```text
DEFINED_NOT_RUN
```

Meaning:

The target exists, but no checker has been implemented yet.

## 3. What This Extraction Unlocks

This extraction strengthens:

```text
PRIME_LOCAL_CARRIER_CANDIDATE.md
FORMATION_MEDIUM_BULK_READOUT_WITNESS_SCHEMA.md
S4 candidate vocabulary
R13/R14 realization-class caution
```

It does not promote:

```text
Prime local carrier -> physical substrate
sign-flip regions -> universal carrier
chiral octagons -> Formation Medium readout proof
same logarithmic form -> physical non-faithfulness
```

## 4. Remaining Blockers

1. No Prime local-carrier source-coverage checker has been implemented.
2. No formal sign-flip/chiral-octagon finite model has been built.
3. No physical substrate implication follows from Prime.
4. The exact prior-GPT shorthand `O_Prime,local = {S^(2), S^(4)}` remains generated shorthand unless separately formalized.
5. Same-boundary/log-form/different-bulk remains positive-geometry scope only.

## 5. Recommended Next Work

### PDS-N1 — Implement Source-Coverage Guard

Add a validator/checker for:

```text
CHK-PRIME-LOCAL-CARRIER-SOURCE-COVERAGE
```

It should enforce that Prime local-carrier claims stay source-scoped and are not promoted to Formation Medium substrate or engineering readiness.

### PDS-N2 — Update Prime Candidate Artifact Later

After the checker exists, update:

```text
PRIME_LOCAL_CARRIER_CANDIDATE.md
```

from `SOURCE_RECHECKED / NOT_SOURCE_EXTRACTED` to `PARTIAL_SOURCE_EXTRACTED`, while preserving non-promotion cautions.

### PDS-N3 — R14 Matrix Population

Populate Prime/R1/R7/R13 cells in:

```text
R1_R14_CLASS_MATRIX_CANDIDATE.json
```

using the new claims, but keep R14 open.

## 6. Non-Promotion Footer

This extraction summary records narrow Prime source claims. It does not prove a carrier theorem, does not define a Formation Medium substrate, does not validate engineering routes, and does not authorize corporate claims.
