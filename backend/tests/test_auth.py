
import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.main import app
from app.db.base import Base
from app.db.database import get_db
from app.models.user import User
from app.core.security import verify_password


@pytest.fixture
def client():
    # Créer une base SQLite temporaire en mémoire
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    Base.metadata.create_all(bind=engine)

    # Remplacer PostgreSQL par SQLite pendant les tests
    def override_get_db():
        with Session(engine) as db:
            yield db

    app.dependency_overrides[get_db] = override_get_db

    try:
        with TestClient(app) as test_client:
            yield test_client, engine
    finally:
        app.dependency_overrides.pop(get_db, None)
        engine.dispose()


# TEST 1 : Inscription réussie (201)
def test_register_success(client):
    test_client, _ = client

    response = test_client.post(
        "/auth/register",
        json={
            "email": "student@example.com",
            "password": "CareerOps123!",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["email"] == "student@example.com"
    assert "id" in data
    assert "created_at" in data
    assert "password" not in data
    assert "hashed_password" not in data


# TEST 2 : E-mail déjà utilisé (409)
def test_register_duplicate_email(client):
    test_client, _ = client

    payload = {
        "email": "student@example.com",
        "password": "CareerOps123!",
    }

    first_response = test_client.post(
        "/auth/register",
        json=payload,
    )

    second_response = test_client.post(
        "/auth/register",
        json=payload,
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 409
    assert second_response.json()["detail"] == "Email already registered"


# TEST 3 : E-mail invalide (422)
def test_register_invalid_email(client):
    test_client, _ = client

    response = test_client.post(
        "/auth/register",
        json={
            "email": "invalid-email",
            "password": "CareerOps123!",
        },
    )

    assert response.status_code == 422


# TEST 4 : Vérification du hachage Argon2
def test_register_password_is_hashed(client):
    test_client, engine = client

    response = test_client.post(
        "/auth/register",
        json={
            "email": "secure@example.com",
            "password": "CareerOps123!",
        },
    )

    assert response.status_code == 201

    # Vérifier directement le contenu de la base
    with Session(engine) as db:
        user = db.scalar(
            select(User).where(
                User.email == "secure@example.com"
            )
        )

        assert user is not None
        assert user.hashed_password != "CareerOps123!"
        assert user.hashed_password.startswith("$argon2id$")

        assert verify_password(
            "CareerOps123!",
            user.hashed_password,
        ) is True
