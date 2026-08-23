# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from plugi.exceptions import HTTPError
from plugi.search.models import SearchModel
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from plugi import Plugi

QUERIES = [
    pytest.param("drago", id="drago"),
]

KIDS_MODE_NAME = "drago kids mode"
"""The recording of the same query with kids mode turned on."""


# TODO: Validate
class SearchTest(RecordedEndpoint):
    MODEL = SearchModel


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_download(client: Plugi, query: str) -> None:
    SearchTest.download_test(query, lambda: client.search.download(query))


# TODO: Validate
@pytest.mark.parametrize("query", QUERIES)
def test_parse(client: Plugi, query: str) -> None:
    results = client.search.load(SearchTest.recorded_content(query))
    assert [container.id for container in results.containers or []] == ["search"]


# TODO: Validate
def test_download_kids_mode(client: Plugi) -> None:
    SearchTest.download_test(
        KIDS_MODE_NAME,
        lambda: client.search.download("drago", is_kids_mode=True),
    )


# TODO: Validate
def test_parse_kids_mode(client: Plugi) -> None:
    # Kids mode is the same query filtered down to what a child may watch.
    kids_mode = client.search.load(SearchTest.recorded_content(KIDS_MODE_NAME))
    everything = client.search.load(SearchTest.recorded_content("drago"))
    # At runtime every id the model knows is a field, and the ones a response
    # does not carry are None, so only the ones that are set are counted.
    kids_mode_matches = kids_mode.contents.model_dump(exclude_none=True)
    everything_matches = everything.contents.model_dump(exclude_none=True)
    assert len(kids_mode_matches) < len(everything_matches)


# TODO: Validate
@pytest.mark.parametrize("query", [pytest.param("", id="query with nothing in it")])
def test_download_invalid(client: Plugi, query: str) -> None:
    SearchTest.error_test(query, lambda: client.search.download(query), HTTPError)
