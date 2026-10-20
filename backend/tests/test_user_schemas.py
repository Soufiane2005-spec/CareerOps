
import pytest
from pydantic import ValidationError

from app.schemas.user import UserCreate


def test_valid_user():
    user = UserCreate(
        email="student@example.com",
        password="TestPassword123!"
    )

    assert user.email == "student@example.com"


def test_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(
            email="invalid-email",
            password="TestPassword123!"
        )


def test_short_password():
    with pytest.raises(ValidationError):
        UserCreate(
            email="student@example.com",
            password="12345"
        )
