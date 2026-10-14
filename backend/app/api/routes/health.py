from fastapi import APIRouter

from app.core.config import get_settings
from app.core.exceptions import ResourceNotFoundError
from app.schemas.health import HealthResponse


router = APIRouter()

settings = get_settings()


@router.get("/health", response_model=HealthResponse)
def health_check():
    return {
        "status": "ok",
        "environment": settings.app_env,
    }


@router.get("/ready", response_model=HealthResponse)
def readiness_check():
    return {
        "status": "ready",
        "environment": settings.app_env,
    }


@router.get("/test-error")
def test_error():
    raise ResourceNotFoundError("Test resource not found")