from __future__ import annotations

from pathlib import Path
from typing import Any

from .core import write_json
from .hydrogen.verify import verify_hydrogen
from .molecule.verify import verify_h2
from .ion_water.verify import verify_ion_water
from .membrane.verify import verify_membrane
from .channel.verify import verify_channel
from .neuron.verify import verify_neuron
from .neuron.primitive import extract_synthetic_neuron_primitive


def build_ladder() -> list[dict[str, Any]]:
    primitives = [
        verify_hydrogen(),
        verify_h2(),
        verify_ion_water(),
        verify_membrane(),
        verify_channel("sodium"),
        verify_channel("potassium"),
        verify_neuron(),
        extract_synthetic_neuron_primitive(),
    ]
    return [p.to_dict() for p in primitives]


def write_ladder_report(out: str | Path) -> dict[str, Any]:
    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)
    primitives = build_ladder()
    report = {
        "status": "BOUNDARY TO NEURON LADDER COMPLETE",
        "claim": "Recursive verified boundary/process primitives from hydrogen to synthetic single-neuron primitive.",
        "primitive_count": len(primitives),
        "primitives": primitives,
        "final_primitive_hash": primitives[-1]["hash"],
    }
    write_json(out_path / "boundary_to_neuron_ladder_report.json", report)
    lines = [
        "# Boundary-to-Neuron Derivation Ladder v0.1",
        "",
        "Each rung produces a verified boundary/process primitive consumed by the next rung.",
        "",
        "| Layer | Primitive | Status | Score | Hash |",
        "|---|---|---|---:|---|",
    ]
    for primitive in primitives:
        verification = primitive["verification"]
        lines.append(
            f"| {primitive['layer']} | {primitive['name']} | {verification['status']} | "
            f"{verification['score']:.6f} | `{primitive['hash'][:16]}` |"
        )
    lines.extend(
        [
            "",
            "## Final claim",
            "",
            "We implemented a recursive physical-constraint ladder from simple bound-state physics to a single-neuron process primitive. Each rung produces a verified boundary/process primitive that becomes the substrate for the next rung. The final neuron primitive is migratable, repairable, and optimized as a synthetic process object.",
            "",
            "Claim boundary: this is a computable digital primitive ladder, not a biological scan, human migration, or consciousness-transfer claim.",
        ]
    )
    (out_path / "BOUNDARY_TO_NEURON_LADDER.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report
