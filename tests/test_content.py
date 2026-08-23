# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from plugi.content.models import ContentModel
from plugi.exceptions import ContentNotFoundError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from plugi import Plugi

CONTENT_IDS = [
    # https://tubitv.com/series/300018492/the-thin-blue-line
    pytest.param("300018492", id="thin blue line series"),
    # https://tubitv.com/movies/100004422/teacher-of-the-year
    pytest.param("100004422", id="teacher of the year movie"),
    # https://tubitv.com/tv-shows/200288826/s01-e01-the-queen-s-birthday-present
    pytest.param("200288826", id="thin blue line episode"),
]

SEASON_NAME = "300018492 season 2"
"""The recording of the series asked for one season at a time."""


# TODO: Validate
class ContentTest(RecordedEndpoint):
    MODEL = ContentModel


# TODO: Validate
@pytest.mark.parametrize("content_id", CONTENT_IDS)
def test_download(client: Plugi, content_id: str) -> None:
    ContentTest.download_test(content_id, lambda: client.content.download(content_id))


# TODO: Validate
@pytest.mark.parametrize("content_id", CONTENT_IDS)
def test_parse(client: Plugi, content_id: str) -> None:
    content = client.content.load(ContentTest.recorded_content(content_id))
    assert content.id == content_id


# TODO: Validate
def test_download_season(client: Plugi) -> None:
    ContentTest.download_test(
        SEASON_NAME,
        lambda: client.content.download("300018492", season=2),
    )


# TODO: Validate
def test_parse_season(client: Plugi) -> None:
    # Asking for one season answers with the series carrying only that season.
    series = client.content.load(ContentTest.recorded_content(SEASON_NAME))
    assert series.id == "300018492"
    assert [season.id for season in series.children or []] == ["2"]


# TODO: Validate
@pytest.mark.parametrize(
    "content_id",
    [pytest.param("999999999999", id="content that does not exist")],
)
def test_download_invalid(client: Plugi, content_id: str) -> None:
    ContentTest.error_test(
        content_id,
        lambda: client.content.download(content_id),
        ContentNotFoundError,
    )
