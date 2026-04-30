# EXTERNAL_REALITY_ADHESION_v0.1

## Core claim

The migration/abstraction/primitive stack should not only work inside a self-defined computational universe. It should attach to external neurobiological or externally standardized data and preserve externally defined observables under held-out protocols.

## v0.1 scope

This implementation provides an external neuron adhesion layer:

```text
external source -> convert to substrate-external-ephys-v1 -> fit/derive primitive -> verify held-out observables -> checkpoint/migrate -> controls fail
```

The executable CI anchor is a canonical HH/NeuroML-style current-clamp fixture generated from the substrate neuron benchmark. The real external path now accepts Allen-style exported sweep JSON, row-per-sample CSV, and optional NWB files through `pynwb`.

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

## HH/NeuroML-style fixture path

```bash
python -m substrate.cli generate-hh-neuroml-fixture --out external/hh_neuroml_fixture.json
python -m substrate.cli fit-primitive-to-ephys --source external/hh_neuroml_fixture.json --out primitives/hh_external
python -m substrate.cli verify-external-ephys --primitive primitives/hh_external --source external/hh_neuroml_fixture.json --out reports/hh_external_adhesion
python -m substrate.cli run-hh-neuroml-adhesion --out reports/hh_neuroml_adhesion
```

## Real external import path

### Allen-style exported sweep JSON

Expected shape:

```json
{
  "source_name": "allen_cell_types_export",
  "cell_id": "specimen_or_cell_id",
  "metadata": {"species": "mouse_or_human"},
  "sweeps": [
    {
      "sweep_number": 1,
      "split": "train",
      "current_pA": 150.0,
      "dt_ms": 0.025,
      "stimulus_start_ms": 100.0,
      "stimulus_end_ms": 700.0,
      "voltage_mv": [-65.0, -64.9]
    }
  ]
}
```

Convert and run adhesion:

```bash
python -m substrate.cli import-allen-sweep-json \
  --source external/allen_cell_export.json \
  --out external/allen_cell_converted.json

python -m substrate.cli fit-primitive-to-ephys \
  --source external/allen_cell_converted.json \
  --out primitives/allen_cell_external

python -m substrate.cli verify-external-ephys \
  --primitive primitives/allen_cell_external \
  --source external/allen_cell_converted.json \
  --out reports/allen_cell_external_adhesion
```

### Row-per-sample CSV

Required columns:

```text
protocol_id, voltage_mv
```

Optional columns:

```text
split, t_ms, dt_ms, current_uA, current_pA, duration_ms, pulse_start_ms, pulse_end_ms
```

Convert and run adhesion:

```bash
python -m substrate.cli import-ephys-csv \
  --source external/ephys_export.csv \
  --out external/ephys_converted.json \
  --source-name allen_or_dandi_csv_export \
  --cell-id cell_001

python -m substrate.cli fit-primitive-to-ephys \
  --source external/ephys_converted.json \
  --out primitives/ephys_cell_001

python -m substrate.cli verify-external-ephys \
  --primitive primitives/ephys_cell_001 \
  --source external/ephys_converted.json \
  --out reports/ephys_cell_001_adhesion
```

### Optional NWB import

The NWB importer is optional because it requires `pynwb` and real NWB files can vary in acquisition structure.

```bash
pip install pynwb

python -m substrate.cli import-nwb \
  --source external/cell_recording.nwb \
  --out external/nwb_converted.json \
  --source-name dandi_nwb_export \
  --cell-id cell_001
```

If the NWB acquisition layout is complex, export the desired sweeps to the Allen-style JSON or CSV adapter first.

## v0.1 result table

| Anchor | Source external? | Process fit? | Held-out pass? | Migration verified? | Controls fail? | Status |
|---|---|---|---|---|---|---|
| HH/NeuroML-style fixture | standardized fixture | yes | yes | yes | yes | pass |
| Allen-style sweep JSON | file-provided export | yes | supported | yes | supported | adapter implemented |
| CSV ephys export | file-provided export | yes | supported | yes | supported | adapter implemented |
| NWB/DANDI file | file-provided export | optional pynwb | supported after import | yes | supported | optional adapter implemented |

## Claim boundary

This is an external-ready adhesion benchmark over published/file-provided electrophysiology-style observables. It is not a biological upload, not consciousness transfer, not a claim of full biological neuron derivation, and not a live Allen/DANDI downloader in v0.1.

## Next anchors

The intended next anchors are:

```text
Allen Cell Types exported electrophysiology
DANDI/NWB exported electrophysiology
NeuroML/Open Source Brain canonical model files
FlyWire / fly-model subset sources
FlyGym or other embodied fly benchmarks
```
