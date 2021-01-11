from typing import Any


def to_bool(value: Any) -> bool:
    """Utility function that converts common binary data values to boolean

    Args:
        value (Any): value to convert to boolean

    Returns:
        bool: True -> "yes", "true", "t", 1 | False -> everything else   
    """
    return str(value).lower() in ("yes", "true", "t", "1")
