import sys

n = int(sys.stdin.readline().rstrip())

graph = [0 for _ in range(n + 1)]
visited = [0] * (n + 1)
res = []
up = []
down = []

def dfs(t):
    if not visited[t]:
        visited[t] = 1
        up.append(t)
        up.sort()
        down.append(graph[t])
        down.sort()
        dfs(graph[t])
    else:
        if up == down:
            for j in up:
                res.append(j)


for i in range(1, n + 1):
    k = int(sys.stdin.readline().rstrip())
    graph[i] = k
    if i == k:
        res.append(k)


for i in range(1, n + 1):
    if i not in res:
        visited = [0] * (n + 1)
        up = []
        down = []
        dfs(i)

res.sort()
print(len(res))

for i in res:
    print(i)
