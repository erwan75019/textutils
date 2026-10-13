import pytest

from textutils.counting import character_count, word_count


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
