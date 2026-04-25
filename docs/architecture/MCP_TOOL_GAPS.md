# MCP Tool Gaps

Status: INFRASTRUCTURE / OPEN

Purpose: record missing MCP-local execution tools needed to close infrastructure loops without adding arbitrary shell access.

## Boundary

Do not add a general-purpose shell tool to satisfy these gaps. Add narrow, auditable tools with explicit input contracts, output contracts, and allowlist boundaries.

## Missing tools

### `install_python_package` / `sync_python_env`

Need: install or synchronize repository-declared Python dependencies inside the MCP virtual environment.

Required behavior:
- consume repo-managed dependency declarations such as `pyproject.toml`;
- report installed package versions;
- avoid arbitrary command execution;
- make pytest environment failures distinguishable from repo failures.

### `lean_aristotle_build_check`

Need: run the Lean/Aristotle compatibility check for the formal scaffold once Aristotle integration is explicitly configured.

Required behavior:
- report Aristotle endpoint/authentication status;
- reject proof-status promotion without a machine-check return contract;
- separate candidate Aristotle output from Lean-checked theorem status.

### `lake_build`

Need: run `lake build` on an explicit Lean project path such as `formal_lean/`.

Required behavior:
- use the project-local `lean-toolchain`;
- report toolchain, mathlib revision, build target, exit code, stdout, and stderr;
- avoid arbitrary shell execution.

### `formal_engine_status`

Need: summarize available formal-engine integrations and their proof-status boundaries.

Required behavior:
- report Lean/Lake availability;
- report Aristotle availability;
- report whether cache retrieval/build tools are enabled;
- state which outputs may or may not be recorded as CHECKED.

## Current consequence

Until these tools exist or equivalent manual runs are reported, `formal_lean/` can be committed only as an intentionally scoped scaffold. It must not be promoted to a checked formal layer merely because files are present.
