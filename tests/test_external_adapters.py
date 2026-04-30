from __future__ import annotations

import csv
import json
from pathlib import Path

from substrate.external.adapters import import_allen_sweep_json, import_ephys_csv
from substrate.external.adhesion import fit_primitive_to_ephys, generate_hh_neuroml_fixture, verify_external_ephys
from substrate.external.ephys import load_ephys_dataset


def test_import_allen_sweep_json_and_run_adhesion(tmp_path: Path) -> None:
    fixture = tmp_path / "fixture.json"
    base = generate_hh_neuroml_fixture(fixture)
    allen_payload = {
        "source_name": "allen_cell_types_export_fixture",
        "cell_id": "allen_fixture_cell_1",
        "metadata": {"species": "mouse", "source": "unit_test_export"},
        "sweeps": [],
    }
    for idx, protocol in enumerate(base["protocols"]):
        allen_payload["sweeps"].append(
            {
                "sweep_number": idx,
                "split": protocol["split"],
                "current_uA": protocol["current_uA"],
                "dt_ms": protocol["dt_ms"],
                "stimulus_start_ms": protocol["pulse_start_ms"],
                "stimulus_end_ms": protocol["pulse_end_ms"],
                "voltage_mv": protocol["voltage_mv"],
            }
        )
    source = tmp_path / "allen_export.json"
    converted = tmp_path / "converted.json"
    source.write_text(json.dumps(allen_payload), encoding="utf-8")

    dataset = import_allen_sweep_json(source, converted)
    primitive_dir = tmp_path / "primitive"
    report_dir = tmp_path / "report"
    fit_primitive_to_ephys(converted, primitive_dir)
    report = verify_external_ephys(primitive_dir, converted, report_dir)

    assert dataset["schema"] == "substrate-external-ephys-v1"
    assert dataset["cell_id"] == "allen_fixture_cell_1"
    assert report["status"] == "EXTERNAL EPHYS ADHESION PASSED"
    assert report["migration"]["status"] == "PRIMITIVE MIGRATION VERIFIED"


def test_import_ephys_csv(tmp_path: Path) -> None:
    fixture = tmp_path / "fixture.json"
    base = generate_hh_neuroml_fixture(fixture)
    csv_path = tmp_path / "external.csv"
    converted = tmp_path / "converted_csv.json"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "protocol_id",
                "split",
                "t_ms",
                "dt_ms",
                "current_uA",
                "duration_ms",
                "pulse_start_ms",
                "pulse_end_ms",
                "voltage_mv",
            ],
        )
        writer.writeheader()
        for protocol in base["protocols"]:
            for idx, voltage in enumerate(protocol["voltage_mv"][:200]):
                writer.writerow(
                    {
                        "protocol_id": protocol["protocol_id"],
                        "split": protocol["split"],
                        "t_ms": idx * protocol["dt_ms"],
                        "dt_ms": protocol["dt_ms"],
                        "current_uA": protocol["current_uA"],
                        "duration_ms": 200 * protocol["dt_ms"],
                        "pulse_start_ms": protocol["pulse_start_ms"],
                        "pulse_end_ms": min(protocol["pulse_end_ms"], 200 * protocol["dt_ms"]),
                        "voltage_mv": voltage,
                    }
                )

    dataset = import_ephys_csv(csv_path, converted, source_name="csv_external_fixture", cell_id="csv_cell_1")
    loaded = load_ephys_dataset(converted)

    assert dataset["source_hash"] == loaded["source_hash"]
    assert loaded["schema"] == "substrate-external-ephys-v1"
    assert loaded["source_name"] == "csv_external_fixture"
    assert loaded["cell_id"] == "csv_cell_1"
    assert len(loaded["protocols"]) == 6
