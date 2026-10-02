import sys
from importlib.machinery import SourceFileLoader

sys.path.append("Code")

module = SourceFileLoader(
    "common_elements",
    "Code/17_common_elements.py"
).load_module()

common_elements = module.common_elements


def test_common_elements():
    assert common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [3, 4, 5]


def test_common_elements_with_no_common():
    assert common_elements([1, 2, 3], [4, 5, 6]) == []
