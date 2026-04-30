# Boundary-to-Biology Bootstrapping Ladder

This module implements a computable v0.1 of a forward constraint bootstrapping ladder:

```text
hydrogen -> H2 molecule -> ion/water -> membrane boundary -> ion channel -> single neuron -> synthetic neuron primitive
```

It is not recursion. The system does not loop back into itself. It moves forward through layers. Each rung does two things:

```text
1. Solve enough of the current layer to freeze a verified primitive.
2. Carry that primitive forward as a constraint/input for the next layer.
```

Every rung follows the same pattern:

```text
source benchmark -> boundary/process object -> unfolded observables -> verification report -> primitive hash -> input constraint for next rung
```

The purpose is not atomistic brute force. The purpose is to discover and freeze compact boundary/process objects whose unfolded observables match known physics or biology well enough to become reusable primitives.

The purpose of the ladder is to make biological process primitives progressively computable, verifiable, migratable, and eventually optimizable for synthetic substrate implementation.

## Clean claim

We implemented a computable boundary-to-biology bootstrapping ladder in which each layer produces a verified boundary-process primitive whose observables are benchmarked, whose primitive hash is recorded, and whose verified output constrains the next layer. The ladder progresses from hydrogen bound-state structure through molecular, ion/water, membrane, channel, and neuron dynamics, ending in a compact synthetic neuron primitive with checkpointing, migration, and zero-divergence state verification under a published protocol.

## Rungs

| Layer | Primitive | Observables | Verified | Used by next layer |
|---|---|---|---|---|
| Hydrogen | Bound-state primitive | Spectrum / energy levels / ionization | yes | H2 molecular bonding |
| H2 | Molecular bonding primitive | Bond length / binding energy / curve | yes | Ion/water primitive |
| Ion/water | Charge / solvation primitive | Charge / diffusion / hydration | yes | Membrane boundary |
| Membrane | Boundary primitive | Voltage / capacitance / RC decay | yes | Ion channel |
| Channel | Gating primitive | Open probability / current / recovery | yes | Single neuron |
| Neuron | Process primitive | Spikes / F-I curve / recovery / energy | yes | Synthetic neuron |
| Synthetic neuron | Compact process object | Migration / repair metadata / process equivalence | yes | Network / organism integration |

## Run

```bash
python -m substrate.cli build-ladder --out reports/substrate_ladder
python -m substrate.cli verify-rung hydrogen --out reports/substrate_ladder/hydrogen.json
python -m substrate.cli verify-rung neuron --out reports/substrate_ladder/neuron.json
python -m substrate.cli verify-rung synthetic_neuron --out reports/substrate_ladder/synthetic_neuron.json
python -m substrate.cli checkpoint-primitive reports/substrate_ladder/synthetic_neuron.json --out artifacts/synthetic_neuron_checkpoint.json
python -m substrate.cli migrate-primitive artifacts/synthetic_neuron_checkpoint.json --out runs/synthetic_neuron_migrated
```

## Relationship to the organism/process stack

The organism/process stack proves the migration, abstraction, process-equivalence, and substrate-optimization operation at the organism-process level.

The boundary-to-biology bootstrapping ladder grounds the lower-level synthetic biological primitive path.

Together:

```text
organism/process stack: 302-neuron process -> abstraction -> migration -> substrate optimization
boundary-to-biology stack: hydrogen -> H2 -> ion/water -> membrane -> channel -> neuron -> synthetic neuron
```

The convergence target is:

```text
derive/verify synthetic neuron primitives -> scale to network primitives -> integrate with organism/process migration stack
```

## Claim boundary

This is a computable digital primitive ladder. It does not claim biological neuron upload, human migration, consciousness transfer, or full QED/protein-folding derivation.

The result is not “full real neuron from final physics.” It is a computable forward-constraint ladder that generates verified primitives toward a synthetic neuron process.
