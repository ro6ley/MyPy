def linear_search(array, item):
    """
    Given an array and an item, this function traverses the array to locate
    the item.
    Parameters: array, item
    Returns: index if item is found, -1 if the item is not found
    """
    for i in range(len(array)):
        if array[i] == item:
            return i
    return -1


print(linear_search([1, 2, 3, 4], 14))  # -1
print(linear_search([1, 2, 3, 4, 14], 14))  # 4

print(linear_search([1, 2, 3, 4, 14, 3, 5, 14], 14))  # 4
