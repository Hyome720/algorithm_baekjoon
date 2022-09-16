import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = [0] * 101
dic = dict()

for _ in range(n + m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    dic[x] = y

q = deque()
q.append(1)


def bfs():
    while q:
        x = q.popleft()
        for i in range(1, 7):
            if 1 <= x + i <= 100:
                if dic.get(x + i) and not lst[x + i]:
                    lst[x + i] = lst[x] + 1
                    q.append(dic[x + i])
                    if not lst[dic[x + i]]:
                        lst[dic[x + i]] = lst[x] + 1
                elif not lst[x + i]:
                    lst[x + i] = lst[x] + 1
                    q.append(x + i)


bfs()

print(lst[100])



