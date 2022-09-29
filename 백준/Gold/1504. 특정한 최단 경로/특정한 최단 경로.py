import sys
import heapq
INF = int(1e9)

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
res = [INF] * (n + 1)
min_num = int(1e9)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
start = 1
one, two = map(int, sys.stdin.readline().rstrip().split())
cnt = 0

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    res[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if res[now] < dist:
            continue
        for nxt in graph[now]:
            cost = dist + nxt[0]
            if cost < res[nxt[1]]:
                res[nxt[1]] = cost
                heapq.heappush(q, (cost, nxt[1]))

# one -> two 가기
dijkstra(start)
cnt += res[one]

start = one
res = [INF] * (n + 1)
dijkstra(start)
cnt += res[two]

start = two
res = [INF] * (n + 1)
dijkstra(start)
cnt += res[n]
min_num = min(cnt, min_num)

# two -> one 가기
cnt = 0
start = 1
res = [INF] * (n + 1)
dijkstra(start)
cnt += res[two]

start = two
res = [INF] * (n + 1)
dijkstra(start)
cnt += res[one]

start = one
res = [INF] * (n + 1)
dijkstra(start)
cnt += res[n]
min_num = min(cnt, min_num)

if min_num >= INF:
    print(-1)
else:
    print(min_num)