import sys
sys.path.append("Code")

from importlib.util import spec_from_file_location, module_from_spec

spec = spec_from_file_location(
    "second_largest",
    "Code/15_second_largest.py"
)

module = module_from_spec(spec)
spec.loader.exec_module(module)

second_largest = module.second_largest


def test_second_largest():
    assert second_largest([12, 36, 16, 5, 8]) == 16


def test_second_largest_with_duplicates():
    assert second_largest([10, 20, 20, 5, 8]) == 10


test_second_largest()
test_second_largest_with_duplicates()

print("All test cases passed.")
