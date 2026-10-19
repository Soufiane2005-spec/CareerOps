
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging


configure_logging()

logger = logging.getLogger(__name__)
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(
        "CareerOps API started | environment=%s",
        settings.app_env,
    )

    yield

    logger.info("CareerOps API stopped")


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    lifespan=lifespan,
)

app.include_router(api_router)
