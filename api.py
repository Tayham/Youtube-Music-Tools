from typing import Dict, List

from ytmusicapi import YTMusic

import constants


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

    def get_library_playlist_by_title(self, title: str) -> dict:
        library_playlists = self.__youtube_music_api.get_library_playlists(
            constants.PLAYLIST_LIMIT)
        matching_library_playlist = self.__find(
            lambda playlists: playlists["title"] == title, library_playlists)
        return self.__youtube_music_api.get_playlist(
            matching_library_playlist["playlistId"], constants.PLAYLIST_SONG_LIMIT)
