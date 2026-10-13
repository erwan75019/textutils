"""Capitalize words in text."""


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in a text.

    Parameters
    ----------
    text : str
        Text whose words are capitalized.

    Returns
    -------
    str
        Text with the first letter of each word capitalized.

    Examples
    --------
    >>> capitalize_words("hello world")
    'Hello World'
    """
    return text.title()
