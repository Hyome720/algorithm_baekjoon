import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = set([sys.stdin.readline().rstrip() for _ in range(n)])
cnt = 0

for _ in range(m):
    if sys.stdin.readline().rstrip() in lst:
        cnt += 1

print(cnt)