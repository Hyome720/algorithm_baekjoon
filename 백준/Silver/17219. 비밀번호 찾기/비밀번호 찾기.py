import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
dic = dict()

for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    dic[a] = b

for _ in range(m):
    c = sys.stdin.readline().rstrip()
    print(dic[c])

