import sys
from re import T
from core.constants.api import RATED_SONGS_FILTER
from core.constants.menu import (ADD_SKIP_LIST_OPTION, MENU_SONG_COMPARE_PROMPT,
                                 PLAYLIST_CHOICE_TITLE, QUIT_OPTION, REMOVE_RATED_SONGS_FROM_PLAYLIST_OPTION, REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS, SEARCH_RESULT_TITLE,
                                 SELECTION_MADE_TITLE, SKIP_OPTION)
from core.constants.printout import (ADDING, FAILURE, LIBRARY, RETRY, SONG,
                                     STREAMING, UPLOADED)
from core.constants.prompt import (ADD_STREAMING_AND_DELETE_UPLOADED_PROMPT,
                                   NEXT_SONG_PROMPT, REMOVE_RATED_SONGS_PROMPT, SEARCH_HISTORY_WARNING_PROMPT)
from core.operations.playlist import (get_library_playlists,
                                      get_matching_songs_from_playlist,
                                      remove_songs_from_playlist)
from core.operations.song import (add_song_to_library, delete_uploaded_song,
                                  get_uploaded_songs, perform_song_search)
from helpers.display.menus import list_selection_menu, main_menu
from helpers.display.printouts import print_title_with_info
from helpers.display.prompts import continue_prompt, yes_or_no_prompt


def remove_rated_songs_from_playlist_selection() -> None:
    """Remove rated songs from one of the current user's library playlists"""
    playlists = get_library_playlists()
    selected_playlist = list_selection_menu(PLAYLIST_CHOICE_TITLE, playlists, allow_quit=True).get(PLAYLIST_CHOICE_TITLE)

    print_title_with_info(SELECTION_MADE_TITLE, selected_playlist)
    songs_to_remove = get_matching_songs_from_playlist(selected_playlist, RATED_SONGS_FILTER)

    if yes_or_no_prompt(REMOVE_RATED_SONGS_PROMPT):
        remove_songs_from_playlist(selected_playlist, songs_to_remove)

    continue_prompt()


def replace_uploaded_songs_with_streaming_versions() -> None:
    """Replace uploaded library songs with the matching streaming version (if applicable)"""
    uploaded_songs = get_uploaded_songs()
    continue_prompt(SEARCH_HISTORY_WARNING_PROMPT, clear_screen=True)

    for uploaded_song in uploaded_songs:
        search_result_songs = perform_song_search(uploaded_song)
        comparing_songs = True

        while comparing_songs:

            print_title_with_info(UPLOADED + SONG, uploaded_song)
            selection = list_selection_menu(SEARCH_RESULT_TITLE, search_result_songs[0: 5],
                MENU_SONG_COMPARE_PROMPT, True, True, True).get(SEARCH_RESULT_TITLE)

            # If user wants to skip this song comparision
            if(selection == SKIP_OPTION):
                break
            if(selection == ADD_SKIP_LIST_OPTION):
                print("need to implement")
            if(selection == QUIT_OPTION):
                sys.exit()
            else:
                print_title_with_info(UPLOADED + SONG, uploaded_song)
                print_title_with_info(STREAMING + SONG, selection)

                if yes_or_no_prompt(ADD_STREAMING_AND_DELETE_UPLOADED_PROMPT):
                    # If streaming song is successfully added to library, delete uploaded song and move to comparing next song
                    if(add_song_to_library(selection)):
                        delete_uploaded_song(uploaded_song)
                        comparing_songs = False
                    # If streaming song is NOT added to library, do NOT delete uploaded song and retry
                    else:
                        print(FAILURE + ADDING + LIBRARY + SONG + selection + RETRY)

    continue_prompt(NEXT_SONG_PROMPT, clear_screen=True)


while True:
    selection = main_menu()
    if selection == REMOVE_RATED_SONGS_FROM_PLAYLIST_OPTION:
        remove_rated_songs_from_playlist_selection()
    if selection == REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS:
        replace_uploaded_songs_with_streaming_versions()
    if selection == QUIT_OPTION:
        sys.exit()
