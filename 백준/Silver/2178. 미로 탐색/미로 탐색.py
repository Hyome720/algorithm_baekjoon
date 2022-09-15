import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

lst = list(list(map(int, sys.stdin.readline().rstrip())) for _ in range(n))

cnt = 0

q = deque()
q.append((0, 0))

def bfs():
    while q:
        x, y = q.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m and lst[x + dx[i]][y + dy[i]] == 1:
                lst[x + dx[i]][y + dy[i]] = lst[x][y] + 1
                q.append((x + dx[i], y + dy[i]))
    return lst[n - 1][m - 1]

print(bfs())