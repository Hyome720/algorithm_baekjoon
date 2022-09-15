import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    lst = list([0] * n for _ in range(n))
    x_start, y_start = map(int, sys.stdin.readline().rstrip().split())
    x_end, y_end = map(int, sys.stdin.readline().rstrip().split())
    lst[x_start][y_start] = 1

    q = deque()
    q.append((x_start, y_start))

    def bfs():
        while q:
            x, y = q.popleft()

            if x == x_end and y == y_end:
                break

            dx = [-1, -2, -2, -1, 1, 2, 2, 1]
            dy = [-2, -1, 1, 2, -2, -1, 1, 2]

            for i in range(8):
                if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n and not lst[x + dx[i]][y + dy[i]]:
                    q.append((x + dx[i], y + dy[i]))
                    lst[x + dx[i]][y + dy[i]] = lst[x][y] + 1

    bfs()

    print(lst[x_end][y_end] - 1)