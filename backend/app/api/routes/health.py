from fastapi import APIRouter 

from app.core.config import get_settings 

router = APIRouter()

settings = get_settings()

@router.get("/health")
def health_check():
    return{
        "status":"ok",
        "environment": settings.app_env,
    }
@router.get("/ready")
def readiness_check():
    return {
        "status" : "ready",
        "environment" : settings.app_env,
    }