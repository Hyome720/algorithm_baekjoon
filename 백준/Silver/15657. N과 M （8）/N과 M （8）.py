import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst.sort()
now = 0

res = []

def sequence(idx, now, res):
    if idx == m:
        print(*res)
        return
    for i in range(now, n):
        res.append(lst[i])
        sequence(idx + 1, i, res)
        res.pop()

sequence(0, now, res)
