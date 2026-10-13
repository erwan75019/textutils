"""Reverse text."""


def reverse(text: str) -> str:
    """Reverse the order of the characters in a text.

    Parameters
    ----------
    text : str
        Text to reverse.

    Returns
    -------
    str
        Text with its characters in reverse order.

    Examples
    --------
    >>> reverse("Hello")
    'olleH'
    """
    return text[::-1]
