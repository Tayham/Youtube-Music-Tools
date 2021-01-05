from typing import Dict, List

from ytmusicapi import YTMusic
from core.constants import ItemType, LikeStatuses, Order
from helpers.data.playlist import get_playlist_id
from helpers.data.util import to_bool


class YoutubeMusicApiSingleton:
    __instance__ = None

    def __init__(self):
        """ Constructor."""
        self.__youtube_music_api = YTMusic("core/auth/headers_auth.json")
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

    def add_song_to_library(self, song: Dict) -> bool:
        """
        Add a song to the current user's Youtube Music library
        True -> Song was successfully added to library
        False -> Song was NOT added to library
        """
        response = self.__youtube_music_api.edit_song_library_status(song['feedbackTokens']['add'])
        # If responseContext is empty then song is already in library
        if not response['responseContext']:
            return True
        return to_bool(response['feedbackResponses'][0]['isProcessed'])

    def delete_uploaded_song(self, uploaded_song_to_delete: Dict) -> None:
        """
        Delete an uploaded song Youtube Music
        """
        self.__youtube_music_api.delete_upload_entity(uploaded_song_to_delete['entityId'])

    def get_library_uploaded_songs(self, song_limit: int, order: Order) -> List[Dict]:
        return self.__youtube_music_api.get_library_upload_songs(song_limit, order.value)

    def get_library_playlists(self, playlist_limit: int) -> List[Dict]:
        """
        Get all playlists that are in the current user's Youtube Music library
        NOTE: THIS DOES NOT RETURN THE COMPLETE INFORMATION FOR EACH PLAYLIST
        """
        return self.__youtube_music_api.get_library_playlists(playlist_limit)

    def get_library_playlist_by_title(self, title: str, playlist_limit: int, playlist_song_limit: int) -> Dict:
        library_playlists = self.__youtube_music_api.get_library_playlists(playlist_limit)
        matching_library_playlist = self.__find(lambda playlists: playlists['title'] == title, library_playlists)
        return self.__youtube_music_api.get_playlist(matching_library_playlist['playlistId'], playlist_song_limit)

    def like_song(self, song: Dict) -> None:
        self.__youtube_music_api.rate_song(song['videoId'], LikeStatuses.LIKE.value)

    def perform_search(
            self, query: str, item_type: ItemType, song_search_limit: int, ignore_spelling: bool) -> List[Dict]:
        """
        Search for an item in Youtube Music
        """
        return self.__youtube_music_api.search(query, item_type.value, song_search_limit, ignore_spelling)

    def get_playlist_with_items(self, playlist: Dict) -> Dict:
        """
        Gets all the information about the given playlist
        """
        return self.__youtube_music_api.get_playlist(get_playlist_id(playlist))

    def remove_songs_from_playlist(self, playlist: Dict, songs: List[Dict]) -> None:
        """
        Remove a song from a playlist in Youtube Music
        """
        self.__youtube_music_api.remove_playlist_items(get_playlist_id(playlist), songs)
