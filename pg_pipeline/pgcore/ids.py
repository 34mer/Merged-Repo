from __future__ import annotations

import hashlib
import json


def stable_id(kind: str, payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
    digest = hashlib.sha256(encoded).hexdigest()[:16]
    return f"{kind}:{digest}"

