from typing import List

from core.api.yt_music import YoutubeMusicApiSingleton
from core.constants.api import FilterFunction
from core.constants.printout import FOUND
from helpers.data.playlist import Playlist
from helpers.data.song import Song

youtube_music_api = YoutubeMusicApiSingleton.get_instance()


def _ensure_complete_playlist(playlist: Playlist, playlist_song_limit: int) -> Playlist:
    """Ensure that the playlist is complete (contains item information), if not the complete playlist will be retrieved

    Args:
        playlist (Playlist): Playlist to check / get complete information for
        playlist_song_limit (int): Max amount of songs to retrieve from the playlist (this is only used if the provided playlist is not complete). 

    Returns:
        Playlist: Complete playlist
    """
    if playlist.songs is None:
        return youtube_music_api.get_complete_playlist(playlist, playlist_song_limit)
    else:
        return playlist


def get_playlist_by_title(playlist_title: str, playlist_limit: int, playlist_song_limit: int) -> Playlist:
    """Get a playlist from the user's library that matches the title given

    Args:
        playlist_title (str): Title of playlist
        playlist_limit (int): Max amount of playlists to retrieve.
        playlist_song_limit (int): Max amount of songs to retrieve from the playlist.

    Returns:
        Dict: Complete playlist
    """
    library_playlists = get_library_playlists(playlist_limit)
    matching_library_playlist = next(
        (playlist for playlist in library_playlists if playlist.title == playlist_title), None)
    return youtube_music_api.get_complete_playlist(matching_library_playlist, playlist_song_limit)


def get_library_playlists(playlist_limit: int) -> List[Playlist]:
    """Get all playlists in the user's library

    Args:
        playlist_limit (int): Max amount of playlists to retrieve.

    Returns:
        List[Dict]: List of simple library playlist information
    """
    return youtube_music_api.get_simple_library_playlists(playlist_limit)

def get_matching_playlists_from_playlist_title_list(playlists: List[Playlist], playlist_titles_to_find: List[str]) -> List[Playlist]:
    """Get list of playlists that match the given string playlist titles list.

    Args:
        playlists (List[Playlist]): List of Playlists that will be searched
        playlist_titles_to_find (List[str]): List of playlist titles that will be used to search

    Returns:
        List[Playlist]: List of matching playlists
    """
    playlist_title_set = set(playlist_titles_to_find) # Needs to be on its own line, if in the loop then it is re-evaluated each loop iteration. 
    return [playlist_item for playlist_item in playlists if playlist_item.title in playlist_title_set]


def get_matching_songs_from_playlist(playlist: Playlist, filter_function: FilterFunction,
                                     playlist_song_limit: int) -> List[Song]:
    """Get list of songs from a playlist that match the given filter

    Args:
        playlist (Playlist): Playlist to get songs from
        filter_function (FilterFunction): Defines how the songs should be filtered
        playlist_song_limit (int): Max amount of songs to retrieve from the playlist.

    Returns:
        List[Song]: List of matching songs
    """
    complete_playlist = _ensure_complete_playlist(playlist, playlist_song_limit)
    filtered_playlist_songs = list(filter(filter_function.function, complete_playlist.songs))
    print(filter_function.printout)
    print(FOUND + str(len(filtered_playlist_songs)))
    return filtered_playlist_songs


def remove_songs_from_playlist(playlist: Playlist, songs_to_remove: List[Song], 
                               playlist_song_limit: int) -> None:
    """Remove songs from a playlist

    Args:
        playlist (Playlist): Playlist to remove songs from
        songs_to_remove (List[Song]): List of songs to remove
        playlist_song_limit (int): Max amount of songs to retrieve from the playlist.
    """
    youtube_music_api.remove_songs_from_playlist(_ensure_complete_playlist(playlist, playlist_song_limit), songs_to_remove)
