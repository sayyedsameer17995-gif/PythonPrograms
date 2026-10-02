import sys
from importlib.machinery import SourceFileLoader

sys.path.append("Code")

module = SourceFileLoader(
    "second_largest",
    "Code/15_second_largest.py"
).load_module()

second_largest = module.second_largest


def test_second_largest():
    assert second_largest([12, 36, 16, 5, 8]) == 16


def test_second_largest_with_duplicates():
    assert second_largest([10, 20, 20, 5, 8]) == 10
