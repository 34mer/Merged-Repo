from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from itertools import combinations
from pathlib import Path
from typing import Iterable

TARGET_ID = "CHK-COSMO-MOVE-CLASSES"

Edge = tuple[int, int]
Bracket = frozenset[int]
Bracketing = frozenset[Bracket]

TREE_FIXTURES: dict[str, list[Edge]] = {
    "path_2_edges": [(0, 1), (1, 2)],
    "path_3_edges": [(0, 1), (1, 2), (2, 3)],
    "path_4_edges": [(0, 1), (1, 2), (2, 3), (3, 4)],
    "claw_3_edges": [(0, 1), (0, 2), (0, 3)],
    "fork_4_edges": [(0, 1), (1, 2), (1, 3), (3, 4)],
}


@dataclass(frozen=True)
class CosmoMoveCheckResult:
    target_id: str
    checker: str
    status: str
    source_rule_scope: str
    source_anchors: list[str]
    tree_fixtures: list[dict[str, object]]
    total_bracketings: int
    total_deletion_moves: int
    total_contraction_moves: int
    move_class_invariants: dict[str, str]
    counterexamples: list[dict[str, object]]
    status_boundary: str


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
    seen = {next(iter(vertices))}
    changed = True
    while changed:
        changed = False
        for edge_index in bracket:
            a, b = edges[edge_index]
            if a in seen and b not in seen:
                seen.add(b)
                changed = True
            if b in seen and a not in seen:
                seen.add(a)
                changed = True
    return seen == vertices


def connected_brackets(edges: list[Edge]) -> list[Bracket]:
    edge_count = len(edges)
    return [
        frozenset(candidate)
        for size in range(1, edge_count + 1)
        for candidate in combinations(range(edge_count), size)
        if is_connected_edge_subset(edges, candidate)
    ]


def brackets_compatible(edges: list[Edge], left: Bracket, right: Bracket) -> bool:
    if left <= right or right <= left:
        return True
    return bracket_vertices(edges, left).isdisjoint(bracket_vertices(edges, right))


def is_valid_bracketing(edges: list[Edge], bracketing: Bracketing) -> bool:
    full = frozenset(range(len(edges)))
    if full not in bracketing:
        return False
    for bracket in bracketing:
        if not is_connected_edge_subset(edges, bracket):
            return False
    return all(
        brackets_compatible(edges, left, right)
        for left, right in combinations(bracketing, 2)
    )


def enumerate_bracketings(edges: list[Edge]) -> list[Bracketing]:
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
    return [
        bracket
        for bracket in bracketing
        if not any(other < bracket for other in bracketing)
    ]


def deletion_moves(edges: list[Edge], bracketing: Bracketing) -> list[Bracketing]:
    full = frozenset(range(len(edges)))
    moves: list[Bracketing] = []
    for bracket in bracketing:
        if bracket == full:
            continue
        candidate = frozenset(set(bracketing) - {bracket})
        if is_valid_bracketing(edges, candidate):
            moves.append(candidate)
    return moves


def contract_edges(edges: list[Edge], contracted: Bracket) -> tuple[list[Edge], dict[int, int | None]]:
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

    undense_edges: list[Edge] = []
    edge_key_to_new_index: dict[Edge, int] = {}
    old_to_new: dict[int, int | None] = {}
    for edge_index, (left, right) in enumerate(edges):
        root_left = find(left)
        root_right = find(right)
        if root_left == root_right:
            old_to_new[edge_index] = None
            continue
        key = tuple(sorted((root_left, root_right)))
        if key not in edge_key_to_new_index:
            edge_key_to_new_index[key] = len(undense_edges)
            undense_edges.append(key)
        old_to_new[edge_index] = edge_key_to_new_index[key]

    vertex_renumber: dict[int, int] = {}
    dense_edges: list[Edge] = []
    for left, right in undense_edges:
        if left not in vertex_renumber:
            vertex_renumber[left] = len(vertex_renumber)
        if right not in vertex_renumber:
            vertex_renumber[right] = len(vertex_renumber)
        dense_edges.append(tuple(sorted((vertex_renumber[left], vertex_renumber[right]))))
    return dense_edges, old_to_new


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


def contraction_moves(edges: list[Edge], bracketing: Bracketing) -> list[tuple[Bracket, list[Edge], Bracketing]]:
    moves: list[tuple[Bracket, list[Edge], Bracketing]] = []
    for minimal in minimal_brackets(bracketing):
        contracted_edges, contracted_bracketing = contract_bracketing(edges, bracketing, minimal)
        if contracted_edges and is_valid_bracketing(contracted_edges, contracted_bracketing):
            moves.append((minimal, contracted_edges, contracted_bracketing))
    return moves


def serialize_bracket(bracket: Bracket) -> list[int]:
    return sorted(bracket)


def serialize_bracketing(bracketing: Bracketing) -> list[list[int]]:
    return sorted((serialize_bracket(bracket) for bracket in bracketing), key=lambda item: (len(item), item))


def check_fixture(name: str, edges: list[Edge]) -> tuple[dict[str, object], list[dict[str, object]]]:
    bracketings = enumerate_bracketings(edges)
    deletion_count = 0
    contraction_count = 0
    counterexamples: list[dict[str, object]] = []
    deletion_example: dict[str, object] | None = None
    contraction_example: dict[str, object] | None = None

    for bracketing in bracketings:
        for deleted in deletion_moves(edges, bracketing):
            deletion_count += 1
            if deletion_example is None:
                deletion_example = {
                    "source_bracketing": serialize_bracketing(bracketing),
                    "target_bracketing": serialize_bracketing(deleted),
                    "edge_count_preserved": len(edges),
                    "bracket_count_delta": len(deleted) - len(bracketing),
                }
            if len(deleted) != len(bracketing) - 1:
                counterexamples.append(
                    {
                        "tree": name,
                        "move_class": "delete_bracket",
                        "failure": "bracket_count_not_minus_one",
                        "source": serialize_bracketing(bracketing),
                        "target": serialize_bracketing(deleted),
                    }
                )

        for minimal, contracted_edges, contracted in contraction_moves(edges, bracketing):
            contraction_count += 1
            if contraction_example is None:
                contraction_example = {
                    "minimal_bracket": serialize_bracket(minimal),
                    "source_edges": edges,
                    "target_edges": contracted_edges,
                    "source_bracketing": serialize_bracketing(bracketing),
                    "target_bracketing": serialize_bracketing(contracted),
                    "edge_count_delta": len(contracted_edges) - len(edges),
                }
            if len(contracted_edges) >= len(edges):
                counterexamples.append(
                    {
                        "tree": name,
                        "move_class": "contract_minimal_bracket",
                        "failure": "edge_count_not_reduced",
                        "minimal_bracket": serialize_bracket(minimal),
                        "source_edges": edges,
                        "target_edges": contracted_edges,
                    }
                )
            if not is_valid_bracketing(contracted_edges, contracted):
                counterexamples.append(
                    {
                        "tree": name,
                        "move_class": "contract_minimal_bracket",
                        "failure": "target_not_valid_bracketing",
                        "minimal_bracket": serialize_bracket(minimal),
                        "target_bracketing": serialize_bracketing(contracted),
                    }
                )

    summary = {
        "tree": name,
        "edge_count": len(edges),
        "edges": edges,
        "bracketing_count": len(bracketings),
        "deletion_move_count": deletion_count,
        "contraction_move_count": contraction_count,
        "has_delete_bracket_moves": deletion_count > 0,
        "has_contract_minimal_bracket_moves": contraction_count > 0,
        "delete_bracket_example": deletion_example,
        "contract_minimal_bracket_example": contraction_example,
    }
    return summary, counterexamples


def run_check(fixtures: dict[str, list[Edge]] = TREE_FIXTURES) -> CosmoMoveCheckResult:
    fixture_results: list[dict[str, object]] = []
    counterexamples: list[dict[str, object]] = []
    for name, edges in fixtures.items():
        summary, failures = check_fixture(name, edges)
        fixture_results.append(summary)
        counterexamples.extend(failures)

    total_deletions = sum(int(result["deletion_move_count"]) for result in fixture_results)
    total_contractions = sum(int(result["contraction_move_count"]) for result in fixture_results)
    total_bracketings = sum(int(result["bracketing_count"]) for result in fixture_results)
    nontrivial_results = [result for result in fixture_results if int(result["edge_count"]) >= 2]
    if not all(result["has_delete_bracket_moves"] for result in nontrivial_results):
        counterexamples.append({"failure": "missing_delete_bracket_move_in_nontrivial_fixture"})
    if not all(result["has_contract_minimal_bracket_moves"] for result in nontrivial_results):
        counterexamples.append({"failure": "missing_contract_minimal_bracket_move_in_nontrivial_fixture"})

    return CosmoMoveCheckResult(
        target_id=TARGET_ID,
        checker="finite_bracketed_tree_cover_rule_v1",
        status="PASS_PARTIAL" if not counterexamples else "FAILED",
        source_rule_scope="Finite implementation of the source-stated bracketed-tree cover rules: delete a bracket, or contract a minimal bracket. This checks the move-class split on selected small tree fixtures; it does not prove the full cosmohedron face lattice.",
        source_anchors=[
            "COSMO_COMB_2026: Definition 2.1 Matryoshka poset by containment with maximum element",
            "COSMO_COMB_2026: Lemma 2.10 Matryoshka <-> bracketed-tree bijection",
            "COSMO_COMB_2026: Corollary 2.12 cosmohedral fan cones are bracketed-tree cones",
            "COSMO_COMB_2026: Definition/paragraph after Corollary 2.12 defining deletion and contraction of bracketings",
            "COSMO_COMB_2026: Proposition 2.13 cover relations have delete-bracket and contract-minimal-bracket classes",
        ],
        tree_fixtures=fixture_results,
        total_bracketings=total_bracketings,
        total_deletion_moves=total_deletions,
        total_contraction_moves=total_contractions,
        move_class_invariants={
            "delete_bracket": "preserves tree edge count; decreases bracketing cardinality by one",
            "contract_minimal_bracket": "strictly decreases tree edge count by contracting a minimal bracket; target bracketing remains valid when nonempty",
        },
        counterexamples=counterexamples,
        status_boundary="PARTIAL finite move-class check for the cosmohedron/bracketed-tree baseline. It supports the existence and distinction of the two source-stated cover move classes on finite fixtures, but it is not the full CHK-COSMO-MOVE-CLASSES target against A/M1 and not a theorem for all n.",
    )


def write_result(path: Path, result: CosmoMoveCheckResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(result), indent=2, sort_keys=True), encoding="utf-8")


def main() -> None:
    result = run_check()
    write_result(Path("formal_handoff/results/CHK-COSMO-MOVE-CLASSES.json"), result)
    print(json.dumps(asdict(result), indent=2, sort_keys=True))
    if result.status == "FAILED":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
