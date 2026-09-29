# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from plugi.exceptions import HTTPError

if TYPE_CHECKING:
    from plugi import Plugi

QUERIES = [pytest.param("drago", id="drago")]


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Plugi, query: str) -> None:
    results = client.search(query)
    assert [container.id for container in results.containers or []] == ["search"]


# TODO: Validate
def test_download_kids_mode(client: Plugi) -> None:
    # Kids mode is the same query filtered down to what a child may watch.
    kids_mode = client.search("drago", is_kids_mode=True)
    everything = client.search("drago")
    # At runtime every id the model knows is a field, and the ones a response
    # does not carry are None, so only the ones that are set are counted.
    kids_mode_matches = kids_mode.contents.model_dump(exclude_none=True)
    everything_matches = everything.contents.model_dump(exclude_none=True)
    assert len(kids_mode_matches) < len(everything_matches)


# TODO: Validate
def test_download_invalid(client: Plugi) -> None:
    with pytest.raises(HTTPError):
        client.search.download("")
