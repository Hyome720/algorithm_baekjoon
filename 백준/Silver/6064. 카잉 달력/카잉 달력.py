import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().rstrip().split())
    res = -1

    while x <= m * n:
        if not (x - y) % n:
            res = x
            break
        x += m
        
    print(res)