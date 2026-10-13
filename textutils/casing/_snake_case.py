"""Convert text to snake case."""

import re


def snake_case(text: str) -> str:
    """Convert text to lowercase words separated by underscores.

    Parameters
    ----------
    text : str
        Text to convert to snake case.

    Returns
    -------
    str
        Text converted to snake case.

    Examples
    --------
    >>> snake_case("Hello world")
    'hello_world'
    >>> snake_case("HTTPResponseCode")
    'http_response_code'
    """
    # Split an acronym from the capitalized word that follows it, then split
    # the remaining camel-case boundaries.
    text = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", text)
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)

    # Treat punctuation and whitespace as separators, collapse consecutive
    # separators, and avoid leading or trailing underscores.
    text = re.sub(r"[^\w]+", "_", text)
    text = re.sub(r"_+", "_", text)
    return text.strip("_").lower()
