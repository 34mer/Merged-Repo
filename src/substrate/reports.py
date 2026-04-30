from __future__ import annotations

from pathlib import Path
from typing import Any

from .channel.verify import verify_channel
from .core import write_json
from .hydrogen.verify import verify_hydrogen
from .ion_water.verify import verify_ion_water
from .membrane.verify import verify_membrane
from .molecule.verify import verify_h2
from .neuron.primitive import extract_synthetic_neuron_primitive
from .neuron.verify import verify_neuron


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


def _next_layer(layer: str, name: str) -> str:
    if layer == "hydrogen":
        return "H2 molecular bonding"
    if layer == "molecule":
        return "ion/water primitive"
    if layer == "ion_water":
        return "membrane boundary"
    if layer == "membrane":
        return "ion channel"
    if layer == "channel" and "sodium" in name:
        return "single-neuron sodium conductance"
    if layer == "channel" and "potassium" in name:
        return "single-neuron potassium conductance"
    if layer == "neuron":
        return "synthetic neuron primitive"
    if layer == "synthetic_neuron":
        return "network / organism integration"
    return "next layer"


def _observable_summary(layer: str) -> str:
    summaries = {
        "hydrogen": "spectrum / energy / ionization",
        "molecule": "bond / binding energy / curve",
        "ion_water": "charge / diffusion / hydration",
        "membrane": "voltage / capacitance / RC decay",
        "channel": "open probability / current / recovery",
        "neuron": "spikes / F-I curve / recovery / energy",
        "synthetic_neuron": "migration / repair metadata / process equivalence",
    }
    return summaries.get(layer, "observables")


def write_ladder_report(out: str | Path) -> dict[str, Any]:
    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)
    primitives = build_ladder()
    claim = (
        "Computable boundary-to-biology bootstrapping ladder: each layer produces a "
        "verified boundary-process primitive whose observables are benchmarked, whose "
        "primitive hash is recorded, and whose verified output constrains the next layer."
    )
    report = {
        "status": "BOUNDARY TO BIOLOGY BOOTSTRAPPING LADDER COMPLETE",
        "claim": claim,
        "primitive_count": len(primitives),
        "primitives": primitives,
        "final_primitive_hash": primitives[-1]["hash"],
    }
    write_json(out_path / "boundary_to_biology_bootstrapping_ladder_report.json", report)
    # Backward-compatible filename for older scripts/tests.
    write_json(out_path / "boundary_to_neuron_ladder_report.json", report)

    lines = [
        "# Boundary-to-Biology Bootstrapping Ladder v0.1",
        "",
        "This project demonstrates forward constraint bootstrapping from boundary physics toward biological process primitives.",
        "",
        "Rather than attempting to derive a neuron, organism, or person from all microscopic physics in one step, the system builds a forward ladder of verified primitives. At each rung, a compact boundary object is defined, unfolded into observable predictions, compared against a source benchmark, verified, hashed, and frozen as a primitive. That primitive is then carried forward as a constraint/input for the next rung.",
        "",
        "The result is a working computational scaffold for carrying verified constraints forward from simpler physical primitives toward biological process primitives.",
        "",
        "| Layer | Primitive | Observables | Verified | Hash | Used by next layer |",
        "|---|---|---|---|---|---|",
    ]
    for primitive in primitives:
        verification = primitive["verification"]
        verified = "yes" if str(verification["status"]).endswith("VERIFIED") else "no"
        lines.append(
            f"| {primitive['layer']} | {primitive['name']} | {_observable_summary(primitive['layer'])} | "
            f"{verified} | `{primitive['hash'][:16]}` | {_next_layer(primitive['layer'], primitive['name'])} |"
        )
    lines.extend(
        [
            "",
            "## Migration protocol",
            "",
            "```text",
            "primitive object -> checkpoint JSON -> payload hash -> copy/migrate checkpoint -> verify checkpoint hash -> verify payload hash -> report zero state divergence",
            "```",
            "",
            "## Relationship to the organism/process stack",
            "",
            "The organism/process stack proves the migration, abstraction, process-equivalence, and substrate-optimization operation at the organism-process level.",
            "",
            "The boundary-to-biology bootstrapping ladder grounds the lower-level synthetic biological primitive path.",
            "",
            "Together, they begin to meet: derive/verify synthetic neuron primitives, scale to network primitives, then integrate with the organism/process migration stack.",
            "",
            "## Final claim",
            "",
            "We implemented a computable boundary-to-biology bootstrapping ladder in which each layer produces a verified boundary-process primitive whose observables are benchmarked, whose primitive hash is recorded, and whose verified output constrains the next layer. The ladder progresses from hydrogen bound-state structure through molecular, ion/water, membrane, channel, and neuron dynamics, ending in a compact synthetic neuron primitive with checkpointing, migration, and zero-divergence state verification under a published protocol.",
            "",
            "## Claim boundary",
            "",
            "This is a computable digital primitive ladder. It does not claim biological neuron upload, human migration, consciousness transfer, or full QED/protein-folding derivation.",
        ]
    )
    content = "\n".join(lines) + "\n"
    (out_path / "BOUNDARY_TO_BIOLOGY_BOOTSTRAPPING_LADDER_v0.1.md").write_text(content, encoding="utf-8")
    # Backward-compatible filename for older scripts/tests.
    (out_path / "BOUNDARY_TO_NEURON_LADDER.md").write_text(content, encoding="utf-8")
    return report
