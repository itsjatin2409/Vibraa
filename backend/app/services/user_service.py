from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:

    @staticmethod
    def register_user(
        db: Session,
        user_data: UserCreate,
    ) -> User:

        # Check whether email already exists
        existing_email = UserRepository.get_by_email(
            db=db,
            email=user_data.email,
        )

        if existing_email is not None:
            raise ValueError(
                "Email is already registered"
            )

        # Check whether username already exists
        existing_username = UserRepository.get_by_username(
            db=db,
            username=user_data.username,
        )

        if existing_username is not None:
            raise ValueError(
                "Username is already taken"
            )

        # Hash password before storing it
        hashed_password = hash_password(
            user_data.password
        )

        # Create user
        return UserRepository.create(
            db=db,
            email=user_data.email,
            username=user_data.username,
            hashed_password=hashed_password,
        )

    @staticmethod
    def authenticate_user(
        db: Session,
        email: str,
        password: str,
    ) -> str | None:

        # Find user
        user = UserRepository.get_by_email(
            db=db,
            email=email,
        )

        if user is None:
            return None

        # Verify password
        if not verify_password(
            plain_password=password,
            hashed_password=user.hashed_password,
        ):
            return None

        # Block inactive users
        if not user.is_active:
            return None

        # Generate JWT
        return create_access_token(
            user_id=user.id
        )