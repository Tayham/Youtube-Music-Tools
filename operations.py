import api
from api import YoutubeMusicApiSingleton

youtube_music_api = YoutubeMusicApiSingleton()

def get_track_info(track):
    trackArtists = track['artists']
    artists = ', '.join([artist['name'] for artist in trackArtists])
    return(f"Track: {track['title']}\nArtist(s): {artists}\nAlbum: {track['album']['name']}\nLiked: {track['likeStatus']}\n")

def add_liked_songs_in_playlist_to_library(playlist_title: str):
    """
    Add liked songs from a playlist to youtube music library
    """
    playlist_tracks = youtube_music_api.get_library_playlist_by_title("Test Playlist")['tracks']
    liked_playlist_tracks = filter(lambda track: track['likeStatus'] == 'LIKE', playlist_tracks)
    print("Liked Songs:\n")
    for track in liked_playlist_tracks:
        print(get_track_info(track))
        
    #TODO add songs to library
    