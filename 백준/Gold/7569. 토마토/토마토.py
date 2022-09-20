import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().rstrip().split())
lst = list(list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)) for _ in range(h))
is_false = 0

q = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def dfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m and 0 <= z + dz[i] < h and not lst[z + dz[i]][x + dx[i]][y + dy[i]]:
                lst[z + dz[i]][x + dx[i]][y + dy[i]] = lst[z][x][y] + 1
                q.append((x + dx[i], y + dy[i], z + dz[i]))

for k in range(h):
    for i in range(n):
        for j in range(m):
            if lst[k][i][j] == 1:
                q.append((i, j, k))

dfs()


for k in range(h):
    for i in range(n):
        for j in range(m):
            if not lst[k][i][j]:
                is_false = 1
                break
        if is_false:
            break
    if is_false:
        break

if is_false:
    print(-1)
else:
    print(max([max(map(max, x)) for x in lst]) - 1)



