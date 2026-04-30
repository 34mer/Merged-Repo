from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

from substrate.core import BoundaryObject, Primitive, VerificationReport, stable_hash, write_json
from substrate.migrate import migrate_checkpoint, save_checkpoint, verify_migration
from substrate.neuron.primitive import extract_synthetic_neuron_primitive

from .ephys import (
    estimate_gain_offset,
    fi_rows_from_protocols,
    load_ephys_dataset,
    protocol_split,
    simulate_fitted_protocol,
    write_ephys_dataset,
)
from .metrics import fi_curve_similarity, protocol_score, summarize_protocol_scores

ADHESION_SCHEMA = "substrate-external-adhesion-v1"


def _control_prediction(protocol: dict[str, Any], mode: str) -> dict[str, Any]:
    target_voltage = [float(v) for v in protocol["voltage_mv"]]
    dt = float(protocol["dt_ms"])
    if mode == "random":
        rng = np.random.default_rng(int(abs(hash(protocol["protocol_id"])) % 2**32))
        baseline = float(np.mean(target_voltage[: max(1, len(target_voltage) // 10)]))
        voltage = (baseline + rng.normal(0.0, 6.0, size=len(target_voltage))).astype(float).tolist()
    elif mode == "over_stable":
        baseline = float(np.mean(target_voltage[: max(1, len(target_voltage) // 10)]))
        voltage = [baseline for _ in target_voltage]
    elif mode == "behavior_only_leakage":
        # Deliberate leakage control: copies external voltage to show fake high score.
        voltage = list(target_voltage)
    else:
        raise ValueError(f"Unknown control mode: {mode}")
    return {
        "protocol_id": f"{mode}_{protocol['protocol_id']}",
        "voltage_mv": voltage,
        "spike_times_ms": [],
        "dt_ms": dt,
    }


def _score_model_on_protocols(protocols: list[dict[str, Any]], fit: dict[str, float]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows = []
    predictions = []
    for protocol in protocols:
        predicted = simulate_fitted_protocol(protocol, fit)
        scores = protocol_score(predicted, protocol)
        scores["protocol_id"] = protocol["protocol_id"]
        rows.append(scores)
        predictions.append(predicted)
    return rows, predictions


def _score_control(protocols: list[dict[str, Any]], mode: str) -> dict[str, Any]:
    rows = []
    for protocol in protocols:
        predicted = _control_prediction(protocol, mode)
        scores = protocol_score(predicted, protocol)
        scores["protocol_id"] = protocol["protocol_id"]
        rows.append(scores)
    summary = summarize_protocol_scores(rows)
    # Leakage is intentionally expected to pass; honest controls should fail.
    expected_to_fail = mode != "behavior_only_leakage"
    passed_gate = summary["heldout_score"] >= 0.80
    return {
        "mode": mode,
        "expected_to_fail": expected_to_fail,
        "passed_gate": passed_gate,
        "failed_as_expected": bool(expected_to_fail and not passed_gate),
        "summary": summary,
        "rows": rows,
    }


def fit_primitive_to_ephys(source: str | Path, out: str | Path) -> dict[str, Any]:
    dataset = load_ephys_dataset(source)
    train = protocol_split(dataset, "train")
    fit = estimate_gain_offset(train)
    parent = extract_synthetic_neuron_primitive()
    boundary = BoundaryObject(
        layer="external_ephys_adhered_neuron",
        parameters={
            "source_name": dataset["source_name"],
            "cell_id": dataset["cell_id"],
            "source_hash": dataset["source_hash"],
            "current_gain": fit["current_gain"],
            "current_offset": fit["current_offset"],
            "fit_loss": fit["loss"],
        },
        grammar={"fit": "synthetic_neuron_primitive + external_current_protocols -> external_observable_predictions"},
        constraints={"train_split_only": True, "heldout_required": True, "external_source_hash": dataset["source_hash"]},
        observables=["voltage_trace", "spike_times", "FI_curve", "heldout_protocol_score"],
        unfold_rule="external_ephys.current_gain_offset_adapter_v1",
    )
    report = VerificationReport(
        layer="external_ephys_adhered_neuron",
        status="EXTERNAL EPHYS PRIMITIVE FIT COMPLETE",
        score=max(0.0, 1.0 - float(fit["loss"])),
        metrics={"fit_loss": fit["loss"], "train_protocols": len(train)},
    )
    primitive = Primitive(
        name=f"external_ephys_primitive_{dataset['cell_id']}",
        version="v0.1",
        layer="external_ephys_adhered_neuron",
        boundary_object=boundary,
        observables={"fit": fit, "source_hash": dataset["source_hash"]},
        verification=report.to_dict(),
        parents=[parent.hash],
    )
    payload = primitive.to_dict()
    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)
    write_json(out_path / "primitive.json", payload)
    write_json(out_path / "fit.json", {"fit": fit, "source_hash": dataset["source_hash"], "primitive_hash": payload["hash"]})
    return payload


def verify_external_ephys(
    primitive: str | Path,
    source: str | Path,
    out: str | Path,
    voltage_threshold: float = 0.70,
    spike_threshold: float = 0.50,
    heldout_threshold: float = 0.80,
    include_controls: bool = True,
) -> dict[str, Any]:
    primitive_path = Path(primitive)
    if primitive_path.is_dir():
        primitive_path = primitive_path / "primitive.json"
    from substrate.core import read_json

    primitive_payload = read_json(primitive_path)
    dataset = load_ephys_dataset(source)
    fit = primitive_payload["observables"]["fit"]
    heldout = protocol_split(dataset, "heldout")
    heldout_rows, predictions = _score_model_on_protocols(heldout, fit)
    heldout_summary = summarize_protocol_scores(heldout_rows)
    target_fi = fi_rows_from_protocols(heldout)
    predicted_fi = [
        {"current_uA": float(protocol["current_uA"]), "spike_count": len(pred.get("spike_times_ms") or []), "rate_hz": len(pred.get("spike_times_ms") or []) / max(float(protocol["duration_ms"]) / 1000.0, 1e-9)}
        for protocol, pred in zip(heldout, predictions)
    ]
    fi_score = fi_curve_similarity(predicted_fi, target_fi)

    controls = []
    if include_controls:
        controls = [
            _score_control(heldout, "random"),
            _score_control(heldout, "over_stable"),
            _score_control(heldout, "behavior_only_leakage"),
        ]

    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)
    checkpoint = save_checkpoint(primitive_payload, out_path / "primitive_checkpoint.json")
    manifest = migrate_checkpoint(out_path / "primitive_checkpoint.json", out_path / "migrated")
    migration_report = verify_migration(out_path / "primitive_checkpoint.json", out_path / "migrated" / "primitive_checkpoint.json")

    pass_gate = (
        heldout_summary["voltage_fidelity"] >= voltage_threshold
        and heldout_summary["spike_timing_score"] >= spike_threshold
        and heldout_summary["heldout_score"] >= heldout_threshold
        and fi_score >= spike_threshold
        and migration_report["status"] == "PRIMITIVE MIGRATION VERIFIED"
    )
    honest_controls_failed = all(c["failed_as_expected"] for c in controls if c["mode"] != "behavior_only_leakage") if controls else True
    report = {
        "schema": ADHESION_SCHEMA,
        "status": "EXTERNAL EPHYS ADHESION PASSED" if pass_gate and honest_controls_failed else "EXTERNAL EPHYS ADHESION FAILED",
        "source_name": dataset["source_name"],
        "cell_id": dataset["cell_id"],
        "source_hash": dataset["source_hash"],
        "primitive_hash": primitive_payload["hash"],
        "heldout_summary": heldout_summary,
        "fi_curve_similarity": fi_score,
        "heldout_rows": heldout_rows,
        "migration": migration_report,
        "checkpoint_payload_hash": checkpoint["payload_hash"],
        "migration_manifest": manifest,
        "controls": controls,
        "pass_gate": pass_gate,
        "honest_controls_failed": honest_controls_failed,
        "claim_boundary": "External-ready adhesion benchmark over published/file-provided electrophysiology-style observables; not a biological upload or consciousness-transfer claim.",
    }
    report["report_hash"] = stable_hash(report)
    write_json(out_path / "external_ephys_adhesion_report.json", report)
    return report


def generate_hh_neuroml_fixture(out: str | Path) -> dict[str, Any]:
    return write_ephys_dataset(
        out,
        source_name="canonical_hh_neuroml_style_fixture",
        cell_id="hh_neuroml_v0_1",
        train_currents=[5.0, 10.0, 15.0],
        heldout_currents=[7.5, 12.5, 17.5],
        metadata={
            "external_anchor": "HH/NeuroML-style canonical current clamp benchmark",
            "note": "Offline deterministic fixture for CI; replace with exported NeuroML/Open Source Brain or NWB/Allen JSON for real external runs.",
        },
    )


def run_hh_neuroml_adhesion(out: str | Path) -> dict[str, Any]:
    out_path = Path(out)
    out_path.mkdir(parents=True, exist_ok=True)
    source = generate_hh_neuroml_fixture(out_path / "hh_neuroml_fixture.json")
    primitive = fit_primitive_to_ephys(out_path / "hh_neuroml_fixture.json", out_path / "primitive")
    report = verify_external_ephys(out_path / "primitive", out_path / "hh_neuroml_fixture.json", out_path / "report")
    master = {
        "status": "HH NEUROML ADHESION PASSED" if report["status"] == "EXTERNAL EPHYS ADHESION PASSED" else "HH NEUROML ADHESION FAILED",
        "source_hash": source["source_hash"],
        "primitive_hash": primitive["hash"],
        "adhesion_report": report,
    }
    write_json(out_path / "hh_neuroml_adhesion_report.json", master)
    return master
