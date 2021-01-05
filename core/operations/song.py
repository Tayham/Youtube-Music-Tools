from typing import Dict, List

from core.api.yt_music import YoutubeMusicApiSingleton
from core.constants import (ADD_LIBRARY_SONG, DELETE_UPLOAD_SONG,
                                         FOUND_SONG_AMOUNTS, SEARCH_SONG_LIMIT,
                                         SONG_SEARCH_START, UPLOAD_SONG_LIMIT,
                                         ItemType, Order)
from helpers.data.song import get_song_info, get_song_query

youtube_music_api = YoutubeMusicApiSingleton.get_instance()


def add_song_to_library(song: Dict) -> bool:
    """
    Add given song to library
    True -> Song was successfully added to library
    False -> Song was NOT added to library
    """
    print(ADD_LIBRARY_SONG + get_song_info(song))
    return youtube_music_api.add_song_to_library(song)


def get_uploaded_songs(song_limit: int = UPLOAD_SONG_LIMIT, order: Order = Order.DSC) -> List[Dict]:
    """
    Return list of uploaded songs
    """
    uploaded_songs = youtube_music_api.get_library_uploaded_songs(
        song_limit, order)
    print(FOUND_SONG_AMOUNTS.format(len(uploaded_songs)))
    return uploaded_songs


def delete_uploaded_song(uploaded_song_to_delete: Dict) -> None:
    """
    Delete given uploaded song
    """
    print(DELETE_UPLOAD_SONG + get_song_info(uploaded_song_to_delete))
    youtube_music_api.delete_uploaded_song(uploaded_song_to_delete)


def perform_song_search(
        song: Dict, song_search_limit: int = SEARCH_SONG_LIMIT, ignore_spelling: bool = True) -> List[Dict]:
    """
    Search for a given song and return a list of song results
    """
    query = get_song_query(song)
    print(SONG_SEARCH_START.format(query))
    return youtube_music_api.perform_search(query, ItemType.SONG, song_search_limit, ignore_spelling)
