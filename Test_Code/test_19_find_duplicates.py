import sys
sys.path.append("Code")

from importlib.util import spec_from_file_location, module_from_spec

spec = spec_from_file_location(
    "find_duplicates",
    "Code/19_find_duplicates.py"
)

module = module_from_spec(spec)
spec.loader.exec_module(module)

find_duplicates = module.find_duplicates


def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 2, 4, 5, 3, 6]) == [2, 3]
    assert find_duplicates([1, 2, 3, 4]) == []
    assert find_duplicates([5, 5, 5, 2, 2]) == [5, 2]


test_find_duplicates()

print("All test cases passed.")
