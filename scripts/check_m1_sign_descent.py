from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from itertools import combinations
from pathlib import Path
from typing import Iterable

TARGET_ID = "CHK-M1-SIGN-DESCENT"
DEFAULT_N_RANGE = range(3, 10)

SignFlipSet = frozenset[int]


@dataclass(frozen=True)
class M1SignDescentCheckResult:
    target_id: str
    checker: str
    status: str
    model_scope: str
    source_anchors: list[str]
    n_range: list[int]
    grading: str
    cover_relation: str
    per_n: list[dict[str, int | bool]]
    counterexamples: list[dict[str, object]]
    status_boundary: str


def all_flip_sets(n: int) -> list[SignFlipSet]:
    if n < 2:
        raise ValueError("sign-flip word model requires n >= 2")
    edges = range(n - 1)
    return [frozenset(candidate) for r in range(n) for candidate in combinations(edges, r)]


def sign_word_from_flip_set(n: int, flips: SignFlipSet) -> tuple[int, ...]:
    """Fix global sign by setting the first sign to +1."""
    signs = [1]
    for edge in range(n - 1):
        next_sign = -signs[-1] if edge in flips else signs[-1]
        signs.append(next_sign)
    return tuple(signs)


def flip_set_from_sign_word(signs: tuple[int, ...]) -> SignFlipSet:
    if not signs or signs[0] != 1:
        raise ValueError("sign word must be global-sign normalized with first sign +1")
    if any(sign not in {-1, 1} for sign in signs):
        raise ValueError("sign word entries must be +/-1")
    return frozenset(i for i in range(len(signs) - 1) if signs[i] != signs[i + 1])


def cover_edges_by_one_flip_change(states: list[SignFlipSet]) -> list[tuple[SignFlipSet, SignFlipSet]]:
    state_set = set(states)
    covers: list[tuple[SignFlipSet, SignFlipSet]] = []
    for lower in states:
        for edge in range(max((max(state) for state in states if state), default=-1) + 2):
            upper = frozenset(set(lower) | {edge})
            if edge not in lower and upper in state_set and len(upper) == len(lower) + 1:
                covers.append((lower, upper))
    return covers


def check_n(n: int) -> tuple[dict[str, int | bool], list[dict[str, object]]]:
    states = all_flip_sets(n)
    covers = cover_edges_by_one_flip_change(states)
    failures: list[dict[str, object]] = []

    sign_words = {sign_word_from_flip_set(n, flips) for flips in states}
    roundtrip_ok = all(flip_set_from_sign_word(sign_word_from_flip_set(n, flips)) == flips for flips in states)
    if len(sign_words) != len(states):
        failures.append({"n": n, "failure": "flip_sets_do_not_biject_to_global_sign_normalized_words"})
    if not roundtrip_ok:
        failures.append({"n": n, "failure": "sign_word_roundtrip_failed"})

    for lower, upper in covers:
        rank_delta = len(upper) - len(lower)
        symmetric_difference_size = len(lower ^ upper)
        if rank_delta != 1 or symmetric_difference_size != 1:
            failures.append(
                {
                    "n": n,
                    "failure": "non_unit_sign_descent_cover",
                    "lower": sorted(lower),
                    "upper": sorted(upper),
                    "rank_delta": rank_delta,
                    "symmetric_difference_size": symmetric_difference_size,
                }
            )

    expected_state_count = 2 ** (n - 1)
    expected_cover_count = (n - 1) * (2 ** (n - 2))
    if len(states) != expected_state_count:
        failures.append({"n": n, "failure": "state_count_mismatch", "observed": len(states), "expected": expected_state_count})
    if len(covers) != expected_cover_count:
        failures.append({"n": n, "failure": "cover_count_mismatch", "observed": len(covers), "expected": expected_cover_count})

    summary = {
        "n": n,
        "edge_count": n - 1,
        "state_count": len(states),
        "expected_state_count": expected_state_count,
        "cover_count": len(covers),
        "expected_cover_count": expected_cover_count,
        "max_rank": max(len(state) for state in states),
        "expected_max_rank": n - 1,
        "all_covers_unit_flip_delta": not any(f.get("failure") == "non_unit_sign_descent_cover" for f in failures),
        "global_sign_normalized_word_bijection": len(sign_words) == len(states) and roundtrip_ok,
    }
    return summary, failures


def run_check(n_range: Iterable[int] = DEFAULT_N_RANGE) -> M1SignDescentCheckResult:
    per_n: list[dict[str, int | bool]] = []
    failures: list[dict[str, object]] = []
    for n in n_range:
        summary, local_failures = check_n(n)
        per_n.append(summary)
        failures.extend(local_failures)

    return M1SignDescentCheckResult(
        target_id=TARGET_ID,
        checker="finite_global_sign_normalized_sign_flip_poset_v1",
        status="PASS_PARTIAL" if not failures else "FAILED",
        model_scope="Finite binary sign-flip stratum model: sign words are global-sign normalized by fixing the first sign to +1 and encoded by adjacent sign-change subsets. Covers add exactly one adjacent sign-change edge. This checks the declared sign-flip descent spine only, not the full amplituhedron geometry.",
        source_anchors=[
            "AMP_2013 / BINARY_AMP_2017: amplituhedron sign-flip/binary characterization is carried as source motivation for a finite sign-vector descent model",
            "FORMAL_CHECK_TARGETS.json: CHK-M1-SIGN-DESCENT predicate and failure condition",
        ],
        n_range=[int(n) for n in n_range],
        grading="rank(sign_flip_set)=number_of_adjacent_sign_changes",
        cover_relation="lower < upper when upper is obtained from lower by adding exactly one adjacent sign-change edge",
        per_n=per_n,
        counterexamples=failures,
        status_boundary="PASS_PARTIAL finite sign-vector check only. This validates the internal unit-descent behavior of the declared binary sign-flip model; it is not a full amplituhedron theorem, not an all-geometry proof, and not a C/M1 comparator result.",
    )


def write_result(path: Path, result: M1SignDescentCheckResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(result), indent=2, sort_keys=True), encoding="utf-8")


def main() -> None:
    result = run_check()
    write_result(Path("formal_handoff/results/CHK-M1-SIGN-DESCENT.json"), result)
    print(json.dumps(asdict(result), indent=2, sort_keys=True))
    if result.status == "FAILED":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
