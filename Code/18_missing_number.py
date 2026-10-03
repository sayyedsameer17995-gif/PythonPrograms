def find_missing_number(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)


arr = [1, 2, 3, 5, 6]
print("Missing number:", find_missing_number(arr))
