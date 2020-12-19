from typing import *
from ytmusicapi import YTMusic
import constants
from constants import LikeStatuses, Order, ItemType


class YoutubeMusicApiSingleton:
    __instance__ = None

    def __init__(self):
        """ Constructor."""
        self.__youtube_music_api = YTMusic("headers_auth.json")
        if YoutubeMusicApiSingleton.__instance__ is None:
            YoutubeMusicApiSingleton.__instance__ = self
        else:
            raise Exception(
                "You cannot create another YoutubeMusicApi class, this class is a singleton"
            )

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance."""
        if not YoutubeMusicApiSingleton.__instance__:
            YoutubeMusicApiSingleton()
        return YoutubeMusicApiSingleton.__instance__

    def __find(self, item_to_find: str, search_list: List[Dict]) -> Dict:
        """Returns first item in a list where itemToFind(item) == True."""
        for item in search_list:
            if item_to_find(item):
                return item

    def get_library_uploaded_songs(self, song_limit: int, order: Order) -> List[Dict]:
        return self.__youtube_music_api.get_library_upload_songs(song_limit, order.value)

    def get_library_playlist_by_title(self, title: str, playlist_limit: int, playlist_song_limit: int) -> Dict:
        library_playlists = self.__youtube_music_api.get_library_playlists(playlist_limit)
        matching_library_playlist = self.__find(lambda playlists: playlists["title"] == title, library_playlists)
        return self.__youtube_music_api.get_playlist(matching_library_playlist["playlistId"], playlist_song_limit)

    def add_song_to_library(self, video_id: str) -> None:
        """
        Add a song to the current user's Youtube Music library
        """
        self.__youtube_music_api.rate_song(video_id, LikeStatuses.LIKE.value)

    def remove_songs_from_playlist(self, playlist_id: str, songs: List[Dict]) -> None:
        """
        Remove a song from a playlist in Youtube Music
        """
        self.__youtube_music_api.remove_playlist_items(playlist_id, songs)

    def perform_search(self, query: str, item_type: ItemType, song_search_limit: int, ignore_spelling: bool) -> List[Dict]:
        """
        Search for an item in Youtube Music
        """
        return self.__youtube_music_api.search(query, item_type.value, song_search_limit, ignore_spelling)
