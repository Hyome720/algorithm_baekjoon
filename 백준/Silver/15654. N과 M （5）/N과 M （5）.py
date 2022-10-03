import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst.sort()

res = []

def sequence(idx, res):
    if idx == m:
        print(*res)
        return
    for i in range(n):
        if lst[i] not in res:
            res.append(lst[i])
            sequence(idx + 1, res)
            res.pop()

sequence(0, res)
