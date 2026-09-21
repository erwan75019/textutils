# textutils

`textutils` is a small Python library for common text operations. It provides
simple functions for counting, reversing, and capitalizing text.

## Available functions

| Function | Description |
| --- | --- |
| `word_count(text)` | Count words separated by whitespace. |
| `character_count(text)` | Count all characters, including spaces and punctuation. |
| `reverse(text)` | Return the characters in reverse order. |
| `capitalize_words(text)` | Capitalize the first letter of each word. |

## Usage

From the repository root, run Python and import the functions:

```python
from textutils import word_count, character_count, reverse, capitalize_words

text = "hello world"

print(word_count(text))        # 2
print(character_count(text))   # 11
print(reverse(text))           # dlrow olleh
print(capitalize_words(text))  # Hello World
```

## Contributing

Contributions are welcome. Create a branch, make a focused change, verify it
locally, and open a pull request with a short description of your change.

## License

This project uses the MIT License. See [LICENSE](LICENSE) for the full text.
