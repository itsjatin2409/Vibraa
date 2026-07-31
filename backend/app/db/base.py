from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from app.db.database import Base
from app.models.playlist import Playlist

__all__ = ["Base", "Playlist"]

DATABASE_URL = "sqlite:///./vibraa.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

Base = declarative_base()
