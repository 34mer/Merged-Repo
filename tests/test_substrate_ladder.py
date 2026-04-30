from __future__ import annotations

from pathlib import Path

from substrate.channel.verify import verify_channel
from substrate.hydrogen.verify import verify_hydrogen
from substrate.ion_water.verify import verify_ion_water
from substrate.membrane.verify import verify_membrane
from substrate.migrate import migrate_checkpoint, save_checkpoint, verify_migration
from substrate.molecule.verify import verify_h2
from substrate.neuron.primitive import extract_synthetic_neuron_primitive
from substrate.neuron.verify import verify_neuron
from substrate.reports import write_ladder_report


def test_hydrogen_primitive_verifies() -> None:
    primitive = verify_hydrogen()
    assert primitive.verification["status"] == "HYDROGEN BOUNDARY OBJECT VERIFIED"
    assert primitive.observables["ionization_energy_ev"] > 13.0
    assert primitive.hash


def test_ladder_rungs_verify() -> None:
    assert verify_h2().verification["status"] == "MOLECULE BOUNDARY OBJECT VERIFIED"
    assert verify_ion_water().verification["status"] == "ION WATER PRIMITIVE VERIFIED"
    assert verify_membrane().verification["status"] == "MEMBRANE PRIMITIVE VERIFIED"
    assert verify_channel("sodium").verification["status"] == "CHANNEL PRIMITIVE VERIFIED"
    assert verify_channel("potassium").verification["status"] == "CHANNEL PRIMITIVE VERIFIED"
    neuron = verify_neuron()
    assert neuron.verification["status"] == "SINGLE NEURON PROCESS PRIMITIVE VERIFIED"
    assert neuron.observables["pulse_response"]["spike_count"] >= 1


def test_synthetic_neuron_and_migration(tmp_path: Path) -> None:
    primitive = extract_synthetic_neuron_primitive().to_dict()
    checkpoint = tmp_path / "checkpoint.json"
    migrated_dir = tmp_path / "migrated"
    save_checkpoint(primitive, checkpoint)
    manifest = migrate_checkpoint(checkpoint, migrated_dir)
    report = verify_migration(checkpoint, migrated_dir / checkpoint.name)
    assert manifest["checkpoint_hash_matched"]
    assert report["status"] == "PRIMITIVE MIGRATION VERIFIED"
    assert report["state_divergence"] == 0.0


def test_write_ladder_report(tmp_path: Path) -> None:
    report = write_ladder_report(tmp_path)
    assert report["status"] == "BOUNDARY TO BIOLOGY BOOTSTRAPPING LADDER COMPLETE"
    assert report["primitive_count"] >= 8
    assert (tmp_path / "boundary_to_neuron_ladder_report.json").exists()
    assert (tmp_path / "BOUNDARY_TO_NEURON_LADDER.md").exists()
    assert (tmp_path / "BOUNDARY_TO_BIOLOGY_BOOTSTRAPPING_LADDER_v0.1.md").exists()
