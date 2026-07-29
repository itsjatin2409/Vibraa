from datetime import datetime, timezone

from fastapi import APIRouter

from app.config.settings import settings

router = APIRouter()


@router.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "message": f"Welcome to {settings.APP_NAME}",
        "status": "running",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/version")
async def version():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "api_version": "v1",
    }