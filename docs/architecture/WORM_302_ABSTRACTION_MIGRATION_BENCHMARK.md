# 302 Abstraction Migration Benchmark

## Project names

- 302 Abstraction Migration Benchmark
- Worm-302 Abstraction Transfer

## Claim

A deterministic 302-neuron organism-like process was compressed into lower-dimensional abstractions, migrated into a new runtime substrate, and benchmarked for retained closed-loop behavior, perturbation recovery, and self-maintenance.

## Baseline

The existing source proof remains the baseline:

```text
302-neuron organism-like process -> checkpoint -> hash -> migrate -> resume -> 0.0 divergence
```

## New proof

```text
302-neuron organism-like process -> record dynamics -> compress/abstract -> instantiate abstracted process -> migrate -> run closed-loop -> measure retained self-maintaining behavior
```

## Minimal viable implementation

The first implementation uses PCA plus Ridge regression:

```text
X_neural[302] -> PCA -> z[k]
z[t+1] = f(z[t], sensory[t], body[t])
motor[t] = g(z[t])
```

The abstracted organism is not a replay. It has its own live runtime loop:

```text
sense world -> update latent state -> emit motor command -> move body -> update world -> repeat
```

## Commands

```bash
python -m wormsim.cli collect-dataset --tasks food,harm,perturb,wall,mixed --episodes 100 --steps 2000 --out datasets/source_302_v1
python -m wormsim.cli train-abstraction --method pca-ridge --latent-dim 64 --dataset datasets/source_302_v1 --out abstractions/pca64
python -m wormsim.cli run-abstracted --model abstractions/pca64 --task mixed --steps 10000 --out runs/pca64_live
python -m wormsim.cli migrate-abstracted --checkpoint runs/pca64_live/checkpoint_t10000.npz --out runs/pca64_migrated
python -m wormsim.cli verify-abstracted-migration --model abstractions/pca64 --checkpoint-a runs/pca64_live/checkpoint_t10000.npz --checkpoint-b runs/pca64_migrated/checkpoint_t10000.npz --steps 1000 --out reports/abstracted_migration_report.json
python -m wormsim.cli benchmark-abstraction --model abstractions/pca64 --task mixed --steps 1000 --out reports/pca64_report
```

## Task battery

- Food seeking
- Harm avoidance
- Perturbation recovery
- Wall / obstacle response
- Mixed world

## Dataset arrays

The dataset writer stores:

- `X_neural`: neural states
- `S_sensory`: sensory inputs
- `A_motor`: motor summaries
- `B_body`: body state
- `E_env`: environment state
- `V_viability`: viability/self-maintenance score
- `episode_index`: episode, step, task index

## Output target

```text
ABSTRACTION MIGRATION BENCHMARK COMPLETE
Source: 302-neuron organism-like process
Abstraction: PCA-Ridge 64 latent units
Compression ratio: 4.72x
Migration: verified
Trajectory divergence after migration: 0.0
Behavior fidelity: X%
Self-maintenance retained: Y%
Perturbation recovery retained: Z%
Controls: failed as expected
```

## Claim boundary

This does not claim biological C. elegans migration. It is a controlled digital testbed for abstraction and substrate-transfer technology.
