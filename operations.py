from typing import Dict, List, Iterator
from constants import *
import api
from consolemenu import *
from api import YoutubeMusicApiSingleton
import time
from dict_helpers import get_song_info, get_song_query, get_playlist_info

youtube_music_api = YoutubeMusicApiSingleton()

def get_playlist(title: str, playlist_limit: int = PLAYLIST_LIMIT, playlist_song_limit: int = PLAYLIST_SONG_LIMIT) -> Dict:
    """
    Returns a playlist that matches the title given
    """
    return youtube_music_api.get_library_playlist_by_title(title, playlist_limit, playlist_song_limit)

def get_matching_songs_from_playlist(console: Screen, playlist_title: str, filter_function: FilterFunction) -> List[Dict]:
    """
    Return filter matched songs from a playlist
    """
    playlist = get_playlist(playlist_title)
    console.println(PLAYLIST_FOUND + get_playlist_info(playlist))
    filtered_playlist_songs = list(filter(filter_function.function, playlist['songs']))
    console.println(filter_function.printout)
    console.println(FOUND_SONG_AMOUNTS.format(len(filtered_playlist_songs)))
    return filtered_playlist_songs

def get_uploaded_songs(console: Screen, song_limit: int = UPLOAD_SONG_LIMIT, order: Order = Order.DSC) -> List[Dict]:
    """
    Return list of uploaded songs
    """
    uploaded_songs = youtube_music_api.get_library_uploaded_songs(song_limit, order)
    console.println(FOUND_SONG_AMOUNTS.format(len(uploaded_songs)))
    # for song in uploaded_songs:
    #     console.println(get_song_info(song))
    return uploaded_songs

def perform_song_search(console: Screen, song: Dict, song_search_limit: int = SEARCH_SONG_LIMIT, ignore_spelling: bool =True) -> List[Dict]:
    """
    Search for a given song and return a list of song results
    """
    console.println(get_song_info(song))
    query = get_song_query(song)
    console.println(SONG_SEARCH_START.format(query))
    return youtube_music_api.perform_search(query, ItemType.SONG, song_search_limit, ignore_spelling)

def remove_songs_from_playlist(console: Screen, playlist_title: str, songs_to_remove: List[Dict]) -> None:
    """
    Remove songs from a playlist
    """
    playlist = get_playlist(playlist_title)
    console.println(PLAYLIST_FOUND + get_playlist_info(playlist))
    youtube_music_api.remove_songs_from_playlist(playlist['id'], songs_to_remove)
    