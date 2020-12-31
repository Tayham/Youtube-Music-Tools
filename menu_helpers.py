import menu3
from constants import *

def main_menu():
    return menu3.Menu(True).menu(title=MENU_TITLE, choices=[REMOVE_LIKED_SONGS_FROM_PLAYLIST_OPTION, REPLACE_UPLOADED_SONGS_WITH_STREAMING_VERSIONS], prompt=MENU_PROMPT)

def list_selection_menu(title: str, choices: list[str], prompt: str) -> int:
    return menu3.Menu(False).menu(title=title, choices=choices, prompt=prompt) - 1

def yes_or_no_prompt(prompt: str) -> bool:
    while(True):
        response = str(input(prompt + " (y/n): ")).lower().strip()
        if response[:1] == "y":
            return True
        if response[:1] == "n":
            return False

def continue_prompt(prompt: str = ""):
    input(prompt + " Press Enter to continue...")