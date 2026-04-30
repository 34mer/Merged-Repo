# Deterministic Worm Migration Demo

This demo implements the first verified digital migration rung described in the user-provided plan: a deterministic 302-neuron worm-like organism whose complete state can be checkpointed, copied to a second run folder, hash-verified, resumed, and compared for identical continuation.

## Claim boundary

This is a verified migration of a deterministic digital worm-like organism process. It is not a biological C. elegans migration claim.

Verification means:

1. The full digital state is captured in a checkpoint.
2. The checkpoint file is hash-verified after transfer.
3. Two resumed continuations from the original and migrated checkpoints produce identical trajectories under the same deterministic update rules.

## Run locally

Use Python 3.11+ and install the repo requirements, then expose `src/` on `PYTHONPATH` for the demo commands:

```bash
pip install -e .
$env:PYTHONPATH="src"  # PowerShell
python -m wormsim.cli init --neurons 302 --seed 42 --out runs/run_001
python -m wormsim.cli run --checkpoint runs/run_001/checkpoint_t0.npz --steps 5000 --out runs/run_001
python -m wormsim.cli migrate --checkpoint runs/run_001/checkpoint_t5000.npz --out runs/migrated_run
python -m wormsim.cli resume --checkpoint runs/migrated_run/checkpoint_t5000.npz --steps 5000 --out runs/migrated_run
python -m wormsim.cli compare --checkpoint-a runs/run_001/checkpoint_t5000.npz --checkpoint-b runs/migrated_run/checkpoint_t5000.npz --steps 1000 --out runs/verification_report.json
```

On macOS/Linux, use:

```bash
export PYTHONPATH=src
```

Expected terminal summary from the final command:

```text
MIGRATION VERIFIED
Checkpoint hash: matched
Config hash: matched
Trajectory divergence: 0.0
```

## Implementation pieces

- `src/wormsim/config.py` - deterministic simulation configuration.
- `src/wormsim/organism.py` - complete organism state container and seeded initialization.
- `src/wormsim/environment.py` - deterministic food/wall sensory environment.
- `src/wormsim/dynamics.py` - fixed-step synthetic 302-neuron update loop.
- `src/wormsim/checkpoint.py` - complete checkpoint save/load and BLAKE3 hash sidecar.
- `src/wormsim/verify.py` - post-migration trajectory comparison and JSON report.
- `src/wormsim/cli.py` - public command-line demo flow.
- `tests/test_wormsim_migration.py` - determinism, checkpoint roundtrip, and copied-checkpoint migration verification tests.

## Hardware note

The first demo runs on CPU by design. CPU-only NumPy float64 avoids common GPU nondeterminism from parallel reductions, driver differences, and kernel scheduling.
