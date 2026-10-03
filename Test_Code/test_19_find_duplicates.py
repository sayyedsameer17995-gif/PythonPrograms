import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

duplicates = SourceFileLoader(
    "find_duplicates",
    "Code/19_find_duplicates.py"
).load_module()


def test_find_duplicates():
    assert duplicates.find_duplicates([1, 2, 3, 2, 4, 5, 3, 6]) == [2, 3]
    assert duplicates.find_duplicates([1, 2, 3, 4]) == []
    assert duplicates.find_duplicates([5, 5, 5, 2, 2]) == [5, 2]
