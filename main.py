from consolemenu import *
from consolemenu.items import *
from consolemenu.prompt_utils import PromptUtils
from ytmusicapi.parsers import playlists

from constants import (ADD_REMOVE_LIKED_PLAYLIST_SONGS_OPTION, MENU_SUBTITLE,
                       MENU_TITLE, PLAYLIST_PROMPT, REMOVE_LIKED_SONGS_PROMPT)
from operations import add_liked_songs_in_playlist_to_library


def add_liked_songs_to_library_and_remove_from_playlist_selection() -> None:
    playlist_title = input(PLAYLIST_PROMPT)
    add_liked_songs_in_playlist_to_library(playlist_title)
    # if(PromptUtils(menu.screen).prompt_for_yes_or_no(REMOVE_LIKED_SONGS_PROMPT))

    PromptUtils(menu.screen).enter_to_continue()

menu = ConsoleMenu(MENU_TITLE, MENU_SUBTITLE)
menu.append_item(FunctionItem(text=ADD_REMOVE_LIKED_PLAYLIST_SONGS_OPTION,
                              function=add_liked_songs_to_library_and_remove_from_playlist_selection))
menu.show()
