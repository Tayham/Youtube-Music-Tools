from typing import Dict, List

from core.api.yt_music import YoutubeMusicApiSingleton
from core.constants import (FOUND_SONG_AMOUNTS, PLAYLIST_FOUND,
                                         PLAYLIST_LIMIT, PLAYLIST_SONG_LIMIT,
                                         FilterFunction)
from helpers.data.playlist import get_playlist_info

youtube_music_api = YoutubeMusicApiSingleton.get_instance()


def get_playlist(title: str, playlist_limit: int = PLAYLIST_LIMIT, playlist_song_limit: int = PLAYLIST_SONG_LIMIT) -> Dict:
    """
    Returns a playlist that matches the title given
    """
    return youtube_music_api.get_library_playlist_by_title(title, playlist_limit, playlist_song_limit)


def get_library_playlists(playlist_limit: int = PLAYLIST_LIMIT) -> List[Dict]:
    """
    Returns all playlists in the user's library
    """
    return youtube_music_api.get_library_playlists(playlist_limit)


def get_matching_songs_using_playlist_title(playlist_title: str, filter_function: FilterFunction) -> List[Dict]:
    """
    Return filter matched songs from a playlist matching the given title
    """
    playlist = get_playlist(playlist_title)
    print(PLAYLIST_FOUND + get_playlist_info(playlist))
    filtered_playlist_songs = list(
        filter(filter_function.function, playlist['tracks']))
    print(filter_function.printout)
    print(FOUND_SONG_AMOUNTS.format(len(filtered_playlist_songs)))
    return filtered_playlist_songs


def get_matching_songs_from_playlist(playlist: Dict, filter_function: FilterFunction) -> List[Dict]:
    """
    Return filter matched songs from a playlist
    """
    # Get full playlist information
    playlist_with_items = youtube_music_api.get_playlist_with_items(playlist)

    filtered_playlist_songs = list(
        filter(filter_function.function, playlist_with_items['tracks']))
    print(filter_function.printout)
    print(FOUND_SONG_AMOUNTS.format(len(filtered_playlist_songs)))
    return filtered_playlist_songs


def remove_songs_from_playlist(playlist: Dict, songs_to_remove: List[Dict]) -> None:
    """
    Remove songs from a playlist
    """
    youtube_music_api.remove_songs_from_playlist(playlist, songs_to_remove)
