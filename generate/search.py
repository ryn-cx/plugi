# TODO: Validate
"""Rebuilds SearchModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, PLUGI_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from plugi import Plugi

SEARCH_REQUESTS = load_ids("SearchModel")
"""What each recording of a search response was downloaded with."""


# TODO: Validate
def generate_search(client: Plugi) -> None:
    """Rebuild SearchModel."""
    for name, arguments in SEARCH_REQUESTS.items():
        download_if_missing(
            FILES_PATH,
            "SearchModel",
            name,
            lambda arguments=arguments: client.search.download(**arguments),
        )
    rebuild_model(FILES_PATH, PLUGI_PATH, "SearchModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search(Plugi(build_client_automatically()))
