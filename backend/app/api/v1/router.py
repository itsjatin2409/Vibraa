from fastapi import APIRouter
from app.api.v1.endpoints import users
from app.api.v1.endpoints import profile

from app.api.v1.endpoints import playlists
from app.api.v1.endpoints import system

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(profile.router)

api_router.include_router(
    system.router,
    tags=["System"],
)

api_router.include_router(
    playlists.router,
    tags=["Playlists"],
)