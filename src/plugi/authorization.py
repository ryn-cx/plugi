# TODO: Validate
"""Helpers used to mint an anonymous access token.

Tubi does not hand out a token to anyone who asks for one. A device first
requests a signing key using a PKCE style challenge, then signs the token
request with an AWS SigV4 style HMAC chain derived from that key. Both steps
are reimplemented here so that no browser is required.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import secrets
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime

ACCOUNT_DOMAIN = "account.production-public.tubi.io"

ALGORITHM = "TUBI-HMAC-SHA256"
"""Name Tubi gives to its request signing algorithm."""

SIGNED_HEADERS = "content-type"
"""The only header that is covered by the signature."""


# TODO: Validate
def code_verifier() -> str:
    """Return a random code verifier for a signing key request."""
    # 16 bytes to match the web player.
    return secrets.token_hex(16)


# TODO: Validate
def code_challenge(verifier: str) -> str:
    """Return the challenge that proves ownership of `verifier`.

    Args:
        verifier: The code verifier the challenge is derived from.

    Returns:
        The URL safe base64 encoded SHA256 hash of the verifier.
    """
    digest = hashlib.sha256(verifier.encode()).digest()
    return base64.urlsafe_b64encode(digest).decode()


# TODO: Validate
def timestamp(now: datetime) -> str:
    """Return `now` formatted the way the signature expects it."""
    return now.strftime("%Y%m%dT%H%M%SZ")


# TODO: Validate
def signature_params(
    body: str,
    signing_key: str,
    signed_at: str,
) -> dict[str, str | int]:
    """Return the query params that sign a token request.

    Args:
        body: The exact JSON body that will be sent.
        signing_key: The base64 encoded key returned by the signing key request.
        signed_at: The timestamp of the request, see `timestamp`.

    Returns:
        The `X-Tubi-*` params that must accompany the request.
    """
    body_hash = hashlib.sha256(body.encode()).hexdigest()
    canonical_request = (
        f"POST\n/device/anonymous/token\n\n{SIGNED_HEADERS}:application/json\n"
        f"\n{SIGNED_HEADERS}\n{body_hash}"
    )
    canonical_hash = hashlib.sha256(canonical_request.encode()).hexdigest()
    string_to_sign = f"{ALGORITHM}\n{signed_at}\n{canonical_hash}"

    key = b"TUBI" + base64.b64decode(signing_key)
    # The key is derived in two steps, first scoped to the day of the request
    # and then to Tubi's request namespace.
    date = signed_at.split("T", maxsplit=1)[0]
    key = hmac.new(key, date.encode(), hashlib.sha256).digest()
    key = hmac.new(key, b"tubi_request", hashlib.sha256).digest()
    signature = hmac.new(key, string_to_sign.encode(), hashlib.sha256).hexdigest()

    return {
        "X-Tubi-Algorithm": ALGORITHM,
        "X-Tubi-Date": signed_at,
        # Seconds the signature stays valid for.
        "X-Tubi-Expires": 30,
        "X-Tubi-SignedHeaders": SIGNED_HEADERS,
        "X-Tubi-Signature": signature,
    }
