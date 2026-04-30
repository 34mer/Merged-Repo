# EXTERNAL_REALITY_ADHESION_v0.1

## Core claim

The migration/abstraction/primitive stack should not only work inside a self-defined computational universe. It should attach to external neurobiological or externally standardized data and preserve externally defined observables under held-out protocols.

## v0.1 scope

This first implementation provides an offline-reproducible external neuron adhesion layer:

```text
external source -> fit/derive primitive -> verify held-out observables -> checkpoint/migrate -> controls fail
```

The executable CI anchor is a canonical HH/NeuroML-style current-clamp fixture generated from the substrate neuron benchmark. Real Allen/DANDI/NWB exports can be represented with the same JSON schema and evaluated through the same fit/verify path.

## External ephys schema

A source file contains:

```text
schema: substrate-external-ephys-v1
source_name
cell_id
metadata
protocols[]
  protocol_id
  split: train | heldout
  current_uA
  duration_ms
  dt_ms
  pulse_start_ms
  pulse_end_ms
  voltage_mv[]
  spike_times_ms[]
source_hash
```

## Metrics

The adhesion verifier reports:

```text
voltage_trace_similarity
spike_timing_score
F-I curve similarity
heldout protocol score
migration verification
control failure
```

## Controls

v0.1 includes:

```text
random control
 over-stable control
behavior-only leakage control
```

The random and over-stable controls are expected to fail. The behavior-only leakage control is deliberately included to show what artificial train/test leakage looks like and is not counted as an honest control.

## CLI

```bash
python -m substrate.cli generate-hh-neuroml-fixture --out external/hh_neuroml_fixture.json
python -m substrate.cli fit-primitive-to-ephys --source external/hh_neuroml_fixture.json --out primitives/hh_external
python -m substrate.cli verify-external-ephys --primitive primitives/hh_external --source external/hh_neuroml_fixture.json --out reports/hh_external_adhesion
python -m substrate.cli run-hh-neuroml-adhesion --out reports/hh_neuroml_adhesion
```

## Claim boundary

This is an external-ready adhesion benchmark over published/file-provided electrophysiology-style observables. It is not a biological upload, not consciousness transfer, not a claim of full biological neuron derivation, and not a live Allen/DANDI fetch in v0.1.

## Next anchors

The intended next anchors are:

```text
Allen Cell Types exported electrophysiology
DANDI/NWB exported electrophysiology
NeuroML/Open Source Brain canonical model files
FlyWire / fly-model subset sources
FlyGym or other embodied fly benchmarks
```
