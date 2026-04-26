from __future__ import annotations

import itertools
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TARGET_ID = "CHK-SURF-GENERATED-GRAPH-FIXTURES"
SPEC_PATH = ROOT / "formal_handoff" / "fixtures" / "surfaceology_generated_graph_fixture_spec.json"
RESULT_PATH = ROOT / "formal_handoff" / "results" / f"{TARGET_ID}.json"
REQUIRED_SOURCE_CLAIMS = {"EXT-SURF-COUNT-2023-001", "EXT-SURF-001"}
REQUIRED_STATUSES = {"GENERATED", "FINITE_GENERATED_FIXTURE_FAMILY", "EXACT_RATIONAL_BINARY_WITNESSES", "NOT_THEOREM", "NOT_SOURCE_EXTRACTED"}
FORBIDDEN_BOUNDARY_PHRASES = [
    "surfaceology theorem",
    "general positive-region solver",
    "Formation Medium substrate evidence",
    "physical settling law",
    "engineering readiness",
]


@dataclass(frozen=True)
class GeneratedGraphFixtureResult:
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


def all_edges(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def graph_from_mask(n: int, mask: int) -> frozenset[tuple[int, int]]:
    edges = all_edges(n)
    return frozenset(edge for bit, edge in enumerate(edges) if mask & (1 << bit))


def neighbors(n: int, graph: frozenset[tuple[int, int]]) -> dict[int, set[int]]:
    out = {i: set() for i in range(n)}
    for a, b in graph:
        out[a].add(b)
        out[b].add(a)
    return out


def is_independent(vertices: set[int], graph: frozenset[tuple[int, int]]) -> bool:
    return all(not ({a, b} <= vertices) for a, b in graph)


def is_maximal_independent(vertices: set[int], n: int, graph: frozenset[tuple[int, int]]) -> bool:
    if not is_independent(vertices, graph):
        return False
    for v in range(n):
        if v not in vertices and is_independent(vertices | {v}, graph):
            return False
    return True


def maximal_independent_sets(n: int, graph: frozenset[tuple[int, int]]) -> list[set[int]]:
    sets: list[set[int]] = []
    for bits in range(1 << n):
        vertices = {i for i in range(n) if bits & (1 << i)}
        if is_maximal_independent(vertices, n, graph):
            sets.append(vertices)
    return sets


def connected_components(n: int, graph: frozenset[tuple[int, int]]) -> list[set[int]]:
    neigh = neighbors(n, graph)
    unseen = set(range(n))
    comps: list[set[int]] = []
    while unseen:
        root = unseen.pop()
        comp = {root}
        stack = [root]
        while stack:
            v = stack.pop()
            for w in neigh[v]:
                if w in unseen:
                    unseen.remove(w)
                    comp.add(w)
                    stack.append(w)
        comps.append(comp)
    return comps


def equation_lhs(vertex: int, witness: dict[int, int], neigh: dict[int, set[int]]) -> int:
    product = 1
    for w in neigh[vertex]:
        product *= witness[w]
    return witness[vertex] + product - 1


def equation_string(vertex: int, neigh: dict[int, set[int]]) -> str:
    variable = f"u_{vertex}"
    if not neigh[vertex]:
        product = "1"
    else:
        product = " * ".join(f"u_{w}" for w in sorted(neigh[vertex]))
    return f"{variable} + {product} - 1 = 0"


def check_spec(spec: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    statuses = set(spec.get("status", []))
    source_claims = set(spec.get("source_claim_ids", []))
    scope = spec.get("generator_scope", {})
    vertex_counts = scope.get("vertex_counts", [])
    summary = {"fixture_id": spec.get("fixture_id"), "vertex_counts": vertex_counts, "source_claim_ids": sorted(source_claims)}
    for status in REQUIRED_STATUSES:
        if status not in statuses:
            failures.append({"failure": "missing_spec_status", "status": status})
    if not REQUIRED_SOURCE_CLAIMS <= source_claims:
        failures.append({"failure": "missing_required_source_claims", "observed": sorted(source_claims), "required": sorted(REQUIRED_SOURCE_CLAIMS)})
    if vertex_counts != [1, 2, 3, 4]:
        failures.append({"failure": "unexpected_vertex_counts", "observed": vertex_counts, "expected": [1, 2, 3, 4]})
    boundary = str(spec.get("non_promotion_boundary", ""))
    for phrase in FORBIDDEN_BOUNDARY_PHRASES:
        if phrase.lower() not in boundary.lower():
            failures.append({"failure": "non_promotion_boundary_missing_phrase", "phrase": phrase})
    return failures, summary


def check_generated_graphs(spec: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    failures: list[dict[str, Any]] = []
    vertex_counts = spec.get("generator_scope", {}).get("vertex_counts", [])
    expected_counts = spec.get("expected_global_counts", {})
    per_n_counts: dict[str, int] = {}
    total_graphs = 0
    total_witnesses = 0
    max_witness_count = 0
    max_degree_seen = 0
    feature_flags = {
        "has_isolated_vertex_graph": False,
        "has_disconnected_graph": False,
        "has_triangle_graph": False,
        "has_degree_at_least_3_graph": False,
        "has_graph_with_multiple_maximal_independent_sets": False,
    }
    examples: dict[str, Any] = {}

    for n in vertex_counts:
        graph_count = 0
        for mask in range(1 << len(all_edges(n))):
            graph = graph_from_mask(n, mask)
            neigh = neighbors(n, graph)
            graph_count += 1
            total_graphs += 1
            degrees = {v: len(neigh[v]) for v in range(n)}
            graph_max_degree = max(degrees.values(), default=0)
            max_degree_seen = max(max_degree_seen, graph_max_degree)
            components = connected_components(n, graph)
            mis_sets = maximal_independent_sets(n, graph)
            total_witnesses += len(mis_sets)
            max_witness_count = max(max_witness_count, len(mis_sets))

            if any(degree == 0 for degree in degrees.values()):
                feature_flags["has_isolated_vertex_graph"] = True
                examples.setdefault("isolated_vertex_graph", {"n": n, "edges": sorted(graph)})
            if len(components) > 1:
                feature_flags["has_disconnected_graph"] = True
                examples.setdefault("disconnected_graph", {"n": n, "edges": sorted(graph), "components": [sorted(c) for c in components]})
            if n >= 3 and all(tuple(sorted(edge)) in graph for edge in [(0, 1), (0, 2), (1, 2)]):
                feature_flags["has_triangle_graph"] = True
                examples.setdefault("triangle_graph", {"n": n, "edges": sorted(graph)})
            if graph_max_degree >= 3:
                feature_flags["has_degree_at_least_3_graph"] = True
                examples.setdefault("degree_at_least_3_graph", {"n": n, "edges": sorted(graph), "degrees": degrees})
            if len(mis_sets) > 1:
                feature_flags["has_graph_with_multiple_maximal_independent_sets"] = True
                examples.setdefault("multiple_mis_graph", {"n": n, "edges": sorted(graph), "mis_sets": [sorted(s) for s in mis_sets]})

            if not mis_sets:
                failures.append({"failure": "graph_has_no_maximal_independent_set", "n": n, "mask": mask})
            for witness_set in mis_sets:
                witness = {v: (0 if v in witness_set else 1) for v in range(n)}
                for v in range(n):
                    lhs = equation_lhs(v, witness, neigh)
                    if lhs != 0:
                        failures.append({"failure": "maximal_independent_witness_fails_equation", "n": n, "mask": mask, "vertex": v, "witness_zero_set": sorted(witness_set), "equation": equation_string(v, neigh), "lhs": lhs})
                    if witness[v] == 0:
                        for w in neigh[v]:
                            if witness[w] != 1:
                                failures.append({"failure": "zero_vertex_neighbor_not_forced_one", "n": n, "mask": mask, "zero_vertex": v, "neighbor": w, "witness_zero_set": sorted(witness_set)})
                    if witness[v] == 1 and neigh[v]:
                        if all(witness[w] == 1 for w in neigh[v]):
                            failures.append({"failure": "one_vertex_has_all_neighbors_one", "n": n, "mask": mask, "vertex": v, "witness_zero_set": sorted(witness_set)})
        per_n_counts[f"n_{n}_graphs"] = graph_count
        expected = int(expected_counts.get(f"n_{n}_graphs", -1))
        if graph_count != expected:
            failures.append({"failure": "per_n_graph_count_mismatch", "n": n, "observed": graph_count, "expected": expected})

    if total_graphs != int(expected_counts.get("total_graphs", -1)):
        failures.append({"failure": "total_graph_count_mismatch", "observed": total_graphs, "expected": expected_counts.get("total_graphs")})
    for flag, observed in feature_flags.items():
        if not observed:
            failures.append({"failure": "missing_required_generated_feature", "feature": flag})

    summary: dict[str, Any] = {
        **per_n_counts,
        "total_graphs": total_graphs,
        "total_maximal_independent_witnesses": total_witnesses,
        "max_witness_count_per_graph": max_witness_count,
        "max_degree_seen": max_degree_seen,
        **feature_flags,
        "examples": examples,
    }
    return failures, summary


def run_check() -> GeneratedGraphFixtureResult:
    spec = read_json(SPEC_PATH)
    failures: list[dict[str, Any]] = []
    spec_failures, spec_summary = check_spec(spec)
    graph_failures, graph_summary = check_generated_graphs(spec)
    failures.extend(spec_failures)
    failures.extend(graph_failures)
    support_summary = {
        **spec_summary,
        **graph_summary,
        "checked_interface": "generated finite simple-graph crossing abstractions for u_v + product_neighbors u_w = 1 with binary maximal-independent-set witnesses",
        "allowed_inference": "all simple graphs on 1..4 vertices pass the declared binary witness equation checks",
        "blocked_inference": "surfaceology theorem, general positive-region solver, Formation Medium substrate evidence, physical settling law, or engineering readiness",
    }
    return GeneratedGraphFixtureResult(
        target_id=TARGET_ID,
        checker="surf_generated_graph_fixtures_check_v1",
        status="PASS" if not failures else "FAILED",
        fixture_id=str(spec.get("fixture_id")),
        inspected_files=["formal_handoff/fixtures/surfaceology_generated_graph_fixture_spec.json"],
        support_summary=support_summary,
        counterexamples=failures,
        status_boundary=(
            "PASS means only the generated finite simple-graph fixtures on 1..4 vertices satisfy the declared binary "
            "maximal-independent-set witness checks for u_v + product_neighbors u_w = 1. It is not a mathematical proof of "
            "surfaceology, not a general positive-region solver, not Formation Medium substrate evidence, not a physical "
            "settling-law result, and not engineering readiness."
        ),
    )


def write_result(path: Path, result: GeneratedGraphFixtureResult) -> None:
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
