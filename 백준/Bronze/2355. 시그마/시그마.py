import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

if b > a:
    res = int(((b - a) + 1) * (a + b) / 2)
else:
    res = int(((a - b) + 1) * (a + b) / 2)
print(res)