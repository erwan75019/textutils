import pytest

from textutils.counting import character_count, text_statistics, word_count


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello world", 2),
        ("one\ttwo\nthree", 3),
        ("punctuation, stays! attached.", 3),
        ("   ", 0),
        ("", 0),
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello world", 11),
        ("spaces count", 12),
        ("café ☕", 6),
        ("", 0),
    ],
)
def test_character_count(text, expected):
    assert character_count(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        (
            "Hello world!",
            {
                "word_count": 2,
                "character_count": 12,
                "line_count": 1,
                "sentence_count": 1,
                "average_word_length": 5.0,
                "longest_word": "Hello",
            },
        ),
        (
            "",
            {
                "word_count": 0,
                "character_count": 0,
                "line_count": 0,
                "sentence_count": 0,
                "average_word_length": 0.0,
                "longest_word": "",
            },
        ),
    ],
)
def test_text_statistics(text, expected):
    assert text_statistics(text) == expected
