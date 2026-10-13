import pytest

from textutils.transformation import capitalize_words, reverse


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello world", "dlrow olleH"),
        ("été", "été"),
        ("a b", "b a"),
        ("", ""),
    ],
)
def test_reverse(text, expected):
    assert reverse(text) == expected


def test_capitalize_words_backward_compatible_import():
    assert capitalize_words("hello world") == "Hello World"
