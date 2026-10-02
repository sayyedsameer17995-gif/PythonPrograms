import importlib.util

spec = importlib.util.spec_from_file_location(
    "fibonacci_series",
    "Code/05_fibonacci_series.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.fibonacci(0) == []
assert module.fibonacci(1) == [0]
assert module.fibonacci(5) == [0, 1, 1, 2, 3]
assert module.fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]

print("All test cases passed.")
