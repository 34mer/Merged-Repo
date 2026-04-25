from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Literal, TypedDict

ROOT = Path(__file__).resolve().parents[1]
LFS_POINTER_VERSION = "version https://git-lfs.github.com/spec/v1"


class PdfBindingCheck(TypedDict):
    storage_kind: Literal["git_lfs_pointer", "binary_pdf"]
    lfs_oid_sha256: str
    lfs_size_bytes: int


def read_json(name: str) -> dict:
    path = ROOT / "research_ledger" / name
    assert path.exists(), name
    return json.loads(path.read_text(encoding="utf-8"))


def parse_lfs_pointer_bytes(data: bytes, path: Path) -> PdfBindingCheck | None:
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return None

    lines = text.splitlines()
    if not lines or lines[0] != LFS_POINTER_VERSION:
        return None

    oid_line = next(line for line in lines if line.startswith("oid sha256:"))
    size_line = next(line for line in lines if line.startswith("size "))
    return {
        "storage_kind": "git_lfs_pointer",
        "lfs_oid_sha256": oid_line.removeprefix("oid sha256:"),
        "lfs_size_bytes": int(size_line.removeprefix("size ")),
    }


def inspect_pdf_binding(path: Path) -> PdfBindingCheck:
    data = path.read_bytes()
    pointer = parse_lfs_pointer_bytes(data, path)
    if pointer is not None:
        return pointer

    assert data.startswith(b"%PDF-"), f"Expected Git LFS pointer or binary PDF: {path}"
    return {
        "storage_kind": "binary_pdf",
        "lfs_oid_sha256": hashlib.sha256(data).hexdigest(),
        "lfs_size_bytes": len(data),
    }


def main() -> None:
    corpus = read_json("SOURCE_CORPUS.json")
    bindings = read_json("SOURCE_PDF_BINDINGS.json")
    claims = read_json("SOURCE_EXTRACTED_CLAIMS.json")
    targets = read_json("FORMAL_CHECK_TARGETS.json")

    manifest_paper_ids = {p["paper_id"] for p in corpus["papers"]}
    binding_paper_ids = {b["paper_id"] for b in bindings["bindings"]}
    claim_ids = [c["id"] for c in claims["claims"]]
    claim_id_set = set(claim_ids)
    target_ids = {t["id"] for t in targets["targets"]}
    claimed_paper_ids = {c["paper_id"] for c in claims["claims"]}

    assert corpus["paper_count"] == 16
    assert bindings["paper_count"] == 16
    assert len(manifest_paper_ids) == 16
    assert binding_paper_ids == manifest_paper_ids, sorted(manifest_paper_ids ^ binding_paper_ids)
    assert len(claim_ids) == len(claim_id_set), "claim ids must be unique"
    assert manifest_paper_ids <= claimed_paper_ids, sorted(manifest_paper_ids - claimed_paper_ids)
    assert claimed_paper_ids <= manifest_paper_ids, sorted(claimed_paper_ids - manifest_paper_ids)
    assert len(claim_id_set) >= 16
    assert len(target_ids) >= 11

    seen_storage_kinds: set[str] = set()
    for binding in bindings["bindings"]:
        assert binding["paper_id"] in manifest_paper_ids
        pdf_path = ROOT / binding["repo_pdf_path"]
        assert pdf_path.exists(), binding["repo_pdf_path"]
        checked = inspect_pdf_binding(pdf_path)
        seen_storage_kinds.add(checked["storage_kind"])
        assert checked["lfs_oid_sha256"] == binding["lfs_oid_sha256"], binding["paper_id"]
        assert checked["lfs_size_bytes"] == binding["lfs_size_bytes"], binding["paper_id"]

    assert seen_storage_kinds <= {"git_lfs_pointer", "binary_pdf"}

    for claim in claims["claims"]:
        assert claim["paper_id"] in manifest_paper_ids
        assert claim["source_file"]
        assert claim["source_anchor"]
        assert claim["claim_text"]
        assert "SOURCE_EXTRACTED" in claim["status"]
        assert claim["formal_check_targets"], claim["id"]
        for target_id in claim["formal_check_targets"]:
            assert target_id in target_ids, target_id

    for target in targets["targets"]:
        assert target["predicate"]
        assert target["failure_condition"]
        for claim_id in target["claim_ids"]:
            assert claim_id in claim_id_set, claim_id

    assert any("R13" in t.get("rows", []) for t in targets["targets"])
    assert any("S" in c.get("families", []) for c in claims["claims"])
    assert any(c["paper_id"] == "COSMO_COMB_2026" for c in claims["claims"])
    print("source extraction validation passed")


if __name__ == "__main__":
    main()
