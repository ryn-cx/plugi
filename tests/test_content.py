# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from plugi.exceptions import ContentNotFoundError
from tests.utils import assert_error, download_and_save, parsed_json

if TYPE_CHECKING:
    from plugi import Plugi
    from plugi.content import Content

SERIES_ID = "300018492"
MOVIE_ID = "100004422"
EPISODE_ID = "200288826"
CONTENT_IDS = [SERIES_ID, MOVIE_ID, EPISODE_ID]
INVALID_CONTENT_ID = "999999999999"

SEASON = 2
SEASON_NAME = f"{SERIES_ID} season {SEASON}"


@pytest.fixture(scope="session")
def client(client: Plugi) -> Content:
    return client.content


@pytest.mark.parametrize("content_id", CONTENT_IDS)
def test_download(client: Content, content_id: str) -> None:
    download_and_save(client, content_id, lambda: client.download(content_id))


def test_download_season(client: Content) -> None:
    download_and_save(
        client,
        SEASON_NAME,
        lambda: client.download(SERIES_ID, season=SEASON),
    )


def test_download_invalid(client: Content) -> None:
    assert_error(
        client,
        INVALID_CONTENT_ID,
        lambda: client.download(INVALID_CONTENT_ID),
        ContentNotFoundError,
    )


@pytest.mark.parametrize("content_id", CONTENT_IDS)
def test_parse(client: Content, content_id: str) -> None:
    data = parsed_json(client, content_id)
    assert data.id == content_id


def test_parse_series(client: Content) -> None:
    data = parsed_json(client, SERIES_ID)
    assert data.type == "s"
    assert data.children
    # Every child of a series is a season that holds its own episodes.
    for season in data.children:
        assert season.children


def test_parse_movie(client: Content) -> None:
    data = parsed_json(client, MOVIE_ID)
    assert data.type == "v"
    assert data.children is None


def test_parse_episode(client: Content) -> None:
    data = parsed_json(client, EPISODE_ID)
    assert data.type == "v"
    assert data.episode_number


def test_parse_season(client: Content) -> None:
    data = parsed_json(client, SEASON_NAME)
    assert data.children
    # Requesting a single season filters out every other season.
    assert [season.id for season in data.children] == [str(SEASON)]
