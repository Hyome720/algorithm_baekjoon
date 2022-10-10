import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = list(list(sys.stdin.readline().rstrip()) for _ in range(n))
lst[0][0] = 1

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q.append((0, 0, 0))
    while q:
        x, y, wall = q.popleft()
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
                if not wall and lst[x + dx[i]][y + dy[i]] == '1':
                    visited[x + dx[i]][y + dy[i]][1] = visited[x][y][0] + 1
                    q.append((x + dx[i], y + dy[i], 1))
                elif lst[x + dx[i]][y + dy[i]] == '0' and not visited[x + dx[i]][y + dy[i]][wall]:
                    visited[x + dx[i]][y + dy[i]][wall] = visited[x][y][wall] + 1
                    q.append((x + dx[i], y + dy[i], wall))

bfs()

if min(visited[n - 1][m - 1]):
    print(min(visited[n - 1][m - 1]))
elif max(visited[n - 1][m - 1]):
    print(max(visited[n - 1][m - 1]))
else:
    print(-1)

