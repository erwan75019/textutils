import textutils


def test_root_public_api():
    assert textutils.__all__ == [
        "word_count",
        "character_count",
        "reverse",
        "capitalize_words",
        "snake_case",
        "text_statistics",
    ]
    assert textutils.word_count("one two") == 2
    assert textutils.character_count("abc") == 3
    assert textutils.reverse("abc") == "cba"
    assert textutils.capitalize_words("hello world") == "Hello World"
    assert textutils.snake_case("Hello world") == "hello_world"
    assert textutils.text_statistics("Hello world")["word_count"] == 2
