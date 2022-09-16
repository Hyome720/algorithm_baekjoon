import sys
from collections import deque

m, n = map(int, sys.stdin.readline().rstrip().split())
lst = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))

q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
                if lst[x + dx[i]][y + dy[i]] == -1:
                    continue
                if not lst[x + dx[i]][y + dy[i]]:
                    lst[x + dx[i]][y + dy[i]] = lst[x][y] + 1
                    q.append((x + dx[i], y + dy[i]))
                elif lst[x + dx[i]][y + dy[i]] and lst[x + dx[i]][y + dy[i]] > lst[x][y] + 1:
                    lst[x + dx[i]][y + dy[i]] = lst[x][y] + 1
                    q.append((x + dx[i], y + dy[i]))
                else:
                    continue

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            q.append((i, j))
bfs()

rotten = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            rotten = 1
            break
    if rotten:
        break

max_value = max(map(max, lst))

if rotten:
    print(-1)
else:
    print(max_value - 1)
