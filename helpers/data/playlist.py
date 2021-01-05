from typing import Dict, List


def _get_playlist_trackCount(playlist: Dict) -> str:
    # Playlist with Item Info
    if 'trackCount' in playlist:
        return playlist['trackCount']
    # Simple Playlist
    elif 'count' in playlist:
        return playlist['count']
    # "Liked Music" Playlist
    else:
        return "Unknown"


def get_playlist_id(playlist: Dict) -> str:
    # Playlist with Item Info
    if 'id' in playlist:
        return playlist['id']
    # Simple Playlist
    else:
        return playlist['playlistId']


def get_playlist_info(playlist: Dict) -> str:
    """
    Returns a nicely readable printout of the playlist's information
    """
    return(f"Title: {playlist['title']}\nSong Count: {_get_playlist_trackCount(playlist)}\n")


def get_playlist_display_list(playlists: List[Dict]) -> List[str]:
    playlist_display_list = []
    for playlist in playlists:
        playlist_display_list.append(get_playlist_info(playlist))
    return playlist_display_list
