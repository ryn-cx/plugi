# TODO: Validate
"""Contains the Search class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from plugi.base_api_endpoint import BaseEndpoint
from plugi.search.models import SearchModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
class Search(BaseEndpoint):
    """Manage the search file.

    Every match is in `contents`, keyed by content id, and the order they are
    meant to be shown in is a list of references in `containers`. A match is a
    movie, a series or a linear channel, told apart by its `type`.

    Source: https://tubitv.com/search/{query}

    Example request:
        - GET /api/v3/search?
            - images[posterarts]=w408h583_poster&
            - images[hero_422]=w422h360_hero&
            - images[hero_feature_desktop_tablet]=w1920h768_hero&
            - images[hero_feature_large_mobile]=w960h480_hero&
            - images[hero_feature_small_mobile]=w540h450_hero&
            - images[hero_feature]=w375h355_hero&
            - images[hero_16x9]=w1280h720_hero&
            - images[landscape_images]=w978h549_landscape&
            - images[linear_larger_poster]=w978h549_landscape&
            - images[backgrounds]=w1614h906_background&
            - images[title_art]=w430h180_title&
            - search={query}&
            - include_channels=true&
            - include_linear=true&
            - is_kids_mode=false&
            - include_apps=true&
            - app_images[logo]=w376h376_logo&
            - app_images[poster]=w408h583_poster
            - HTTP/2
        - Host: search.production-public.tubi.io
        - User-Agent: __REDACTED__
        - Accept: */*
        - Accept-Language: en-US
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://tubitv.com/
        - Origin: https://tubitv.com
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: cross-site
        - Authorization: Bearer __REDACTED__
        - Connection: keep-alive
    """

    # TODO: Validate
    def __call__(
        self,
        query: str,
        *,
        include_channels: bool = True,
        include_linear: bool = True,
        include_apps: bool = True,
        is_kids_mode: bool = False,
    ) -> SearchModel:
        """Run the search and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                query,
                include_channels=include_channels,
                include_linear=include_linear,
                include_apps=include_apps,
                is_kids_mode=is_kids_mode,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        query: str,
        *,
        include_channels: bool = True,
        include_linear: bool = True,
        include_apps: bool = True,
        is_kids_mode: bool = False,
    ) -> str:
        """Download the search file."""
        log_id = self.get_log_id(self.download, locals())
        # The image renditions are the ones the website asks for, they decide
        # which images are returned.
        params: dict[str, Any] = {
            "search": query,
            "include_channels": str(include_channels).lower(),
            "include_linear": str(include_linear).lower(),
            "include_apps": str(include_apps).lower(),
            "is_kids_mode": str(is_kids_mode).lower(),
            "images[posterarts]": "w408h583_poster",
            "images[hero_422]": "w422h360_hero",
            "images[hero_feature_desktop_tablet]": "w1920h768_hero",
            "images[hero_feature_large_mobile]": "w960h480_hero",
            "images[hero_feature_small_mobile]": "w540h450_hero",
            "images[hero_feature]": "w375h355_hero",
            "images[hero_16x9]": "w1280h720_hero",
            "images[landscape_images]": "w978h549_landscape",
            "images[linear_larger_poster]": "w978h549_landscape",
            "images[backgrounds]": "w1614h906_background",
            "images[title_art]": "w430h180_title",
            "app_images[logo]": "w376h376_logo",
            "app_images[poster]": "w408h583_poster",
        }
        return self._client.download(
            endpoint="api/v3/search",
            params=params,
            headers={},
            log_id=log_id,
            # Search is the one endpoint that lives on its own host.
            domain="search.production-public.tubi.io",
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> SearchModel:
        """Read a downloaded search file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)
