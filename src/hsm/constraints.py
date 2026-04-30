from __future__ import annotations

from pathlib import Path
from typing import Any

from .core import stable_hash, write_json

CONSTRAINT_SOURCES = {
    "allen_human": "Allen Cell Types Database / Allen human neuronal cell resources",
    "h01": "Harvard/Google H01 human cortex dataset",
    "hcp": "Human Connectome Project Young Adult release",
    "microns": "MICrONS mammalian structure-function bridge",
}

CONSTRAINT_DEFS = [
    ("human_neuron_excitability_class", "Allen Cell Types Database", "operator_constraint", "bounded_excitability_family", True, "human"),
    ("human_neuron_adaptation_class", "Allen Cell Types Database", "operator_constraint", "bounded_adaptation_family", True, "human"),
    ("human_neuron_threshold_regime", "Allen Cell Types Database", "operator_constraint", "human_threshold_envelope", True, "human"),
    ("human_neuron_morphology_envelope", "Allen Cell Types Database", "geometry_constraint", "human_morphology_envelope", True, "human"),
    ("human_neuron_cell_type_signature", "Allen Cell Types Database", "metadata_constraint", "human_cell_type_signature", True, "human"),
    ("human_micro_synapse_density_range", "H01 human cortex dataset", "microstructure_constraint", "human_synapse_density_range", True, "human"),
    ("human_micro_cell_density_range", "H01 human cortex dataset", "microstructure_constraint", "human_cell_density_range", True, "human"),
    ("human_micro_motif_signature", "H01 human cortex dataset", "motif_constraint", "human_cortical_motif_signature", True, "human"),
    ("human_micro_boundary_geometry_signature", "H01 human cortex dataset", "boundary_constraint", "human_micro_boundary_geometry_signature", True, "human"),
    ("human_macro_network_modularity", "Human Connectome Project", "macro_constraint", "human_network_modularity_envelope", True, "human"),
    ("human_macro_rest_task_state_structure", "Human Connectome Project", "macro_constraint", "human_rest_task_state_structure", True, "human"),
    ("human_macro_connectivity_signature", "Human Connectome Project", "macro_constraint", "human_connectivity_signature", True, "human"),
    ("human_macro_state_transition_envelope", "Human Connectome Project", "macro_constraint", "human_state_transition_envelope", True, "human"),
    ("mammalian_structure_function_coupling", "MICrONS", "bridge_constraint", "microconnectome_activity_coupling", True, "bridge"),
    ("microconnectome_to_activity_signature", "MICrONS", "bridge_constraint", "structure_function_bridge_signature", True, "bridge"),
]


def _constraint(defn: tuple[str, str, str, str, bool, str], parent_hashes: list[str] | None = None) -> dict[str, Any]:
    cid, source, ctype, expected, required, plane = defn
    payload = {
        "id": cid,
        "source": source,
        "type": ctype,
        "constraint_plane": plane,
        "expected": expected,
        "required": required,
        "parent_hashes": parent_hashes or [],
    }
    payload["hash"] = stable_hash(payload)
    return payload


def build_constraint_packet(out: str | Path = "artifacts/hsm_constraints_v0") -> dict[str, Any]:
    constraints = [_constraint(defn) for defn in CONSTRAINT_DEFS]
    packet = {
        "schema": "hsm-constraint-packet-v0",
        "protocol": "HSM-v0",
        "constraint_count": len(constraints),
        "human_constraint_count": len([c for c in constraints if c["constraint_plane"] == "human"]),
        "bridge_constraint_count": len([c for c in constraints if c["constraint_plane"] == "bridge"]),
        "sources": CONSTRAINT_SOURCES,
        "constraints": constraints,
    }
    packet["constraint_packet_hash"] = stable_hash(packet)
    outp = Path(out)
    write_json(outp / "constraints.json", packet)
    manifest = {
        "protocol": "HSM-v0",
        "source_manifest_hash": stable_hash(CONSTRAINT_SOURCES),
        "sources": CONSTRAINT_SOURCES,
        "constraint_packet_hash": packet["constraint_packet_hash"],
    }
    write_json(outp / "source_manifest.json", manifest)
    return packet


def verify_constraint_packet(packet: dict[str, Any]) -> dict[str, Any]:
    required = [c for c in packet.get("constraints", []) if c.get("required")]
    hashes_ok = all(c.get("hash") == stable_hash({k: v for k, v in c.items() if k != "hash"}) for c in packet.get("constraints", []))
    recomputed = dict(packet)
    existing_hash = recomputed.pop("constraint_packet_hash", None)
    packet_hash_ok = existing_hash == stable_hash(recomputed)
    human_count = len([c for c in packet.get("constraints", []) if c.get("constraint_plane") == "human"])
    bridge_count = len([c for c in packet.get("constraints", []) if c.get("constraint_plane") == "bridge"])
    ok = packet.get("schema") == "hsm-constraint-packet-v0" and len(required) == 15 and human_count == 13 and bridge_count == 2 and hashes_ok and packet_hash_ok
    return {
        "status": "PASS" if ok else "FAIL",
        "constraint_count": len(packet.get("constraints", [])),
        "human_constraints": human_count,
        "bridge_constraints": bridge_count,
        "hashes_ok": hashes_ok,
        "packet_hash_ok": packet_hash_ok,
        "constraint_packet_hash": existing_hash,
    }
