import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

lst = [[] for _ in range(n + 1)]
res = dict()

q = deque()

def bfs():
    global cnt
    while q:
        now = q.popleft()
        for nxt in lst[now]:
            if not visited[nxt]:
                visited[nxt] = visited[now] + 1
                q.append(nxt)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    lst[a].append(b)
    lst[b].append(a)

for i in range(1, n + 1):
    cnt = 0
    visited = [0] * (n + 1)
    visited[i] = 1
    q.append(i)
    bfs()
    res[i] = sum(visited) - n

res = sorted(res.items(), key=lambda x:(x[1], x[0]))
print(res[0][0])

