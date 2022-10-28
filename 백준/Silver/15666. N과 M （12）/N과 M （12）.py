import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = set(map(int, sys.stdin.readline().rstrip().split()))
lst = list(lst)
lst.sort()
n = len(lst)

res = []
last = 0

def sequence():
    global last
    if len(res) == m:
        print(*res)
        return


    for i in range(n):
        if last <= lst[i]:
            res.append(lst[i])
            last = lst[i]
            sequence()
            last = 0
            res.pop()

sequence()
