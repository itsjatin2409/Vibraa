from sqlalchemy.orm import Session

from app.models.playlist import Playlist
from app.repositories.playlist_repository import PlaylistRepository
from app.schemas.playlist import PlaylistCreate, PlaylistUpdate


class PlaylistService:

    @staticmethod
    def create_playlist(
        db: Session,
        playlist_data: PlaylistCreate,
    ) -> Playlist:
        return PlaylistRepository.create(
            db=db,
            playlist_data=playlist_data,
        )

    @staticmethod
    def get_playlists(
        db: Session,
    ) -> list[Playlist]:
        return PlaylistRepository.get_all(db)

    @staticmethod
    def get_playlist(
        db: Session,
        playlist_id: int,
    ) -> Playlist | None:
        return PlaylistRepository.get_by_id(
            db=db,
            playlist_id=playlist_id,
        )

    @staticmethod
    def update_playlist(
        db: Session,
        playlist_id: int,
        playlist_data: PlaylistUpdate,
    ) -> Playlist | None:
        playlist = PlaylistRepository.get_by_id(
            db=db,
            playlist_id=playlist_id,
        )

        if playlist is None:
            return None

        return PlaylistRepository.update(
            db=db,
            playlist=playlist,
            playlist_data=playlist_data,
        )

    @staticmethod
    def delete_playlist(
        db: Session,
        playlist_id: int,
    ) -> bool:
        playlist = PlaylistRepository.get_by_id(
            db=db,
            playlist_id=playlist_id,
        )

        if playlist is None:
            return False

        PlaylistRepository.delete(
            db=db,
            playlist=playlist,
        )

        return True