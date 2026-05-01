# HSM-v0.1 Independent Constraint Preservation

HSM-v0.1 upgrades HSM-v0 from closed-world hash preservation to independent numeric constraint preservation.

The protocol writes two separate constraint objects:

```text
artifacts/hsm_constraints_v0_1/construction_constraints.json
artifacts/hsm_constraints_v0_1/verifier_oracle.json
```

The builder consumes the construction packet. The final verifier consumes the separately hashed verifier oracle. The migrated substrate must expose numeric post-migration observables that fall within the oracle ranges.

This means the proof can fail for scientific/protocol reasons even if checkpoint/hash migration succeeds.

## Command

```bash
python -m hsm.cli prove-independent
```

## Claim boundary

This demonstrates that a human-constrained synthetic substrate object can preserve independently frozen numeric human-style constraints across substrate transition under HSM-v0.1. It is not a claim that a human person has been migrated, nor a claim of full human brain simulation.
