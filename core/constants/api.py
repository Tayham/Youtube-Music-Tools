from enum import Enum

### API Query Limits ###

PLAYLIST_SONG_LIMIT = 2000
PLAYLIST_LIMIT = 50
UPLOAD_SONG_LIMIT = 25
SEARCH_SONG_LIMIT = 20

### Enums ###


class LikeStatuses(Enum):
    LIKE = "LIKE"
    INDIFFERENT = "INDIFFERENT"
    DISLIKE = "DISLIKE"
    UNKNOWN = "UNKNOWN"


class Order(Enum):
    DSC = "a_to_z"
    ASC = "z_to_a"
    RECENT = "recently_added"


class ItemType(Enum):
    SONG = "songs"
    VIDEO = "videos"
    ALBUM = "albums"
    ARTIST = "artists"
    PLAYLIST = "playlists"
    UPLOAD = "uploads"

### Filter Functions ###


class FilterFunction:
    def __init__(self, printout: str, function: callable) -> None:
        """Initializes FilterFunction object"""
        self.printout = printout
        self.function = function


LIKED_SONGS_FILTER = FilterFunction("Liked Songs:\n", lambda song: song.like_status == LikeStatuses.LIKE)
DISLIKED_SONGS_FILTER = FilterFunction(
    "Disliked Songs:\n", lambda song: song.like_status == LikeStatuses.DISLIKE)
RATED_SONGS_FILTER = FilterFunction("Rated Songs:\n", lambda song: (
    (song.like_status == LikeStatuses.LIKE) or (song.like_status == LikeStatuses.DISLIKE)))
