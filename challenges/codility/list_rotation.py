# An array A consisting of N integers is given. Rotation of the array means 
# that each element is shifted right by one index, and the last element of the
# array is moved to the first place. 

# Given an array A consisting of N integers and an integer K, 
# returns the array A rotated K times.

# Assumptions:
# - N and K are integers within the range [0..100]
# - each element of array A is an integer within the range [−1,000..1,000].


def solution(A, K):
    K %= len(A)
    if len(A) == 0:
        return 1
    return A[-K:] + A[:-K]
