import pytest

from textutils.casing import capitalize_words, snake_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("hello world", "Hello World"),
        ("hELLo woRLD", "Hello World"),
        ("hello\tworld\nagain", "Hello\tWorld\nAgain"),
        ("", ""),
    ],
)
def test_capitalize_words(text, expected):
    assert capitalize_words(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello world", "hello_world"),
        ("HTTPResponseCode", "http_response_code"),
        ("version2Value", "version2_value"),
        ("  hello---world!  ", "hello_world"),
        ("already__snake_case", "already_snake_case"),
        ("Crème brûlée", "crème_brûlée"),
        ("", ""),
    ],
)
def test_snake_case(text, expected):
    assert snake_case(text) == expected
