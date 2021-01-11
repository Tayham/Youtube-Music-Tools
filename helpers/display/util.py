import os


def clear_output() -> None:
    """Clears console output"""
    os.system('cls' if os.name == 'nt' else 'clear')
