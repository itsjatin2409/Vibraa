from pydantic import BaseModel, Field


class PlaylistCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    description: str = Field(default="", max_length=500)
    is_public: bool = True


class PlaylistResponse(BaseModel):
    name: str
    description: str
    is_public: bool