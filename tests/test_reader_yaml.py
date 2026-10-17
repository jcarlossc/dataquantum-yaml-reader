"""Tests for the YAML configuration reader."""

from pathlib import Path

from dataquantum_yaml_reader.reader_yaml import get_reader_yaml


def test_get_reader_yaml() -> None:
    """Load and validate YAML files from the config_test directory."""
    project_root = Path(__file__).resolve().parent.parent
    config_path = project_root / "config_test"

    configs = get_reader_yaml(config_path)

    assert configs["test_config"] == {
        "test": {
            "testing": "testing_yaml",
        }
    }