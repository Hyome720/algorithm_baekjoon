import sys
import heapq
INF = int(1e9)

n = int(input())
graph = [[] for _ in range(n + 1)]
res = [INF] * (n + 1)

for _ in range(n - 1):
    a, b, dist = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

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

dijkstra(1)
far = 0
new_start = 1

for idx, value in enumerate(res):
    if value == INF:
        pass
    else:
        if value > far:
           far = value
           new_start = idx

res = [INF] * (n + 1)
dijkstra(new_start)

print(max(res[1:]))
