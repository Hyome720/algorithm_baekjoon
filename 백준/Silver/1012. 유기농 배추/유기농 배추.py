import sys
sys.setrecursionlimit(10 ** 9)

def dfs(x, y):
    visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        if 0 <= x + dx[i] < m and 0 <= y + dy[i] < n and lst[x + dx[i]][y + dy[i]] and not visited[x + dx[i]][y + dy[i]]:
            dfs(x + dx[i], y + dy[i])


t = int(input())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    lst = list([0] * n for _ in range(m))
    cnt = 0
    visited = list([0] * n for _ in range(m))

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        lst[a][b] = 1

    for i in range(m):
        for j in range(n):
            if lst[i][j] and not visited[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)


