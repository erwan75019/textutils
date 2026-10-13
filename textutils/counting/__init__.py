"""Functions for counting elements in text."""

from ._character_count import character_count
from ._text_statistics import text_statistics
from ._word_count import word_count

__all__ = ["word_count", "character_count", "text_statistics"]
