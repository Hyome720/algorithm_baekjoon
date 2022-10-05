import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
n_ori = n
now = n
res = []
min_cnt = 4

def lagrangian(n, res):
    global min_cnt

    if res:
        if res[-1] < int(n ** 0.5):
            return
        
    if len(res) > 4:
        return

    if n and len(res) >= min_cnt:
        return

    if min_cnt == 1 or min_cnt == 2:
        return

    if not n:
        min_cnt = min(len(res), min_cnt)
        return

    now = int(n ** 0.5)
    for i in range(now):
        res.append(now - i)
        lagrangian(n - (now - i) ** 2, res)
        res.pop()


lagrangian(n, res)

print(min_cnt)