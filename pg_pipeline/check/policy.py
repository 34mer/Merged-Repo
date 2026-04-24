from __future__ import annotations

from pg_pipeline.pgcore.schemas.check_result import CheckResultRecord


def all_checks_passed(results: list[CheckResultRecord]) -> bool:
    return all(result.payload.passed for result in results)

