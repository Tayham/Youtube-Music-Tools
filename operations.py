from typing import Dict, List, Iterator
from constants import *
import constants
import api
from consolemenu import *
from api import YoutubeMusicApiSingleton

#TODO: Normalize Song / song naming

youtube_music_api = YoutubeMusicApiSingleton()

def _get_playlist_info(playlist: Dict) -> str:
    """
    Returns a nicely readable printout of the playlist's information
    """
    return(f"Title: {playlist['title']}\nsong Count: {playlist['songCount']}\n")

def _get_song_query(song: Dict) -> str:
    """
    Returns a good search query based on the songs information
    """
    artists = ', '.join([artist['name'] for artist in song['artists']])
    return(f"Title: {song['title']} by {artists}")

def _get_song_info(song: Dict) -> str:
    """
    Returns a nicely readable printout of the song's information
    """
    artists = ', '.join([artist['name'] for artist in song['artists']])
    return(f"Title: {song['title']}\nArtist(s): {artists}\nAlbum: {song['album']['name']}\nLiked: {song['likeStatus']}\n")

def _get_playlist(title: str, playlist_limit: int = constants.PLAYLIST_LIMIT, playlist_song_limit: int = constants.PLAYLIST_SONG_LIMIT) -> Dict:
    """
    Returns a playlist that matches the title given
    """
    return youtube_music_api.get_library_playlist_by_title(title, playlist_limit, playlist_song_limit)

def get_matching_songs_from_playlist(console: Screen, playlist_title: str, filter_function: FilterFunction) -> List[Dict]:
    """
    Return filter matched songs from a playlist
    """
    playlist = _get_playlist(playlist_title)
    console.println(PLAYLIST_FOUND + _get_playlist_info(playlist))
    filtered_playlist_songs = list(filter(filter_function.function, playlist['songs']))
    console.println(filter_function.printout)
    console.println(FOUND_SONG_AMOUNTS.format(len(filtered_playlist_songs)))
    return filtered_playlist_songs

def get_uploaded_songs(console: Screen, song_limit: int = constants.UPLOAD_SONG_LIMIT, order: Order = Order.DSC) -> List[Dict]:
    uploaded_songs = youtube_music_api.get_library_uploaded_songs(song_limit, order)
    console.println(FOUND_SONG_AMOUNTS.format(len(uploaded_songs)))
    for song in uploaded_songs:
        console.println(_get_song_info(song))
    return uploaded_songs

def perform_song_search(console: Screen, song: Dict, song_search_limit: int = constants.SEARCH_SONG_LIMIT, ignore_spelling: bool =True) -> List[Dict]:
    query = _get_song_query(song)
    console.println(SONG_SEARCH_START.format(query))
    return youtube_music_api.perform_search(query, ItemType.SONG, song_search_limit, ignore_spelling)

def remove_songs_from_playlist(console: Screen, playlist_title: str, songs_to_remove: List[Dict]) -> None:
    """
    Remove songs from a playlist
    """
    playlist = _get_playlist(playlist_title)
    console.println(PLAYLIST_FOUND + _get_playlist_info(playlist))
    youtube_music_api.remove_songs_from_playlist(playlist['id'], songs_to_remove)
    