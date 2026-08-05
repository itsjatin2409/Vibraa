from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import VibraaException
from app.core.logger import logger


async def vibraa_exception_handler(
    request: Request,
    exc: VibraaException,
):
    logger.error(
        "Application error: %s",
        exc.message,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "message": exc.message,
            },
        },
    )