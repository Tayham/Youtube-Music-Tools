from core.constants.api import DISLIKED_SONGS_FILTER, LIKED_SONGS_FILTER, RATED_SONGS_FILTER
from core.constants.menu import (MENU_SONG_COMPARE_PROMPT,
                                 PLAYLIST_CHOICE_TITLE, SEARCH_RESULT_TITLE,
                                 SELECTION_MADE_TITLE)
from core.constants.printout import (ADDING, FAILURE, LIBRARY, RETRY, SONG,
                                     STREAMING, UPLOADED)
from core.constants.prompt import (ADD_STREAMING_AND_DELETE_UPLOADED_PROMPT,
                                   NEXT_SONG_PROMPT, REMOVE_RATED_SONGS_PROMPT)
from core.operations.playlist import (get_library_playlists,
                                      get_matching_songs_from_playlist,
                                      remove_songs_from_playlist)
from core.operations.song import (add_song_to_library, delete_uploaded_song,
                                  get_uploaded_songs, perform_song_search)
from helpers.data.playlist import get_playlist_display_list, get_playlist_info
from helpers.data.song import get_song_display_list, get_song_info
from helpers.display.menus import list_index_selection_menu, main_menu
from helpers.display.printouts import print_title_with_info
from helpers.display.prompts import continue_prompt, yes_or_no_prompt


def remove_rated_songs_from_playlist_selection() -> None:
    """Remove rated songs from one of the current user's library playlists"""
    playlists = get_library_playlists()
    selected_index = list_index_selection_menu(
        PLAYLIST_CHOICE_TITLE, get_playlist_display_list(playlists), allow_quit=True)
    selected_playlist = playlists[selected_index]

    print_title_with_info(SELECTION_MADE_TITLE, get_playlist_info(selected_playlist))
    songs_to_remove = get_matching_songs_from_playlist(selected_playlist, RATED_SONGS_FILTER)

    if yes_or_no_prompt(REMOVE_RATED_SONGS_PROMPT):
        remove_songs_from_playlist(selected_playlist, songs_to_remove)

    continue_prompt()


def replace_uploaded_songs_with_streaming_versions() -> None:
    """Replace uploaded library songs with the matching streaming version (if applicable)"""
    uploaded_songs = get_uploaded_songs()

    for uploaded_song in uploaded_songs:
        search_result_songs = perform_song_search(uploaded_song)
        comparing_songs = True

        while comparing_songs:

            print_title_with_info(UPLOADED + SONG, get_song_info(uploaded_song))
            selected_index = list_index_selection_menu(
                SEARCH_RESULT_TITLE, get_song_display_list(search_result_songs)[0: 5],
                MENU_SONG_COMPARE_PROMPT, True, True)

            # If user wants to skip this song comparision
            if(selected_index == -1):
                comparing_songs = False
            else:
                selected_streaming_song = search_result_songs[selected_index]
                print_title_with_info(UPLOADED + SONG, get_song_info(uploaded_song))
                print_title_with_info(STREAMING + SONG, get_song_info(selected_streaming_song))

                if yes_or_no_prompt(ADD_STREAMING_AND_DELETE_UPLOADED_PROMPT):
                    # If streaming song is successfully added to library, delete uploaded song and move to comparing next song
                    if(add_song_to_library(selected_streaming_song)):
                        delete_uploaded_song(uploaded_song)
                        comparing_songs = False
                    # If streaming song is NOT added to library, do NOT delete uploaded song and retry
                    else:
                        print(FAILURE + ADDING + LIBRARY + SONG + get_song_info(selected_streaming_song) + RETRY)

    continue_prompt(NEXT_SONG_PROMPT, clear_screen=True)


while True:
    selection = main_menu()
    if selection == 1:
        remove_rated_songs_from_playlist_selection()
    if selection == 2:
        replace_uploaded_songs_with_streaming_versions()
