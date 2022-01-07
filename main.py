import sys
from re import T
from core.constants.api import RATED_SONGS_FILTER
from core.constants.menu import (
    ADD_SKIP_LIST_OPTION, MENU_SONG_COMPARE_PROMPT, PLAYLIST_CHOICE_TITLE, QUIT_OPTION,
    REMOVE_RATED_SONGS_FROM_DEFAULT_PLAYLISTS_OPTION, REMOVE_RATED_SONGS_FROM_PLAYLIST_OPTION,
    REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS, SEARCH_RESULT_TITLE, SELECTION_MADE_TITLE, SKIP_OPTION)
from core.constants.printout import (ADDING, FAILURE, LIBRARY, PLAYLIST, RETRY, SKIPPING, SONG,
                                     STREAMING, UPLOADED)
from core.constants.prompt import (ADD_STREAMING_AND_DELETE_UPLOADED_PROMPT,
                                   NEXT_SONG_PROMPT, REMOVE_RATED_SONGS_PROMPT, SEARCH_HISTORY_WARNING_PROMPT)
from core.operations.playlist import (get_library_playlists, get_matching_playlists_from_playlist_title_list,
                                      get_matching_songs_from_playlist,
                                      remove_songs_from_playlist)
from core.operations.song import (add_song_to_library, delete_uploaded_song,
                                  get_uploaded_songs, perform_song_search)
from core.settings.uploaded_song_streaming_skip_list_handler import UploadedSongStreamingSkipListHandler
from core.settings.yt_music_tools_settings import YoutubeMusicToolsSettingsSingleton
from helpers.display.menus import list_selection_menu, main_menu
from helpers.display.printouts import print_title_with_info
from helpers.display.prompts import continue_prompt, yes_or_no_prompt

youtube_music_tools_settings = YoutubeMusicToolsSettingsSingleton.get_instance()


def remove_rated_songs_from_default_playlists_selection() -> None:
    """Remove rated songs from all of the library playlist titles configured in the settings.json"""
    remove_rated_songs_playlists = get_matching_playlists_from_playlist_title_list(
        get_library_playlists(), youtube_music_tools_settings.get_default_remove_rated_songs_playlist_titles())

    for playlist_item in remove_rated_songs_playlists:
        print_title_with_info(PLAYLIST, playlist_item)
        songs_to_remove = get_matching_songs_from_playlist(playlist_item, RATED_SONGS_FILTER)
        if songs_to_remove:  # If songs_to_remove is NOT empty
            remove_songs_from_playlist(playlist_item, songs_to_remove)

    continue_prompt()


def remove_rated_songs_from_playlist_selection() -> None:
    """Remove rated songs from one of the current user's library playlists"""
    selected_playlist = list_selection_menu(
        PLAYLIST_CHOICE_TITLE, get_library_playlists(),
        allow_quit=True).get(PLAYLIST_CHOICE_TITLE)

    print_title_with_info(SELECTION_MADE_TITLE, selected_playlist)
    songs_to_remove = get_matching_songs_from_playlist(selected_playlist, RATED_SONGS_FILTER)
    if songs_to_remove:  # If songs_to_remove is NOT empty
        if yes_or_no_prompt(REMOVE_RATED_SONGS_PROMPT):
            remove_songs_from_playlist(selected_playlist, songs_to_remove)

    continue_prompt()


def replace_uploaded_songs_with_streaming_versions() -> None:
    """Replace uploaded library songs with the matching streaming version (if applicable)"""
    continue_prompt(SEARCH_HISTORY_WARNING_PROMPT, clear_screen=True)
    with UploadedSongStreamingSkipListHandler() as skip_list:
        for uploaded_song in get_uploaded_songs():
            if next(
                (skip_song for skip_song in skip_list.get_uploaded_song_streaming_check_skip_list()
                 if skip_song["id"] == uploaded_song.id),
                    None) is None:
                # if uploaded_song.id not in skip_list.get_uploaded_song_streaming_check_skip_list():
                search_result_songs = perform_song_search(uploaded_song)
                comparing_songs = True

                while comparing_songs:
                    print_title_with_info(UPLOADED + SONG, uploaded_song)
                    selection = list_selection_menu(SEARCH_RESULT_TITLE, search_result_songs[0: 5],
                                                    MENU_SONG_COMPARE_PROMPT, True, True, True).get(SEARCH_RESULT_TITLE)

                    if(selection == SKIP_OPTION):  # If user wants to skip this song comparision
                        break
                    if(selection == ADD_SKIP_LIST_OPTION):
                        skip_list.add_song_to_uploaded_song_streaming_check_skip_list(uploaded_song)
                        break
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
            else:  # Song is in the skip list
                print_title_with_info(SKIPPING + UPLOADED + SONG, uploaded_song)

    continue_prompt(NEXT_SONG_PROMPT, clear_screen=True)


while True:
    selection = main_menu()
    if selection == REMOVE_RATED_SONGS_FROM_DEFAULT_PLAYLISTS_OPTION:
        remove_rated_songs_from_default_playlists_selection()
    if selection == REMOVE_RATED_SONGS_FROM_PLAYLIST_OPTION:
        remove_rated_songs_from_playlist_selection()
    if selection == REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS:
        replace_uploaded_songs_with_streaming_versions()
    if selection == QUIT_OPTION:
        sys.exit()
