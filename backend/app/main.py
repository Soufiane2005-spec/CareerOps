import logging

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging


configure_logging()

logger = logging.getLogger(__name__)

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.include_router(api_router)


@app.on_event("startup")
def startup_event():
    logger.info(
        "CareerOps API started | environment=%s",
        settings.app_env,
    )