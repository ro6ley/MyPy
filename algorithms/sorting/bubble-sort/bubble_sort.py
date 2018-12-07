# Bubble sort makes multiple passess through a list comparing adjacent values
# and exchanegs those that are out of order.
# In each round, the next largest number is placed in it's correct position


def bubble_sort(a_list):
    for passnum in range(len(a_list)-1, 0, -1):
        for i in range(passnum):
            if a_list[i] > a_list[i+1]:
                temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp

    return a_list


example_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(bubble_sort(example_list))  # [17, 20, 26, 31, 44, 54, 55, 77, 93]
