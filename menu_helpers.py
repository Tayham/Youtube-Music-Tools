import menu3
import os
from constants import *

def _clear_screen() -> None:
    os.system('cls' if os.name=='nt' else 'clear')

### Menus ###

def main_menu() -> None:
    return menu3.Menu(True).menu(title=MENU_TITLE, choices=[REMOVE_RATED_SONGS_FROM_PLAYLIST_OPTION, REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS], prompt=MENU_PROMPT_QUIT)

def list_index_selection_menu(title: str, choices: list[str], prompt: str = MENU_PROMPT, allow_quit: bool = False, allow_skip: bool = False) -> int:
    selection_index = menu3.Menu(allow_quit).menu(title=title, choices=choices, prompt=prompt) - 1
    # If given 0 and allow skip is not selected then redisplay the menu
    if selection_index == -1 and not allow_skip:
        return list_index_selection_menu(title,choices,prompt,allow_quit,allow_skip)
    else:
        return selection_index

### Prompts ###

def yes_or_no_prompt(prompt: str) -> bool:
    while True:
        response = str(input(prompt + " (y/n): ")).lower().strip()
        if response[:1] == "y":
            return True
        if response[:1] == "n":
            return False

def continue_prompt(prompt: str = "", clear_screen: bool = False) -> None:
    input(prompt + " Press Enter to continue...")
    if clear_screen:
        _clear_screen()

### Print Helpers ###

def print_title_with_info(title: str, info:str) -> None:
    print(f"\n{title}\n{HORIZONTAL_RULE}\n{info}")