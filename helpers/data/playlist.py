from dataclasses import dataclass
from helpers.data.song import Song


@dataclass
class Playlist:
    """Class for Playlist Data (Maybe incomplete depending on API)"""
    id: str = None
    title: str = None
    song_count: int = None
    songs: list[Song] = None

    def __str__(self) -> str:
        return(f"Title: {self.title}\nSong Count: {self.song_count}\n")
