"""
CLI integration tests for Synapse System

Tests the command-line interface functionality including
project initialization and manifest operations.
"""

import pytest
from pathlib import Path


def test_synapse_init(cli_runner, tmp_path):
    """
    Test synapse init command functionality.

    This test verifies that the synapse init command:
    1. Creates a .synapse.yml configuration file
    2. Creates the .claude/agents/ directory structure
    3. Creates the synapse-project-manager.md agent file

    Args:
        cli_runner: CLI runner fixture
        tmp_path: Pytest temporary directory fixture
    """
    # Execute synapse init in temporary directory
    result = cli_runner("init", ".", cwd=tmp_path)

    # Assert command succeeded
    assert result.exit_code == 0, f"Command failed: {result.stderr}"

    # Assert .synapse.yml file was created
    synapse_config = tmp_path / ".synapse.yml"
    assert synapse_config.exists(), ".synapse.yml file was not created"
    assert synapse_config.is_file(), ".synapse.yml is not a file"

    # Assert .claude/agents directory was created
    agents_dir = tmp_path / ".claude" / "agents"
    assert agents_dir.exists(), ".claude/agents directory was not created"
    assert agents_dir.is_dir(), ".claude/agents is not a directory"

    # Assert synapse-project-manager.md agent file exists
    project_manager_agent = agents_dir / "synapse-project-manager.md"
    assert project_manager_agent.exists(), "synapse-project-manager.md was not created"
    assert project_manager_agent.is_file(), "synapse-project-manager.md is not a file"

    # Verify the agent file has content
    assert project_manager_agent.stat().st_size > 0, "synapse-project-manager.md is empty"

    # Optional: Verify the .synapse.yml has expected structure
    config_content = synapse_config.read_text()
    assert len(config_content) > 0, ".synapse.yml is empty"


def test_manifest_list_snapshot(cli_runner, snapshot):
    """
    Test synapse manifest list command with snapshot testing.

    This test verifies that the manifest list command produces
    consistent output by comparing against a stored snapshot.

    Args:
        cli_runner: CLI runner fixture
        snapshot: Pytest snapshot fixture
    """
    # Execute synapse manifest list command
    result = cli_runner("manifest", "list")

    # Assert command succeeded
    assert result.exit_code == 0, f"Command failed: {result.stderr}"

    # Assert stdout is not empty
    assert result.stdout.strip(), "Command produced no output"

    # Compare output with snapshot
    snapshot.assert_match(result.stdout, "manifest_list_output.txt")