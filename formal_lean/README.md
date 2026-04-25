# Formation Lean Scaffold

Status: ARISTOTLE-COMPATIBLE LEAN SCAFFOLD / NOT CHECKED FORMAL LAYER

This directory is an intentionally minimal Lean scaffold for future formation-medium formalization work.

## Pins

- Lean toolchain: `leanprover/lean4:v4.28.0`
- mathlib: `v4.28.0`

## Boundary

The files here are scaffolding only until a formal-engine build is run and recorded.

- Aristotle/Ax-Prover output is candidate material only.
- Lean `lake build` is the checker for Lean status.
- File presence is not theorem status.
- Do not promote this scaffold to CHECKED until a build result is available.

## Current MCP gap

The current MCP does not expose a Lean/Lake build tool. See `docs/architecture/MCP_TOOL_GAPS.md`.
