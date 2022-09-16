import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())

q = deque()
q.append(n)

visited = [0] * 200001


def bfs():
    while q:
        x = q.popleft()
        if x == k:
            break

        dx = [1, -1, x]
        for i in range(3):
            if 0 <= x + dx[i] < 200001 and not visited[x + dx[i]]:
                visited[x + dx[i]] = visited[x] + 1
                q.append(x + dx[i])


bfs()
print(visited[k])