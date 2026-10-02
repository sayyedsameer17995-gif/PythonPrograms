def is_palindrome(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return text == reversed_text


if __name__ == "__main__":
    print(is_palindrome("madam"))
