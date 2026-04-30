# Worm Migration Test Result

Targeted test run:

```text
python -m pytest tests/test_wormsim_migration.py -q
```

Result:

```text
3 passed, 1 warning in 2.22s
```

The warning was a pytest cache write permission warning for `.pytest_cache` in the MCP runner and did not affect the migration tests.
