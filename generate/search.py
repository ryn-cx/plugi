# TODO: Validate
"""Rebuilds SearchModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, PLUGI_PATH
from generate.utils import download_if_missing
from plugi import Plugi

QUERIES = ["drago"]

KIDS_MODE_QUERY = "drago"
KIDS_MODE_NAME = f"{KIDS_MODE_QUERY} kids mode"
"""The recording of the same query with kids mode turned on."""


# TODO: Validate
def generate_search(client: Plugi) -> None:
    """Rebuild SearchModel."""
    for query in QUERIES:
        download_if_missing(
            FILES_PATH,
            "SearchModel",
            query,
            lambda query=query: client.search.download(query),
        )
    download_if_missing(
        FILES_PATH,
        "SearchModel",
        KIDS_MODE_NAME,
        lambda: client.search.download(KIDS_MODE_QUERY, is_kids_mode=True),
    )
    generate_model(FILES_PATH, PLUGI_PATH, "SearchModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search(Plugi(build_client_automatically()))
