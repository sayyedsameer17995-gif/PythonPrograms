def common_elements(list1, list2):
    result = []

    for item in list1:
        if item in list2 and item not in result:
            result.append(item)

    return result


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]

    print("Common elements:", common_elements(list1, list2))
