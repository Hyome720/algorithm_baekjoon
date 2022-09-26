import sys

def dfs(start, now):
    if dic.get(now):
        for nxt in dic[now]:
            if not visited[start][nxt]:
                visited[start][nxt] = 1
                dfs(start, nxt)

n = int(sys.stdin.readline().rstrip())
lst = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))
dic = dict()
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if dic.get(i) and lst[i][j]:
            dic[i].append(j)
        elif not dic.get(i) and lst[i][j]:
            dic[i] = [j]

for i in range(n):
    dfs(i, i)

for i in visited:
    print(*i)
