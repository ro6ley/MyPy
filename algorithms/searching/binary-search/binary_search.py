def binary_search(array, item):
    """
    Given a sorted array, this function performs a binary search to locate the
    item.
    Parameters: Array, item
    Returns: index of the item or -1 if the item is not found
    """
    first = 0
    last = len(array) - 1
    indx = None

    while first <= last:
        mid = (first + last) / 2

        # Check if the item is at the middle
        if array[mid] == item:
            indx = mid
            return indx

        # If item is greater than half, ignore the left half of the array
        elif array[mid] < item:
            first = mid + 1

        # If item is less than half, ignore the right half of the array
        elif array[mid] > item:
            last = mid - 1

    return -1


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

print(binary_search(test_list, 17))  # 5
print(binary_search(test_list, 22))  # -1
