import sys
sys.path.append("Code")

from importlib.util import spec_from_file_location, module_from_spec

spec = spec_from_file_location(
    "remove_duplicates",
    "Code/16_remove_duplicates.py"
)

module = module_from_spec(spec)
spec.loader.exec_module(module)

remove_duplicates = module.remove_duplicates


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]


def test_remove_duplicates_with_strings():
    assert remove_duplicates(["apple", "apple", "banana", "orange"]) == [
        "apple",
        "banana",
        "orange"
    ]


test_remove_duplicates()
test_remove_duplicates_with_strings()

print("All test cases passed.")
