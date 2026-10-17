from pathlib import Path
from typing import Any

import yaml


def get_reader_yaml(config_path: Path) -> dict[str, Any]:

    configs: dict[str, Any] = {}

    for file in config_path.glob("*.yaml"):
        with open(file, "r", encoding="utf-8") as f:
            configs[file.stem] = yaml.safe_load(f)

    return configs
