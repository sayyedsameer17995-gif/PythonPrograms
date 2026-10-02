def fibonacci(n):
    series = []
    a = 0
    b = 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series


if __name__ == "__main__":
    print(fibonacci(10))
