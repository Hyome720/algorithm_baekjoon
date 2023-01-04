import sys
sys.setrecursionlimit(10**9)

n, m = map(int, sys.stdin.readline().rstrip().split())

lst = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))
visited = list([0] * m for _ in range(n))

drawing_cnt = 0
res = 0
total = 0


def check_drawing(x, y):
    global drawing_cnt

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m and not visited[x + dx[i]][y + dy[i]] and lst[x + dx[i]][y + dy[i]]:
            visited[x + dx[i]][y + dy[i]] = 1
            check_drawing(x + dx[i], y + dy[i])
            drawing_cnt += 1


for i in range(n):
    for j in range(m):
        if lst[i][j] and not visited[i][j]:
            drawing_cnt = 0
            check_drawing(i, j)
            res = max(res, drawing_cnt)
            total += 1

if total:
    print(total)
    if res:
        print(res)
    else:
        print(1)
else:
    print(0)
    print(0)
