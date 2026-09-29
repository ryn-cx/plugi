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

MODEL_NAME = "ContentModel"


# TODO: Validate
class ContentId(RecordingId[Plugi]):
    written_as_fields = True

    content_id: str

    # TODO: Validate
    def download(self, client: Plugi) -> str:
        return client.content.download(**self.model_dump(exclude_unset=True))


CONTENT_REQUESTS = load_named_ids(GENERATOR_PATHS, MODEL_NAME, ContentId)


# TODO: Validate
def generate_content(client: Plugi) -> None:
    download_named_missing(GENERATOR_PATHS, MODEL_NAME, CONTENT_REQUESTS, client)
    rebuild_model(GENERATOR_PATHS, MODEL_NAME, ContentId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_content(Plugi(build_client_automatically()))
