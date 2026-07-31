from fastapi import FastAPI

from app.api.v1.router import api_router
from app.config.settings import settings
from app.core.logger import logger
from app.core.exceptions import VibraaException
from app.core.handlers import vibraa_exception_handler

app = FastAPI(
    title=settings.APP_NAME,
    description="AI-Powered Music Platform",
    version=settings.APP_VERSION,
)

logger.info("Starting Vibraa Backend")

app.add_exception_handler(
    VibraaException,
    vibraa_exception_handler,
)

app.include_router(api_router)