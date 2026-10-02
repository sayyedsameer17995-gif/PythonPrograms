import sys
from importlib.machinery import SourceFileLoader

sys.path.append("Code")

module = SourceFileLoader(
    "remove_duplicates",
    "Code/16_remove_duplicates.py"
).load_module()

remove_duplicates = module.remove_duplicates


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]


def test_remove_duplicates_with_strings():
    assert remove_duplicates(["apple", "apple", "banana", "orange"]) == [
        "apple",
        "banana",
        "orange"
    ]
