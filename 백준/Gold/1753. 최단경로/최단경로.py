import sys
import heapq
from collections import deque
INF = int(1e9)

n, m = map(int, sys.stdin.readline().rstrip().split())
start = int(sys.stdin.readline().rstrip())
graph = [[] for i in range(n + 1)]
res = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    res[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if res[now] < dist:
            continue
        for nxt in graph[now]:
            cost = dist + nxt[1]
            if cost < res[nxt[0]]:
                res[nxt[0]] = cost
                heapq.heappush(q, (cost, nxt[0]))

dijkstra(start)

for i in range(1, n + 1):
    if res[i] == INF:
        print('INF')
    else:
        print(res[i])
