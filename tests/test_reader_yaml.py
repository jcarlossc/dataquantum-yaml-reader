from pathlib import Path

import pytest

from dataquantum_yaml_reader.reader_yaml import get_reader_yaml


def test_get_reader_yaml_success(tmp_path):
    """
    Verifies that all YAML files in the directory
    are loaded correctly.
    """

    (tmp_path / "logging.yaml").write_text(
        "level: INFO",
        encoding="utf-8",
    )

    # Executes the function.
    configs = get_reader_yaml(tmp_path)

    # Checks whether the files have been uploaded.
    assert "logging" in configs

    # Verifies the loaded content.
    assert configs["logging"]["level"] == "INFO"


def test_get_reader_yaml_directory_not_found():
    """
    Verifies whether FileNotFoundError is raised when
    the specified directory does not exist.
    """

    config_path = Path("nonexistent_directory")

    with pytest.raises(FileNotFoundError):
        get_reader_yaml(config_path)


def test_get_reader_yaml_not_directory(tmp_path):
    """
    Verifies whether NotADirectoryError is raised when
    the provided path is not a directory.
    """

    # Creates a regular file.
    file = tmp_path / "config.yaml"
    file.write_text("test", encoding="utf-8")

    with pytest.raises(NotADirectoryError):
        get_reader_yaml(file)


def test_get_reader_yaml_invalid_yaml(tmp_path):
    """
    Verifies that a ValueError is raised when
    a YAML file has invalid syntax.
    """

    # Creates an invalid YAML.
    (tmp_path / "config.yaml").write_text(
        "host: localhost\nporta: [1,2",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="YAML_ERROR"):
        get_reader_yaml(tmp_path)
