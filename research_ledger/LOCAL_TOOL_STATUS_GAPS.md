# Local Tool Status Gaps

STATUS: GENERATED / OPEN  
PURPOSE: Record local tool/workstation gaps observed during Formation Medium repo work so broken or insufficient tools do not silently degrade the workflow.

## 1. Current Working Tools

Observed available through `local_tool_status`:

- Python: available
- Git: available
- Z3 CLI: available
- Python `z3`: import available
- Lean / Lake / Elan: available, though reported Lean/Lake are currently newer than the Aristotle pin target and should be checked with project pin tools before use
- PyYAML / pypdf: available

## 2. Blocked / Degraded Tools

### TG-001 — Sage via WSL blocked

Observed state:

```text
sage_configured command: wsl sage
result: WSL has no installed distributions
```

Impact:

- Sage-backed checks cannot be trusted as available.
- Do not mark Sage checks as run until WSL distro + Sage are installed/configured or a native Sage path is exposed.

Required action:

- Install/configure a WSL distro with Sage, or expose a native Sage command.
- Re-run `sage_status` before using Sage-based check results.

Status:

```text
OPEN / LOCAL_TOOL_GAP
```

### TG-002 — polymake via WSL blocked

Observed state:

```text
polymake_configured command: wsl polymake
result: WSL has no installed distributions
```

Impact:

- polymake-backed polytope checks cannot be trusted as available.
- Do not mark polymake checks as run until WSL distro + polymake are installed/configured or a native polymake path is exposed.

Required action:

- Install/configure a WSL distro with polymake, or expose a native polymake command.
- Re-run `polymake_status` before using polymake-based check results.

Status:

```text
OPEN / LOCAL_TOOL_GAP
```

### TG-003 — MCP restart required for server-side tool fixes

Observed patch:

- `formation-mcp/server.py` was patched so `run_cmd` handles `None` stdout/stderr safely.
- `formation-mcp/server.py` validator allowlist was patched to include `validate_formation_medium_discipline.py`.
- `py_compile server.py` passed.
- `agent_self_check` passed.

Impact:

- The currently running MCP process may not expose the patched behavior until restart.
- `run_validator("validate_formation_medium_discipline.py")` may remain unavailable until restart even though the repo script itself passes directly.

Required action:

- Restart the MCP server process from `formation-mcp`.
- After restart, re-run:

```text
agent_self_check
run_validator("validate_formation_medium_discipline.py")
run_all_validators
run_all_tests
```

Status:

```text
OPEN / RESTART_REQUIRED
```

## 3. Non-Promotion Rule

Tool availability is not proof. A checker result may be recorded only when the relevant local tool is available, the command actually ran, and the result artifact is present.

Do not mark Sage, polymake, or restarted-MCP-dependent checks as run until their statuses are re-verified.
