from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from itertools import combinations
from pathlib import Path
from typing import Iterable

TARGET_ID = "CHK-COSMO-NESTING-POSSET"

Edge = tuple[int, int]
Bracket = frozenset[int]
Bracketing = frozenset[Bracket]
StateKey = tuple[tuple[Edge, ...], tuple[tuple[int, ...], ...]]

TREE_FIXTURES: dict[str, list[Edge]] = {
    "path_2_edges": [(0, 1), (1, 2)],
    "path_3_edges": [(0, 1), (1, 2), (2, 3)],
    "path_4_edges": [(0, 1), (1, 2), (2, 3), (3, 4)],
    "claw_3_edges": [(0, 1), (0, 2), (0, 3)],
    "fork_4_edges": [(0, 1), (1, 2), (1, 3), (3, 4)],
}


@dataclass(frozen=True)
class CosmoNestingPosetCheckResult:
    target_id: str
    checker: str
    status: str
    source_rule_scope: str
    source_anchors: list[str]
    fixture_results: list[dict[str, object]]
    total_states: int
    total_delete_covers: int
    total_contract_covers: int
    total_cover_edges: int
    checked_invariants: list[str]
    counterexamples: list[dict[str, object]]
    status_boundary: str


def dense_edges(edges: Iterable[Edge]) -> list[Edge]:
    vertex_map: dict[int, int] = {}
    dense: set[Edge] = set()
    for left, right in edges:
        if left == right:
            continue
        for vertex in (left, right):
            if vertex not in vertex_map:
                vertex_map[vertex] = len(vertex_map)
        dense.add(tuple(sorted((vertex_map[left], vertex_map[right]))))
    return sorted(dense)


def contract_edges(edges: list[Edge], contracted: Bracket) -> tuple[list[Edge], dict[int, int | None]]:
    """Contract selected edge indices and return canonical quotient edges plus old->new edge map."""
    vertices = {vertex for edge in edges for vertex in edge}
    parent = {vertex: vertex for vertex in vertices}

    def find(vertex: int) -> int:
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    def union(left: int, right: int) -> None:
        root_left = find(left)
        root_right = find(right)
        if root_left != root_right:
            parent[root_right] = root_left

    for edge_index in contracted:
        left, right = edges[edge_index]
        union(left, right)

    old_to_key: dict[int, Edge | None] = {}
    quotient_keys: set[Edge] = set()
    for edge_index, (left, right) in enumerate(edges):
        root_left = find(left)
        root_right = find(right)
        if root_left == root_right:
            old_to_key[edge_index] = None
        else:
            key = tuple(sorted((root_left, root_right)))
            old_to_key[edge_index] = key
            quotient_keys.add(key)

    vertex_map: dict[int, int] = {}
    dense_key_lookup: dict[Edge, Edge] = {}
    for left, right in sorted(quotient_keys):
        for vertex in (left, right):
            if vertex not in vertex_map:
                vertex_map[vertex] = len(vertex_map)
        dense_key_lookup[(left, right)] = tuple(sorted((vertex_map[left], vertex_map[right])))

    contracted_dense = dense_edges(dense_key_lookup.values())
    dense_index = {edge: index for index, edge in enumerate(contracted_dense)}
    old_to_new: dict[int, int | None] = {}
    for edge_index, key in old_to_key.items():
        old_to_new[edge_index] = None if key is None else dense_index[dense_key_lookup[key]]
    return contracted_dense, old_to_new


def bracket_vertices(edges: list[Edge], bracket: Bracket) -> set[int]:
    vertices: set[int] = set()
    for edge_index in bracket:
        vertices.update(edges[edge_index])
    return vertices


def is_connected_edge_subset(edges: list[Edge], subset: Iterable[int]) -> bool:
    bracket = frozenset(subset)
    if not bracket:
        return False
    vertices = bracket_vertices(edges, bracket)
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    changed = True
    while changed:
        changed = False
        for edge_index in bracket:
            left, right = edges[edge_index]
            if left in seen and right not in seen:
                seen.add(right)
                changed = True
            if right in seen and left not in seen:
                seen.add(left)
                changed = True
    return seen == vertices


def connected_brackets(edges: list[Edge]) -> list[Bracket]:
    return [
        frozenset(candidate)
        for size in range(1, len(edges) + 1)
        for candidate in combinations(range(len(edges)), size)
        if is_connected_edge_subset(edges, candidate)
    ]


def brackets_compatible(edges: list[Edge], left: Bracket, right: Bracket) -> bool:
    if left <= right or right <= left:
        return True
    return bracket_vertices(edges, left).isdisjoint(bracket_vertices(edges, right))


def is_valid_bracketing(edges: list[Edge], bracketing: Bracketing) -> bool:
    if not edges:
        return bracketing == frozenset()
    full = frozenset(range(len(edges)))
    if full not in bracketing:
        return False
    if not all(is_connected_edge_subset(edges, bracket) for bracket in bracketing):
        return False
    return all(
        brackets_compatible(edges, left, right)
        for left, right in combinations(bracketing, 2)
    )


def enumerate_bracketings(edges: list[Edge]) -> list[Bracketing]:
    if not edges:
        return [frozenset()]
    full = frozenset(range(len(edges)))
    non_full_brackets = [bracket for bracket in connected_brackets(edges) if bracket != full]
    bracketings: list[Bracketing] = []
    for size in range(len(non_full_brackets) + 1):
        for selected in combinations(non_full_brackets, size):
            bracketing = frozenset(set(selected) | {full})
            if is_valid_bracketing(edges, bracketing):
                bracketings.append(bracketing)
    return bracketings


def minimal_brackets(bracketing: Bracketing) -> list[Bracket]:
    return [bracket for bracket in bracketing if not any(other < bracket for other in bracketing)]


def image_bracket(bracket: Bracket, old_to_new: dict[int, int | None]) -> Bracket:
    return frozenset(
        mapped
        for edge_index in bracket
        for mapped in [old_to_new[edge_index]]
        if mapped is not None
    )


def contract_bracketing(edges: list[Edge], bracketing: Bracketing, minimal: Bracket) -> tuple[list[Edge], Bracketing]:
    contracted_edges, old_to_new = contract_edges(edges, minimal)
    image: set[Bracket] = set()
    for bracket in bracketing:
        mapped = image_bracket(bracket, old_to_new)
        if mapped:
            image.add(mapped)
    return contracted_edges, frozenset(image)


def state_key(edges: list[Edge], bracketing: Bracketing) -> StateKey:
    return (
        tuple(edges),
        tuple(sorted((tuple(sorted(bracket)) for bracket in bracketing), key=lambda item: (len(item), item))),
    )


def state_complexity(key: StateKey) -> int:
    edges, bracketing = key
    return len(edges) + len(bracketing)


def graph_contractions(edges: list[Edge]) -> list[list[Edge]]:
    contractions: dict[tuple[Edge, ...], list[Edge]] = {}
    for size in range(len(edges) + 1):
        for contracted in combinations(range(len(edges)), size):
            contracted_edges, _old_to_new = contract_edges(edges, frozenset(contracted))
            if contracted_edges:
                contractions[tuple(contracted_edges)] = contracted_edges
    return list(contractions.values())


def all_prebracketing_states(original_edges: list[Edge]) -> dict[StateKey, tuple[list[Edge], Bracketing]]:
    states: dict[StateKey, tuple[list[Edge], Bracketing]] = {}
    for edges in graph_contractions(original_edges):
        for bracketing in enumerate_bracketings(edges):
            states[state_key(edges, bracketing)] = (edges, bracketing)
    return states


def cover_edges(states: dict[StateKey, tuple[list[Edge], Bracketing]]) -> list[tuple[StateKey, StateKey, str]]:
    covers: list[tuple[StateKey, StateKey, str]] = []
    state_set = set(states)
    for upper_key, (edges, bracketing) in states.items():
        full = frozenset(range(len(edges)))
        for bracket in bracketing:
            if bracket == full:
                continue
            lower_bracketing = frozenset(set(bracketing) - {bracket})
            if is_valid_bracketing(edges, lower_bracketing):
                lower_key = state_key(edges, lower_bracketing)
                if lower_key in state_set:
                    covers.append((upper_key, lower_key, "delete_bracket"))
        for minimal in minimal_brackets(bracketing):
            contracted_edges, contracted_bracketing = contract_bracketing(edges, bracketing, minimal)
            if not contracted_edges:
                continue
            if is_valid_bracketing(contracted_edges, contracted_bracketing):
                lower_key = state_key(contracted_edges, contracted_bracketing)
                if lower_key in state_set:
                    covers.append((upper_key, lower_key, "contract_minimal_bracket"))
    return covers


def reachable_pairs(nodes: set[StateKey], covers: list[tuple[StateKey, StateKey, str]]) -> set[tuple[StateKey, StateKey]]:
    adjacency: dict[StateKey, list[StateKey]] = {node: [] for node in nodes}
    for upper, lower, _kind in covers:
        adjacency[upper].append(lower)
    reach: set[tuple[StateKey, StateKey]] = set()
    for start in nodes:
        stack = list(adjacency[start])
        seen: set[StateKey] = set()
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            reach.add((start, node))
            stack.extend(adjacency[node])
    return reach


def check_fixture(name: str, edges: list[Edge]) -> tuple[dict[str, object], list[dict[str, object]]]:
    states = all_prebracketing_states(edges)
    covers = cover_edges(states)
    nodes = set(states)
    failures: list[dict[str, object]] = []

    delete_count = sum(1 for _upper, _lower, kind in covers if kind == "delete_bracket")
    contract_count = sum(1 for _upper, _lower, kind in covers if kind == "contract_minimal_bracket")

    for upper, lower, kind in covers:
        upper_complexity = state_complexity(upper)
        lower_complexity = state_complexity(lower)
        if lower_complexity >= upper_complexity:
            failures.append(
                {
                    "tree": name,
                    "failure": "cover_does_not_reduce_complexity",
                    "kind": kind,
                    "upper_complexity": upper_complexity,
                    "lower_complexity": lower_complexity,
                }
            )

    reach = reachable_pairs(nodes, covers)
    for node in nodes:
        if (node, node) in reach:
            failures.append({"tree": name, "failure": "cycle_detected", "state": str(node)})
            break
    for left, right in reach:
        if (right, left) in reach:
            failures.append({"tree": name, "failure": "antisymmetry_violation"})
            break

    if delete_count == 0:
        failures.append({"tree": name, "failure": "no_delete_bracket_covers"})
    if contract_count == 0:
        failures.append({"tree": name, "failure": "no_contract_minimal_bracket_covers"})

    summary = {
        "tree": name,
        "edge_count": len(edges),
        "state_count": len(states),
        "cover_count": len(covers),
        "delete_cover_count": delete_count,
        "contract_cover_count": contract_count,
        "reachable_pair_count": len(reach),
        "acyclic": not any(f["failure"] == "cycle_detected" for f in failures),
        "antisymmetric_transitive_closure": not any(f["failure"] == "antisymmetry_violation" for f in failures),
        "all_covers_reduce_complexity": not any(f["failure"] == "cover_does_not_reduce_complexity" for f in failures),
    }
    return summary, failures


def run_check(fixtures: dict[str, list[Edge]] = TREE_FIXTURES) -> CosmoNestingPosetCheckResult:
    fixture_results: list[dict[str, object]] = []
    counterexamples: list[dict[str, object]] = []
    for name, edges in fixtures.items():
        summary, failures = check_fixture(name, edges)
        fixture_results.append(summary)
        counterexamples.extend(failures)

    total_states = sum(int(result["state_count"]) for result in fixture_results)
    total_delete_covers = sum(int(result["delete_cover_count"]) for result in fixture_results)
    total_contract_covers = sum(int(result["contract_cover_count"]) for result in fixture_results)
    total_cover_edges = sum(int(result["cover_count"]) for result in fixture_results)

    return CosmoNestingPosetCheckResult(
        target_id=TARGET_ID,
        checker="finite_prebracketing_poset_consistency_v1",
        status="PASS_PARTIAL" if not counterexamples else "FAILED",
        source_rule_scope="Finite pre-bracketing/bracketed-tree consistency check for the source-stated Matryoshka/bracketed-tree poset. It verifies that delete-bracket and contract-minimal-bracket cover rules generate an acyclic finite poset on selected small tree fixtures. It does not prove the full Matryoshka face-lattice anti-isomorphism.",
        source_anchors=[
            "COSMO_COMB_2026: Definition 2.1 Matryoshka poset by containment with maximum element",
            "COSMO_COMB_2026: Theorem 2.4 order-preserving bijection from Matryoshkas to cosmohedral fan face lattice",
            "COSMO_COMB_2026: Lemma 2.10 Matryoshka <-> bracketed-tree bijection",
            "COSMO_COMB_2026: Proposition 2.13 bracketed-tree poset isomorphic to Matryoshka lattice",
            "COSMO_COMB_2026: Proposition 3.2 pre-bracketings ordered by deletion/contraction biject to positive bracket associahedral fan faces",
        ],
        fixture_results=fixture_results,
        total_states=total_states,
        total_delete_covers=total_delete_covers,
        total_contract_covers=total_contract_covers,
        total_cover_edges=total_cover_edges,
        checked_invariants=[
            "generated covers land in valid finite pre-bracketing states",
            "delete-bracket and contract-minimal-bracket covers both occur in every nontrivial fixture",
            "each cover strictly decreases the finite state complexity edge_count + bracket_count",
            "the directed cover graph is acyclic",
            "the transitive closure is antisymmetric",
        ],
        counterexamples=counterexamples,
        status_boundary="PASS_PARTIAL finite consistency evidence for CHK-COSMO-NESTING-POSSET. This is not full source-range extraction, not an all-n theorem, and not a proof of the cosmohedron face lattice; it is a finite falsifiable guard for the bracketed-tree/Matryoshka nesting-poset machinery.",
    )


def write_result(path: Path, result: CosmoNestingPosetCheckResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(result), indent=2, sort_keys=True), encoding="utf-8")


def main() -> None:
    result = run_check()
    write_result(Path("formal_handoff/results/CHK-COSMO-NESTING-POSSET.json"), result)
    print(json.dumps(asdict(result), indent=2, sort_keys=True))
    if result.status == "FAILED":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
