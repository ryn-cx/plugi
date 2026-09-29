# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from plugi.exceptions import ContentNotFoundError

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

SERIES_ID = "300018492"
"""The series a single season is asked for out of."""


# TODO: Validate
@pytest.mark.parametrize("content_id", CONTENT_IDS)
def test_download(client: Plugi, content_id: str) -> None:
    content = client.content(content_id)
    assert content.id == content_id


# TODO: Validate
def test_download_season(client: Plugi) -> None:
    # Asking for one season answers with the series carrying only that season.
    series = client.content(SERIES_ID, season=2)
    assert series.id == SERIES_ID
    assert [season.id for season in series.children or []] == ["2"]


# TODO: Validate
def test_download_invalid(client: Plugi) -> None:
    with pytest.raises(ContentNotFoundError):
        client.content.download("999999999999")
