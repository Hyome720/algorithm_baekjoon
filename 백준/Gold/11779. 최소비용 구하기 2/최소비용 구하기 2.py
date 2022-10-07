import sys
import heapq
INF = int(1e9)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
res = [INF] * (n + 1)
way_lst = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

start, end = map(int, sys.stdin.readline().rstrip().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    res[start] = 0
    way_lst[start].append(start)
    while q:
        dist, now = heapq.heappop(q)
        if res[now] < dist:
            continue
        for nxt in graph[now]:
            cost = dist + nxt[1]
            if cost < res[nxt[0]]:
                res[nxt[0]] = cost
                heapq.heappush(q, (cost, nxt[0]))
                way_lst[nxt[0]] = []
                for i in way_lst[now]:
                    way_lst[nxt[0]].append(i)
                way_lst[nxt[0]].append(nxt[0])

dijkstra(start)

print(res[end])
print(len(way_lst[end]))
print(*way_lst[end])
