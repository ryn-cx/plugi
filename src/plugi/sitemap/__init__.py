# TODO: Validate
from __future__ import annotations

from logging import NullHandler, getLogger
from xml.etree.ElementTree import fromstring

from plugi.base_api_endpoint import BaseEndpoint

logger = getLogger(__name__)
logger.addHandler(NullHandler())

LOCATION_TAG = "{http://www.sitemaps.org/schemas/sitemap/0.9}loc"
SITEMAPS_PATH = "sitemaps"


# TODO: Validate
def locations(data: str) -> list[str]:
    root = fromstring(data)  # noqa: S314
    return [
        element.text for element in root.iter(LOCATION_TAG) if element.text is not None
    ]


# TODO: Validate
class SitemapIndex(BaseEndpoint):
    # TODO: Validate
    def __call__(self) -> list[str]:
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(), log_id)

    # TODO: Validate
    def download(self) -> str:
        log_id = self.get_log_id(self.download, locals())
        return self._client.download_website("sitemap.xml", log_id=log_id)

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> list[str]:  # noqa: ARG002
        return [
            location.rpartition(f"/{SITEMAPS_PATH}/")[2].removesuffix(".xml")
            for location in locations(data)
        ]


# TODO: Validate
class Sitemap(BaseEndpoint):
    # TODO: Validate
    def __call__(self, name: str) -> list[str]:
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(name), log_id)

    # TODO: Validate
    def download(self, name: str) -> str:
        log_id = self.get_log_id(self.download, locals())
        return self._client.download_website(
            f"{SITEMAPS_PATH}/{name}.xml",
            log_id=log_id,
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> list[str]:  # noqa: ARG002
        return locations(data)
