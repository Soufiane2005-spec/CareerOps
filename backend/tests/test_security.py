
from app.core.security import hash_password, verify_password


def test_hash_password():
    password = "CareerOps123!"
    hashed = hash_password(password)

    assert hashed != password
    assert hashed.startswith("$argon2id$")


def test_verify_correct_password():
    password = "CareerOps123!"
    hashed = hash_password(password)

    assert verify_password(password, hashed) is True


def test_verify_incorrect_password():
    password = "CareerOps123!"
    hashed = hash_password(password)

    assert verify_password("WrongPassword123!", hashed) is False


def test_same_password_different_hashes():
    password = "CareerOps123!"

    hash1 = hash_password(password)
    hash2 = hash_password(password)

    assert hash1 != hash2
    assert verify_password(password, hash1) is True
    assert verify_password(password, hash2) is True
