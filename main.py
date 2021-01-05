from ytmusicapi.parsers import playlists
from constants import *
from operations import *
from dict_helpers import get_song_display_list, get_playlist_display_list
from menu_helpers import *

def remove_liked_songs_from_playlist_selection() -> None:
    playlists = get_library_playlists()
    selected_index = list_index_selection_menu("Choose a Playlist:", get_playlist_display_list(playlists), MENU_PROMPT_QUIT, True, False)
    selected_playlist = playlists[selected_index]
    print(SELECTION_MADE + get_playlist_info(selected_playlist))
    songs_to_remove = get_matching_songs_from_playlist(selected_playlist, LIKED_SONGS_FILTER)

    if yes_or_no_prompt(REMOVE_LIKED_SONGS_PROMPT):
        remove_songs_from_playlist(selected_playlist, songs_to_remove)

    continue_prompt()

def replace_uploaded_songs_with_streaming_versions() -> None:
    uploaded_songs = get_uploaded_songs()

    for uploaded_song in uploaded_songs:
        search_result_songs = perform_song_search(uploaded_song)
        comparing_songs = True

        while comparing_songs:
            print_title_with_info("Uploaded Song:", get_song_info(uploaded_song))
            selected_index = list_index_selection_menu("Search Results:", get_song_display_list(search_result_songs)[0:5], MENU_SONG_COMPARE_PROMPT, True, True)
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
                        delete_uploaded_song(uploaded_song)
                        comparing_songs = False
                    # If streaming song is NOT added to library, do NOT delete uploaded song and retry 
                    else:
                        print(FAILURE_ADD_LIBRARY_SONG_RETRY + get_song_info(selected_streaming_song))

    continue_prompt("Moving to next song. ", clear_screen=True)

while True:
    selection = main_menu()
    if selection == 1:
        remove_liked_songs_from_playlist_selection()
    if selection == 2:
        replace_uploaded_songs_with_streaming_versions()