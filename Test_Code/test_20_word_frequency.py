import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

word_freq = SourceFileLoader(
    "word_frequency",
    "Code/20_word_frequency.py"
).load_module()


def test_word_frequency():
    assert word_freq.word_frequency("python is easy and python is powerful") == {
        "python": 2,
        "is": 2,
        "easy": 1,
        "and": 1,
        "powerful": 1
    }

    assert word_freq.word_frequency("hello hello world") == {
        "hello": 2,
        "world": 1
    }
