# Route A Topoelectrical + Superconducting Microwave Source Review Plan

STATUS: GENERATED / OPEN / SOURCE_REVIEW_PLAN  
ARGUMENT_STATUS: ENGINEERING_TRIAGE / GENERATED  
CHECK_STATUS: NOT_CHECKED  
SOURCE_STATUS: EXTERNAL_SOURCE_NEEDED  
PROMOTION_STATUS: BLOCKED  
TARGET_LOCATION: research_ledger/  
DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json

## 0. Non-Promotion Notice

This is a source-review plan for Route A:

```text
topoelectrical / topological circuit boundary-readout layer
+ superconducting microwave resonator/coupler transport layer
```

It is not a source-extracted claim, not a theorem, not engineering feasibility evidence, not a selected substrate, not IP, not a prototype architecture, and not corporate/investor language.

Inputs:

```text
research_ledger/FORMATION_MEDIUM_ENGINEERING_TRIAGE_001.md
research_ledger/FORMATION_MEDIUM_ENGINEERING_GATE_MATRIX_001.json
research_ledger/FORMATION_MEDIUM_NEGATIVE_CONTROLS.md
research_ledger/PREVIOUS_GPT_TRANSPORT_SYMBOL_MINING_SYNTHESIS_001.md
research_ledger/FORMATION_MEDIUM_BULK_READOUT_WITNESS_SCHEMA.md
```

## 1. Purpose

Route A is currently the leading generated/open engineering lead because it decomposes the engineering problem into two candidate layers:

```text
topoelectrical/topological circuit cells
  -> candidate boundary/readout localization layer

superconducting microwave resonator/coupler systems
  -> candidate controllable transport/coupling layer
```

The source review must decide whether this decomposition is meaningful or whether it collapses into negative controls:

```text
NC-006 mere boundary-mode visualization
NC-007 hardware routing without intrinsic readout
NC-008 readout-faithfulness assumption
```

## 2. Review Gates

Route A must be reviewed against the current engineering gates:

```text
G1 native carrier
G2 native admissibility/local operations
G3 intrinsic boundary/readout
G4 bulk/readout faithfulness status
G5 native settling/formation dynamics
G6 lab/corporate tractability
G7 failure interface
G8 transport/readout separation
G9 equality-layer intrinsicness
```

Current default statuses remain:

```text
G4 = READOUT_FAITHFULNESS_UNKNOWN
G9 = EQUALITY_UNKNOWN
```

No source review may change those statuses without explicit evidence.

## 3. Source Target Families

### RA-S1 — Topolectrical Circuit Boundary / Readout Layer

Initial source candidates:

```text
Lee et al., Topolectrical Circuits, Communications Physics 1, 39 (2018), DOI 10.1038/s42005-018-0035-2
Imhof et al., Topolectrical-circuit realization of topological corner modes, Nature Physics 14, 925–929 (2018), DOI 10.1038/s41567-018-0246-1
```

Review questions:

1. Are topological boundary resonances or corner modes intrinsic to the circuit Laplacian/topological band structure, or mainly measurement/impedance features chosen by the observer?
2. Does impedance readout count as intrinsic boundary/readout for Formation Medium purposes, or does it remain an externally designated output channel?
3. Are boundary/corner modes robust enough to serve as readout-bearing structures, or only visual/diagnostic modes?
4. What exactly is native: circuit nodes, admittance/Laplacian structure, impedance response, boundary resonance, or topological invariant?

Possible Formation contacts:

```text
S1 native carrier/admissibility
S2* intrinsic boundary/readout
G3 intrinsic boundary/readout
NC-006 mere boundary-mode visualization
```

Current status:

```text
SOURCE_REVIEW_NEEDED / DO_NOT_PROMOTE
```

Kill condition:

If the reviewed sources show only engineered boundary-mode visualization without intrinsic readout semantics, Route A’s topoelectrical layer becomes an analog/negative-control layer rather than a Formation Medium readout candidate.

---

### RA-S2 — Superconducting Microwave Resonator / Coupler Transport Layer

Initial source candidates:

```text
Wulschner et al., Tunable coupling of transmission-line microwave resonators mediated by an rf SQUID, EPJ Quantum Technology 3, 10 (2016), DOI 10.1140/epjqt/s40507-016-0048-2
Kim et al., Tunable Superconducting Cavity using Superconducting Quantum Interference Device Metamaterials, Scientific Reports 9, 4633 (2019), DOI 10.1038/s41598-019-40891-1
Scarlino et al., Coherent microwave-photon-mediated coupling between a semiconductor and a superconducting qubit, Nature Communications 10, 3011 (2019), DOI 10.1038/s41467-019-10798-6
Stehlik et al., Tunable Coupling Architecture for Fixed-Frequency Transmon Superconducting Qubits, Physical Review Letters 127, 080505 (2021), DOI 10.1103/PhysRevLett.127.080505
```

Review questions:

1. Can tunable microwave couplers/resonators provide native transport/coupling rather than externally programmed signal routing?
2. What is the native carrier: microwave photons, resonator modes, SQUID flux-tunable mutual inductance, transmon/cavity excitations, or network modes?
3. Does tunability preserve intrinsic structure, or does it merely implement control knobs for ordinary engineered dynamics?
4. Can transport be separated from readout in a way consistent with G8?
5. Are there experimentally demonstrated regimes where coupling can be dynamically controlled without destroying mode identity?

Possible Formation contacts:

```text
S3 native local operations / transport
G8 transport/readout separation
NC-007 hardware routing without intrinsic readout
```

Current status:

```text
SOURCE_REVIEW_NEEDED / DO_NOT_PROMOTE
```

Kill condition:

If the reviewed sources show only externally programmed signal routing or ordinary quantum-control coupling, the microwave layer remains a controllable transport tool, not a Formation Medium operation layer.

---

### RA-S3 — Hybrid Interface Question

Core question:

> Can a topological circuit boundary/readout layer and superconducting microwave transport/coupling layer be combined without reducing the whole route to external routing or analog simulation?

Review questions:

1. Is there a source-supported interface between topological circuit boundary modes and superconducting microwave resonator/coupler modes?
2. Can boundary-localized modes be coupled or transported while preserving their readout identity?
3. Does the hybrid system have a native admissibility layer, or only designer-fabricated connectivity?
4. Can any proposed interface state a readout map and bulk/equivalence relation?
5. What would a minimal negative-control demo look like?

Possible Formation contacts:

```text
G3 intrinsic boundary/readout
G4 bulk/readout faithfulness status
G8 transport/readout separation
G9 equality-layer intrinsicness
NC-006
NC-007
NC-008
```

Current status:

```text
UNREVIEWED / HIGH_RISK / DO_NOT_PROMOTE
```

Kill condition:

If the hybrid is only a boundary-mode device connected to a tunable signal router, it is not Formation Medium. It may remain useful as a demo/negative control.

## 4. Extraction Targets If Sources Are Ingested

Do not create these until sources are actually ingested and inspected.

### RA-EXT-T1 — Topolectrical Boundary Resonance Claim

Candidate extraction target:

```text
topological boundary resonances / corner modes appear in impedance or circuit response and are tied to circuit topology/admittance structure
```

Blocked inference:

```text
impedance readout is Formation Medium canonical readout
```

### RA-EXT-T2 — Circuit Laplacian / Hamiltonian Analogy Claim

Candidate extraction target:

```text
circuit Laplacian plays a Hamiltonian-like role in topolectrical systems
```

Blocked inference:

```text
Hamiltonian analogy proves substrate-level formation
```

### RA-EXT-T3 — Tunable Microwave Coupling Claim

Candidate extraction target:

```text
superconducting microwave resonator coupling can be tuned in situ using SQUID or related coupler mechanisms
```

Blocked inference:

```text
tunable coupling is native Formation Medium transport
```

### RA-EXT-T4 — Coherent Microwave Bus Claim

Candidate extraction target:

```text
microwave resonators can mediate coherent coupling or act as quantum buses in circuit-QED-like systems
```

Blocked inference:

```text
quantum bus behavior is Formation Medium transport/readout
```

### RA-EXT-T5 — Hybrid Failure Interface

Candidate extraction target:

```text
limitations/noise/calibration/control requirements of tunable resonator/coupler systems
```

Blocked inference:

```text
laboratory controllability equals formation dynamics
```

## 5. Required Review Output

A future source review should produce:

```text
ROUTE_A_SOURCE_REVIEW_001.md
ROUTE_A_SOURCE_REVIEW_001.json
```

with fields:

```text
source_id
title
authors/year/DOI
review_layer: topolectrical | microwave_coupler | hybrid_interface
extracted_claim_candidates
blocked_inferences
relevant_gates
negative_control_risks
route_status_update
```

Allowed route-status updates:

```text
SOURCE_REVIEWED_NO_PROMOTION
ANALOG_DEMO_ONLY
NEGATIVE_CONTROL_ONLY
CONTINUE_AS_CANDIDATE
REJECT_ROUTE_A
```

Forbidden route-status updates at this stage:

```text
FEASIBLE_ENGINEERING
SELECTED_SUBSTRATE
PROTOTYPE_READY
INVESTOR_READY
```

## 6. Near-Term Review Order

Priority order:

```text
1. Topolectrical Circuits — Communications Physics 2018
2. Topolectrical-circuit realization of topological corner modes — Nature Physics 2018
3. Tunable coupling of transmission-line microwave resonators mediated by an rf SQUID — EPJ Quantum Technology 2016
4. Tunable Superconducting Cavity using SQUID Metamaterials — Scientific Reports 2019
5. Coherent microwave-photon-mediated coupling — Nature Communications 2019
6. Tunable Coupling Architecture for Fixed-Frequency Transmon Superconducting Qubits — PRL 2021
```

Rationale:

First establish whether the boundary/readout layer is meaningful, then establish whether the transport/coupling layer is only routing/control or can preserve a native transport layer.

## 7. Corporate Boundary

Route A should be described internally as:

```text
leading generated/open engineering review queue
```

not as:

```text
selected engineering substrate
prototype architecture
lab-ready demonstration
fundraising claim
```

Safe internal sentence:

> Route A is the current leading review queue because it cleanly separates candidate boundary/readout localization from candidate transport/coupling hardware, while exposing clear negative-control risks.

Unsafe external sentence:

> We can build the Formation Medium with topolectrical circuits and superconducting microwave couplers.

## 8. Kill Conditions

Reject or demote Route A if:

1. topolectrical boundary/corner modes are only visualization features, not intrinsic readout candidates;
2. impedance readout is entirely observer-designated output;
3. microwave couplers provide only external routing/control;
4. no native admissibility layer can be stated;
5. no readout map or bulk/equivalence relation can be stated;
6. G8 transport/readout separation fails;
7. G9 equality-layer status cannot even be scoped;
8. any reviewed source support is used as substrate or engineering feasibility evidence.

## 9. Non-Promotion Footer

This plan defines a source-review queue for Route A. It does not create source-extracted claims, validate feasibility, select a substrate, create IP, or authorize corporate/investor language.
