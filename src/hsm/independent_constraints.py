from __future__ import annotations

from pathlib import Path
from typing import Any

from .core import stable_hash, write_json, read_json

# HSM-v0.1 uses numeric external-style constraints. The construction packet is
# intentionally separate from the verifier oracle. Builders consume construction
# ranges; final verification consumes held-out oracle ranges.
NUMERIC_CONSTRAINTS = [
    {
        "id": "human_neuron_threshold_regime",
        "feature": "threshold_norm",
        "source": "Allen human neuronal electrophysiology constraints",
        "plane": "human_neuron",
        "construction_range": [0.22, 0.78],
        "oracle_range": [0.30, 0.70],
        "units": "normalized_operator",
    },
    {
        "id": "human_neuron_adaptation_class",
        "feature": "adaptation_norm",
        "source": "Allen human neuronal electrophysiology constraints",
        "plane": "human_neuron",
        "construction_range": [0.18, 0.82],
        "oracle_range": [0.28, 0.72],
        "units": "normalized_operator",
    },
    {
        "id": "human_neuron_excitability_class",
        "feature": "excitability_norm",
        "source": "Allen human neuronal electrophysiology constraints",
        "plane": "human_neuron",
        "construction_range": [0.20, 0.84],
        "oracle_range": [0.32, 0.76],
        "units": "normalized_operator",
    },
    {
        "id": "human_micro_synapse_density_range",
        "feature": "synapse_density_norm",
        "source": "H01 human cortex microstructure constraints",
        "plane": "human_microstructure",
        "construction_range": [0.12, 0.88],
        "oracle_range": [0.26, 0.74],
        "units": "normalized_density",
    },
    {
        "id": "human_micro_motif_signature",
        "feature": "micro_motif_norm",
        "source": "H01 human cortex motif constraints",
        "plane": "human_microstructure",
        "construction_range": [0.16, 0.86],
        "oracle_range": [0.24, 0.78],
        "units": "normalized_motif_score",
    },
    {
        "id": "human_macro_network_modularity",
        "feature": "macro_modularity_norm",
        "source": "Human Connectome Project macro-connectivity constraints",
        "plane": "human_macro",
        "construction_range": [0.14, 0.90],
        "oracle_range": [0.25, 0.80],
        "units": "normalized_graph_statistic",
    },
    {
        "id": "human_macro_state_transition_envelope",
        "feature": "state_transition_norm",
        "source": "Human Connectome Project rest/task dynamics constraints",
        "plane": "human_macro",
        "construction_range": [0.10, 0.84],
        "oracle_range": [0.22, 0.72],
        "units": "normalized_transition_statistic",
    },
    {
        "id": "mammalian_structure_function_coupling",
        "feature": "structure_function_coupling_norm",
        "source": "MICrONS structure-function bridge constraints",
        "plane": "bridge",
        "construction_range": [0.18, 0.82],
        "oracle_range": [0.30, 0.70],
        "units": "normalized_coupling_score",
    },
]


def _row_for_construction(row: dict[str, Any]) -> dict[str, Any]:
    payload = {
        "id": row["id"],
        "feature": row["feature"],
        "source": row["source"],
        "plane": row["plane"],
        "range": row["construction_range"],
        "units": row["units"],
        "required": True,
    }
    payload["hash"] = stable_hash(payload)
    return payload


def _row_for_oracle(row: dict[str, Any]) -> dict[str, Any]:
    payload = {
        "id": row["id"],
        "feature": row["feature"],
        "source": row["source"],
        "plane": row["plane"],
        "range": row["oracle_range"],
        "units": row["units"],
        "required": True,
        "split": "heldout_verifier_oracle",
    }
    payload["hash"] = stable_hash(payload)
    return payload


def build_independent_constraint_packets(out: str | Path = "artifacts/hsm_constraints_v0_1") -> dict[str, Any]:
    outp = Path(out)
    construction_constraints = [_row_for_construction(row) for row in NUMERIC_CONSTRAINTS]
    oracle_constraints = [_row_for_oracle(row) for row in NUMERIC_CONSTRAINTS]
    construction = {
        "schema": "hsm-v0.1-construction-constraints",
        "protocol": "HSM-v0.1",
        "description": "Numeric construction constraints consumed by substrate builders.",
        "constraints": construction_constraints,
    }
    construction["construction_packet_hash"] = stable_hash(construction)
    oracle = {
        "schema": "hsm-v0.1-independent-verifier-oracle",
        "protocol": "HSM-v0.1",
        "description": "Independently frozen held-out numeric verifier constraints not consumed by builders.",
        "constraints": oracle_constraints,
    }
    oracle["oracle_packet_hash"] = stable_hash(oracle)
    manifest = {
        "schema": "hsm-v0.1-independent-constraint-manifest",
        "protocol": "HSM-v0.1",
        "construction_packet_hash": construction["construction_packet_hash"],
        "oracle_packet_hash": oracle["oracle_packet_hash"],
        "independence_rule": "Builders consume construction_constraints.json only; final verifier consumes verifier_oracle.json.",
    }
    manifest["manifest_hash"] = stable_hash(manifest)
    write_json(outp / "construction_constraints.json", construction)
    write_json(outp / "verifier_oracle.json", oracle)
    write_json(outp / "independence_manifest.json", manifest)
    return {"construction": construction, "oracle": oracle, "manifest": manifest}


def verify_independent_packets(construction: dict[str, Any], oracle: dict[str, Any]) -> dict[str, Any]:
    construction_ok = construction.get("construction_packet_hash") == stable_hash({k: v for k, v in construction.items() if k != "construction_packet_hash"})
    oracle_ok = oracle.get("oracle_packet_hash") == stable_hash({k: v for k, v in oracle.items() if k != "oracle_packet_hash"})
    disjoint_hashes = construction.get("construction_packet_hash") != oracle.get("oracle_packet_hash")
    same_features = {c["feature"] for c in construction.get("constraints", [])} == {c["feature"] for c in oracle.get("constraints", [])}
    return {
        "status": "PASS" if construction_ok and oracle_ok and disjoint_hashes and same_features else "FAIL",
        "construction_ok": construction_ok,
        "oracle_ok": oracle_ok,
        "disjoint_hashes": disjoint_hashes,
        "same_feature_set": same_features,
        "construction_packet_hash": construction.get("construction_packet_hash"),
        "oracle_packet_hash": oracle.get("oracle_packet_hash"),
    }


def load_independent_packets(root: str | Path = "artifacts/hsm_constraints_v0_1") -> tuple[dict[str, Any], dict[str, Any]]:
    rootp = Path(root)
    return read_json(rootp / "construction_constraints.json"), read_json(rootp / "verifier_oracle.json")
