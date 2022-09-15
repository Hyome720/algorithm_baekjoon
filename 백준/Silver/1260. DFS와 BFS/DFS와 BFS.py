import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().rstrip().split())
lst = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    lst[a].append(b)
    lst[b].append(a)

for i in lst:
    i.sort()

visited_dfs = [0] * (n + 1)
visited_dfs[v] = 1
visited_bfs = [0] * (n + 1)
visited_bfs[v] = 1

res_dfs = [0] * (n + 1)
res_dfs[v] = 1
res_bfs = [0] * (n + 1)
res_bfs[v] = 1

cnt = 1

def dfs(v):
    global cnt
    for nxt in lst[v]:
        if not visited_dfs[nxt]:
            if not res_dfs[nxt]:
                cnt += 1
                res_dfs[nxt] = cnt
            visited_dfs[nxt] = 1
            dfs(nxt)

dfs(v)

cnt = 1

q = deque()
q.append(v)

def bfs():
    global cnt
    while q:
        now = q.popleft()
        for nxt in lst[now]:
            if not visited_bfs[nxt]:
                if not res_bfs[nxt]:
                    cnt += 1
                    res_bfs[nxt] = cnt
                visited_bfs[nxt] = now
                q.append(nxt)

bfs()

dic_dfs = dict()
dic_bfs = dict()

for idx, value in enumerate(res_dfs):
    if value:
        dic_dfs[idx] = res_dfs[idx]

for idx, value in enumerate(res_bfs):
    if value:
        dic_bfs[idx] = res_bfs[idx]

dic_dfs = sorted(dic_dfs.items(), key=lambda x:x[1])
dic_bfs = sorted(dic_bfs.items(), key=lambda x:x[1])


for i in range(len(dic_dfs)):
    print(dic_dfs[i][0], end=' ')
print()
for i in range(len(dic_bfs)):
    print(dic_bfs[i][0], end=' ')