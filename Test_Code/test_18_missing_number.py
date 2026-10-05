import sys
sys.path.append("Code")

from importlib.util import spec_from_file_location, module_from_spec

spec = spec_from_file_location(
    "missing_number",
    "Code/18_missing_number.py"
)

module = module_from_spec(spec)
spec.loader.exec_module(module)

find_missing_number = module.find_missing_number


def test_find_missing_number():
    assert find_missing_number([1, 2, 3, 5, 6]) == 4
    assert find_missing_number([1, 2, 4, 5]) == 3
    assert find_missing_number([1, 3, 4, 5]) == 2


test_find_missing_number()

print("All test cases passed.")
