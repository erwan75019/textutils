"""Simple utilities for working with text."""


def word_count(text: str) -> int:
    """Return the number of words separated by whitespace in text."""
    return len(text.split())


def character_count(text: str) -> int:
    """Return the number of characters in text, including whitespace."""
    return len(text)
