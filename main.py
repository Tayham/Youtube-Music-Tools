from ytmusicapi.parsers import playlists
from constants import *
from operations import *
from dict_helpers import get_song_display_list
from menu_helpers import *

def remove_liked_songs_from_playlist_selection() -> None:
    playlist_title = input(PLAYLIST_PROMPT)
    songs_to_remove = get_matching_songs_from_playlist(playlist_title, LIKED_SONGS_FILTER)

    if yes_or_no_prompt(REMOVE_LIKED_SONGS_PROMPT):
        remove_songs_from_playlist(playlist_title, songs_to_remove)

    continue_prompt()

def replace_uploaded_songs_with_streaming_versions() -> None:
    uploaded_songs = get_uploaded_songs()

    for uploaded_song in uploaded_songs:
        search_result_songs = perform_song_search(uploaded_song)
        comparing_songs = True

        while comparing_songs:
            print_title_with_info("Uploaded Song:", get_song_info(uploaded_song))
            selected_index = list_selection_menu("Search Results:", get_song_display_list(search_result_songs)[0:5], MENU_SONG_COMPARE_PROMPT, True, True)
            # If user wants to skip this song comparision
            if(selected_index == -1):
                comparing_songs = False
            else:
                print_title_with_info("Uploaded Song:", get_song_info(uploaded_song))
                print_title_with_info("Streaming Song:", get_song_info(search_result_songs[selected_index]))
                if yes_or_no_prompt("Add this streaming song to your library and deleted the uploaded version?"):
                    comparing_songs = False

    continue_prompt("Moving to next song. ", True)

while True:
    selection = main_menu()
    if selection == 1:
        remove_liked_songs_from_playlist_selection()
    if selection == 2:
        replace_uploaded_songs_with_streaming_versions()