from __future__ import annotations

from pathlib import Path
from typer.testing import CliRunner

from hsm.cli import app
from hsm.independent_constraints import build_independent_constraint_packets, verify_independent_packets
from hsm.independent_protocol import (
    build_independent_source_substrate,
    migrate_independent_substrate,
    prove_independent,
    translate_independent_to_synthetic,
    verify_independent_hsm,
)
from hsm.observable import evaluate_against_oracle
from hsm.parent_chain import verify_parent_chain


def test_independent_packets_are_distinct_and_verified(tmp_path: Path) -> None:
    packets = build_independent_constraint_packets(tmp_path / "constraints")
    result = verify_independent_packets(packets["construction"], packets["oracle"])
    assert result["status"] == "PASS"
    assert result["construction_packet_hash"] != result["oracle_packet_hash"]
    assert result["same_feature_set"] is True


def test_independent_protocol_passes_and_numeric_corruption_fails(tmp_path: Path) -> None:
    constraints = tmp_path / "constraints"
    source = tmp_path / "source"
    target = tmp_path / "target"
    migrated = tmp_path / "migration"
    parent = tmp_path / "parent.json"
    report_path = tmp_path / "report.json"

    packets = build_independent_constraint_packets(constraints)
    verify_parent_chain(parent)
    build_independent_source_substrate(constraints, parent, source)
    translate_independent_to_synthetic(source, target)
    migration = migrate_independent_substrate(target, out=migrated)
    report = verify_independent_hsm(constraints, source, target, migrated, report_path)

    assert report["status"] == "PASS"
    assert report["state_divergence"] == 0.0
    assert report["post_migration_independent_constraints_preserved"] is True
    assert report["controls_failed_as_expected"] is True

    corrupted = dict(migration["post_migration_observables"])
    key = next(iter(corrupted))
    corrupted[key] = 1.5
    assert evaluate_against_oracle(corrupted, packets["oracle"])["status"] == "FAIL"


def test_prove_independent_function_and_cli(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    report = prove_independent()
    assert report["status"] == "PASS"
    assert Path("reports/hsm_v0_1_verification.json").exists()

    runner = CliRunner()
    result = runner.invoke(app, ["prove-independent"])
    assert result.exit_code == 0, result.output
    assert "HUMAN-CONSTRAINED SUBSTRATE MIGRATION PRESERVED INDEPENDENT CONSTRAINTS" in result.output
    assert "Status: PASS" in result.output
