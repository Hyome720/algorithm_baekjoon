import sys
from collections import deque, defaultdict

n, k = map(int, sys.stdin.readline().rstrip().split())

q = deque()
q.append(n)

visited = [0] * 200001
check = dict()
check[n] = 1

def bfs():
    while q:
        x = q.popleft()
        if x == k:
            break

        dx = [x, 1, -1]
        for i in range(3):
            if 0 <= x + dx[i] < 200001 and x + dx[i] != n:
                if not check.get(x + dx[i]):
                    if i:
                        visited[x + dx[i]] = visited[x] + 1
                        q.append(x + dx[i])
                        check[x + dx[i]] = 1
                    else:
                        visited[x + dx[i]] = visited[x]
                        q.append(x + dx[i])
                        check[x + dx[i]] = 1
                else:
                    if not i and visited[x + dx[i]] > visited[x]:
                        visited[x + dx[i]] = visited[x]
                        q.append(x + dx[i])
                    elif i and visited[x + dx[i]] > visited[x] + 1:
                        visited[x + dx[i]] = visited[x] + 1
                        q.append(x + dx[i])

bfs()

print(visited[k])