# CEF-v0.1 / CEF-v0.2 Forcing Upgrades

## CEF-v0.1: verifier-blind projection

CEF-v0.1 fixes the main CEF-v0 protocol weakness: the synthetic runtime no longer uses verifier-oracle centers or ranges to generate held-out observables.

The runtime receives:

```text
construction_packet.json
heldout_driver.json
```

The runtime does **not** receive:

```text
verifier_oracle.json
```

The verifier oracle is evaluation-only.

The key report fields are:

```json
{
  "protocol": "CEF-v0.1",
  "capture_origin": "fixture",
  "real_organism_constraints_loaded": false,
  "verifier_blind_projection": true,
  "runtime_used_oracle_for_generation": false
}
```

CEF-v0.1 is still a fixture-blind forcing proof, not real organism forcing.

## CEF-v0.2: real-dataset adapter path

CEF-v0.2 adds adapters for real-dataset-shaped C. elegans data.

Current adapters:

```text
import-real-json
import-real-csv
import-dryad-copper-h5
```

Converted capture packets carry:

```json
{
  "capture_origin": "real_dataset",
  "real_organism_constraints_loaded": true
}
```

CEF-v0.2 uses the same verifier-blind projection rule as v0.1:

```text
construction packet + held-out driver -> blind projection -> verifier oracle evaluation
```

## Current honesty boundary

CEF-v0.2 validates the real-dataset adapter and blind forcing path using a real-dataset-shaped fixture, and includes a dataset-specific Dryad copper-boundary H5 converter. It is ready to ingest WormWideWeb / Dryad / NWB-converted C. elegans captures, but this commit does not include a downloaded external biological dataset.

The first real-data milestone is:

```text
choose WormWideWeb or Dryad copper-boundary H5
-> write dataset-specific converter
-> emit CEF capture packet
-> run prove-forcing-blind
```


## Dryad copper-boundary H5 adapter

The `import-dryad-copper-h5` command converts one per-worm Dryad H5 file into a CEF-v0.2 capture packet. It searches for calcium traces, velocity, reversal events, copper-distance stimulus, posture/angular channels, and timing; then windows those streams into construction and held-out CEF episodes.

Example:

```text
python -m cef.cli import-dryad-copper-h5 --source external/dryad_celegans_copper/2023-03-30-01-cudata.h5 --out external/celegans_dryad_copper_capture_v0_2.json --windows 6
python -m cef.cli prove-forcing-blind --source external/celegans_dryad_copper_capture_v0_2.json --out reports/cef_v0_2
```

Honesty boundary: the adapter marks `capture_origin=real_dataset` only for an imported H5-derived capture. It does not claim worm migration; it only creates a real-organism forcing packet suitable for the construction/held-out CEF-v0.2 protocol.
