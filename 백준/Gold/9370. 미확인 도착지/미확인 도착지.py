import sys
import heapq
INF = int(1e9)

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().rstrip().split())
    s, g, h = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(n + 1)]
    res = [INF] * (n + 1)
    possible = []
    final = []

    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    for _ in range(t):
        possible.append(int(sys.stdin.readline().rstrip()))

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

    def find(k):
        global res
        min_num = INF
        start = s
        res = [INF] * (n + 1)
        cnt = 0
        dijkstra(start)
        cnt += res[g]
        original = res[k]

        start = g
        res = [INF] * (n + 1)
        dijkstra(start)
        cnt += res[h]

        start = h
        res = [INF] * (n + 1)
        dijkstra(start)
        cnt += res[k]
        if original == cnt:
            final.append(k)

        start = s
        res = [INF] * (n + 1)
        cnt = 0
        dijkstra(start)
        cnt += res[h]

        start = h
        res = [INF] * (n + 1)
        dijkstra(start)
        cnt += res[g]

        start = g
        res = [INF] * (n + 1)
        dijkstra(start)
        cnt += res[k]
        if original == cnt:
            final.append(k)

    for i in possible:
        find(i)

    final.sort()
    print(*final)