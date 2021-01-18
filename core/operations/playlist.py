from typing import Dict, List

from core.api.yt_music import YoutubeMusicApiSingleton
from core.constants.api import (PLAYLIST_LIMIT, PLAYLIST_SONG_LIMIT,
                                FilterFunction)
from core.constants.printout import FOUND
from helpers.data.playlist import has_item_info

youtube_music_api = YoutubeMusicApiSingleton.get_instance()


def _ensure_complete_playlist(playlist: Dict, playlist_song_limit: int = PLAYLIST_SONG_LIMIT) -> Dict:
    """Ensure that the playlist is complete (contains item information), if not the complete playlist will be retrieved

    Args:
        playlist (Dict): Playlist to check / get complete information for
        playlist_song_limit (int): Max amount of songs to retrieve from the playlist (this is only used if the provided playlist is not complete). 
        Defaults to PLAYLIST_SONG_LIMIT.

    Returns:
        Dict: Complete playlist
    """
    if has_item_info(playlist):
        return playlist
    else:
        return youtube_music_api.get_complete_playlist(playlist, playlist_song_limit)


def get_playlist_by_title(playlist_title: str, playlist_limit: int = PLAYLIST_LIMIT,
                          playlist_song_limit: int = PLAYLIST_SONG_LIMIT) -> Dict:
    """Get a playlist from the user's library that matches the title given

    Args:
        playlist_title (str): Title of playlist
        playlist_limit (int, optional): Max amount of playlists to retrieve. Defaults to PLAYLIST_LIMIT.
        playlist_song_limit (int, optional): Max amount of songs to retrieve from the playlist. Defaults to PLAYLIST_SONG_LIMIT.

    Returns:
        Dict: Complete playlist
    """
    library_playlists = get_library_playlists(playlist_limit)
    matching_library_playlist = next(
        (playlist for playlist in library_playlists if playlist['title'] == playlist_title), None)
    return youtube_music_api.get_complete_playlist(matching_library_playlist, playlist_song_limit)


def get_library_playlists(playlist_limit: int = PLAYLIST_LIMIT) -> List[Dict]:
    """Get all playlists in the user's library

    Args:
        playlist_limit (int, optional): Max amount of playlists to retrieve. Defaults to PLAYLIST_LIMIT.

    Returns:
        List[Dict]: List of simple library playlist information
    """
    return youtube_music_api.get_simple_library_playlists(playlist_limit)


def get_matching_songs_from_playlist(playlist: Dict, filter_function: FilterFunction,
                                     playlist_song_limit: int = PLAYLIST_SONG_LIMIT) -> List[Dict]:
    """Get list of songs from a playlist that match the given filter

    Args:
        playlist (Dict): Playlist to get songs from
        filter_function (FilterFunction): Defines how the songs should be filtered
        playlist_song_limit (int, optional): Max amount of songs to retrieve from the playlist. Defaults to PLAYLIST_SONG_LIMIT.

    Returns:
        List[Dict]: List of songs
    """
    complete_playlist = _ensure_complete_playlist(playlist, playlist_song_limit)
    filtered_playlist_songs = list(filter(filter_function.function, complete_playlist['tracks']))
    print(filter_function.printout)
    print(FOUND + str(len(filtered_playlist_songs)))
    return filtered_playlist_songs


def remove_songs_from_playlist(playlist: Dict, songs_to_remove: List[Dict]) -> None:
    """Remove songs from a playlist

    Args:
        playlist (Dict): Playlist to remove songs from
        songs_to_remove (List[Dict]): List of songs to remove
    """
    youtube_music_api.remove_songs_from_playlist(_ensure_complete_playlist(playlist), songs_to_remove)
