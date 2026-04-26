# Physical Regime Source-Intake Criteria

STATUS: GENERATED / OPEN / SOURCE_INTAKE_CRITERIA / NOT_SOURCE_EXTRACTED / NOT_SUBSTRATE_SELECTION / NOT_ENGINEERING_READY  
ARTIFACT ROLES: GUARD / SOURCE_REVIEW / COMPARATOR / NEGATIVE_CONTROL / ENGINEERING_GATE  
DO_NOT_PLACE_IN: SOURCE_EXTRACTED_CLAIMS.json

## 0. Non-Promotion Notice

This artifact defines criteria for future source intake only. It does not ingest sources, extract source claims, validate CRBSM, validate Route A, select scattering-native physics, select high-resonance regimes, validate Ising machines, select Ising machines, prove a substrate, prove a settling law, or authorize engineering/corporate claims.

## 1. Critical-Review Prework

Hard bottleneck attacked:

```text
physical-regime triage and substrate uncertainty, especially persistent support/channel identity and native readout versus external measurement
```

Thin-stick risks:

```text
Route A source review treated as feasibility
CRBSM mechanism language treated as physics
scattering-native mathematical proximity treated as substrate selection
high-resonance tunability treated as native settling law
```

Negative-progress risk:

```text
This could become a speculative shopping list unless it remains criteria-driven with rejection gates.
```

Why this is not merely convenient drift:

```text
It constrains future source intake and can reject regimes before more artifacts are added.
```

## 2. Anti-Flattening Rule

```text
CRBSM = mechanism-language
Route A = hardware/proxy
scattering-native = mandatory comparator
high-resonance = possible bridge comparator
Ising machines = hardware-combinatorial / combinatorial-machine comparator
```

Source intake must preserve these roles and must not declare a winner.

## 3. Global Gate Axes

Every physical-regime source review must score against:

| Gate | Question | Kill condition |
|---|---|---|
| PG1 native carrier | Does the regime provide native carrier degrees of freedom rather than externally encoded variables? | Carrier exists only as software labels, externally programmed states, or measurement bookkeeping. |
| PG2 native admissibility | Does the regime impose native admissibility/constraint structure without external filtering? | Admissibility is only imposed by controller, postselection, or user-designed circuit logic. |
| PG3 relay or transport | Does the regime support native relay/transport/connectivity relevant to readout formation? | Transport is ordinary signal routing or gate scheduling without intrinsic readout relevance. |
| PG4 persistent support identity | Can the regime preserve support/channel/mode identity long enough to carry formation-relevant state? | Identity exists only because the observer tracks it or because control software labels it. |
| PG5 intrinsic readout | Is the readout intrinsic to the regime rather than only a measurement convenience? | Readout is only an externally chosen diagnostic, visualization, or probe measurement. |
| PG6 bulk/readout separation | Does the regime separate readout from bulk realization strongly enough to test non-faithfulness? | Readout is a fully faithful reconstruction of the bulk or direct measurement of all relevant bulk state. |
| PG7 harnessability | Can the regime be harnessed without reducing it to ordinary computation or externally routed control? | Harnessing requires complete external programming, postselection, or simulation. |
| PG8 negative-control clarity | Can the regime be cleanly failed if it is only an analog/computation/visualization route? | Regime cannot be distinguished from ordinary simulation, analog visualization, or measurement apparatus. |

## 4. Regime Tracks

### TRACK_CRBSM — Mechanism-Language

Question:

> Are there real physical systems that natively instantiate CRBSM-like boundary sheets, chiral relay pockets, quarter-turn/A2-like transport, and persistent support identity?

Must find:

```text
native boundary-sheet-like state variables
relay pockets or localized transport centers not imposed by controller
chiral or quarter-turn-like transport law
persistent support/channel identity or relay memory
```

Must not accept:

```text
CRBSM terminology as evidence
constructed-by-assumption relay ledgers
externally routed quarter-turn operations
Route A hardware convenience as CRBSM implementation
```

Kill conditions:

```text
persistent support identity remains only software/observer tracked
boundary sheets are designer interfaces, not native state variables
quarter-turn transport is only simulation or circuit routing
no physical source class can be named without analogy drift
```

### TRACK_ROUTE_A — Hardware/Proxy Route

Question:

> Which Route A sources can support proxy instrumentation while clearly failing or satisfying native Formation Medium gates?

Must find:

```text
source-backed topoelectrical boundary/corner impedance readout
source-backed superconducting microwave transport/coupling
separation of transport bus from readout channel
negative controls showing ordinary routing/measurement failure
```

Must not accept:

```text
impedance readout as canonical readout
tunable microwave coupling as native settling law
high-fidelity qubit gates as Formation Medium operations
source review as engineering feasibility
```

### TRACK_SCATTERING_NATIVE — Mandatory Comparator

Question:

> Does scattering-native physics supply the formation/readout structure more natively than CRBSM or Route A, and can it be harnessed without remaining only a mathematical comparator?

Must not accept:

```text
mathematical proximity as substrate selection
positive-geometry source support as physical realization
scattering theory as engineering route by default
comparator status as winner status
```

### TRACK_HIGH_RESONANCE_NATIVE — Possible Bridge Comparator

Question:

> Can mesoscopic high-resonance regimes provide native carrier, relay/transport, persistent mode identity, intrinsic readout, and harnessability more naturally than high-energy scattering or ordinary hardware routing?

Must find:

```text
long-lived or metastable resonant modes/channels
native mode conversion, chiral transport, or relay-like behavior
boundary/corner/resonant readout not merely measurement convenience
coupling/control that preserves native dynamics rather than replacing them
```

Must not accept:

```text
high-Q or tunable resonance as native settling law
controlled resonance hardware as Formation Medium
Route A resonance components as proof of high-resonance-native substrate
bridge-candidate status as winner status
```



### TRACK_ISING_MACHINE — Hardware-Combinatorial / Combinatorial-Machine Comparator

Question:

> Do Ising machines provide a physically instantiated combinatorial settling/ground-state search comparator that is closer to Formation Medium formation behavior than S-matrix observables, without collapsing into ordinary optimization hardware?

Must find:

```text
hardware-native spin or oscillator variables with clear physical carrier status
combinatorial energy or constraint landscape that settles through physical dynamics rather than software enumeration
readout of ground/low-energy states with explicit mapping from problem graph to physical couplings
negative controls distinguishing physical settling from digital optimization or externally programmed annealing schedule
```

Must not accept:

```text
combinatorial optimization performance as Formation Medium evidence
Ising Hamiltonian ground state as canonical positive-geometric readout
programmable couplings as native admissibility without qualification
annealing schedule or optimizer dynamics as native settling law
hardware solver status as substrate selection
```

Kill conditions:

```text
settling is mostly externally scheduled optimization rather than native formation behavior
problem graph/couplings are entirely user-programmed and no intrinsic admissibility remains
readout is only the conventional Ising objective value or spin assignment with no Formation Medium semantics
hardware advantage is benchmark performance rather than substrate/readout evidence
the track cannot be distinguished from ordinary analog/digital combinatorial optimization
```

## 5. Review Queue

| ID | Track | Question | Expected output |
|---|---|---|---|
| PRI-001 | HIGH_RESONANCE_NATIVE | Which source classes show long-lived mesoscopic resonant modes with native identity and nontrivial coupling/readout? | source-review candidate list with PG1-PG8 evidence tags and kill-condition notes |
| PRI-002 | SCATTERING_NATIVE | Which scattering-native sources connect physical observables or S-matrix structure to intrinsic readout rather than only formal amplitude geometry? | comparator source-intake plan, not winner declaration |
| PRI-003 | ROUTE_A | Which Route A reviewed sources are worth ingestion into SOURCE_EXTRACTED_CLAIMS, and what claims must stay blocked? | narrow extraction plan plus negative-control demo spec |
| PRI-004 | CRBSM | Which physical systems, if any, could instantiate CRBSM-like persistent support/channel identity without constructed-by-assumption ledgers? | mechanism-source review or demotion memo |
| PRI-005 | ISING_MACHINE | Which Ising-machine source classes are relevant as hardware-combinatorial comparators, and which fail as ordinary optimization hardware? | source-candidate list with PG1-PG8 evidence tags and kill-condition notes |

## 6. Source Promotion Policy

Allowed next status:

```text
EXTERNAL_SOURCE_REVIEW or SOURCE_INTAKE_PLAN
```

Blocked statuses:

```text
SOURCE_EXTRACTED without ingested source
CHECKED without validator
SUBSTRATE_SELECTED
ENGINEERING_READY
WINNER_DECLARED
```

Minimum for SOURCE_EXTRACTED:

```text
specific source file or citation ingested into repo/source corpus
claim text extracted narrowly
blocked inferences recorded
formal_check_targets linked or explicitly absent
non-promotion boundary stated
```

## 7. Non-Promotion Footer

This artifact defines criteria for future source intake only. It does not ingest sources, extract source claims, validate CRBSM, validate Route A, select scattering-native physics, select high-resonance regimes, validate Ising machines, select Ising machines, prove a substrate, prove a settling law, or authorize engineering/corporate claims.
