from typing import Dict, List
import constants
from constants import LikeStatuses

# TODO: see if multiple contsructors are needed. If so follow this: https://stackoverflow.com/questions/141545/how-to-overload-init-method-based-on-argument-type

def _create_track_list(trackList: List[Dict]) -> List['Track']:
    track_object_list = []
    for track in trackList:
        track_object_list.append(Track(track))
    return track_object_list

class Track:
    def __init__(self, track: Dict) -> None:
        """
        Initializes Track object using the YT Music API Dict
        """
        self.id = track['videoId']
        self.title = track['title']
        self.artists = track['artists']
        self.album = track['album']
        self.likeStatus = track['likeStatus']

    def get_track_info(self) -> str:
        """
        Returns a nicely readable printout of the track's information
        """
        artists = ', '.join([artist['name'] for artist in self.artists])
        return(f"Title: {self.title}\nArtist(s): {artists}\nAlbum: {self.album['name']}\nLiked: {self.likeStatus}\n")

class Playlist:

    def __init__(self, playlist: Dict) -> None:
        """
        Initializes Playlist object using the YT Music API Dict
        """
        self.id = playlist['id']
        self.title = playlist['title']
        self.trackCount = playlist['trackCount']
        self.tracks = _create_track_list(playlist['tracks'])

    def get_playlist_info(self) -> str:
        """
        Returns a nicely readable printout of the playlist's information
        """
        return(f"Title: {self.title}\nTrack Count: {self.trackCount}\n")