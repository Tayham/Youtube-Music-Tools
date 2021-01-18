from typing import Dict, List

from core.api.yt_music import YoutubeMusicApiSingleton
from core.constants.api import (SEARCH_SONG_LIMIT, UPLOAD_SONG_LIMIT, ItemType,
                                Order)
from core.constants.printout import (ADDING, DELETING, FOUND, LIBRARY,
                                     SEARCHING, SONG, UPLOADED)
from helpers.data.song import get_song_info, get_song_query

youtube_music_api = YoutubeMusicApiSingleton.get_instance()


def add_song_to_library(song: Dict) -> bool:
    """Add song to current user's library

    Args:
        song (Dict): Song to add to library

    Returns:
        bool: True -> Song successfully added to library | False -> Song FAILED to be added to library
    """
    print(ADDING + LIBRARY + SONG + get_song_info(song))
    return youtube_music_api.add_song_to_library(song)


def get_uploaded_songs(song_limit: int = UPLOAD_SONG_LIMIT, order: Order = Order.DSC) -> List[Dict]:
    """Get a list of current user's uploaded library songs

    Args:
        song_limit (int, optional): Max amount of songs to retrieve. Defaults to UPLOAD_SONG_LIMIT.
        order (Order, optional): Order to retrieve the songs in. Defaults to Order.DSC.

    Returns:
        List[Dict]: List of uploaded library songs
    """
    uploaded_songs = youtube_music_api.get_library_uploaded_songs(song_limit, order)
    print(FOUND + str(len(uploaded_songs)))
    return uploaded_songs


def delete_uploaded_song(song: Dict) -> None:
    """Delete an uploaded song from the current user's library

    Args:
        song (Dict): Uploaded song to delete
    """
    print(DELETING + UPLOADED + SONG + get_song_info(song))
    youtube_music_api.delete_library_uploaded_song(song)


def perform_song_search(
        song: Dict, song_search_limit: int = SEARCH_SONG_LIMIT, ignore_spelling: bool = True) -> List[Dict]:
    """Perform a song search and return a list of song results

    Args:
        song (Dict): Song to search for
        song_search_limit (int, optional): Max amount of songs in the search results. Defaults to SEARCH_SONG_LIMIT.
        ignore_spelling (bool, optional): True -> Ignore spelling suggestions | False -> Use autocorrected text. Defaults to True.

    Returns:
        List[Dict]: List of song search results
    """
    query = get_song_query(song)
    print(SEARCHING + format(query))
    return youtube_music_api.perform_search(query, ItemType.SONG, song_search_limit, ignore_spelling)
