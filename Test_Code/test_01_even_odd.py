import importlib.util

spec = importlib.util.spec_from_file_location(
    "even_odd", "Code/01_even_odd.py"
)

program = importlib.util.module_from_spec(spec)
spec.loader.exec_module(program)

assert program.check_even_odd(2) == "Even"
assert program.check_even_odd(5) == "Odd"
assert program.check_even_odd(0) == "Even"
assert program.check_even_odd(-3) == "Odd"

print("All test cases passed.")
