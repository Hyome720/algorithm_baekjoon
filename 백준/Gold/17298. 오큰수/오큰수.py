import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

stack = []
res = [-1] * n

lst.reverse()
idx = 0
stack.append((idx, lst.pop()))

while lst:
    k = lst.pop()
    idx += 1

    while stack and stack[-1][-1] < k:
        a, b = stack.pop()
        res[a] = k

    stack.append((idx, k))

print(*res)