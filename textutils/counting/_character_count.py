"""Count characters in text."""


def character_count(text: str) -> int:
    """Count the characters in a text, including whitespace.

    Parameters
    ----------
    text : str
        Text whose characters are counted.

    Returns
    -------
    int
        Number of characters in the text.

    Examples
    --------
    >>> character_count("Hello world")
    11
    """
    return len(text)
