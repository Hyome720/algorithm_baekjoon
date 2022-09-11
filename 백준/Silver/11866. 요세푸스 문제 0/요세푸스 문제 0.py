import sys
from collections import deque

n, k = map(int, input().split())
lst = deque(range(1, n + 1))
res = []

while lst:
    for _ in range(k - 1):
        lst.append(lst.popleft())
    res.append(lst.popleft())

print("<", end="")
for i in range(len(res) - 1):
    print(f'{res[i]}, ', end="")
print(f'{res[-1]}>')


