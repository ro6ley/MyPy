"""
Quick Sort Pseudocode:
- a control value called a pivot is picked from the array
- all the values greater than the pivot are moved to the right of the pivot
- all values less than the pivot are moved to the left of the pivot
- the pivot is in its rightfull place now
- the same steps are applied recursively for the right and left parts of the pivot

The time complexity for this algorithm is O(n^2)
"""


def partition(array, start, end): 
    """
    This function takes last element as pivot, places the pivot element at its 
    correct position in the array.
    All smaller elements smaller than the pivot are placed to the left of pivot 
    and all greater elements to right 
    """
    i = (start - 1)
    pivot = array[end]

    for j in range(start, end): 

        # If current element is smaller than or equal to pivot 
        if array[j] <= pivot: 
        
            # increment index of smaller element 
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[end] = array[end], array[i + 1] 
    return (i + 1) 


def quick_sort(array, start, end): 
    """
    Main function to implement QuickSort.
    start: starting index
    end: ending index
    """
    if start < end: 

        # pivot is partitioning index, it is now at right place 
        pivot = partition(array, start, end) 

        # Recursively Quick Sort the two halves on either side of pivot 
        quick_sort(array, start, pivot-1) 
        quick_sort(array, pivot+1, end) 


array = [10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1) 
print("Sorted array is:") 
print(array)
