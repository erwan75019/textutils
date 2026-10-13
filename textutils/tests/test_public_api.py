import textutils


def test_root_public_api():
    assert textutils.__all__ == [
        "word_count",
        "character_count",
        "reverse",
        "capitalize_words",
        "snake_case",
    ]
    assert textutils.word_count("one two") == 2
    assert textutils.character_count("abc") == 3
    assert textutils.reverse("abc") == "cba"
    assert textutils.capitalize_words("hello world") == "Hello World"
    assert textutils.snake_case("Hello world") == "hello_world"
