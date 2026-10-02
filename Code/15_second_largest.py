def second_largest(arr):
    unique_values = list(set(arr))

    if len(unique_values) < 2:
        return None

    unique_values.sort(reverse=True)

    return unique_values[1]


if __name__ == "__main__":
    arr = [12, 36, 16, 5, 8]
    print("Second largest:", second_largest(arr))
