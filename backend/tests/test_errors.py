from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_resource_not_found_error():
    response = client.get("/test-error")

    assert response.status_code == 404

    assert response.json() == {
        "detail": {
            "error": "resource_not_found",
            "message": "Test resource not found",
        }
    }