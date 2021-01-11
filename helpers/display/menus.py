import menu3
from core.constants import (
    MENU_PROMPT, MENU_PROMPT_SKIP_QUIT, MENU_TITLE,
    REMOVE_RATED_SONGS_FROM_PLAYLIST_OPTION,
    REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS)


def main_menu() -> int:
    """Displays Main Menu for application

    Returns:
        int: User selection starting at 1
    """
    return menu3.Menu(True).menu(
        title=MENU_TITLE,
        choices=[REMOVE_RATED_SONGS_FROM_PLAYLIST_OPTION, REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS],
        prompt=MENU_PROMPT_SKIP_QUIT)


def list_index_selection_menu(
        title: str, choices: list[str],
        prompt: str = MENU_PROMPT, allow_quit: bool = False, 
        allow_skip: bool = False) -> int:
    """Displays a menu that returns the index of the user selection.

    Args:
        title (str): Menu title text
        choices (list[str]): Choices to display to the user
        prompt (str, optional): Optional user promt text. Defaults to MENU_PROMPT.
        allow_quit (bool, optional): Set to True to allow user to enter 'q' to quit application. Defaults to False.
        allow_skip (bool, optional): Set to True to allow user to enter 0 to as a "Skip" option. Defaults to False.

    Returns:
        int: List index of the user selection
    """
    selection_index = menu3.Menu(allow_quit).menu(title=title, choices=choices, prompt=prompt) - 1
    # If given 0 and allow skip is not selected then redisplay the menu
    if selection_index == -1 and not allow_skip:
        return list_index_selection_menu(title, choices, prompt, allow_quit, allow_skip)
    else:
        return selection_index
