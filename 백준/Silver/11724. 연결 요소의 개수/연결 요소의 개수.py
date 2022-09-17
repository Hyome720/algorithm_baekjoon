import sys
sys.setrecursionlimit(10 ** 9)

n, m = map(int, sys.stdin.readline().rstrip().split())

lst = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    lst[a].append(b)
    lst[b].append(a)

visited = [0] * (n + 1)

cnt = 0

def dfs(x):
    global cnt
    if visited[x]:
        cnt -= 1
        return
    visited[x] = 1

    for nxt in lst[x]:
        if not visited[nxt]:
            dfs(nxt)


for i in range(1, n + 1):
    cnt += 1
    dfs(i)

print(cnt)
