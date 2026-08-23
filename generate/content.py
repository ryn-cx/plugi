# TODO: Validate
"""Rebuilds ContentModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, PLUGI_PATH
from generate.utils import download_if_missing
from plugi import Plugi

CONTENT_IDS = [
    "100004422",
    "200288826",
    "300018492",
]

SEASON_CONTENT_ID = "300018492"
SEASON = 2
SEASON_NAME = f"{SEASON_CONTENT_ID} season {SEASON}"
"""The recording of the series asked for one season at a time."""


# TODO: Validate
def generate_content(client: Plugi) -> None:
    """Rebuild ContentModel."""
    for content_id in CONTENT_IDS:
        download_if_missing(
            FILES_PATH,
            "ContentModel",
            content_id,
            lambda content_id=content_id: client.content.download(content_id),
        )
    download_if_missing(
        FILES_PATH,
        "ContentModel",
        SEASON_NAME,
        lambda: client.content.download(SEASON_CONTENT_ID, season=SEASON),
    )
    generate_model(FILES_PATH, PLUGI_PATH, "ContentModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_content(Plugi(build_client_automatically()))
