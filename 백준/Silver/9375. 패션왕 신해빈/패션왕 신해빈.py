import sys
from collections import defaultdict

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    dic = defaultdict(list)
    for _ in range(n):
        cloth, kind = sys.stdin.readline().split()
        dic[kind].append(cloth)

    total = 1

    for item in dic:
        total *= len(dic[item]) + 1

    print(total - 1)
