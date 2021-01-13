from typing import Dict, List


def _get_playlist_trackCount(playlist: Dict) -> str:
    """Retrieves the playlist's track count

    Args:
        playlist (Dict): Playlist Dict

    Returns:
        str: If track count data -> Playlist Track Count | If NO track count data -> "unknown"
    """
    # Playlist with Item Info
    if 'trackCount' in playlist:
        return playlist['trackCount']
    # Simple Playlist
    elif 'count' in playlist:
        return playlist['count']
    # "Liked Music" Playlist
    else:
        return "unknown"


def get_playlist_id(playlist: Dict) -> str:
    """Retrieves the playlist's ID

    Args:
        playlist (Dict): Playlist Dict

    Returns:
        str: Playlist ID
    """
    # Playlist with Item Info
    if 'id' in playlist:
        return playlist['id']
    # Simple Playlist
    else:
        return playlist['playlistId']


def get_playlist_info(playlist: Dict) -> str:
    """Returns readable playlist text

    Args:
        playlist (Dict): Playlist used to generate readable playlist text

    Returns:
        str: Readable playlist text
    """
    return(f"Title: {playlist['title']}\nSong Count: {_get_playlist_trackCount(playlist)}\n")


def get_playlist_display_list(playlists: List[Dict]) -> List[str]:
    """Returns a list of readable playlist text

    Args:
        playlists (List[Dict]): List of playlists used to generate readable playlist text

    Returns:
        List[str]: List of readable playlist text
    """
    playlist_display_list = []
    for playlist in playlists:
        playlist_display_list.append(get_playlist_info(playlist))
    return playlist_display_list

def has_item_info(playlist: Dict) -> bool:
    """Checks whether playlist is complete (has item information)

    Args:
        playlist (Dict): Playlist to check

    Returns:
        bool: True -> Playlist is complete | False -> Playlist is NOT complete
    """
    return 'tracks' in playlist
