import sys
sys.path.append("Code")

from importlib.util import spec_from_file_location, module_from_spec

spec = spec_from_file_location(
    "char_frequency",
    "Code/14_char_frequency.py"
)

module = module_from_spec(spec)
spec.loader.exec_module(module)

char_frequency = module.char_frequency


def test_char_frequency():
    assert char_frequency("hello") == {
        "h": 1,
        "e": 1,
        "l": 2,
        "o": 1
    }


def test_char_frequency_with_spaces():
    assert char_frequency("hello world") == {
        "h": 1,
        "e": 1,
        "l": 3,
        "o": 2,
        "w": 1,
        "r": 1,
        "d": 1
    }


test_char_frequency()
test_char_frequency_with_spaces()

print("All test cases passed.")
