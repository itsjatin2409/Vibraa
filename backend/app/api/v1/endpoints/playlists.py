from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.playlist import (
    PlaylistCreate,
    PlaylistResponse,
    PlaylistUpdate,
)
from app.services.playlist_service import PlaylistService


router = APIRouter(
    prefix="/playlists",
    tags=["Playlists"],
)


@router.post(
    "/",
    response_model=PlaylistResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_playlist(
    playlist_data: PlaylistCreate,
    db: Session = Depends(get_db),
):
    return PlaylistService.create_playlist(
        db=db,
        playlist_data=playlist_data,
    )


@router.get(
    "/",
    response_model=list[PlaylistResponse],
)
def get_playlists(
    db: Session = Depends(get_db),
):
    return PlaylistService.get_playlists(db=db)


@router.get(
    "/{playlist_id}",
    response_model=PlaylistResponse,
)
def get_playlist(
    playlist_id: int,
    db: Session = Depends(get_db),
):
    playlist = PlaylistService.get_playlist(
        db=db,
        playlist_id=playlist_id,
    )

    if playlist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Playlist not found",
        )

    return playlist


@router.patch(
    "/{playlist_id}",
    response_model=PlaylistResponse,
)
def update_playlist(
    playlist_id: int,
    playlist_data: PlaylistUpdate,
    db: Session = Depends(get_db),
):
    playlist = PlaylistService.update_playlist(
        db=db,
        playlist_id=playlist_id,
        playlist_data=playlist_data,
    )

    if playlist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Playlist not found",
        )

    return playlist


@router.delete(
    "/{playlist_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_playlist(
    playlist_id: int,
    db: Session = Depends(get_db),
):
    deleted = PlaylistService.delete_playlist(
        db=db,
        playlist_id=playlist_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Playlist not found",
        )

    return None