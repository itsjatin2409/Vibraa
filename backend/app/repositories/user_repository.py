from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.exceptions import DatabaseException
from app.models.user import User


class UserRepository:

    @staticmethod
    def get_by_email(
        db: Session,
        email: str,
    ) -> User | None:
        statement = select(User).where(
            User.email == email
        )

        return db.scalar(statement)

    @staticmethod
    def get_by_username(
        db: Session,
        username: str,
    ) -> User | None:
        statement = select(User).where(
            User.username == username
        )

        return db.scalar(statement)

    @staticmethod
    def get_by_id(
        db: Session,
        user_id: int,
    ) -> User | None:
        statement = select(User).where(
            User.id == user_id
        )

        return db.scalar(statement)

    @staticmethod
    def create(
        db: Session,
        email: str,
        username: str,
        hashed_password: str,
    ) -> User:
        try:
            user = User(
                email=email,
                username=username,
                hashed_password=hashed_password,
            )

            db.add(user)
            db.commit()
            db.refresh(user)

            return user

        except SQLAlchemyError:
            db.rollback()

            raise DatabaseException(
                "Failed to create user"
            )