# Selection sort improves on the bubble sort since it makes on one exchange for
# every pass through the list.
# It looks for the largest value during a pass and places it in the proper
# position


def selection_sort(a_list):
    # Traverse through all array elements
    for i in range(len(a_list)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(a_list)):
            if a_list[min_idx] > a_list[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        a_list[i], a_list[min_idx] = a_list[min_idx], a_list[i]

    return a_list


example_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(selection_sort(example_list))  # [17, 20, 26, 31, 44, 54, 55, 77, 93]
