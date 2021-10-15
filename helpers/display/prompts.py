from helpers.display.util import clear_output

from PyInquirer import prompt


def yes_or_no_prompt(prompt_text: str) -> bool:
    """Prompts user for a (y/n) input

    Args:
        prompt (str): Text to display before (y/n)

    Returns:
        bool: True -> "y" | False -> "n"
    """
    options = {
        'type': 'confirm',
        'message': prompt_text,
        'name': prompt_text
    }
    return prompt(options).get(prompt_text)


def continue_prompt(prompt: str = "", clear_screen: bool = False) -> None:
    """Prompts user to "Press Enter to continue..."

    Args:
        prompt (str, optional): Optional text to display before the "Press Enter to continue..." message. Defaults to "".
        clear_screen (bool, optional): Set to True to clear the console after user presses enter. Defaults to False.
    """
    input(prompt + " Press Enter to continue...")
    if clear_screen:
        clear_output()
