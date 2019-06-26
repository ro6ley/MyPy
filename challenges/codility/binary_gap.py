# A binary gap within a positive integer N is any maximal sequence of 
# consecutive zeros that is surrounded by ones at both ends in the binary 
# representation of N.

# Given a positive integer N, returns the length of its longest binary gap. 
# The function should return 0 if N doesn't contain a binary gap.

# Assumption(s):
# - N is an integer within the range [1..2,147,483,647].


def solution(N):
    return len(max(format(N, 'b').strip('0').split('1')))
