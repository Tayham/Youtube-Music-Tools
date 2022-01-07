import json
import traceback
from typing import Dict, List
from core.constants.paths import UPLOADED_SONG_CHECK_SKIP_LIST_FILE_PATH
from helpers.data.song import Song


class UploadedSongStreamingSkipListHandler:

    def __init__(self):
        self.__uploaded_song_streaming_check_skip_list = []

    def __enter__(self):
        self.__skip_list_json_file = open(UPLOADED_SONG_CHECK_SKIP_LIST_FILE_PATH, "r+")
        self.__uploaded_song_streaming_check_skip_list = json.load(self.__skip_list_json_file)
        return self

    def __exit__(self, exception_type, exception_value, trace_back):
        if self.__uploaded_song_streaming_check_skip_list:  # If there are songs in the list
            self.__skip_list_json_file.seek(0)
            json.dump(self.__uploaded_song_streaming_check_skip_list, self.__skip_list_json_file)
            self.__skip_list_json_file.truncate()
        if exception_type is not None:
            traceback.print_exception(exception_type, exception_value, trace_back)
        self.__skip_list_json_file.close

    def add_song_to_uploaded_song_streaming_check_skip_list(self, song: Song) -> None:
        """Adds a song id to the list of uploaded song ids that should be skipped when checking if they are available for streaming

        Args:
            Song: Song to add to the list of uploaded songs that should be skipped when checking if they are available for streaming
        """
        self.__uploaded_song_streaming_check_skip_list.append({"id": song.id})

    def get_uploaded_song_streaming_check_skip_list(self) -> List[Dict]:
        """Gets the list of uploaded song ids that should be skipped when checking if they are available for streaming

        Returns:
            List[Dict]: List of uploaded song ids that should be skipped when checking if they are available for streaming
        """
        return self.__uploaded_song_streaming_check_skip_list
