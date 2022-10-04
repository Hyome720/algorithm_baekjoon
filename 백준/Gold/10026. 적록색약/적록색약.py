import sys
sys.setrecursionlimit(int(1e9))

n = int(sys.stdin.readline().rstrip())
lst = list(list(sys.stdin.readline().rstrip()) for _ in range(n))
visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
red = 'R'
blue = 'B'
green = 'G'
cnt_normal = 0
cnt_blind = 0


def normal(x, y, check):
    visited[x][y] = 1

    for i in range(4):
        if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n and not visited[x + dx[i]][y + dy[i]] and lst[x + dx[i]][y + dy[i]] == check:
            normal(x + dx[i], y + dy[i], check)


def blind(x, y, check_lst):
    visited[x][y] = 1

    for i in range(4):
        if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n and not visited[x + dx[i]][y + dy[i]] and lst[x + dx[i]][y + dy[i]] in check_lst:
            blind(x + dx[i], y + dy[i], check_lst)


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if lst[i][j] == red:
                check = red
                normal(i, j, check)
                cnt_normal += 1
            elif lst[i][j] == blue:
                check = blue
                normal(i, j, check)
                cnt_normal += 1
            elif lst[i][j] == green:
                check = green
                normal(i, j, check)
                cnt_normal += 1

visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if lst[i][j] == red or lst[i][j] == green:
                check_lst = [red, green]
                blind(i, j, check_lst)
                cnt_blind += 1
            elif lst[i][j] == blue:
                check_lst = [blue]
                blind(i, j, check_lst)
                cnt_blind += 1

print(cnt_normal, cnt_blind)