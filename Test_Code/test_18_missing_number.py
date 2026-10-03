import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

missing_number = SourceFileLoader(
    "missing_number",
    "Code/18_missing_number.py"
).load_module()


def test_find_missing_number():
    assert missing_number.find_missing_number([1, 2, 3, 5, 6]) == 4
    assert missing_number.find_missing_number([1, 2, 4, 5]) == 3
    assert missing_number.find_missing_number([1, 3, 4, 5]) == 2
