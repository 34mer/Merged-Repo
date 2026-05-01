from __future__ import annotations

import json
from pathlib import Path
from typing import Any

try:
    from blake3 import blake3
except Exception:  # pragma: no cover
    import hashlib

    class _CompatHash:
        def __init__(self, data: bytes):
            self._digest = hashlib.sha256(data).hexdigest()

        def hexdigest(self) -> str:
            return self._digest

    def blake3(data: bytes) -> _CompatHash:  # type: ignore
        return _CompatHash(data)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def stable_hash(value: Any) -> str:
    return blake3(canonical_json(value).encode("utf-8")).hexdigest()


def write_json(path: str | Path, value: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_json(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def mean(values: list[float]) -> float:
    return sum(float(v) for v in values) / max(len(values), 1)


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, float(value)))
