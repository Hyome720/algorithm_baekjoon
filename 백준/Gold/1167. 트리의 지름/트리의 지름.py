import sys
from collections import deque

v = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(v + 1)]
dist = 0
res = 0

for _ in range(v):
    lst = deque(map(int, sys.stdin.readline().rstrip().split()))
    tree = lst.popleft()
    while True:
        x = lst.popleft()
        if not lst:
            break
        y = lst.popleft()
        graph[tree].append((x, y))


def bfs(start):
    visited = [-1] * (v + 1)
    q = deque()
    q.append(start)
    visited[start] = 0
    max_dist = (0, 0)

    while q:
        now = q.popleft()
        for nxt, dist in graph[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + dist
                q.append(nxt)
                if max_dist[0] < visited[nxt]:
                    max_dist = visited[nxt], nxt

    return max_dist

dist, node = bfs(1)
dist, node = bfs(node)
print(dist)