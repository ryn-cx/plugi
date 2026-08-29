# TODO: Validate
"""Constants."""

from pathlib import Path

FILES_PATH = Path(__file__).parent / "_files"
"""Where the recorded responses live."""

IDS_PATH = Path(__file__).parent / "ids"
"""Where the ids each model's responses are recorded for live."""

PLUGI_PATH = Path(__file__).parent.parent / "src" / "plugi"
"""The package the models are written into."""
