import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    q = deque()
    q.append(a)

    dic = dict()
    dic[a] = '0'

    while q:
        x = q.popleft()
        if x == b:
            break
        dx = [(2 * x) % 10000, (10000 + x - 1) % 10000, (x - x // 1000 % 10 * 1000) * 10 + x // 1000, (x - x // 10 * 10) * 1000 + x // 10]
        dy = ['D', 'S', 'L', 'R']
        for i in range(4):
            if not dic.get(dx[i]):
                q.append(dx[i])
                dic[dx[i]] = dic[x] + dy[i]

    print(dic[b][1:])
