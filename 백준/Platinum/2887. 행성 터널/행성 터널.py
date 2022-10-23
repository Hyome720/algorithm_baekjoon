import sys
INF = int(1e9)

n = int(sys.stdin.readline().rstrip())
graph = []
edges = []
parent = [i for i in range(n + 1)]
res = 0

for i in range(n):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    graph.append((x, y, z, i))


def find(c):
    while c != parent[c]:
        c = parent[parent[c]]
    return parent[c]


def union(c, d):
    c = find(c)
    d = find(d)

    if c < d:
        parent[d] = c
    else:
        parent[c] = d


for i in range(3):
    graph.sort(key=lambda x:x[i])
    for j in range(1, n):
        edges.append((abs(graph[j - 1][i] - graph[j][i]), graph[j - 1][3], graph[j][3]))

edges.sort()

for i in range(len(edges)):
    if find(edges[i][1]) != find(edges[i][2]):
        union(edges[i][1], edges[i][2])
        res += edges[i][0]

print(res)
