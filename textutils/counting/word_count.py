"""Count words in text."""


def word_count(text: str) -> int:
    """Count the words separated by whitespace in a text.

    Parameters
    ----------
    text : str
        Text whose words are counted.

    Returns
    -------
    int
        Number of words in the text.

    Examples
    --------
    >>> word_count("Hello world")
    2
    """
    return len(text.split())
