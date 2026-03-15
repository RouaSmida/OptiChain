from __future__ import annotations

import os
import pathlib
from typing import Any

import yaml


def _project_root() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[2]


def load_yaml_config(config_path: str | os.PathLike[str] = "configs/dev.yaml") -> dict[str, Any]:
    path = pathlib.Path(config_path)
    if not path.is_absolute():
        path = _project_root() / path

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}

    if not isinstance(data, dict):
        raise ValueError(f"Config at {path} must be a mapping")
    return data
