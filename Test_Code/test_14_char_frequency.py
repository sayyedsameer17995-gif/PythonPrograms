import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

char_frequency_module = SourceFileLoader(
    "char_frequency",
    "Code/14_char_frequency.py"
).load_module()

char_frequency = char_frequency_module.char_frequency


def test_char_frequency():
    assert char_frequency("hello") == {
        "h": 1,
        "e": 1,
        "l": 2,
        "o": 1
    }


def test_char_frequency_with_spaces():
    assert char_frequency("hello world") == {
        "h": 1,
        "e": 1,
        "l": 3,
        "o": 2,
        "w": 1,
        "r": 1,
        "d": 1
    }
