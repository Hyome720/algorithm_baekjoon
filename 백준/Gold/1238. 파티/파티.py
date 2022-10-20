import sys
import heapq
INF = int(1e9)

n, m, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
res = [INF] * (n + 1)

for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, t))


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

def dijkstra_return(start, x):
    q = []
    heapq.heappush(q, (0, start))
    res_new[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if now == x:
            break
        if res_new[now] < dist:
            continue
        for nxt in graph[now]:
            cost = dist + nxt[1]
            if cost < res_new[nxt[0]]:
                res_new[nxt[0]] = cost
                heapq.heappush(q, (cost, nxt[0]))
    return res_new[x]

dijkstra(x)
res[0] = 0
final = 0

for i in range(1, n + 1):
    res_new = [INF] * (n + 1)
    final = max(final, res[i] + dijkstra_return(i, x))

print(final)