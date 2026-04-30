from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
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


@dataclass(frozen=True)
class BoundaryObject:
    layer: str
    parameters: dict[str, Any]
    grammar: dict[str, Any]
    constraints: dict[str, Any]
    observables: list[str]
    unfold_rule: str

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["hash"] = stable_hash(payload)
        return payload

    @property
    def hash(self) -> str:
        return self.to_dict()["hash"]


@dataclass(frozen=True)
class Primitive:
    name: str
    version: str
    layer: str
    boundary_object: BoundaryObject
    observables: dict[str, Any]
    verification: dict[str, Any]
    parents: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        payload = {
            "name": self.name,
            "version": self.version,
            "layer": self.layer,
            "boundary_object": self.boundary_object.to_dict(),
            "observables": self.observables,
            "verification": self.verification,
            "parents": self.parents,
        }
        payload["hash"] = stable_hash(payload)
        return payload

    @property
    def hash(self) -> str:
        return self.to_dict()["hash"]


@dataclass(frozen=True)
class VerificationReport:
    layer: str
    status: str
    score: float
    metrics: dict[str, Any]
    primitive_hash: str | None = None

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["hash"] = stable_hash(payload)
        return payload


def relative_error(predicted: float, target: float, floor: float = 1e-12) -> float:
    return abs(float(predicted) - float(target)) / max(abs(float(target)), floor)


def score_from_errors(errors: list[float]) -> float:
    if not errors:
        return 1.0
    return max(0.0, 1.0 - sum(errors) / len(errors))
