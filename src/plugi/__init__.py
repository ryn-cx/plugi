# TODO: Validate
"""Contains the Plugi class."""

import json
import time
import uuid
from datetime import UTC, datetime, timedelta
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from plugi import authorization
from plugi.content import Content
from plugi.exceptions import AuthorizationError, HTTPError, ResourceNotFoundError
from plugi.search import Search

logger = getLogger(__name__)
logger.addHandler(NullHandler())

WEBSITE = "https://tubitv.com"
PLATFORM = "web"
# Tubi splits its API across hosts that otherwise take the same parameters, and
# this one answers for everything except search.
CONTENT_DOMAIN = "content-cdn.production-public.tubi.io"


# TODO: Validate
class Plugi:
    """Tubi API wrapper."""

    # TODO: Validate
    def __init__(
        self,
        get_around_client: GetAround | None = None,
        locale: str = "en-US",
        device_id: str | None = None,
    ) -> None:
        """Initialize the Plugi client.

        The client holds one attribute per endpoint, so `client.content(id)`
        looks a content up and `client.content.download(id)` and
        `client.content.load(data)` are the halves of it.
        """
        self.locale = locale
        self.get_around_client = get_around_client or GetAround()
        # Tubi ties an anonymous token to a device, any UUID is accepted.
        self.device_id = device_id or str(uuid.uuid4())
        self._access_token_value = ""
        self._token_expires_at = datetime.now(tz=UTC)

        self.content = Content(self)
        self.search = Search(self)

    # TODO: Validate
    def _headers(self) -> dict[str, str]:
        return {
            # "Host": Set by httpx
            # "User-Agent": Set by httpx
            "Accept": "*/*",
            "Accept-Language": self.locale,
            # "Accept-Encoding": Set by httpx
            "Origin": WEBSITE,
            "Referer": f"{WEBSITE}/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
        }

    # TODO: Validate
    @property
    def _access_token(self) -> str:
        if not self._access_token_value or self._token_expires_at < datetime.now(UTC):
            self._download_access_token()
        return self._access_token_value

    # TODO: Validate
    def _download_signing_key(self, verifier: str) -> dict[str, str]:
        """Request the key that the token request is signed with."""
        response = self.get_around_client.post(
            f"https://{authorization.ACCOUNT_DOMAIN}/device/anonymous/signing_key",
            json={
                "challenge": authorization.code_challenge(verifier),
                # Version of the signing key request that the web player sends.
                "version": "1.0.0",
                "platform": PLATFORM,
                "device_id": self.device_id,
            },
            headers={**self._headers(), "content-type": "application/json"},
        )
        if response.status_code != HTTPStatus.OK:
            raise AuthorizationError(response.status_code, response.text)
        signing_key: dict[str, str] = response.json()
        return signing_key

    # TODO: Validate
    def _download_access_token(self) -> None:
        logger.debug("Downloading token:")
        start = time.monotonic()

        verifier = authorization.code_verifier()
        signing_key = self._download_signing_key(verifier)
        # The signature covers the exact bytes that are sent, so the body is
        # serialized once and passed through as-is.
        body = json.dumps(
            {
                "verifier": verifier,
                "id": signing_key["id"],
                "platform": PLATFORM,
                "device_id": self.device_id,
            },
            separators=(",", ":"),
        )
        signed_at = authorization.timestamp(datetime.now(tz=UTC))
        response = self.get_around_client.post(
            f"https://{authorization.ACCOUNT_DOMAIN}/device/anonymous/token",
            content=body,
            params=authorization.signature_params(body, signing_key["key"], signed_at),
            headers={**self._headers(), "content-type": "application/json"},
        )
        if response.status_code != HTTPStatus.OK:
            raise AuthorizationError(response.status_code, response.text)

        logger.debug("Downloaded token (%.4f s)", time.monotonic() - start)

        parsed = response.json()
        self._access_token_value = parsed["access_token"]
        self._token_expires_at = datetime.now(tz=UTC) + timedelta(
            seconds=parsed["expires_in"],
        )

    # TODO: Validate
    def download(
        self,
        endpoint: str,
        params: dict[str, Any],
        headers: dict[str, str],
        log_id: str,
        domain: str = CONTENT_DOMAIN,
    ) -> str:
        """Download from the API and return the body as text.

        `domain` selects the host the endpoint lives on, because Tubi splits its
        API across hosts that otherwise take the same parameters and token.
        """
        headers = {
            **self._headers(),
            "Accept-Version": "~5.0.0",
            **headers,
            "Authorization": f"Bearer {self._access_token}",
        }
        params = {
            "app_id": "tubitv",
            "platform": PLATFORM,
            "device_id": self.device_id,
            **params,
        }

        logger.debug("Downloading: %s", log_id)
        url = f"https://{domain}/{endpoint}"
        start = time.monotonic()
        response = self.get_around_client.get(url, params=params, headers=headers)

        if response.status_code != HTTPStatus.OK:
            if response.status_code == HTTPStatus.NOT_FOUND:
                raise ResourceNotFoundError(response.status_code, response.text)
            raise HTTPError(response.status_code, response.text)

        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return response.text
