"""
Merge Sort is a divide an conquer algorithm that works by:
- dividing an unsorted array iteratively until an atomic value is reached
- the values are now combined in the way they were split but now in a sorted manner

The time complexity is O(n Log n)
"""


def merge_sort(array):
    if len(array) > 1:
        # find the midpoint of the array
        mid = len(array) // 2  
        # divide the array into two halves
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        
        # Copy data to temp arrays left[] and right[] 
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                array[k] = left[i] 
                i += 1
            else: 
                array[k] = right[j] 
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left): 
            array[k] = left[i] 
            i += 1
            k += 1

        while j < len(right): 
            array[k] = right[j]
            j += 1
            k += 1


array = [12, 11, 13, 5, 6, 7]

merge_sort(array)

print("Sorted array: ")
print(array)  # [5, 6, 7, 11, 12, 13]
