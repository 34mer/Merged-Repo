from __future__ import annotations

from pathlib import Path
from typer.testing import CliRunner

from hsm.cli import app
from hsm.constraints import build_constraint_packet, verify_constraint_packet
from hsm.migrate import migrate_substrate
from hsm.parent_chain import verify_parent_chain
from hsm.substrate import build_source_substrate, verify_substrate_constraints
from hsm.translate import translate_to_synthetic
from hsm.verify import verify_hsm


def test_hsm_constraint_packet_hash_deterministic(tmp_path: Path) -> None:
    a = build_constraint_packet(tmp_path / "a")
    b = build_constraint_packet(tmp_path / "b")
    assert a["constraint_packet_hash"] == b["constraint_packet_hash"]
    assert a["constraint_count"] == 15
    assert a["human_constraint_count"] == 13
    assert a["bridge_constraint_count"] == 2
    assert verify_constraint_packet(a)["status"] == "PASS"


def test_hsm_parent_chain_verifies(tmp_path: Path) -> None:
    report = verify_parent_chain(tmp_path / "parent.json")
    assert report["verified"] is True
    assert report["status"] == "BOUNDARY-TO-BIOLOGY PRIMITIVE CHAIN VERIFIED"
    assert report["primitive_count"] >= 8


def test_hsm_translation_migration_and_verify(tmp_path: Path) -> None:
    constraints_dir = tmp_path / "constraints"
    parent_path = tmp_path / "parent.json"
    source_dir = tmp_path / "source"
    synthetic_dir = tmp_path / "synthetic"
    migration_dir = tmp_path / "migration"
    report_path = tmp_path / "verification.json"

    packet = build_constraint_packet(constraints_dir)
    parent = verify_parent_chain(parent_path)
    source = build_source_substrate(constraints_dir, parent_path, source_dir)
    synthetic = translate_to_synthetic(source_dir, synthetic_dir)
    migration = migrate_substrate(synthetic_dir, out=migration_dir)
    report = verify_hsm(source_dir, synthetic_dir, migration_dir, constraints_dir / "constraints.json", parent_path, report_path)

    assert verify_substrate_constraints(source, packet["constraint_packet_hash"], parent["parent_chain_hash"])
    assert synthetic["constraint_signature"]["constraint_packet_hash"] == packet["constraint_packet_hash"]
    assert migration["state_divergence"] == 0.0
    assert report["status"] == "PASS"
    assert report["controls_failed_as_expected"] is True


def test_hsm_prove_command(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    runner = CliRunner()
    result = runner.invoke(app, ["prove"])
    assert result.exit_code == 0, result.output
    assert "HUMAN SUBSTRATE MIGRATION IS EMPIRICALLY POSSIBLE" in result.output
    assert "Status: PASS" in result.output
    assert Path("reports/hsm_v0_verification.json").exists()
    assert Path("reports/hsm_v0_summary.md").exists()
