import menu3
from core.constants import (
    MENU_PROMPT, MENU_PROMPT_SKIP_QUIT, MENU_TITLE,
    REMOVE_RATED_SONGS_FROM_PLAYLIST_OPTION,
    REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS)


def main_menu() -> None:
    return menu3.Menu(True).menu(
        title=MENU_TITLE,
        choices=[REMOVE_RATED_SONGS_FROM_PLAYLIST_OPTION, REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS],
        prompt=MENU_PROMPT_SKIP_QUIT)


def list_index_selection_menu(
        title: str, choices: list[str],
        prompt: str = MENU_PROMPT, allow_quit: bool = False, allow_skip: bool = False) -> int:
    selection_index = menu3.Menu(allow_quit).menu(title=title, choices=choices, prompt=prompt) - 1
    # If given 0 and allow skip is not selected then redisplay the menu
    if selection_index == -1 and not allow_skip:
        return list_index_selection_menu(title, choices, prompt, allow_quit, allow_skip)
    else:
        return selection_index
