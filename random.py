def solution(A, K):
    # print(len(A), K)
    K %= len(A)

    # print(K)
    return A[-K:] + A[:-K]

    # i = 0
    # new_list = []
    # while (i < K):
    #     try:
    #         new_list.Append(A.pop())
    #     except IndexError:
    #         pAss
    # return new_list


print(solution([3, 8, 9, 7, 6], 3))

print(solution([1, 2, 3, 4], 4))

X = [3, 8, 9, 7, 6]
print(X[4:])

print([4, 'abc'])

thislist = ["apple", "banana", "cherry"]
# print(thislist.index("app") or -1)


def search(A, item):
    return A.index(item) if item in A else -1

print(search(thislist, "app"))
