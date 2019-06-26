

def solution(A):
    for i in range(1, len(A)+2):
        if i not in A:
            return i


print(solution([2, 3, 1, 5]))
