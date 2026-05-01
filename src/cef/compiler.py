from __future__ import annotations

from pathlib import Path
from typing import Any

from .capture import load_capture, split_episodes
from .core import mean, stable_hash, write_json

OBSERVABLES = [
    "neural_mean",
    "posture_mean",
    "stimulus_mean",
    "motor_mean",
    "perturbation_response",
    "body_loop_coupling",
]




def _driver_rows(episodes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for ep in episodes:
        env = ep.get("channels", {}).get("environment_stimulus_state", [0.0, 0.0])
        perturbations = ep.get("channels", {}).get("perturbation_events", [])
        perturbation = max([float(p.get("magnitude", 0.0)) for p in perturbations] or [float(env[1]) if len(env) > 1 else 0.0])
        rows.append({
            "episode_id": ep["episode_id"],
            "stimulus_mean": float(ep["observables"].get("stimulus_mean", sum(env) / max(len(env), 1))),
            "perturbation_magnitude": perturbation,
            "driver_channels": {
                "environment_stimulus_state": env,
                "perturbation_events": perturbations,
            },
        })
    return rows


def _training_examples(episodes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    drivers = _driver_rows(episodes)
    examples = []
    for ep, driver in zip(episodes, drivers):
        examples.append({
            "episode_id": ep["episode_id"],
            "driver": driver,
            "observables": {feature: float(ep["observables"][feature]) for feature in OBSERVABLES},
        })
    return examples

def _feature_rows(episodes: list[dict[str, Any]], margin: float) -> list[dict[str, Any]]:
    rows = []
    for feature in OBSERVABLES:
        values = [float(ep["observables"][feature]) for ep in episodes]
        center = mean(values)
        lo = min(values) - margin
        hi = max(values) + margin
        row = {
            "feature": feature,
            "center": center,
            "range": [max(0.0, lo), min(1.0, hi)],
            "episode_count": len(values),
            "required": True,
        }
        row["hash"] = stable_hash(row)
        rows.append(row)
    return rows


def compile_capture_to_packets(
    source: str | Path,
    out: str | Path = "artifacts/cef_v0",
    construction_margin: float = 0.08,
    oracle_margin: float = 0.05,
) -> dict[str, Any]:
    capture = load_capture(source)
    construction_eps = split_episodes(capture, "construction")
    heldout_eps = split_episodes(capture, "heldout")
    if not construction_eps:
        raise ValueError("CEF-v0 requires at least one construction episode")
    if not heldout_eps:
        raise ValueError("CEF-v0 requires at least one held-out verifier episode")

    individual_packet = {
        "schema": "cef-v0-individual-worm-constraint-packet",
        "protocol": "CEF-v0",
        "individual_id": capture["individual_id"],
        "capture_origin": capture.get("capture_origin", "unknown"),
        "dataset_source": capture.get("dataset_source", "unknown"),
        "real_organism_constraints_loaded": bool(capture.get("real_organism_constraints_loaded", False)),
        "capture_hash": capture["capture_hash"],
        "required_channels": capture["capture_channels"],
        "state_variables": OBSERVABLES,
        "coupling_constraints": ["body_loop_coupling", "neural_mean", "motor_mean"],
        "body_loop_constraints": ["posture_mean", "body_loop_coupling"],
        "stimulus_response_constraints": ["stimulus_mean", "motor_mean"],
        "perturbation_response_constraints": ["perturbation_response"],
        "failure_boundaries": [
            "missing construction/verifier split",
            "held-out perturbation response outside oracle",
            "internal constraints absent while behavior-only output passes",
            "random or over-stable control passes",
        ],
    }
    individual_packet["packet_hash"] = stable_hash(individual_packet)

    construction_packet = {
        "schema": "cef-v0-construction-packet",
        "protocol": "CEF-v0",
        "individual_id": capture["individual_id"],
        "capture_origin": capture.get("capture_origin", "unknown"),
        "dataset_source": capture.get("dataset_source", "unknown"),
        "real_organism_constraints_loaded": bool(capture.get("real_organism_constraints_loaded", False)),
        "capture_hash": capture["capture_hash"],
        "source_packet_hash": individual_packet["packet_hash"],
        "split": "construction",
        "features": _feature_rows(construction_eps, construction_margin),
        "training_examples": _training_examples(construction_eps),
    }
    construction_packet["construction_packet_hash"] = stable_hash(construction_packet)

    verifier_oracle = {
        "schema": "cef-v0-heldout-verifier-oracle",
        "protocol": "CEF-v0",
        "individual_id": capture["individual_id"],
        "capture_origin": capture.get("capture_origin", "unknown"),
        "dataset_source": capture.get("dataset_source", "unknown"),
        "real_organism_constraints_loaded": bool(capture.get("real_organism_constraints_loaded", False)),
        "capture_hash": capture["capture_hash"],
        "source_packet_hash": individual_packet["packet_hash"],
        "split": "heldout",
        "heldout_episode_ids": [ep["episode_id"] for ep in heldout_eps],
        "features": _feature_rows(heldout_eps, oracle_margin),
    }
    verifier_oracle["oracle_hash"] = stable_hash(verifier_oracle)

    heldout_driver = {
        "schema": "cef-v0.1-heldout-driver",
        "protocol": "CEF-v0.1",
        "individual_id": capture["individual_id"],
        "capture_hash": capture["capture_hash"],
        "split": "heldout_driver",
        "driver_rows": _driver_rows(heldout_eps),
        "oracle_excluded_from_generation": True,
    }
    heldout_driver["heldout_driver_hash"] = stable_hash(heldout_driver)

    manifest = {
        "schema": "cef-v0-independence-manifest",
        "protocol": "CEF-v0",
        "individual_id": capture["individual_id"],
        "construction_packet_hash": construction_packet["construction_packet_hash"],
        "oracle_hash": verifier_oracle["oracle_hash"],
        "independence_rule": "Synthetic runtime construction consumes construction_packet.json; blind projection consumes heldout_driver.json; held-out verification consumes verifier_oracle.json.",
        "heldout_driver_hash": heldout_driver["heldout_driver_hash"],
    }
    manifest["manifest_hash"] = stable_hash(manifest)

    outp = Path(out)
    write_json(outp / "individual_worm_constraint_packet.json", individual_packet)
    write_json(outp / "construction_packet.json", construction_packet)
    write_json(outp / "verifier_oracle.json", verifier_oracle)
    write_json(outp / "heldout_driver.json", heldout_driver)
    write_json(outp / "independence_manifest.json", manifest)
    return {
        "individual_packet": individual_packet,
        "construction_packet": construction_packet,
        "verifier_oracle": verifier_oracle,
        "heldout_driver": heldout_driver,
        "manifest": manifest,
    }


def verify_packet_independence(construction_packet: dict[str, Any], verifier_oracle: dict[str, Any]) -> dict[str, Any]:
    construction_hash_ok = construction_packet.get("construction_packet_hash") == stable_hash({k: v for k, v in construction_packet.items() if k != "construction_packet_hash"})
    oracle_hash_ok = verifier_oracle.get("oracle_hash") == stable_hash({k: v for k, v in verifier_oracle.items() if k != "oracle_hash"})
    split_ok = construction_packet.get("split") == "construction" and verifier_oracle.get("split") == "heldout"
    distinct_hashes = construction_packet.get("construction_packet_hash") != verifier_oracle.get("oracle_hash")
    same_features = {row["feature"] for row in construction_packet.get("features", [])} == {row["feature"] for row in verifier_oracle.get("features", [])}
    ok = construction_hash_ok and oracle_hash_ok and split_ok and distinct_hashes and same_features
    return {
        "status": "PASS" if ok else "FAIL",
        "construction_hash_ok": construction_hash_ok,
        "oracle_hash_ok": oracle_hash_ok,
        "split_ok": split_ok,
        "distinct_hashes": distinct_hashes,
        "same_feature_set": same_features,
    }
