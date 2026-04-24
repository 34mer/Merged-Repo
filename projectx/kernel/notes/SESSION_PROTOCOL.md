# Session Protocol

## Start of session
1. Load INVARIANT.
2. Load STATE.
3. Load DECISIONS.
4. Load OPEN_UNKNOWNS.
5. Load TASK_GRAPH.
6. Identify current active task.

## End of session
1. Write deltas to STATE.
2. Log new decisions.
3. Log new errors.
4. Update task statuses.
5. Record unresolved tensions.

## Rule
No model session is authoritative unless it reads from and writes back to the kernel.
