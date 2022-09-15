import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort(reverse=True)

q = deque()
q.append(r)

lst = [0] * (n + 1)
lst[r] = 1
res = [0] * (n + 1)
res[r] = 1
cnt = 1

def bfs():
    global cnt
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not lst[i]:
                if not res[i]:
                    cnt += 1
                    res[i] = cnt
                lst[i] = now
                q.append(i)

bfs()

for i in res[1:]:
    print(i)
