import importlib.util

spec = importlib.util.spec_from_file_location(
    "largest_of_three",
    "Code/02_largest_of_three.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.largest_of_three(10, 25, 15) == 25
assert module.largest_of_three(50, 20, 30) == 50
assert module.largest_of_three(5, 8, 12) == 12
assert module.largest_of_three(7, 7, 3) == 7

print("All test cases passed.")
