from typing import Dict, List
from constants import LIKED_SONGS, LikeStatuses, PLAYLIST_FOUND
import api
from api import YoutubeMusicApiSingleton
import music_objects
from music_objects import Track

youtube_music_api = YoutubeMusicApiSingleton()


def add_liked_songs_in_playlist_to_library(playlist_title: str) -> None:
    """
    Add liked songs from a playlist to youtube music library
    """
    playlist = youtube_music_api.get_library_playlist_by_title(playlist_title)
    print(PLAYLIST_FOUND + playlist.get_playlist_info())
    liked_playlist_tracks = filter(lambda track: track.likeStatus == LikeStatuses.LIKE.value, playlist.tracks)
    print(LIKED_SONGS)
    for track in liked_playlist_tracks:
        print(track.get_track_info())

    #TODO add songs to library
    