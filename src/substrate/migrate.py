from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from .core import read_json, stable_hash, write_json


def save_checkpoint(obj: dict[str, Any], path: str | Path) -> dict[str, Any]:
    payload = {"payload": obj, "payload_hash": stable_hash(obj)}
    write_json(path, payload)
    return payload


def migrate_checkpoint(checkpoint: str | Path, out: str | Path) -> dict[str, Any]:
    source = Path(checkpoint)
    target_dir = Path(out)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / source.name
    shutil.copy2(source, target)
    source_payload = read_json(source)
    target_payload = read_json(target)
    manifest = {
        "source": str(source),
        "target": str(target),
        "source_hash": stable_hash(source_payload),
        "target_hash": stable_hash(target_payload),
        "payload_hash_matched": source_payload.get("payload_hash") == target_payload.get("payload_hash"),
        "checkpoint_hash_matched": stable_hash(source_payload) == stable_hash(target_payload),
    }
    write_json(target_dir / "migration_manifest.json", manifest)
    return manifest


def verify_migration(checkpoint_a: str | Path, checkpoint_b: str | Path) -> dict[str, Any]:
    a = read_json(checkpoint_a)
    b = read_json(checkpoint_b)
    matched = stable_hash(a) == stable_hash(b) and a.get("payload_hash") == b.get("payload_hash")
    return {
        "status": "PRIMITIVE MIGRATION VERIFIED" if matched else "PRIMITIVE MIGRATION FAILED",
        "checkpoint_hash_matched": stable_hash(a) == stable_hash(b),
        "payload_hash_matched": a.get("payload_hash") == b.get("payload_hash"),
        "state_divergence": 0.0 if matched else 1.0,
    }
