from core.constants.api import LikeStatuses
from dataclasses import dataclass
from helpers.data.feedback_tokens import FeedbackTokens


@dataclass
class Song:
    """Class for Song Data (Maybe incomplete depending on API)"""
    id: str = None
    title: str = None
    artists: list[str] = None
    album: str = None
    explicit: bool = None
    length: str = None
    like_status: LikeStatuses = None
    set_id: str = None  # Only used if song is in a playlist
    entity_id: str = None # Only used if a song is an uploaded song
    feedback_tokens: FeedbackTokens = None

    def __str__(self):
        return(f"Title: {self.title}\nArtist(s): {self.artists}\nAlbum: {self.album}\nExplicit: {self.explicit}\nLength: {self.length}\nLiked: {('N/A' if self.like_status is None else self.like_status.value)}\n")
