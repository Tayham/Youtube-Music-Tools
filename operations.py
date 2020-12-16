from typing import Dict, List, Iterator
from constants import *
import api
from consolemenu import *
from api import YoutubeMusicApiSingleton
import music_objects
from music_objects import *

youtube_music_api = YoutubeMusicApiSingleton()

def _get_playlist_info(playlist: Dict) -> str:
    """
    Returns a nicely readable printout of the playlist's information
    """
    return(f"Title: {playlist['title']}\nTrack Count: {playlist['trackCount']}\n")

def _get_track_info(track: Dict) -> str:
    """
    Returns a nicely readable printout of the track's information
    """
    artists = ', '.join([artist['name'] for artist in track['artists']])
    return(f"Title: {track['title']}\nArtist(s): {artists}\nAlbum: {track['album']['name']}\nLiked: {track['likeStatus']}\n")



def get_matching_songs_from_playlist(console: Screen, playlist_title: str, filter_function: FilterFunction) -> List[Dict]:
    """
    Return filter matched songs from a playlist
    """
    playlist = youtube_music_api.get_library_playlist_by_title(playlist_title)
    console.println(PLAYLIST_FOUND + _get_playlist_info(playlist))

    filtered_playlist_tracks = list(filter(filter_function.function, playlist['tracks']))
    console.println(filter_function.printout)

    for track in filtered_playlist_tracks:
        console.println(_get_track_info(track))

    console.println(FOUND_SONG_AMOUNTS.format(len(filtered_playlist_tracks)))
    return filtered_playlist_tracks

def remove_songs_from_playlist(console: Screen, playlist_title: str, tracks_to_remove: List[Dict]) -> None:
    """
    Remove songs from a playlist
    """
    playlist = youtube_music_api.get_library_playlist_by_title(playlist_title)
    console.println(PLAYLIST_FOUND + _get_playlist_info(playlist))
    youtube_music_api.remove_songs_from_playlist(playlist['id'], tracks_to_remove)
    