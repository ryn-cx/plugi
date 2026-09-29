# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from plugi.exceptions import ResourceNotFoundError

if TYPE_CHECKING:
    from plugi import Plugi

SITEMAP_NAMES = [
    pytest.param("movies-1", id="movies"),
    pytest.param("category/featured", id="category"),
]


# TODO: Validate
def test_download_index(client: Plugi) -> None:
    names = client.sitemap_index()
    assert "movies-1" in names
    assert "tv-shows-1" in names
    assert all(not name.endswith(".xml") for name in names)


# TODO: Validate
@pytest.mark.parametrize("name", SITEMAP_NAMES)
def test_download(client: Plugi, name: str) -> None:
    urls = client.sitemap(name)
    assert urls
    assert all(url.startswith("https://tubitv.com/") for url in urls)


# TODO: Validate
def test_download_invalid(client: Plugi) -> None:
    with pytest.raises(ResourceNotFoundError):
        client.sitemap.download("not-a-sitemap")
