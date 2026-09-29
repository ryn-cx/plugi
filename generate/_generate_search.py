from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_named_missing,
    load_named_ids,
    rebuild_model,
)

from generate.constants import GENERATOR_PATHS
from plugi import Plugi

MODEL_NAME = "SearchModel"


# TODO: Validate
class SearchId(RecordingId[Plugi]):
    written_as_fields = True

    query: str
    is_kids_mode: bool | None = None

    # TODO: Validate
    def download(self, client: Plugi) -> str:
        return client.search.download(**self.model_dump(exclude_unset=True))


SEARCH_REQUESTS = load_named_ids(GENERATOR_PATHS, MODEL_NAME, SearchId)


# TODO: Validate
def generate_search(client: Plugi) -> None:
    download_named_missing(GENERATOR_PATHS, MODEL_NAME, SEARCH_REQUESTS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, SearchId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_search(Plugi(build_client_automatically()))
