from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PlaylistCreate(BaseModel):
    name: str
    description: str | None = None
    is_public: bool = True


class PlaylistUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    is_public: bool | None = None


class PlaylistResponse(BaseModel):
    id: int
    name: str
    description: str | None
    is_public: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)