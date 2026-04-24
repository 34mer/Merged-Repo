from __future__ import annotations

import json
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from typing import Iterable

TARGET_ID = "CHK-ASSOCIAHEDRON-UNIT-DESCENT"
DEFAULT_N_RANGE = range(4, 9)

Diagonal = tuple[int, int]
Face = frozenset[Diagonal]


@dataclass(frozen=True)
class AssociahedronCheckResult:
    target_id: str
    checker: str
    status: str
    n_range: list[int]
    grading: str
    cover_relation: str
    per_n: list[dict[str, int | bool]]
    counterexamples: list[dict[str, object]]


def normalize_diagonal(i: int, j: int) -> Diagonal:
    if i == j:
        raise ValueError("diagonal endpoints must be distinct")
    return (i, j) if i < j else (j, i)


def is_boundary_edge(n: int, d: Diagonal) -> bool:
    i, j = d
    return (j - i) % n == 1 or (i == 0 and j == n - 1)


def polygon_diagonals(n: int) -> list[Diagonal]:
    if n < 4:
        raise ValueError("associahedron baseline starts at n >= 4")
    return [
        normalize_diagonal(i, j)
        for i, j in combinations(range(n), 2)
        if not is_boundary_edge(n, normalize_diagonal(i, j))
    ]


def strictly_between_cyclic(a: int, x: int, b: int, n: int) -> bool:
    if a < b:
        return a < x < b
    return x > a or x < b


def diagonals_cross(n: int, d1: Diagonal, d2: Diagonal) -> bool:
    a, b = d1
    c, d = d2
    if len({a, b, c, d}) < 4:
        return False
    c_between = strictly_between_cyclic(a, c, b, n)
    d_between = strictly_between_cyclic(a, d, b, n)
    return c_between != d_between


def is_noncrossing(n: int, face: Iterable[Diagonal]) -> bool:
    ds = list(face)
    return all(not diagonals_cross(n, d1, d2) for d1, d2 in combinations(ds, 2))


def noncrossing_faces(n: int) -> list[Face]:
    diagonals = polygon_diagonals(n)
    faces: list[Face] = []
    for size in range(len(diagonals) + 1):
        for candidate in combinations(diagonals, size):
            if is_noncrossing(n, candidate):
                faces.append(frozenset(candidate))
    return faces


def cover_edges_by_single_chord_addition(faces: list[Face]) -> list[tuple[Face, Face]]:
    covers: list[tuple[Face, Face]] = []
    for face in faces:
        for other in faces:
            if len(other) == len(face) + 1 and face < other and len(other - face) == 1:
                covers.append((face, other))
    return covers


def check_n(n: int) -> tuple[dict[str, int | bool], list[dict[str, object]]]:
    faces = noncrossing_faces(n)
    covers = cover_edges_by_single_chord_addition(faces)
    counterexamples: list[dict[str, object]] = []
    for lower, upper in covers:
        rank_delta = len(upper) - len(lower)
        if rank_delta != 1:
            counterexamples.append({"n": n, "lower": sorted(lower), "upper": sorted(upper), "rank_delta": rank_delta})
    expected_max_rank = n - 3
    max_rank = max((len(face) for face in faces), default=0)
    summary = {
        "n": n,
        "diagonal_count": len(polygon_diagonals(n)),
        "face_count": len(faces),
        "cover_count": len(covers),
        "max_rank": max_rank,
        "expected_max_rank": expected_max_rank,
        "all_covers_unit_rank": len(counterexamples) == 0,
        "has_triangulation_top_rank": any(len(face) == expected_max_rank for face in faces),
    }
    if max_rank != expected_max_rank:
        counterexamples.append({"n": n, "failure": "max_rank_mismatch", "max_rank": max_rank, "expected_max_rank": expected_max_rank})
    return summary, counterexamples


def run_check(n_range: Iterable[int] = DEFAULT_N_RANGE) -> AssociahedronCheckResult:
    per_n: list[dict[str, int | bool]] = []
    counterexamples: list[dict[str, object]] = []
    for n in n_range:
        summary, failures = check_n(n)
        per_n.append(summary)
        counterexamples.extend(failures)
    return AssociahedronCheckResult(
        target_id=TARGET_ID,
        checker="finite_noncrossing_chord_poset_v1",
        status="PASS" if not counterexamples else "FAILED",
        n_range=[int(n) for n in n_range],
        grading="rank(face)=number_of_noncrossing_diagonals",
        cover_relation="face < face_plus_one_diagonal by strict inclusion with exactly one added noncrossing diagonal",
        per_n=per_n,
        counterexamples=counterexamples,
    )


def write_result(path: Path, result: AssociahedronCheckResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result.__dict__, indent=2, sort_keys=True), encoding="utf-8")


def main() -> None:
    result = run_check()
    write_result(Path("formal_handoff/results/CHK-ASSOCIAHEDRON-UNIT-DESCENT.json"), result)
    print(json.dumps(result.__dict__, indent=2, sort_keys=True))
    if result.status != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
