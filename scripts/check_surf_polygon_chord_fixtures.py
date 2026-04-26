from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "CHK-SURF-POLYGON-CHORD-FIXTURES"
SPEC_PATH = ROOT / "formal_handoff" / "fixtures" / "surfaceology_polygon_chord_fixture_spec.json"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
REQUIRED_SOURCE_CLAIMS = {"EXT-SURF-COUNT-2023-001", "EXT-SURF-001"}
REQUIRED_STATUSES = {"GENERATED", "FINITE_GENERATED_CHORD_FIXTURE_FAMILY", "EXACT_RATIONAL_BINARY_WITNESSES", "NOT_THEOREM", "NOT_SOURCE_EXTRACTED"}
FORBIDDEN_BOUNDARY_PHRASES = [
    "surfaceology theorem",
    "full source-faithful surface curve enumeration",
    "general positive-region solver",
    "Formation Medium substrate evidence",
    "physical settling law",
    "engineering readiness",
]


@dataclass(frozen=True)
class PolygonChordFixtureResult:
    target_id: str
    checker: str
    status: str
    fixture_id: str
    inspected_files: list[str]
    support_summary: dict[str, Any]
    counterexamples: list[dict[str, Any]]
    status_boundary: str


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def internal_chords(n: int) -> list[tuple[int, int]]:
    chords: list[tuple[int, int]] = []
    for i in range(n):
        for j in range(i + 1, n):
            if (j - i) % n == 1:
                continue
            if i == 0 and j == n - 1:
                continue
            chords.append((i, j))
    return chords


def chord_crosses(a: tuple[int, int], b: tuple[int, int]) -> bool:
    a0, a1 = a
    b0, b1 = b
    if len({a0, a1, b0, b1}) < 4:
        return False
    # Endpoints strictly interleave around the cyclic order.
    return (a0 < b0 < a1 < b1) or (b0 < a0 < b1 < a1)


def crossing_edges(chords: list[tuple[int, int]]) -> frozenset[tuple[int, int]]:
    edges: set[tuple[int, int]] = set()
    for i, chord_i in enumerate(chords):
        for j, chord_j in enumerate(chords):
            if i < j and chord_crosses(chord_i, chord_j):
                edges.add((i, j))
    return frozenset(edges)


def neighbors(vertex_count: int, edges: frozenset[tuple[int, int]]) -> dict[int, set[int]]:
    out = {i: set() for i in range(vertex_count)}
    for a, b in edges:
        out[a].add(b)
        out[b].add(a)
    return out


def is_independent(vertices: set[int], edges: frozenset[tuple[int, int]]) -> bool:
    return all(not ({a, b} <= vertices) for a, b in edges)


def is_maximal_independent(vertices: set[int], vertex_count: int, edges: frozenset[tuple[int, int]]) -> bool:
    if not is_independent(vertices, edges):
        return False
    for vertex in range(vertex_count):
        if vertex not in vertices and is_independent(vertices | {vertex}, edges):
            return False
    return True


def maximal_independent_sets(vertex_count: int, edges: frozenset[tuple[int, int]]) -> list[set[int]]:
    result: list[set[int]] = []
    for bits in range(1 << vertex_count):
        vertices = {i for i in range(vertex_count) if bits & (1 << i)}
        if is_maximal_independent(vertices, vertex_count, edges):
            result.append(vertices)
    return result


def equation_lhs(vertex: int, witness: dict[int, int], neigh: dict[int, set[int]]) -> int:
    product = 1
    for other in neigh[vertex]:
        product *= witness[other]
    return witness[vertex] + product - 1


def equation_string(vertex: int, chord: tuple[int, int], chords: list[tuple[int, int]], neigh: dict[int, set[int]]) -> str:
    var = f"u_{chord[0]}_{chord[1]}"
    if not neigh[vertex]:
        product = "1"
    else:
        factors = [f"u_{chords[other][0]}_{chords[other][1]}" for other in sorted(neigh[vertex])]
        product = " * ".join(factors)
    return f"{var} + {product} - 1 = 0"


def check_spec(spec: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    statuses = set(spec.get("status", []))
    source_claims = set(spec.get("source_claim_ids", []))
    scope = spec.get("generator_scope", {})
    polygon_counts = scope.get("polygon_vertex_counts", [])
    summary = {"fixture_id": spec.get("fixture_id"), "polygon_vertex_counts": polygon_counts, "source_claim_ids": sorted(source_claims)}
    for status in REQUIRED_STATUSES:
        if status not in statuses:
            failures.append({"failure": "missing_spec_status", "status": status})
    if not REQUIRED_SOURCE_CLAIMS <= source_claims:
        failures.append({"failure": "missing_required_source_claims", "observed": sorted(source_claims), "required": sorted(REQUIRED_SOURCE_CLAIMS)})
    if polygon_counts != [4, 5, 6, 7]:
        failures.append({"failure": "unexpected_polygon_vertex_counts", "observed": polygon_counts, "expected": [4, 5, 6, 7]})
    boundary = str(spec.get("non_promotion_boundary", ""))
    for phrase in FORBIDDEN_BOUNDARY_PHRASES:
        if phrase.lower() not in boundary.lower():
            failures.append({"failure": "non_promotion_boundary_missing_phrase", "phrase": phrase})
    return failures, summary


def check_polygon_cases(spec: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    polygon_counts = spec.get("generator_scope", {}).get("polygon_vertex_counts", [])
    expected_counts = spec.get("expected_counts", {})
    total_chords = 0
    total_crossing_edges = 0
    total_witnesses = 0
    max_degree_seen = 0
    max_witness_count = 0
    case_summaries: dict[str, Any] = {}

    for n in polygon_counts:
        chords = internal_chords(n)
        edges = crossing_edges(chords)
        neigh = neighbors(len(chords), edges)
        mis_sets = maximal_independent_sets(len(chords), edges)
        degrees = {idx: len(neigh[idx]) for idx in range(len(chords))}
        max_degree = max(degrees.values(), default=0)
        total_chords += len(chords)
        total_crossing_edges += len(edges)
        total_witnesses += len(mis_sets)
        max_degree_seen = max(max_degree_seen, max_degree)
        max_witness_count = max(max_witness_count, len(mis_sets))
        key = f"n_{n}"
        case_summaries[key] = {
            "chord_count": len(chords),
            "crossing_edge_count": len(edges),
            "max_degree": max_degree,
            "maximal_noncrossing_witness_count": len(mis_sets),
            "example_chords": chords[: min(6, len(chords))],
        }

        expected_chords = int(expected_counts.get(f"n_{n}_chords", -1))
        expected_edges = int(expected_counts.get(f"n_{n}_crossing_edges", -1))
        if len(chords) != expected_chords:
            failures.append({"failure": "chord_count_mismatch", "n": n, "observed": len(chords), "expected": expected_chords})
        if len(edges) != expected_edges:
            failures.append({"failure": "crossing_edge_count_mismatch", "n": n, "observed": len(edges), "expected": expected_edges})
        if not edges:
            failures.append({"failure": "polygon_case_has_no_crossing_edges", "n": n})
        if not mis_sets:
            failures.append({"failure": "polygon_case_has_no_maximal_noncrossing_witnesses", "n": n})

        for witness_set in mis_sets:
            witness = {idx: (0 if idx in witness_set else 1) for idx in range(len(chords))}
            for idx, chord in enumerate(chords):
                lhs = equation_lhs(idx, witness, neigh)
                if lhs != 0:
                    failures.append({
                        "failure": "maximal_noncrossing_witness_fails_equation",
                        "n": n,
                        "chord_index": idx,
                        "chord": chord,
                        "equation": equation_string(idx, chord, chords, neigh),
                        "witness_zero_chords": [chords[j] for j in sorted(witness_set)],
                        "lhs": lhs,
                    })
                if witness[idx] == 0:
                    for other in neigh[idx]:
                        if witness[other] != 1:
                            failures.append({
                                "failure": "zero_chord_crossing_neighbor_not_forced_one",
                                "n": n,
                                "chord": chord,
                                "neighbor_chord": chords[other],
                                "witness_zero_chords": [chords[j] for j in sorted(witness_set)],
                            })
                if witness[idx] == 1 and neigh[idx]:
                    if all(witness[other] == 1 for other in neigh[idx]):
                        failures.append({
                            "failure": "one_chord_has_all_crossing_neighbors_one",
                            "n": n,
                            "chord": chord,
                            "witness_zero_chords": [chords[j] for j in sorted(witness_set)],
                        })

    if max_degree_seen < 4:
        failures.append({"failure": "required_high_degree_chord_not_seen", "max_degree_seen": max_degree_seen, "expected_at_least": 4})
    if case_summaries.get("n_7", {}).get("chord_count", 0) <= 10:
        failures.append({"failure": "n7_does_not_have_more_than_ten_chords", "observed": case_summaries.get("n_7", {}).get("chord_count")})

    summary: dict[str, Any] = {
        "cases": case_summaries,
        "total_polygon_cases": len(polygon_counts),
        "total_chords": total_chords,
        "total_crossing_edges": total_crossing_edges,
        "total_maximal_noncrossing_witnesses": total_witnesses,
        "max_degree_seen": max_degree_seen,
        "max_witness_count_per_polygon": max_witness_count,
    }
    return failures, summary


def run_check() -> PolygonChordFixtureResult:
    spec = read_json(SPEC_PATH)
    failures: list[dict[str, Any]] = []
    spec_failures, spec_summary = check_spec(spec)
    polygon_failures, polygon_summary = check_polygon_cases(spec)
    failures.extend(spec_failures)
    failures.extend(polygon_failures)
    support_summary = {
        **spec_summary,
        **polygon_summary,
        "checked_interface": "finite convex-polygon chord-intersection fixtures for u_chord + product_crossing_chords u = 1 with binary maximal-noncrossing witnesses",
        "allowed_inference": "polygon chord fixtures on n=4..7 pass endpoint-interleaving crossing and binary maximal-noncrossing witness checks",
        "blocked_inference": "surfaceology theorem, full source-faithful surface curve enumeration, general positive-region solver, Formation Medium substrate evidence, physical settling law, or engineering readiness",
    }
    return PolygonChordFixtureResult(
        target_id=TARGET_ID,
        checker="surf_polygon_chord_fixtures_check_v1",
        status="PASS" if not failures else "FAILED",
        fixture_id=str(spec.get("fixture_id")),
        inspected_files=["formal_handoff/fixtures/surfaceology_polygon_chord_fixture_spec.json"],
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS means only the finite convex-polygon chord fixtures for n=4..7 satisfy endpoint-interleaving crossing, "
            "maximal-noncrossing binary witness, and u-equation checks. It is not a mathematical proof of surfaceology, "
            "not full source-faithful surface curve enumeration, not a general positive-region solver, not Formation Medium "
            "substrate evidence, not a physical settling-law result, and not engineering readiness."
        ),
    )


def write_result(path: Path, result: PolygonChordFixtureResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(result), indent=2, sort_keys=True), encoding="utf-8")


def main() -> None:
    result = run_check()
    write_result(RESULT_PATH, result)
    print(json.dumps(asdict(result), indent=2, sort_keys=True))
    if result.status == "FAILED":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
