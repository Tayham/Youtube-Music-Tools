from typing import Dict, List

from core.constants.api import ItemType, LikeStatuses, Order
from helpers.data.playlist import get_playlist_id
from helpers.data.util import to_bool
from ytmusicapi import YTMusic


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
    def get_instance() -> 'YoutubeMusicApiSingleton':
        """Static method to get the current instance

        Returns:
            YoutubeMusicApiSingleton: Instance of the YoutubeMusicApiSingleton
        """
        if not YoutubeMusicApiSingleton.__instance__:
            YoutubeMusicApiSingleton()
        return YoutubeMusicApiSingleton.__instance__

    def add_song_to_library(self, song: Dict) -> bool:
        """Add a song to the current user's Youtube Music library

        Args:
            song (Dict): Song to add

        Returns:
            bool: True -> Song was successfully added to library | False -> Song was NOT added to library
        """
        response = self.__youtube_music_api.edit_song_library_status(song['feedbackTokens']['add'])
        # If responseContext is empty then song is already in library
        if not response['responseContext']:
            return True
        return to_bool(response['feedbackResponses'][0]['isProcessed'])

    def delete_library_uploaded_song(self, uploaded_song_to_delete: Dict) -> None:
        """Delete an uploaded song from the current user's Youtube Music Library

        Args:
            uploaded_song_to_delete (Dict): Uploaded song to delete
        """
        self.__youtube_music_api.delete_upload_entity(uploaded_song_to_delete['entityId'])

    def get_library_uploaded_songs(self, song_limit: int, order: Order) -> List[Dict]:
        """Get a list of uploaded songs from the current user's Youtube Music Library

        Args:
            song_limit (int): Max amount of songs to retrieve
            order (Order): Order to retrieve the songs in

        Returns:
            List[Dict]: List of uploaded library songs
        """
        return self.__youtube_music_api.get_library_upload_songs(song_limit, order.value)

    def get_simple_library_playlists(self, playlist_limit: int) -> List[Dict]:
        """Get a list of simple (no song info included) playlist information from the current user's Youtube Music library

        Args:
            playlist_limit (int): Max amount of playlists to retrieve

        Returns:
            List[Dict]: List of simple library playlist information
        """
        return self.__youtube_music_api.get_library_playlists(playlist_limit)

    def rate_song(self, song: Dict, rating: LikeStatuses) -> None:
        """Rate a song (Like / Dislike / Indifferent)

        Args:
            song (Dict): Song to rate
        """
        self.__youtube_music_api.rate_song(song['videoId'], LikeStatuses.LIKE.value)

    def perform_search(
            self, query: str, item_type: ItemType, item_search_limit: int, ignore_spelling: bool) -> List[Dict]:
        """Search for an item in Youtube Music

        Args:
            query (str): Search query
            item_type (ItemType): Item type to search for
            item_search_limit (int): Max amount of items in the search results
            ignore_spelling (bool): True -> Ignore spelling suggestions | False -> Use autocorrected text

        Returns:
            List[Dict]: List of search result items
        """

        return self.__youtube_music_api.search(query, item_type.value, item_search_limit, ignore_spelling)

    def get_complete_playlist(self, playlist: Dict, playlist_song_limit: int) -> Dict:
        """Get complete information about the given playlist (including information about the items in the playlist)

        Args:
            playlist (Dict): Playlist to get information for
            playlist_song_limit (int): Max amount of songs to retrieve from the playlist

        Returns:
            Dict: Complete playlist
        """
        return self.__youtube_music_api.get_playlist(get_playlist_id(playlist), playlist_song_limit)

    def remove_songs_from_playlist(self, playlist: Dict, songs: List[Dict]) -> None:
        """Remove songs from a playlist in Youtube Music

        Args:
            playlist (Dict): Playlist to remove the song from (Complete playlist info required)
            songs (List[Dict]): List of songs to remove from the playlist
        """
        self.__youtube_music_api.remove_playlist_items(get_playlist_id(playlist), songs)
