from consolemenu import *
from consolemenu.items import *
from consolemenu.prompt_utils import PromptUtils
from ytmusicapi.parsers import playlists
from constants import *
from operations import *
from dict_helpers import get_song_display_list

def remove_liked_songs_from_playlist_selection() -> None:
    screen = Screen()

    playlist_title = screen.input(PLAYLIST_PROMPT)
    songs_to_remove = get_matching_songs_from_playlist(screen, playlist_title, LIKED_SONGS_FILTER)

    if PromptUtils(screen).prompt_for_yes_or_no(REMOVE_LIKED_SONGS_PROMPT) :
        remove_songs_from_playlist(screen, playlist_title, songs_to_remove)

    PromptUtils(screen).enter_to_continue()
    screen.clear()

def replace_uploaded_songs_with_streaming_versions() -> None:
    screen = Screen()

    uploaded_songs = get_uploaded_songs(screen)

    for uploaded_song in uploaded_songs:
        search_result_songs = perform_song_search(screen, uploaded_song)
        PromptUtils(screen).enter_to_continue("Look at results")
        PromptUtils(screen).prompt_for_numbered_choice(get_song_display_list(search_result_songs)[0:5], "Search Results", "Select song to compare: ")
        # for result in search_result_songs:
        #     # screen.println(result)
        PromptUtils(screen).enter_to_continue()
        

    PromptUtils(screen).enter_to_continue()
    screen.clear()

menu = ConsoleMenu(MENU_TITLE, MENU_SUBTITLE)
menu.append_item(FunctionItem(text=REMOVE_LIKED_SONGS_FROM_PLAYLIST_OPTION,
                              function=remove_liked_songs_from_playlist_selection))
menu.append_item(FunctionItem(text=REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS,
                              function=replace_uploaded_songs_with_streaming_versions))
menu.show()