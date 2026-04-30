# Process-Preserving Substrate Optimization

## Core claim

A 302-neuron organism-like process was translated into a lower-dimensional synthetic substrate, migrated, and optimized for stability, robustness, efficiency, repairability, and inspectability while preserving source-equivalent self-maintaining behavior under held-out tasks.

## Frame

Preserve the process. Improve the substrate.

## Score split

Round 3 separates the benchmark into three major scores plus a repair score:

1. Equivalence Score - source behavior preservation under the benchmark.
2. Viability / Improvement Score - self-maintenance, stability, and robustness improvements.
3. Efficiency / Substrate Score - compression, checkpoint/model size, and migration integrity.
4. Repairability Score - recovery after latent corruption.

The total score is gated:

```text
Total Score = Equivalence Gate * (Improvement Score + Efficiency Score + Repairability Score)
```

The gate is zero unless the equivalence score reaches the configured threshold.

## Minimal v1 implementation

The first implementation uses the existing PCA-Ridge substrate and creates a compatible improved model by applying conservative substrate regularization:

- stronger Ridge regularization if fitting a new base model
- transition shrinkage for smoother latent dynamics
- motor smoothing to reduce left/right motor conflict
- repair tests by latent zeroing, Gaussian noise, and sign flips
- explicit controls: random latent and over-stable controller

## CLI commands

```bash
python -m wormsim.cli train-improved-substrate --dataset datasets/source_302_hard_v1 --base-abstraction abstractions/pca8 --latent-dim 8 --out abstractions/pca8_improved
python -m wormsim.cli run-improved-substrate --model abstractions/pca8_improved --task hard_mixed --steps 5000 --out runs/pca8_improved_live
python -m wormsim.cli migrate-improved-substrate --checkpoint runs/pca8_improved_live/checkpoint_t5000.npz --out runs/pca8_improved_migrated
python -m wormsim.cli repair-test --model abstractions/pca8_improved --task hard_mixed --out reports/repair_test_pca8_improved
python -m wormsim.cli benchmark-improved-substrate --dataset datasets/source_302_hard_v1 --base abstractions/pca8 --improved abstractions/pca8_improved --task hard_mixed --out reports/process_preserving_substrate_optimization
```

## Claim boundary

This is a digital process-preserving substrate optimization benchmark. It does not claim biological C. elegans transfer, human migration, consciousness transfer, or identity solved.
