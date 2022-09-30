import sys
sys.setrecursionlimit(int(1e9))

n, m = map(int, sys.stdin.readline().rstrip().split())
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

def find(c):
    if c == parent[c]:
        return c
    p = find(parent[c])
    parent[c] = p
    return parent[c]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    o, a, b = map(int, sys.stdin.readline().rstrip().split())
    if o:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)
