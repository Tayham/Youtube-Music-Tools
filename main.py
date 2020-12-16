from consolemenu import *
from consolemenu.items import *
from consolemenu.prompt_utils import PromptUtils
from ytmusicapi.parsers import playlists

from constants import *
from operations import *



def remove_liked_songs_from_playlist_selection() -> None:
    screen = Screen()

    playlist_title = screen.input(PLAYLIST_PROMPT)
    songs_to_remove = get_matching_songs_from_playlist(screen, playlist_title, LIKED_SONGS_FILTER)

    # for playlist_track in songs_to_remove :
    #     screen.println("loop execute")
    #     screen.println(playlist_track.get_track_info)
    #     screen.println("\n")
    #     screen.println(playlist_track.setVideoId)
    #     screen.println("\n")
    #     screen.println(playlist_track['setVideoId'])
    #     screen.println("-----------\n")
    #     screen.println(playlist_track.videoId)
    #     screen.println("\n")
    #     screen.println(playlist_track['videoId'])

    if PromptUtils(screen).prompt_for_yes_or_no(REMOVE_LIKED_SONGS_PROMPT) :
        remove_songs_from_playlist(screen, playlist_title, songs_to_remove)

    PromptUtils(screen).enter_to_continue()
    screen.clear()

menu = ConsoleMenu(MENU_TITLE, MENU_SUBTITLE)
menu.append_item(FunctionItem(text=REMOVE_LIKED_SONGS_FROM_PLAYLIST_OPTION,
                              function=remove_liked_songs_from_playlist_selection))
menu.show()