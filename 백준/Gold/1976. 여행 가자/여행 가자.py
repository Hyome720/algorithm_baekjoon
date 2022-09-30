import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
parent = [i for i in range(n + 1)]
rank = [1] * (n + 1)

def find(x):
    while x != parent[x]:
        x = parent[parent[x]]
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if rank[x] == rank[y]:
        parent[y] = x
        rank[x] += 1
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x

for i in range(1, n + 1):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if lst[j]:
            union(i, j + 1)

visit = list(map(int, sys.stdin.readline().rstrip().split()))

temp = find(visit[0])

for i in visit:
    if find(i) != temp:
        print('NO')
        break
else:
    print('YES')

