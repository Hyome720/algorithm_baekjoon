import sys
import heapq

v, e = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(v + 1)]
visited = [0] * (v + 1)


for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((c, b))
    graph[b].append((c, a))


def dijkstra(start):
    res = 0
    q = graph[start]
    heapq.heapify(q)
    visited[start] = 1

    while q:
        dist, now = heapq.heappop(q)
        if not visited[now]:
            visited[now] = 1
            res += dist
            for nxt in graph[now]:
                if not visited[nxt[1]]:
                    heapq.heappush(q, nxt)
    return res

print(dijkstra(1))
