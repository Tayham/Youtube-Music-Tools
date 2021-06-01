from dataclasses import dataclass


@dataclass
class SongClass:
    """Class for Song Data (Maybe incomplete depending on API)"""
    title: str = None
    artists: list[str] = None
    album: str = None
    explicit: bool = None
    length: str = None
    likeStatus: str = None
