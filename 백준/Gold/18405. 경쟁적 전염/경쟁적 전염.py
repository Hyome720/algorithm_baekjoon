from collections import deque

n, k = map(int, input().split())

lst = []
virus = [n**2]*(k+1)
visited = [[0]*n for _ in range(n)]

for i in range(n):
    lst.append(list(map(int, input().split())))

s, target_x, target_y = map(int, input().split())
target_x = target_x - 1
target_y = target_y - 1

q = deque()

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q.append((target_x, target_y))
if lst[target_x][target_y] != 0:
    print(lst[target_x][target_y])
else:
    while q:
        x, y = q.popleft()
        if visited[x][y] >= s:
            continue
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                if lst[nx][ny] != 0:
                    virus[lst[nx][ny]] = min(virus[lst[nx][ny]], visited[nx][ny])

    if min(virus) == n**2:
        print(0)
    else:
        print(virus.index(min(virus)))