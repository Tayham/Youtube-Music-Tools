from core.constants import HORIZONTAL_RULE


def print_title_with_info(title: str, info: str) -> None:
    """Print formatted title with information underneath

    Args:
        title (str): Title text to print
        info (str): Information text to print
    """
    print(f"\n{title}\n{HORIZONTAL_RULE}\n{info}")
