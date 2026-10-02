import importlib.util

spec = importlib.util.spec_from_file_location(
    "palindrome_number",
    "Code/09_palindrome_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome(121) == True
assert module.is_palindrome(1221) == True
assert module.is_palindrome(123) == False
assert module.is_palindrome(10) == False
assert module.is_palindrome(0) == True

print("All test cases passed.")
