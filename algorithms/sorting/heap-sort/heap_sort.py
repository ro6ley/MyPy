"""
Heap Sort works by visualizing the elements to be sorted as a heap.
A heap is a complete binary tree where nodes either have 2 or no kids and each
    level must be full.
A Heapify method is used to convert an array into a Max or Min heap.
Once Heapified, we can identify the largest or the smallest value since it is
    at the root of the heap.
This element is put at the end of the array and we can now use the same steps 
    to find the next element.

Time complexity of Heap Sort is O(n Log n)

NB: For an element `a` in the array at the index a:
- it's left child is at the index 2 * a + 1
- it's right child is at the index 2 * a + 2
- it's parent is at (a -1)//2 

"""


def heapsort(alist):
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)


def parent(i):
    return (i - 1)//2


def build_max_heap(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1


def max_heapify(alist, index, size):
    l = 2 * index + 1
    r = 2 * index + 2
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)


a_list = [12, 11, 13, 5, 6, 7]
heapsort(a_list)
print('Sorted list: ')
print(a_list)
