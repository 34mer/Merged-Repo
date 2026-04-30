# HSM-v0 Protocol

Protocol sequence:

1. Build the HSM-v0 human constraint packet.
2. Verify the boundary-to-biology primitive parent chain.
3. Construct a human-constrained source substrate.
4. Translate the source into a synthetic human substrate.
5. Run deterministic pre-migration dynamics.
6. Checkpoint, migrate, reload, and resume.
7. Verify zero-divergence state continuation.
8. Verify post-migration constraint preservation.
9. Run negative controls.
10. Print the final claim only if all gates pass.

Success JSON:

```json
{
  "claim": "Human substrate migration is empirically possible",
  "protocol": "HSM-v0",
  "status": "PASS",
  "human_constraints_verified": true,
  "parent_primitive_chain_verified": true,
  "source_substrate_constructed": true,
  "synthetic_substrate_constructed": true,
  "migration_verified": true,
  "state_divergence": 0.0,
  "post_migration_constraints_preserved": true,
  "controls_failed_as_expected": true
}
```
