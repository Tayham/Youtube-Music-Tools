from typing import Dict, List


def _get_song_artists(song: Dict) -> str:
    """Retrieves the song's artist(s)

    Args:
        song (Dict): Song Dict

    Returns:
        str: Song Artist(s)
    """
    # Uploaded Song
    if 'artist' in song:
        return ', '.join([artist['name'] for artist in song['artist']])
    # Streaming Song or Song Search Result
    elif 'artists' in song:
        return ', '.join([artist['name'] for artist in song['artists']])


def _get_song_album(song: Dict) -> str:
    """Retrieves the song's album

    Args:
        song (Dict): Song Dict

    Returns:
        str: If album data -> Album Name | If NO album data -> "none"
    """
    # Song has album
    if song['album']:
        return song['album']['name']
    # Song does not have album
    else:
        return "none"


def _get_song_length(song: Dict) -> str:
    """Retrieves the song's length

    Args:
        song (Dict): Song Dict

    Returns:
        str: If length data -> Song Length | If NO length data -> "unknown"
    """
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
    """Retrieves the song's like status

    Args:
        song (Dict): Song Dict

    Returns:
        str: If like status data -> Like Status | If NO status data -> "n/a"
    """
    # Uploaded Song or Streaming Song
    if 'likeStatus' in song:
        return song['likeStatus']
    # Song Search Result
    else:
        return "n/a"


def get_song_query(song: Dict) -> str:
    """Returns search query text

    Args:
        song (Dict): Song used to generate search query text

    Returns:
        str: Search query text
    """
    return(f"{song['title']} by {_get_song_artists(song)}\n")


def get_song_info(song: Dict) -> str:
    """Returns readable song text

    Args:
        song (Dict): Song used to generate readable song text

    Returns:
        str: Readable song text
    """
    return(f"Title: {song['title']}\nArtist(s): {_get_song_artists(song)}\nAlbum: {_get_song_album(song)}\nLiked: {_get_song_like_status(song)}\nLength: {_get_song_length(song)}\n")


def get_song_display_list(songs: List[Dict]) -> List[str]:
    """Returns a list of readable song text

    Args:
        songs (List[Dict]): List of songs used to generate readable song text list

    Returns:
        List[str]: List of readable song text
    """
    song_display_list = []
    for song in songs:
        song_display_list.append(get_song_info(song))
    return song_display_list
