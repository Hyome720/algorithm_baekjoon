import sys
import math

n = int(sys.stdin.readline().rstrip())
graph = []
edges = []
parent = [i for i in range(n + 1)]
res = 0

for i in range(n):
    x, y = map(float, sys.stdin.readline().rstrip().split())
    graph.append((x, y))


def find(a):
    while a != parent[a]:
        a = parent[parent[a]]
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n - 1):
    for j in range(i + 1, n):
        edges.append((math.sqrt((graph[i][0] - graph[j][0]) ** 2 + (graph[i][1] - graph[j][1]) ** 2), i, j))

edges.sort()

for edge in edges:
    cost, x, y = edge

    if find(x) != find(y):
        union(x, y)
        res += cost

print(round(res, 2))