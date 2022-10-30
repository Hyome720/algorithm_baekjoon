import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())

dic = dict()
dic[n] = [0, 1]

q = deque()
q.append((n, 0, 1))

def bfs():
    while q:
        x, time, cnt = q.popleft()

        dx = [-1, 1, x]

        for i in range(3):
            if 0 <= x + dx[i] <= 200000:
                if not dic.get(x + dx[i]):
                    dic[x + dx[i]] = [time + 1, cnt]
                    q.append((x + dx[i], time + 1, cnt))
                else:
                    if dic[x + dx[i]][0] == time + 1:
                        dic[x + dx[i]][1] += 1
                        q.append((x + dx[i], time + 1, cnt))

bfs()

print(dic[k][0])
print(dic[k][1])