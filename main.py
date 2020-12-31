from ytmusicapi.parsers import playlists
from constants import *
from operations import *
from dict_helpers import get_song_display_list
from menu_helpers import *

def remove_liked_songs_from_playlist_selection() -> None:
    playlist_title = input(PLAYLIST_PROMPT)
    songs_to_remove = get_matching_songs_from_playlist(playlist_title, LIKED_SONGS_FILTER)

    if yes_or_no_prompt(REMOVE_LIKED_SONGS_PROMPT) :
        remove_songs_from_playlist(playlist_title, songs_to_remove)

    continue_prompt()

def replace_uploaded_songs_with_streaming_versions() -> None:
    uploaded_songs = get_uploaded_songs()

    for uploaded_song in uploaded_songs:
        search_result_songs = perform_song_search(uploaded_song)
        continue_prompt("Look at results")
        list_selection_menu(get_song_display_list(search_result_songs)[0:5], "Search Results", "Select song to compare: ")
        continue_prompt()

    continue_prompt()

while(True):
    selection = main_menu()
    if selection == 1:
        remove_liked_songs_from_playlist_selection()
    if selection == 2:
        replace_uploaded_songs_with_streaming_versions()