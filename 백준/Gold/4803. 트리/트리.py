import sys
from collections import deque

def find(x):
    while x != parent[x]:
        x = parent[x]
    return parent[x]

def union(x, y):
    global final
    if x > y:
        x, y = y, x
    x = find(x)
    y = find(y)
    if x == y:
        cycle.add(x)

    if rank[x] == rank[y]:
        parent[y] = x
        rank[x] += 1
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y


case = 0
while True:
    case += 1
    n, m = map(int, sys.stdin.readline().rstrip().split())
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)
    cycle = set()
    final = 0

    if not n:
        break

    lst = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        lst[a].append(b)
        lst[b].append(a)
        union(a, b)

    for i in range(n + 1):
        parent[i] = find(i)
    cycle_p = set()
    for i in cycle:
        cycle_p.add(find(i))

    res = len(set(parent)) - 1 - len(cycle_p)

    if res > 1:
        print(f'Case {case}: A forest of {res} trees.')
    elif res == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: No trees.')

