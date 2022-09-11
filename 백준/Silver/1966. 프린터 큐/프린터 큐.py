import sys
from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    q = deque()
    cnt = 0
    for idx, value in enumerate(lst):
        q.append([idx, value])
    lst.sort(reverse=True)
    lst_q = deque(lst)

    while True:
        if q[0][1] == lst_q[0]:
            if q[0][0] == m:
                cnt += 1
                print(cnt)
                break
            else:
                q.popleft()
                lst_q.popleft()
                cnt += 1
        else:
            q.append(q.popleft())
