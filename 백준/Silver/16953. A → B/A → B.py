import sys
from collections import deque

a, b = map(int, sys.stdin.readline().rstrip().split())
dic = dict()
dic[b] = 1

def bfs():
    q = deque()
    q.append(b)

    while q:
        x = q.popleft()

        if x == a or x < 0:
            break
        for i in range(2):
            if not i:
                if not x % 2 and not dic.get(x // 2):
                    dic[x // 2] = dic[x] + 1
                    q.append(x // 2)
            else:
                if x % 10 == 1 and not dic.get(x // 10):
                    dic[x // 10] = dic[x] + 1
                    q.append(x // 10)

bfs()

if dic.get(a):
    print(dic[a])
else:
    print(-1)