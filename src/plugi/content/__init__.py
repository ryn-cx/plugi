# TODO: Validate
"""Contains the Content class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from plugi.base_api_endpoint import BaseEndpoint
from plugi.content.models import ContentModel, model_validate_json
from plugi.exceptions import ContentNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())

PAGE_SIZE_IN_SEASON = 20
"""Episodes a page of a season holds, which is what the website asks for."""


# TODO: Validate
class Content(BaseEndpoint):
    """Manage the content file.

    A movie, a series, or a single episode are all content, the `type` field of
    the response tells them apart. A series embeds its seasons and episodes in
    `children`.

    Source: https://tubitv.com/{movies,series,tv-shows}/{content_id}/{slug}

    Example request:
        - GET /api/v3/content?
            - app_id=tubitv&
            - platform=web&
            - content_id={content_id}&
            - device_id={device_id}&
            - include_channels=true&
            - pagination[season]={season}&
            - pagination[page_in_season]={page_in_season}&
            - pagination[page_size_in_season]=20&
            - limit_resolutions[]=h264_1080p&
            - video_resources[]=hlsv6&
            - images[posterarts]=w408h583_poster
            - HTTP/2
        - Host: content-cdn.production-public.tubi.io
        - User-Agent: __REDACTED__
        - Accept: */*
        - Accept-Language: en-US
        - Accept-Encoding: gzip, deflate, br, zstd
        - Referer: https://tubitv.com/
        - Accept-Version: ~5.0.0
        - x-capability: {"content_types":["se"]}
        - Origin: https://tubitv.com
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: cross-site
        - Authorization: Bearer __REDACTED__
        - Connection: keep-alive
        - Priority: u=0
        - TE: trailers
    """

    # TODO: Validate
    def __call__(
        self,
        content_id: str,
        *,
        season: int | None = None,
        page_in_season: int = 1,
        page_size_in_season: int = PAGE_SIZE_IN_SEASON,
        include_channels: bool = True,
    ) -> ContentModel:
        """Look the content up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                content_id,
                season=season,
                page_in_season=page_in_season,
                page_size_in_season=page_size_in_season,
                include_channels=include_channels,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        content_id: str,
        *,
        season: int | None = None,
        page_in_season: int = 1,
        page_size_in_season: int = PAGE_SIZE_IN_SEASON,
        include_channels: bool = True,
    ) -> str:
        """Download the content file."""
        log_id = self.get_log_id(self.download, locals())
        # The image renditions and video resources are the ones the website asks
        # for, they decide which images and streams are returned.
        params: dict[str, Any] = {
            "content_id": content_id,
            "include_channels": str(include_channels).lower(),
            "limit_resolutions[]": ["h264_1080p", "h265_1080p"],
            "video_resources[]": [
                "hlsv6_widevine_nonclearlead",
                "hlsv6_playready_psshv0",
                "hlsv6_fairplay",
                "hlsv6",
            ],
            "creator_tensor_app_images[logo]": "w100h100_logo",
            "creator_tensor_app_images[title_art]": "w430h180_title",
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
        }
        # Without a season every season is returned, with one the response only
        # holds that season.
        if season is not None:
            params["pagination[season]"] = season
            params["pagination[page_in_season]"] = page_in_season
            params["pagination[page_size_in_season]"] = page_size_in_season

        try:
            return self._client.download(
                endpoint="api/v3/content",
                params=params,
                # `se` marks support for series.
                headers={"x-capability": '{"content_types":["se"]}'},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise ContentNotFoundError(
                content_id,
                err.status_code,
                err.response,
            ) from err

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ContentModel:
        """Read a downloaded content file into its model."""
        return model_validate_json(data, log_id or self.default_log_id)
