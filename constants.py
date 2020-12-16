from enum import Enum

# API Query Limits
PLAYLIST_SONG_LIMIT = 2000
PLAYLIST_LIMIT = 50

# Strings

# Menu Titles
MENU_TITLE = "Youtube Music Tools"
MENU_SUBTITLE = "Please select an option below"

# Menu Options
REMOVE_LIKED_SONGS_FROM_PLAYLIST_OPTION ="Remove the Liked Songs from the Playlist"

# Prompts
PLAYLIST_PROMPT = "Please type the name of the playlist: "
REMOVE_LIKED_SONGS_PROMPT = "Proceed with removing these songs from the playlist?"

# Print Outs
PLAYLIST_FOUND = "Playlist Found!:\n"
FOUND_SONG_AMOUNTS = "Found {0} Songs in Total\n"

#Filter Functions
class FilterFunction:
    def __init__(self, printout: str, function: callable) -> None:
        """
        Initializes FilterFunction object
        """
        self.printout = printout
        self.function = function

LIKED_SONGS_FILTER = FilterFunction("Liked Songs:\n", lambda track: track.likeStatus == LikeStatuses.LIKE.value)

class LikeStatuses(Enum):
    LIKE = "LIKE"
    NEUTRAL = "INDIFFERENT"
    DISLIKE = "DISLIKE"