from typing import List

import menu3
from core.constants.menu import (
    MAIN_MENU_TITLE, MENU_CHOOSE_PROMPT, QUIT_OPTION,
    REMOVE_RATED_SONGS_FROM_PLAYLIST_OPTION,
    REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS, SKIP_OPTION)


def _get_prompt_with_menu_options(prompt, allow_quit, allow_skip):
    return prompt + (SKIP_OPTION if allow_skip else "") + (QUIT_OPTION if allow_quit else "") + ":"


def main_menu() -> int:
    """Displays Main Menu for application

    Returns:
        int: User selection starting at 1
    """
    return menu3.Menu(True).menu(
        title=MAIN_MENU_TITLE,
        choices=[REMOVE_RATED_SONGS_FROM_PLAYLIST_OPTION, REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS],
        prompt=_get_prompt_with_menu_options(MENU_CHOOSE_PROMPT, True, False))


def list_index_selection_menu(
        title: str, choices: List[str],
        prompt: str = MENU_CHOOSE_PROMPT, allow_quit: bool = False,
        allow_skip: bool = False) -> int:
    """Displays a menu that returns the index of the user selection.

    Args:
        title (str): Menu title text
        choices (List[str]): Choices to display to the user
        prompt (str, optional): Optional user promt text. Defaults to MENU_CHOOSE.
        allow_quit (bool, optional): Set to True to allow user to enter 'q' to quit application. Defaults to False.
        allow_skip (bool, optional): Set to True to allow user to enter 0 to as a "Skip" option. Defaults to False.

    Returns:
        int: List index of the user selection
    """
    prompt_with_menu_options = _get_prompt_with_menu_options(prompt, allow_quit, allow_skip)
    selection_index = menu3.Menu(allow_quit).menu(title=title, choices=choices, prompt=prompt_with_menu_options) - 1
    # If given 0 and allow skip is not selected then redisplay the menu
    if selection_index == -1 and not allow_skip:
        return list_index_selection_menu(title, choices, prompt_with_menu_options, allow_quit, allow_skip)
    else:
        return selection_index
