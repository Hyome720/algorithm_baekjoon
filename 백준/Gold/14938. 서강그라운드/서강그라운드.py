import sys
import heapq

INF = int(1e9)

n, m, r = map(int, sys.stdin.readline().rstrip().split())
item = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
graph = [[] for _ in range(n + 1)]
max_item = 0
for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    res[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if res[now] < dist:
            continue
        for nxt in graph[now]:
            cost = nxt[1] + dist
            if cost < res[nxt[0]]:
                res[nxt[0]] = cost
                heapq.heappush(q, (cost, nxt[0]))

for i in range(1, n + 1):
    cnt = 0
    res = [INF] * (n + 1)
    dijkstra(i)
    for i in range(1, n + 1):
        if res[i] <= m:
            cnt += item[i]
    max_item = max(cnt, max_item)

print(max_item)
