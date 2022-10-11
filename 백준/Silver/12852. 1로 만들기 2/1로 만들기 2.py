import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

q = deque()
q.append(1)

lst = [[] for _ in range(n + 1)]
lst[1] = [1]

def bfs():
    while q:
        x = q.popleft()
        if x == n:
            return

        dx = [x * 2, x, 1]
        for i in range(3):
            if 0 <= x + dx[i] < n + 1 and not lst[x + dx[i]]:
                lst[x + dx[i]] = lst[x] + [x + dx[i]]
                q.append(x + dx[i])

bfs()

print(len(lst[n]) - 1)
while lst[n]:
    print(lst[n].pop(), end=' ')