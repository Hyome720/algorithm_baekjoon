import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

lst = [0] * (n + 1)

q = deque()
q.append(1)

def bfs():
    while q:
        x = q.popleft()
        dx = [2 * x, x, 1]

        for i in range(3):
            if x + dx[i] < n + 1 and not lst[x + dx[i]]:
                lst[x + dx[i]] = lst[x] + 1
                q.append(x + dx[i])

bfs()
print(lst[n])