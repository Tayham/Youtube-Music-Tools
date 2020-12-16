from typing import Dict, List, Iterator
from constants import *
import api
from consolemenu import *
from api import YoutubeMusicApiSingleton
import music_objects
from music_objects import *

youtube_music_api = YoutubeMusicApiSingleton()

def get_matching_songs_from_playlist(console: Screen, playlist_title: str, filter_function: FilterFunction) -> List[PlaylistTrack]:
    """
    Return filter matched songs from a playlist
    """
    playlist = youtube_music_api.get_library_playlist_by_title(playlist_title)
    console.println(PLAYLIST_FOUND + playlist.get_playlist_info())

    filtered_playlist_tracks = list(filter(filter_function.function, playlist.tracks))
    console.println(filter_function.printout)

    # tracks_found_counter = 0
    for track in filtered_playlist_tracks:
        console.println(track.get_track_info())
        console.println(track.setVideoId)
        console.println(track['setVideoId'])
        # tracks_found_counter += 1

    console.println(FOUND_SONG_AMOUNTS.format(len(filtered_playlist_tracks)))
    return filtered_playlist_tracks

def remove_songs_from_playlist(console: Screen, playlist_title: str, tracks_to_remove: List[PlaylistTrack]) -> None:
    """
    Remove songs from a playlist
    """
    playlist = youtube_music_api.get_library_playlist_by_title(playlist_title)
    console.println(PLAYLIST_FOUND + playlist.get_playlist_info())
    youtube_music_api.remove_songs_from_playlist(playlist, tracks_to_remove)
    