# Worm Migration Proof Package Template

## Required release files

- `README.md`
- `demo_video.mp4`
- `source_code/`
- `checkpoint_file/`
- `checkpoint_hash.txt`
- `pre_migration_log.jsonl`
- `post_migration_log.jsonl`
- `verification_report.json`
- `reproduction_steps.md`
- `capital_next_step.md`

## Publication checklist

- Replace every placeholder artifact with real generated release output.
- Do not fabricate `demo_video.mp4`.
- Verify that the published checkpoint hash matches the published checkpoint file.
- Verify that the public reproduction steps produce `MIGRATION VERIFIED`.
- Include the frozen claim exactly once at the top of the package.
- Include the claim boundary in the README.

## Release README skeleton

```markdown
# Verified Digital Worm Migration

We verified lossless migration of a complete digital worm-like organism process between computational substrates.

This package demonstrates a deterministic digital organism process being checkpointed, transferred, hash-verified, resumed, and compared for identical continuation under the published protocol.

This does not claim biological worm upload, mind transfer, life transfer, medical benefit, or human transfer.
```
