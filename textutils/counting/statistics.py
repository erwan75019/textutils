import re


def text_statistics(text: str) -> dict:
    """Analyze a text and return a dictionary containing comprehensive statistics.

    Parameters
    ----------
    text : str
        Text to analyze.

    Returns
    -------
    dict
        A dictionary containing word_count, character_count, line_count,
        sentence_count, average_word_length, and longest_word.

    Examples
    --------
    >>> text_statistics("Hello world!")
    {'word_count': 2, 'character_count': 12, 'line_count': 1, 'sentence_count': 1, 'average_word_length': 5.0, 'longest_word': 'Hello'}
    """
    lines = text.splitlines()
    line_count = len(lines)
    character_count = len(text)

    tokens = text.split()
    words = [re.sub(r"^\W+|\W+$", "", token) for token in tokens]
    word_count = len(words)

    sentences = [
        sentence
        for sentence in re.split(r"[.!?]+", text)
        if re.search(r"\w", sentence)
    ]
    sentence_count = len(sentences)

    if word_count > 0:
        total_letters = sum(len(word) for word in words)
        average_word_length = round(total_letters / word_count, 2)
        longest_word = max(words, key=len, default="")
    else:
        average_word_length = 0.0
        longest_word = ""

    statistics_result = {
        "word_count": word_count,
        "character_count": character_count,
        "line_count": line_count,
        "sentence_count": sentence_count,
        "average_word_length": average_word_length,
        "longest_word": longest_word
    }

    return statistics_result
