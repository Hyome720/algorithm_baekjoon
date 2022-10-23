import sys

tc = int(sys.stdin.readline().rstrip())

for _ in range(tc):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
    print(n - 1)