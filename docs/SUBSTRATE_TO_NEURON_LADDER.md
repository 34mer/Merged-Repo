# Substrate-to-Neuron Boundary Derivation Ladder

This module implements a computable v0.1 of the recursive ladder:

```text
hydrogen -> H2 molecule -> water/ions -> membrane boundary -> ion channel -> single neuron -> synthetic neuron primitive
```

Every rung follows the same pattern:

```text
source benchmark -> boundary object -> unfolded observables -> verification report -> primitive hash
```

The purpose is not atomistic brute force. The purpose is to discover and freeze compact boundary/process objects whose unfolded observables match known physics or biology well enough to become reusable primitives.

## Run

```bash
python -m substrate.cli build-ladder --out reports/substrate_ladder
python -m substrate.cli verify-rung hydrogen --out reports/substrate_ladder/hydrogen.json
python -m substrate.cli checkpoint-primitive reports/substrate_ladder/hydrogen.json --out artifacts/hydrogen_checkpoint.json
python -m substrate.cli migrate-primitive artifacts/hydrogen_checkpoint.json --out runs/hydrogen_migrated
```

## Claim boundary

This is a computable digital primitive ladder. It does not claim biological neuron upload, human migration, consciousness transfer, or full QED/protein-folding derivation.
