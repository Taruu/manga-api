from datetime import datetime
from pathlib import Path
from typing import Optional
import enum
from sqlmodel import Field, SQLModel, Enum, Column


class TagType(str, enum.Enum):
    # https://ehwiki.org/wiki/Namespace
    metadata = "metadata"
    artist = "artist"
    cosplayer = "cosplayer"
    language = "language"
    group = "group"
    character = "character"
    parody = "parody"
    other = "other"
    male = "male"
    female = "female"
    mixed = "mixed"
    reclass = "reclass"


class VisualNovel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    created_at: datetime
    added_at: datetime = Field(default_factory=lambda: datetime.now())
    size: int = Field(default=0)
    pages: int
    path: Path = Field(unique=True)
    cover_filename: str


class Tag(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: Enum[TagType]
    name: str
