import sys

a, b = map(int, input().split())

set_a = set(list(map(int, sys.stdin.readline().rstrip().split())))
set_b = set(list(map(int, sys.stdin.readline().rstrip().split())))

res = len((set_a - set_b) | (set_b - set_a))
print(res)