import sys
from collections import deque


n = int(input())
q = deque(list(range(1, n + 1)))
i = 0

if n == 1:
    print(1)
else:
    while i < n - 2:
        q.popleft()
        q.append(q.popleft())
        i += 1
    print(q.pop())
