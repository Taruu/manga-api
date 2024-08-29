from datetime import datetime
from pathlib import Path
from typing import Optional
import enum

from sqlalchemy import create_engine
from sqlmodel import Field, SQLModel, Enum, Column, Relationship

from .config import database_url


class SourceHost(str, enum.Enum):
    e_hentai = 0
    hitomi_la = 1


# class TagType(str, enum.Enum):
#     # https://ehwiki.org/wiki/Namespace
#     temp = "temp"
#     reclass = "reclass"
#     metadata = "metadata"
#     artist = "artist"
#     cosplayer = "cosplayer"
#     language = "language"
#     group = "group"
#     character = "character"
#     parody = "parody"
#     other = "other"
#     male = "male"
#     female = "female"
#     mixed = "mixed"

class TagsNovelLink(SQLModel, table=True):
    tag_id: int | None = Field(default=None, foreign_key="tag.id", primary_key=True)
    novel_id: int | None = Field(default=None, foreign_key="visualnovel.id", primary_key=True)


class VisualNovel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    gid: int | None = Field(default=None, index=True)
    token: str | None = Field(default=None, index=True)

    archive_path: Path
    thumb_path: Path

    created_at: datetime
    added_at: datetime = Field(default_factory=lambda: datetime.now())

    title: str = Field(index=True)
    title_jpn: str = Field(index=True)

    file_count: int = Field(default=0)
    file_size: int = Field(default=0)

    rating: float
    source_mirror: list["SourceMirror"] = Relationship(back_populates="novel")
    tags: list["Tag"] = Relationship(back_populates="heroes", link_model=TagsNovelLink)
    torrents: list["NovelTorrent"] = Relationship(back_populates="novel")


class SourceMirror(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    novel_id: int | None = Field(default=None, foreign_key="visualnovel.id", primary_key=True)
    novel: VisualNovel = Relationship(back_populates="source_mirror")
    host: SourceHost = Field(default=-1)
    url: str


class TagType(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    name: str = Field(unique=True)
    tags: list["Tag"] = Relationship(back_populates="tag_type")


class Tag(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tag_type_id: int | None = Field(default=None, foreign_key="tagtype.id", primary_key=True)
    tag_type: TagType | None = Relationship(back_populates="tags")

    name: str = Field(unique=True, index=True)
    novels: list[VisualNovel] = Relationship(back_populates="tags", link_model=TagsNovelLink)


class NovelTorrent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Auto-incrementing primary key
    novel_id: int | None = Field(default=None, foreign_key="visualnovel.id")

    added: datetime

    novel: VisualNovel = Relationship(back_populates="torrents")
    hash: str = Field(index=True)
    name: str = Field(index=True)
    t_size: int
    f_size: int


connect_args = {"check_same_thread": False}
engine = create_engine(database_url, echo=False, connect_args=connect_args)


def create_db_and_tables():
    """Create database model"""
    SQLModel.metadata.create_all(engine)
