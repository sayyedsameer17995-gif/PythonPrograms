import importlib.util

spec = importlib.util.spec_from_file_location(
    "palindrome_string",
    "Code/13_palindrome_string.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome("madam") == True
assert module.is_palindrome("level") == True
assert module.is_palindrome("hello") == False
assert module.is_palindrome("Python") == False
assert module.is_palindrome("") == True

print("All test cases passed.")
