from typing import Dict, List


def _get_song_artists(song: Dict) -> str:
    # Uploaded Song
    if 'artist' in song:
        return ', '.join([artist['name'] for artist in song['artist']])
    # Streaming Song or Song Search Result
    elif 'artists' in song:
        return ', '.join([artist['name'] for artist in song['artists']])


def _get_song_album(song: Dict) -> str:
    # Song has album
    if song['album']:
        return song['album']['name']
    # Song does not have album
    else:
        return "none"


def _get_song_length(song: Dict) -> str:
    # Streaming Song
    if 'lengthSeconds' in song:
        return song['lengthSeconds']
    # Song Search Result
    elif 'duration' in song:
        return song['duration']
    # Uploaded Song
    else:
        return "unknown"


def _get_song_like_status(song: Dict) -> str:
    # Uploaded Song or Streaming Song
    if 'likeStatus' in song:
        return song['likeStatus']
    # Song Search Result
    else:
        return "n/a"


def get_song_query(song: Dict) -> str:
    """
    Returns a good search query based on the songs information
    """
    return(f"{song['title']} by {_get_song_artists(song)}\n")


def get_song_info(song: Dict) -> str:
    """
    Returns a nicely readable printout of the song's information
    """
    return(f"Title: {song['title']}\nArtist(s): {_get_song_artists(song)}\nAlbum: {_get_song_album(song)}\nLiked: {_get_song_like_status(song)}\nLength: {_get_song_length(song)}\n")


def get_song_display_list(songs: List[Dict]) -> List[str]:
    song_display_list = []
    for song in songs:
        song_display_list.append(get_song_info(song))
    return song_display_list
