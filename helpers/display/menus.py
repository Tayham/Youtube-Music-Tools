from typing import List

from InquirerPy import prompt

from core.constants.menu import (
    ADD_SKIP_LIST_OPTION, MAIN_MENU_TITLE, MENU_CHOOSE_PROMPT, QUIT_OPTION,
    REMOVE_RATED_SONGS_FROM_DEFAULT_PLAYLISTS_OPTION, REMOVE_RATED_SONGS_FROM_PLAYLIST_OPTION,
    REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS, SKIP_OPTION)


def _get_list_menu_options(choices: List[dict], allow_quit: bool = False,
                           allow_skip: bool = False, allow_add_to_skip_list: bool = False) -> List:
    menu_options = [{'name': str(choice), 'value': choice, 'short': str(choice)} for choice in choices]
    if allow_add_to_skip_list:
        menu_options.append(ADD_SKIP_LIST_OPTION)
    if allow_skip:
        menu_options.append(SKIP_OPTION)
    if allow_quit:
        menu_options.append(QUIT_OPTION)
    return menu_options


def main_menu() -> str:
    """Displays Main Menu for application

    Returns:
        str: User Selected Option
    """
    main_menu = {
        'type': 'list',
        'name':  MAIN_MENU_TITLE,
        'message': MENU_CHOOSE_PROMPT,
        'choices': _get_list_menu_options([REMOVE_RATED_SONGS_FROM_DEFAULT_PLAYLISTS_OPTION,
                                           REMOVE_RATED_SONGS_FROM_PLAYLIST_OPTION,
                                           REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS], True, False, False),
    }
    return prompt(main_menu).get(MAIN_MENU_TITLE)


def list_selection_menu(title: str, choices: List[dict], prompt_text: str = MENU_CHOOSE_PROMPT) -> dict:
    """Displays a menu with quit option. Returns the index of the user selection.

    Args:
        title (str): Menu title text
        choices (List[dict]): Choices to display to the user
        prompt (str, optional): Optional user prompt text. Defaults to MENU_CHOOSE_PROMPT.

    Returns:
        dict: kv dict with key=title and value=selection dict
    """

    list_menu = {
        'type': 'list',
        'name':  title,
        'message': prompt_text,
        'choices': _get_list_menu_options(choices, True, False, False),
    }
    return prompt(list_menu)

def list_comparison_selection_menu(title: str, choices: List[dict], prompt_text: str = MENU_CHOOSE_PROMPT) -> dict:
    """Displays a comparision menu with skip, add to skip list, and quit options. Returns the index of the user selection.

    Args:
        title (str): Menu title text
        choices (List[dict]): Choices to display to the user
        prompt (str, optional): Optional user prompt text. Defaults to MENU_CHOOSE_PROMPT.

    Returns:
        dict: kv dict with key=title and value=selection dict
    """

    list_menu = {
        'type': 'list',
        'name':  title,
        'message': prompt_text,
        'choices': _get_list_menu_options(choices, True, True, True),
    }
    return prompt(list_menu)
