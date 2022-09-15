import sys
sys.setrecursionlimit(10**6)

n, m, r = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


visited = [0] * (n + 1)
visited[r] = 1

lst = [0] * (n + 1)
lst[r] = 1
cnt = 1

def dfs(t):
    global cnt
    for i in graph[t]:
        if visited[i] == 0:
            cnt += 1
            visited[i] = t
            lst[i] = cnt
            dfs(i)

dfs(r)

for i in lst[1:]:
    print(i)