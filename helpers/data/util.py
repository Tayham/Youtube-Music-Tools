def to_bool(value) -> bool:
    return str(value).lower() in ("yes", "true", "t", "1")
