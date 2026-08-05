from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.exceptions import DatabaseException
from app.models.playlist import Playlist
from app.schemas.playlist import PlaylistCreate, PlaylistUpdate


class PlaylistRepository:

    @staticmethod
    def create(
        db: Session,
        playlist_data: PlaylistCreate,
    ) -> Playlist:
        try:
            playlist = Playlist(
                name=playlist_data.name,
                description=playlist_data.description,
                is_public=playlist_data.is_public,
            )

            db.add(playlist)
            db.commit()
            db.refresh(playlist)

            return playlist

        except SQLAlchemyError:
            db.rollback()
            raise DatabaseException(
                "Failed to create playlist"
            )

    @staticmethod
    def get_all(
        db: Session,
    ) -> list[Playlist]:
        statement = select(Playlist).order_by(
            Playlist.id
        )

        return list(
            db.scalars(statement).all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        playlist_id: int,
    ) -> Playlist | None:
        statement = select(Playlist).where(
            Playlist.id == playlist_id
        )

        return db.scalar(statement)

    @staticmethod
    def update(
        db: Session,
        playlist: Playlist,
        playlist_data: PlaylistUpdate,
    ) -> Playlist:
        try:
            update_data = playlist_data.model_dump(
                exclude_unset=True
            )

            for field, value in update_data.items():
                setattr(
                    playlist,
                    field,
                    value,
                )

            db.commit()
            db.refresh(playlist)

            return playlist

        except SQLAlchemyError:
            db.rollback()
            raise DatabaseException(
                "Failed to update playlist"
            )

    @staticmethod
    def delete(
        db: Session,
        playlist: Playlist,
    ) -> None:
        try:
            db.delete(playlist)
            db.commit()

        except SQLAlchemyError:
            db.rollback()
            raise DatabaseException(
                "Failed to delete playlist"
            )