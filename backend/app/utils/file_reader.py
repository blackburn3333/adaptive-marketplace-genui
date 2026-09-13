"""
Filename: file_reader.py
Author: Jayendra Matarage
Created on: 9/6/2026 12:45 PM
Description: 
"""
import yaml
from pathlib import Path
from typing import Any, Dict

def load_yaml(yaml_path: str | Path) -> Dict[str, Any]:
    """
    Loads and verifies a YAML file using industry standards.

    Args:
        yaml_path: Path to the YAML file.

    Returns:
        Dict: The parsed YAML data.

    Raises:
        FileNotFoundError: If the path does not exist or is not a file.
        TypeError: If the root YAML element is not a dictionary/object.
        ValueError: If the YAML syntax is invalid.
    """
    path = Path(yaml_path)

    # Path Verification
    if not path.is_file():
        raise FileNotFoundError(f"No file found at: {path.absolute()}")

    # Safe Reading
    with path.open('r', encoding='utf-8') as stream:
        try:
            data = yaml.safe_load(stream)

            # Object Verification
            if data is not None and not isinstance(data, dict):
                raise TypeError(f"YAML root must be an object (dict), got {type(data).__name__}")

            return data if data is not None else {}

        except yaml.YAMLError as exc:
            raise ValueError(f"Error parsing YAML file: {exc}")