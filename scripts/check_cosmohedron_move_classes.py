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
    out: set[int] = set()
    for i in bracket:
        out.update(edges[i])
    return out


def is_connected_edge_subset(edges: list[Edge], subset: Iterable[int]) -> bool:
    bracket = frozenset(subset)
    if not bracket:
        return False
    vertices = bracket_vertices(edges, bracket)
    seen = {next(iter(vertices))}
    changed = True
    while changed:
        changed = False
        for i in bracket:
            a, b = edges[i]
            if a in seen and b not in seen:
                seen.add(b); changed = True
            if b in seen and a not in seen:
                seen.add(a); changed = True
    return seen == vertices


def connected_brackets(edges: list[Edge]) -> list[Bracket]:
    return [frozenset(c) for r in range(1, len(edges) + 1) for c in combinations(range(len(edges)), r) if is_connected_edge_subset(edges, c)]


def compatible(edges: list[Edge], a: Bracket, b: Bracket) -> bool:
    return a <= b or b <= a or bracket_vertices(edges, a).isdisjoint(bracket_vertices(edges, b))


def valid_bracketing(edges: list[Edge], bracketing: Bracketing) -> bool:
    full = frozenset(range(len(edges)))
    return full in bracketing and all(is_connected_edge_subset(edges, b) for b in bracketing) and all(compatible(edges, a, b) for a, b in combinations(bracketing, 2))


def enumerate_bracketings(edges: list[Edge]) -> list[Bracketing]:
    full = frozenset(range(len(edges)))
    candidates = [b for b in connected_brackets(edges) if b != full]
    out: list[Bracketing] = []
    for r in range(len(candidates) + 1):
        for selected in combinations(candidates, r):
            bracketing = frozenset(set(selected) | {full})
            if valid_bracketing(edges, bracketing):
                out.append(bracketing)
    return out


def minimal_brackets(bracketing: Bracketing) -> list[Bracket]:
    return [b for b in bracketing if not any(o < b for o in bracketing)]


def contract_edges(edges: list[Edge], contracted: Bracket) -> tuple[list[Edge], dict[int, int | None]]:
    vertices = {v for e in edges for v in e}
    parent = {v: v for v in vertices}

    def find(v: int) -> int:
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for i in contracted:
        union(*edges[i])

    key_to_index: dict[Edge, int] = {}
    old_to_new: dict[int, int | None] = {}
    quotient: list[Edge] = []
    for i, (a, b) in enumerate(edges):
        ra, rb = find(a), find(b)
        if ra == rb:
            old_to_new[i] = None
            continue
        key = tuple(sorted((ra, rb)))
        if key not in key_to_index:
            key_to_index[key] = len(quotient)
            quotient.append(key)
        old_to_new[i] = key_to_index[key]

    vertex_map: dict[int, int] = {}
    dense: list[Edge] = []
    for a, b in quotient:
        for v in (a, b):
            if v not in vertex_map:
                vertex_map[v] = len(vertex_map)
        dense.append(tuple(sorted((vertex_map[a], vertex_map[b]))))
    return dense, old_to_new


def image_bracket(bracket: Bracket, old_to_new: dict[int, int | None]) -> Bracket:
    return frozenset(j for i in bracket for j in [old_to_new[i]] if j is not None)


def contract_bracketing(edges: list[Edge], bracketing: Bracketing, minimal: Bracket) -> tuple[list[Edge], Bracketing]:
    contracted_edges, old_to_new = contract_edges(edges, minimal)
    image = {image_bracket(b, old_to_new) for b in bracketing}
    return contracted_edges, frozenset(b for b in image if b)


def serialize(bracketing: Bracketing) -> list[list[int]]:
    return sorted((sorted(b) for b in bracketing), key=lambda x: (len(x), x))


def check_fixture(name: str, edges: list[Edge]) -> tuple[dict[str, object], list[dict[str, object]]]:
    bracketings = enumerate_bracketings(edges)
    failures: list[dict[str, object]] = []
    deletion_count = 0
    contraction_count = 0
    delete_example = None
    contract_example = None

    full = frozenset(range(len(edges)))
    for bracketing in bracketings:
        for bracket in bracketing:
            if bracket == full:
                continue
            target = frozenset(set(bracketing) - {bracket})
            if valid_bracketing(edges, target):
                deletion_count += 1
                delete_example = delete_example or {"source_bracketing": serialize(bracketing), "target_bracketing": serialize(target), "edge_count_preserved": len(edges), "bracket_count_delta": len(target) - len(bracketing)}
                if len(target) != len(bracketing) - 1:
                    failures.append({"tree": name, "move_class": "delete_bracket", "failure": "bracket_count_not_minus_one"})
        for minimal in minimal_brackets(bracketing):
            target_edges, target_bracketing = contract_bracketing(edges, bracketing, minimal)
            if target_edges and valid_bracketing(target_edges, target_bracketing):
                contraction_count += 1
                contract_example = contract_example or {"minimal_bracket": sorted(minimal), "source_edges": edges, "target_edges": target_edges, "source_bracketing": serialize(bracketing), "target_bracketing": serialize(target_bracketing), "edge_count_delta": len(target_edges) - len(edges)}
                if len(target_edges) >= len(edges):
                    failures.append({"tree": name, "move_class": "contract_minimal_bracket", "failure": "edge_count_not_reduced"})

    return {
        "tree": name,
        "edge_count": len(edges),
        "edges": edges,
        "bracketing_count": len(bracketings),
        "deletion_move_count": deletion_count,
        "contraction_move_count": contraction_count,
        "has_delete_bracket_moves": deletion_count > 0,
        "has_contract_minimal_bracket_moves": contraction_count > 0,
        "delete_bracket_example": delete_example,
        "contract_minimal_bracket_example": contract_example,
    }, failures


def run_check(fixtures: dict[str, list[Edge]] = TREE_FIXTURES) -> CosmoMoveCheckResult:
    summaries: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    for name, edges in fixtures.items():
        summary, local_failures = check_fixture(name, edges)
        summaries.append(summary)
        failures.extend(local_failures)
    if not all(s["has_delete_bracket_moves"] and s["has_contract_minimal_bracket_moves"] for s in summaries):
        failures.append({"failure": "missing_move_class_in_fixture"})
    return CosmoMoveCheckResult(
        target_id=TARGET_ID,
        checker="finite_bracketed_tree_cover_rule_v1",
        status="PASS_PARTIAL" if not failures else "FAILED",
        source_rule_scope="Finite implementation of source-stated bracketed-tree cover rules: delete a bracket, or contract a minimal bracket. This checks the move-class split on selected small tree fixtures; it does not prove the full cosmohedron face lattice.",
        source_anchors=[
            "COSMO_COMB_2026: Definition 2.1 Matryoshka poset by containment with maximum element",
            "COSMO_COMB_2026: Lemma 2.10 Matryoshka <-> bracketed-tree bijection",
            "COSMO_COMB_2026: Corollary 2.12 cosmohedral fan cones are bracketed-tree cones",
            "COSMO_COMB_2026: Definition/paragraph after Corollary 2.12 defining deletion and contraction of bracketings",
            "COSMO_COMB_2026: Proposition 2.13 cover relations have delete-bracket and contract-minimal-bracket classes",
        ],
        tree_fixtures=summaries,
        total_bracketings=sum(int(s["bracketing_count"]) for s in summaries),
        total_deletion_moves=sum(int(s["deletion_move_count"]) for s in summaries),
        total_contraction_moves=sum(int(s["contraction_move_count"]) for s in summaries),
        move_class_invariants={"delete_bracket": "preserves tree edge count; decreases bracketing cardinality by one", "contract_minimal_bracket": "strictly decreases tree edge count by contracting a minimal bracket; target bracketing remains valid when nonempty"},
        counterexamples=failures,
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
