from enum import Enum

# API Query Limits
PLAYLIST_SONG_LIMIT = 2000
PLAYLIST_LIMIT = 50
UPLOAD_SONG_LIMIT = 25
SEARCH_SONG_LIMIT = 20

# Strings

# Menu Titles
MENU_TITLE = "Youtube Music Tools"
MENU_SUBTITLE = "Please select an option below"
MENU_PROMPT = "Please choose an option, 'q' to quit: "

# Menu Options
REMOVE_LIKED_SONGS_FROM_PLAYLIST_OPTION = "Remove the Liked Songs from the Playlist"
REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS = "Replace Uploaded Songs with Streaming Versions"

# Prompts
PLAYLIST_PROMPT = "Please type the name of the playlist: "
REMOVE_LIKED_SONGS_PROMPT = "Proceed with removing these songs from the playlist?"

# Print Outs
PLAYLIST_FOUND = "Playlist Found!:\n"
FOUND_SONG_AMOUNTS = "Found {0} Songs in Total\n"
SONG_SEARCH_START = "Searching for {0}"

#Filter Functions
class FilterFunction:
    def __init__(self, printout: str, function: callable) -> None:
        """
        Initializes FilterFunction object
        """
        self.printout = printout
        self.function = function

LIKED_SONGS_FILTER = FilterFunction("Liked Songs:\n", lambda song: song['likeStatus'] == LikeStatuses.LIKE.value)

class LikeStatuses(Enum):
    LIKE = "LIKE"
    NEUTRAL = "INDIFFERENT"
    DISLIKE = "DISLIKE"

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