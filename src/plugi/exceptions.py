"""Exceptions."""

from __future__ import annotations

from typing import Any


class PlugiError(Exception):
    """Base exception for Plugi."""

    response: str | dict[str, Any] | None = None


class HTTPError(PlugiError):
    """Raised when HTTP request fails with unexpected status code."""

    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


class AuthorizationError(HTTPError):
    """Raised when an anonymous access token could not be generated."""


class ResourceNotFoundError(HTTPError):
    """Raised when the API reports that the requested resource does not exist."""


class ContentNotFoundError(ResourceNotFoundError):
    """Raised when the requested content does not exist."""

    def __init__(
        self,
        content_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the content id and the originating response."""
        self.content_id = content_id
        super().__init__(status_code, response)
