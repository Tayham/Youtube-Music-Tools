from typing import Dict, List
import constants
from constants import LikeStatuses

# TODO: see if multiple contsructors are needed. If so follow this: https://stackoverflow.com/questions/141545/how-to-overload-init-method-based-on-argument-type

# def _create_playlist_track_list(playlistTrackList: List[Dict]) -> List['Track']:
#     track_object_list = []
#     for track in playlistTrackList:
#         track_object_list.append(PlaylistTrack(track))
#     return track_object_list

# class Track:
#     def __init__(self, track: Dict) -> None:
#         """
#         Initializes Track object using the YT Music API Dict
#         """
#         self.videoId = track['videoId']
#         self.title = track['title']
#         self.artists = track['artists']
#         self.album = track['album']
#         self.likeStatus = track['likeStatus']

#     def get_track_info(self) -> str:
#         """
#         Returns a nicely readable printout of the track's information
#         """
#         artists = ', '.join([artist['name'] for artist in self.artists])
#         return(f"Title: {self.title}\nArtist(s): {artists}\nAlbum: {self.album['name']}\nLiked: {self.likeStatus}\n")

#     def __getitem__(self,key : str):
#         print ("Inside `__getitem__` method!")
#         print(key)
#         print(type(key))
#         return getattr(self,str(key))

# class PlaylistTrack(Track):
#        def __init__(self, playlist_track: Dict) -> None:
#         """
#         Initializes Track object using the YT Music API Dict
#         """
#         super(PlaylistTrack, self).__init__(playlist_track)
#         self.setVideoId = playlist_track['setVideoId']


# class Playlist:

#     def __init__(self, playlist: Dict) -> None:
#         """
#         Initializes Playlist object using the YT Music API Dict
#         """
#         self.id = playlist['id']
#         self.title = playlist['title']
#         self.trackCount = playlist['trackCount']
#         self.tracks = _create_playlist_track_list(playlist['tracks'])

#     def get_playlist_info(self) -> str:
#         """
#         Returns a nicely readable printout of the playlist's information
#         """
#         return(f"Title: {self.title}\nTrack Count: {self.trackCount}\n")
    
#     def __getitem__(self,key):
#         print ("Inside `__getitem__` method!")
#         return getattr(self,key)