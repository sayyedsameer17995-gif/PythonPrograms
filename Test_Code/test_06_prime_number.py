import importlib.util

spec = importlib.util.spec_from_file_location(
    "prime_number",
    "Code/06_prime_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_prime(2) == True
assert module.is_prime(7) == True
assert module.is_prime(11) == True
assert module.is_prime(4) == False
assert module.is_prime(1) == False
assert module.is_prime(0) == False

print("All test cases passed.")
