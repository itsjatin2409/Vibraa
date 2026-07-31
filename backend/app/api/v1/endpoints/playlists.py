from fastapi import APIRouter

from app.models.playlist import PlaylistCreate

router = APIRouter(
    prefix="/playlists",
    tags=["Playlists"],
)


@router.post("/")
async def create_playlist(payload: PlaylistCreate):
    return {
        "success": True,
        "message": "Playlist created successfully.",
        "data": payload.model_dump(),
    }