from helpers.display.util import clear_output


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
        clear_output()
