from enum import Enum

# API Query Limits
PLAYLIST_SONG_LIMIT = 2000
PLAYLIST_LIMIT = 50

# Strings

# Menu Titles
MENU_TITLE = "Youtube Music Tools"
MENU_SUBTITLE = "Please select an option below"

# Menu Options
ADD_REMOVE_LIKED_PLAYLIST_SONGS_OPTION ="Add Liked Songs from a Playlist to your Library"
# and Remove the Liked Songs from the Playlist"

# Prompts
PLAYLIST_PROMPT = "Please type the name of the playlist: "
REMOVE_LIKED_SONGS_PROMPT = "Would you like to remove the liked songs from the playlist?"

# Print Outs
PLAYLIST_FOUND = "Playlist Found!:\n"
LIKED_SONGS = "Liked Songs:\n"

class LikeStatuses(Enum):
    LIKE = "LIKE"
    NEUTRAL = "INDIFFERENT"
    DISLIKE = "DISLIKE"