# TODO: Validate
from __future__ import annotations

from datetime import UTC, datetime

from plugi import authorization

# Values captured from a browser session, they pin the signing algorithm so a
# refactor cannot silently change the bytes that get signed.
VERIFIER = "e0b6a1c8d3f2495a7b8c9d0e1f2a3b4c"
SIGNING_KEY = "TONi7Ry2Nc6sXEFoGKpxg/tW2DXj5Y/+HuJ6ipRVe/I="
SIGNED_AT = "20260729T211500Z"
BODY = '{"verifier":"abc","id":"def","platform":"web","device_id":"ghi"}'


def test_code_verifier_is_random() -> None:
    assert authorization.code_verifier() != authorization.code_verifier()
    # 16 random bytes, hex encoded.
    verifier_length = 32
    assert len(authorization.code_verifier()) == verifier_length


def test_code_challenge() -> None:
    assert (
        authorization.code_challenge(VERIFIER)
        == "_sbMgQ16TwCp7WoAKP2aeLEZTWBKvHkphaY6CL8N0jM="
    )


def test_timestamp() -> None:
    now = datetime(2026, 7, 29, 21, 15, 0, 123456, tzinfo=UTC)
    assert authorization.timestamp(now) == SIGNED_AT


def test_signature_params() -> None:
    params = authorization.signature_params(BODY, SIGNING_KEY, SIGNED_AT)
    assert params == {
        "X-Tubi-Algorithm": "TUBI-HMAC-SHA256",
        "X-Tubi-Date": SIGNED_AT,
        "X-Tubi-Expires": 30,
        "X-Tubi-SignedHeaders": "content-type",
        "X-Tubi-Signature": (
            "18a330627efaff5b0980a11bee9122bc0e30bd627b21fd285da3ac9c68d671ca"
        ),
    }
