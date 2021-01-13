
from core.constants import (DELETE_UPLOAD_SONG, DISLIKED_SONGS_FILTER,
                            FAILURE_ADD_LIBRARY_SONG_RETRY, LIKED_SONGS_FILTER,
                            MENU_PROMPT_QUIT, MENU_SONG_COMPARE_PROMPT,
                            REMOVE_RATED_SONGS_PROMPT, SELECTION_MADE)
from core.operations.playlist import (get_library_playlists,
                                      get_matching_songs_from_playlist,
                                      remove_songs_from_playlist)
from core.operations.song import (add_song_to_library, get_uploaded_songs,
                                  perform_song_search)
from helpers.data.playlist import get_playlist_display_list, get_playlist_info
from helpers.data.song import get_song_display_list, get_song_info
from helpers.display.menus import list_index_selection_menu, main_menu
from helpers.display.printouts import print_title_with_info
from helpers.display.prompts import continue_prompt, yes_or_no_prompt


def remove_rated_songs_from_playlist_selection() -> None:
    """Remove rated songs from one of the current user's library playlists"""
    playlists = get_library_playlists()
    selected_index = list_index_selection_menu(
        "Choose a Playlist:", get_playlist_display_list(playlists),
        MENU_PROMPT_QUIT, True, False)
    selected_playlist = playlists[selected_index]
    print(SELECTION_MADE + get_playlist_info(selected_playlist))
    songs_to_remove = get_matching_songs_from_playlist(selected_playlist, LIKED_SONGS_FILTER)
    songs_to_remove.extend(get_matching_songs_from_playlist(selected_playlist, DISLIKED_SONGS_FILTER))

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
            print_title_with_info("Uploaded Song:", get_song_info(uploaded_song))
            selected_index = list_index_selection_menu(
                "Search Results:", get_song_display_list(search_result_songs)[0: 5],
                MENU_SONG_COMPARE_PROMPT, True, True)

            # If user wants to skip this song comparision
            if(selected_index == -1):
                comparing_songs = False
            else:
                selected_streaming_song = search_result_songs[selected_index]
                print_title_with_info("Uploaded Song:", get_song_info(uploaded_song))
                print_title_with_info("Streaming Song:", get_song_info(selected_streaming_song))

                if yes_or_no_prompt("Add this streaming song to your library and deleted the uploaded version?"):
                    # If streaming song is successfully added to library, delete uploaded song and move to comparing next song
                    if(add_song_to_library(selected_streaming_song)):
                        DELETE_UPLOAD_SONG(uploaded_song)
                        comparing_songs = False
                    # If streaming song is NOT added to library, do NOT delete uploaded song and retry
                    else:
                        print(FAILURE_ADD_LIBRARY_SONG_RETRY + get_song_info(selected_streaming_song))

    continue_prompt("Moving to next song. ", clear_screen=True)


while True:
    selection = main_menu()
    if selection == 1:
        remove_rated_songs_from_playlist_selection()
    if selection == 2:
        replace_uploaded_songs_with_streaming_versions()
