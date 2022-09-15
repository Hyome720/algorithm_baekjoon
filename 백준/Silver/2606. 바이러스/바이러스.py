import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
link = [[] for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    link[a].append(b)
    link[b].append(a)

visited = [0] * (n + 1)
visited[1] = 1

q = deque()
q.append(1)

cnt = 0

def bfs():
    global cnt
    while q:
        now = q.popleft()
        for nxt in link[now]:
            if not visited[nxt]:
                visited[nxt] = 1
                cnt += 1
                q.append(nxt)

bfs()

print(cnt)
