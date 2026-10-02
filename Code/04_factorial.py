def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"

    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


if __name__ == "__main__":
    print(factorial(5))
