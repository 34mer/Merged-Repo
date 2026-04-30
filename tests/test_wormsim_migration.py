from __future__ import annotations

import shutil
from pathlib import Path

import numpy as np

from wormsim.checkpoint import file_hash, load_checkpoint, save_checkpoint, verify_hash
from wormsim.config import WormConfig
from wormsim.dynamics import run_steps
from wormsim.environment import initial_environment
from wormsim.organism import initial_state
from wormsim.verify import compare_from_checkpoints


def test_deterministic_update_repeats_exactly() -> None:
    config = WormConfig(seed=123)
    env_a = initial_environment(config)
    env_b = initial_environment(config)
    state_a = initial_state(config)
    state_b = initial_state(config)

    _, final_a, traj_a = run_steps(config, env_a, state_a, 25)
    _, final_b, traj_b = run_steps(config, env_b, state_b, 25)

    np.testing.assert_array_equal(traj_a, traj_b)
    np.testing.assert_array_equal(final_a.neuron_state, final_b.neuron_state)
    np.testing.assert_array_equal(final_a.position, final_b.position)


def test_checkpoint_roundtrip_preserves_state(tmp_path: Path) -> None:
    config = WormConfig(seed=7)
    env = initial_environment(config)
    env, state, _ = run_steps(config, env, initial_state(config), 12)
    checkpoint = tmp_path / "checkpoint_t12.npz"

    digest = save_checkpoint(checkpoint, config, env, state)
    loaded_config, loaded_env, loaded_state = load_checkpoint(checkpoint)

    assert verify_hash(checkpoint, digest)
    assert loaded_config == config
    assert loaded_env == env
    assert loaded_state.step == state.step
    np.testing.assert_array_equal(loaded_state.neuron_state, state.neuron_state)
    np.testing.assert_array_equal(loaded_state.muscle_state, state.muscle_state)
    np.testing.assert_array_equal(loaded_state.position, state.position)
    np.testing.assert_array_equal(loaded_state.velocity, state.velocity)


def test_migration_verification_matches_identical_copied_checkpoint(tmp_path: Path) -> None:
    config = WormConfig(seed=42)
    env = initial_environment(config)
    env, state, _ = run_steps(config, env, initial_state(config), 40)
    source = tmp_path / "source" / "checkpoint_t40.npz"
    migrated = tmp_path / "migrated" / "checkpoint_t40.npz"
    digest = save_checkpoint(source, config, env, state)
    migrated.parent.mkdir(parents=True)
    shutil.copy2(source, migrated)

    assert file_hash(migrated) == digest
    report = compare_from_checkpoints(source, migrated, steps=50)

    assert report.status == "MIGRATION VERIFIED"
    assert report.checkpoint_hash_matched
    assert report.config_hash_matched
    assert report.max_trajectory_error == 0.0
