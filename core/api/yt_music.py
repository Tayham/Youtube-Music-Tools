from typing import Dict, List

from core.constants.api import ItemType, LikeStatuses, Order
from core.constants.paths import HEADERS_AUTH_FILE_PATH
from helpers.data.feedback_tokens import FeedbackTokens
from helpers.data.playlist import Playlist
from helpers.data.song import Song
from helpers.data.util import to_bool
from ytmusicapi import YTMusic


class YoutubeMusicApiSingleton:
    __instance__ = None

    def __init__(self):
        """ Constructor."""
        self.__youtube_music_api = YTMusic(HEADERS_AUTH_FILE_PATH)
        if YoutubeMusicApiSingleton.__instance__ is None:
            YoutubeMusicApiSingleton.__instance__ = self
        else:
            raise Exception(
                "You cannot create another YoutubeMusicApiSingleton class, this class is a singleton"
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

    def add_song_to_library(self, song_to_add: Song) -> bool:
        """Add a song to the current user's Youtube Music library

        Args:
            song_to_add (Song): Song to add to library

        Returns:
            bool: True -> Song was successfully added to library | False -> Song was NOT added to library
        """
        response = self.__youtube_music_api.edit_song_library_status(song_to_add.feedback_tokens.add)
        # If responseContext is empty then song is already in library
        if not response['responseContext']:
            return True
        return to_bool(response['feedbackResponses'][0]['isProcessed'])

    def delete_library_uploaded_song(self, uploaded_song_to_delete: Song) -> None:
        """Delete an uploaded song from the current user's Youtube Music Library

        Args:
            uploaded_song_to_delete (Song): Uploaded song to delete
        """
        self.__youtube_music_api.delete_upload_entity(uploaded_song_to_delete.id)

    def get_library_uploaded_songs(self, song_limit: int, order: Order) -> List[Song]:
        """Get a list of uploaded songs from the current user's Youtube Music Library

        Args:
            song_limit (int): Max amount of songs to retrieve
            order (Order): Order to retrieve the songs in

        Returns:
            List[Song]: List of uploaded library songs
        """
        return [Song(
            id=song_dict['videoId'],
            title=song_dict['title'],
            artists=[artist['name'] for artist in song_dict['artists']],
            album=song_dict['album']['name'],
            length=song_dict['duration'],
            like_status=LikeStatuses[song_dict['likeStatus']]) for song_dict in self.__youtube_music_api.get_library_upload_songs(song_limit, order.value)]

    def get_simple_library_playlists(self, playlist_limit: int) -> List[Playlist]:
        """Get a list of simple (no song info included) playlist information from the current user's Youtube Music library

        Args:
            playlist_limit (int): Max amount of playlists to retrieve

        Returns:
            List[Playlist]: List of simple library playlist information
        """
        return [Playlist(
            id=playlist_dict['playlistId'],
            title=playlist_dict['title'],
            song_count=playlist_dict.get('count', None)) for playlist_dict in self.__youtube_music_api.get_library_playlists(playlist_limit)]

    def rate_song(self, song: Song, rating: LikeStatuses) -> None:
        """Rate a song (Like / Dislike / Indifferent)

        Args:
            song (Song): Song to rate
        """
        self.__youtube_music_api.rate_song(song.id, rating)

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

        search_results = []
        for result in self.__youtube_music_api.search(query=query, filter=item_type.value, limit=item_search_limit, ignore_spelling=ignore_spelling):

            if result['resultType'] == "song":
                search_results.append(
                    Song(
                        id=result['videoId'],
                        title=result['title'],
                        artists=[artist['name'] for artist in result['artists']],
                        album=result['album']['name'],
                        explicit=to_bool(result['isExplicit']),
                        length=result['duration'],
                        feedback_tokens=FeedbackTokens(
                            add=result['feedbackTokens']['add'],
                            remove=result['feedbackTokens']['remove'])))

            if result['resultType'] == "playlist":
                search_results.append(
                    Playlist(
                        id=result['browseId'],
                        title=result['title'],
                        song_count=result['itemCount']))

        return search_results

    def get_complete_playlist(self, playlist: Playlist, playlist_song_limit: int) -> Playlist:
        """Get complete information about the given playlist (including information about the items in the playlist)

        Args:
            playlist (Playlist): Playlist to get information for
            playlist_song_limit (int): Max amount of songs to retrieve from the playlist

        Returns:
            Playlist: Complete playlist
        """
        response = self.__youtube_music_api.get_playlist(playlist.id, playlist_song_limit)
        return Playlist(
            id=response['id'],
            title=response['title'],
            song_count=response['trackCount'],
            songs=[Song(
                id=song_dict['videoId'],
                title=song_dict['title'],
                artists=[artist['name'] for artist in song_dict['artists']],
                album=song_dict['album']['name'],
                explicit=to_bool(song_dict['isExplicit']),
                length=song_dict.get('duration'),
                like_status=LikeStatuses(song_dict['likeStatus']) if song_dict['likeStatus'] else None,
                set_id=song_dict['setVideoId'],
                feedback_tokens=FeedbackTokens(
                    add=song_dict.get('feedbackTokens', {}).get('add'),
                    remove=song_dict.get('feedbackTokens', {}).get('remove'))) for song_dict in response['tracks']])

    def remove_songs_from_playlist(self, playlist: Playlist, songs: List[Song]) -> None:
        """Remove songs from a playlist in Youtube Music

        Args:
            playlist (Playlist): Playlist to remove the song from (Complete playlist info required)
            songs (List[Song]): List of songs to remove from the playlist
        """
        self.__youtube_music_api.remove_playlist_items(playlist.id,
                                                       [{'videoId': song.id, 'setVideoId': song.set_id}
                                                        for song in songs])
