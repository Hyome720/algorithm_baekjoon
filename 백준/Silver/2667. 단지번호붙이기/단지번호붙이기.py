import sys
from pprint import pprint

def danji(x, y):
    global build, cnt
    build += 1
    visited[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        if (0 <= x + dx[i] < n) and (0 <= y + dy[i] < n) and lst[x + dx[i]][y + dy[i]] and not visited[x + dx[i]][y + dy[i]]:
            danji(x + dx[i], y + dy[i])



n = int(sys.stdin.readline().rstrip())

lst = list(list(map(int, sys.stdin.readline().rstrip())) for _ in range(n))
cnt = 0

build_lst = []
visited = list([0] * n for _ in range(n))

for i in range(n):
    for j in range(n):
        if lst[i][j] and not visited[i][j]:
            build = 0
            danji(i, j)
            build_lst.append(build)
            cnt += 1

print(cnt)
build_lst.sort()
for i in build_lst:
    print(i)