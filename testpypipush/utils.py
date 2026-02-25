"""
utils.py - Helper functions.
"""


def format_message(message: str) -> str:
    if not isinstance(message, str):
        raise TypeError(f"Expected str, got {type(message).__name__}")
    return message.strip()


def validate_input(value, expected_type: type, name: str = "value") -> None:
    if not isinstance(value, expected_type):
        raise TypeError(
            f"'{name}' must be of type {expected_type.__name__}, "
            f"got {type(value).__name__} instead."
        )
    if isinstance(value, str) and not value.strip():
        raise ValueError(f"'{name}' must not be an empty string.")


def chunk_list(lst: list, size: int) -> list:
    if size < 1:
        raise ValueError("Chunk size must be at least 1.")
    return [lst[i : i + size] for i in range(0, len(lst), size)]


def flatten(nested: list) -> list:
    return [item for sublist in nested for item in sublist]