from pathlib import Path
from typing import Any

import yaml


def get_reader_yaml(config_path: Path) -> dict[str, Any]:
    """
    Loads all YAML configuration files present in a
    specified directory.

    Parameters
    ----------
    config_path : Path
        Path to the directory containing the configuration files.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing all the loaded configurations.
        The key corresponds to the name of the YAML file, and the
        value corresponds to the file's content converted into
        a Python structure.
    """

    # Initialize the dictionary that will store all configurations
    # loaded from the YAML files.
    configs: dict[str, Any] = {}

    try:
        # Checks if the configuration directory exists.
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration directory not found: {config_path}")

        # Checks if the configuration path exists.
        if not config_path.is_dir():
            raise NotADirectoryError(
                f"The specified path is not a directory: {config_path}"
            )

        # Iterates through all files with the .yaml extension
        for file in config_path.glob("*.yaml"):
            # Opens the YAML file in read mode, using
            # UTF-8 encoding to ensure compatibility.
            with open(file, "r", encoding="utf-8") as f:
                # Loads the YAML content securely using
                # yaml.safe_load, which prevents the execution of arbitrary code.
                configs[file.stem] = yaml.safe_load(f)

        # Returns the dictionary containing all loaded settings.
        return configs

    except yaml.YAMLError as error:
        raise ValueError(f"YAML_ERROR: error processing YAML -> {error}") from error
