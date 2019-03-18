"""
- Insertion sort maintains a sorted sublist in the lower positions of the list.
- Each new item is then inserted into the previous list in its sorted position.
- It has a time complexity of O(n^2)
"""


def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position-1]
            position = position - 1

        a_list[position] = current_value

    return a_list


example_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(insertion_sort(example_list))  # [17, 20, 26, 31, 44, 54, 55, 77, 93]
