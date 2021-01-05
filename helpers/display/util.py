import os


def clear_output() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
