
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_database_connection():
    response = client.get("/db-check")

    assert response.status_code == 200
    assert response.json() == {
        "database": "connected"
    }
