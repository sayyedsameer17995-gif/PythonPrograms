import sys
sys.path.append("Code")

from importlib.util import spec_from_file_location, module_from_spec

spec = spec_from_file_location(
    "common_elements",
    "Code/17_common_elements.py"
)

module = module_from_spec(spec)
spec.loader.exec_module(module)

common_elements = module.common_elements


def test_common_elements():
    assert common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [3, 4, 5]


def test_common_elements_with_no_common():
    assert common_elements([1, 2, 3], [4, 5, 6]) == []


test_common_elements()
test_common_elements_with_no_common()

print("All test cases passed.")
