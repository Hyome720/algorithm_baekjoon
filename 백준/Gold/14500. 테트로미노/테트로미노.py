import sys
from collections import deque

def tetro(x, y, cnt, tetro_sum):
    global max_sum
    tetro_sum += lst[x][y]
    visited.append([x, y])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if cnt == 3:
        max_sum = max(tetro_sum, max_sum)
        return

    for i in range(4):
        if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m and [x + dx[i], y + dy[i]] not in visited:
            tetro(x + dx[i], y + dy[i], cnt + 1, tetro_sum)
            visited.pop()

def ah(x, y, tetro_sum):
    global max_sum
    dxy = [deque([(0, 1), (0, 2), (1, 1)]), deque([(0, 1), (0, 2), (-1, 1)]), deque([(1, 0), (2, 0), (1, 1)]), deque([(1, 0), (2, 0), (1, -1)])]

    for i in range(4):
        try:
            tetro_sum = lst[x][y]
            for _ in range(3):
                nx, ny = dxy[i].popleft()
                tetro_sum += lst[x + nx][y + ny]
            else:
                max_sum = max(tetro_sum, max_sum)
        except:
            continue


n, m = map(int, sys.stdin.readline().rstrip().split())
lst = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))
sum_lst = []
tetro_sum = 0
max_sum = 0

for i in range(n):
    for j in range(m):
        visited = []
        tetro_sum = 0
        tetro(i, j, 0, tetro_sum)
        tetro_sum = 0
        ah(i, j, tetro_sum)

print(max_sum)