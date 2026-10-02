def remove_duplicates(arr):
    result = []

    for item in arr:
        if item not in result:
            result.append(item)

    return result


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 5]
    print("List after removing duplicates:", remove_duplicates(arr))
