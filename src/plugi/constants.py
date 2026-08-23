# TODO: Validate
"""Constants."""

from collections.abc import Mapping, Sequence
from pathlib import Path

PLUGI_PATH = Path(__file__).parent
FILES_PATH = PLUGI_PATH / "_files"

type JSON_VALUE = (
    str | int | float | bool | Mapping[str, JSON_VALUE] | Sequence[JSON_VALUE] | None
)
"""Anything that can appear in a parsed JSON document."""
