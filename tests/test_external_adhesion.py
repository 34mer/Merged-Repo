from __future__ import annotations

from pathlib import Path

from substrate.external.adhesion import (
    fit_primitive_to_ephys,
    generate_hh_neuroml_fixture,
    run_hh_neuroml_adhesion,
    verify_external_ephys,
)
from substrate.external.ephys import load_ephys_dataset


def test_generate_hh_neuroml_fixture(tmp_path: Path) -> None:
    source = tmp_path / "hh_fixture.json"
    dataset = generate_hh_neuroml_fixture(source)
    loaded = load_ephys_dataset(source)

    assert loaded["schema"] == "substrate-external-ephys-v1"
    assert loaded["source_name"] == "canonical_hh_neuroml_style_fixture"
    assert loaded["source_hash"] == dataset["source_hash"]
    assert len(loaded["protocols"]) == 6
    assert {row["split"] for row in loaded["protocols"]} == {"train", "heldout"}


def test_external_ephys_fit_verify_and_migration(tmp_path: Path) -> None:
    source = tmp_path / "hh_fixture.json"
    primitive_dir = tmp_path / "primitive"
    report_dir = tmp_path / "report"

    generate_hh_neuroml_fixture(source)
    primitive = fit_primitive_to_ephys(source, primitive_dir)
    report = verify_external_ephys(primitive_dir, source, report_dir)

    assert primitive["layer"] == "external_ephys_adhered_neuron"
    assert report["schema"] == "substrate-external-adhesion-v1"
    assert report["status"] == "EXTERNAL EPHYS ADHESION PASSED"
    assert report["heldout_summary"]["heldout_score"] >= 0.80
    assert report["migration"]["status"] == "PRIMITIVE MIGRATION VERIFIED"
    assert report["migration"]["state_divergence"] == 0.0
    honest_controls = [row for row in report["controls"] if row["mode"] != "behavior_only_leakage"]
    assert honest_controls
    assert all(row["failed_as_expected"] for row in honest_controls)
    assert (report_dir / "external_ephys_adhesion_report.json").exists()


def test_run_hh_neuroml_adhesion(tmp_path: Path) -> None:
    report = run_hh_neuroml_adhesion(tmp_path)
    assert report["status"] == "HH NEUROML ADHESION PASSED"
    assert report["adhesion_report"]["status"] == "EXTERNAL EPHYS ADHESION PASSED"
    assert (tmp_path / "hh_neuroml_adhesion_report.json").exists()
