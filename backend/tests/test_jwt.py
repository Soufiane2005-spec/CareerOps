
from datetime import datetime, timedelta, timezone

import jwt

from app.core.config import get_settings
from app.core.security import (
    create_access_token,
    decode_access_token,
)


def test_valid_access_token():
    token = create_access_token(1)

    assert decode_access_token(token) == 1


def test_invalid_access_token():
    assert decode_access_token("invalid-token") is None


def test_expired_access_token():
    settings = get_settings()
    now = datetime.now(timezone.utc)

    token = jwt.encode(
        {
            "sub": "1",
            "iat": now - timedelta(minutes=60),
            "exp": now - timedelta(minutes=30),
        },
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm,
    )

    assert decode_access_token(token) is None


def test_invalid_signature():
    token = create_access_token(1)

    header, payload, signature = token.split(".")

    replacement = "A" if signature[0] != "A" else "B"
    modified_signature = replacement + signature[1:]

    tampered_token = f"{header}.{payload}.{modified_signature}"

    assert decode_access_token(tampered_token) is None
