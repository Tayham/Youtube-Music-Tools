import json
from typing import List
from core.constants.paths import SETTINGS_FILE_PATH


class YoutubeMusicToolsSettingsSingleton:
    __instance__ = None

    def __init__(self):
        """Constructor."""
        with open(SETTINGS_FILE_PATH) as jsonSettings:
            self.__youtube_music_tools_settings = json.load(jsonSettings)
        if YoutubeMusicToolsSettingsSingleton.__instance__ is None:
            YoutubeMusicToolsSettingsSingleton.__instance__ = self
        else:
            raise Exception(
                "You cannot create another YoutubeMusicToolsSettingsSingleton class, this class is a singleton"
            )

    @staticmethod
    def get_instance() -> 'YoutubeMusicToolsSettingsSingleton':
        """Static method to get the current instance

        Returns:
            YoutubeMusicToolsSettingsSingleton: Instance of the YoutubeMusicToolsSettingsSingleton
        """
        if not YoutubeMusicToolsSettingsSingleton.__instance__:
            YoutubeMusicToolsSettingsSingleton()
        return YoutubeMusicToolsSettingsSingleton.__instance__

    def get_default_remove_rated_songs_playlist_titles(self) -> List[str]:
        """Gets the list of configured library playlist titles to remove rated songs from

        Returns:
            List[str]: List of configured library playlist titles to remove rated songs from
        """
        return self.__youtube_music_tools_settings["defaultRemoveRatedSongsPlaylists"]

    def get_playlist_limit(self) -> int:
        """Gets the limit of playlists to retrieve via API

        Returns:
            int: The limit of playlists to retrieve via API
        """
        return self.__youtube_music_tools_settings["playlistLimit"]

    def get_playlist_song_limit(self) -> int:
        """Gets the limit of songs in a playlist to retrieve via API

        Returns:
            int: The limit of songs in a playlist to retrieve via API
        """
        return self.__youtube_music_tools_settings["playlistSongLimit"]

    def get_song_search_result_limit(self) -> int:
        """Gets the limit of search result songs to retrieve via API

        Returns:
            int: The limit of search result songs to retrieve via API
        """
        return self.__youtube_music_tools_settings["songSearchResultLimit"]

    def get_uploaded_song_limit(self) -> int:
        """Gets the limit of uploaded songs to retrieve via API

        Returns:
            int: The limit of uploaded songs to retrieve via API
        """
        return self.__youtube_music_tools_settings["uploadedSongLimit"]
