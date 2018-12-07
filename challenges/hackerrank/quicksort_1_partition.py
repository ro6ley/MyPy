# Link to problem statement: https://www.hackerrank.com/challenges/quicksort1/problem


def quick_sort(m, ar):
    if m < 2:
        print(ar[0])
    else:
        p = ar[0]
        less = []
        more = []
        for item in ar[1:]:
            if item < p:
                less.append(item)
            else:
                more.append(item)
        final = less + [p] + more
        print(' '.join([str(x) for x in final]))
    


m = int(input())
ar = [int(i) for i in input().strip().split()]
quick_sort(m, ar)
