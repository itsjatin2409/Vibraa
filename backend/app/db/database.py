from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


DATABASE_URL = "sqlite:///./vibraa.db"


class Base(DeclarativeBase):
    pass


engine = create_engine(
    DATABASE_URL,
    echo=True,
)