# TODO: Validate
"""Rebuilds ContentModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, PLUGI_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from plugi import Plugi

CONTENT_REQUESTS = load_ids("ContentModel")
"""What each recording of a content response was downloaded with."""


# TODO: Validate
def generate_content(client: Plugi) -> None:
    """Rebuild ContentModel."""
    for name, arguments in CONTENT_REQUESTS.items():
        download_if_missing(
            FILES_PATH,
            "ContentModel",
            name,
            lambda arguments=arguments: client.content.download(**arguments),
        )
    rebuild_model(FILES_PATH, PLUGI_PATH, "ContentModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_content(Plugi(build_client_automatically()))
