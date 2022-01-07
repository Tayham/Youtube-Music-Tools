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
