import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
cnt = 0
dic = dict()
for i in range(1, n + 1):
    dic[i] = 0
truth = list(map(int, sys.stdin.readline().rstrip().split()))
for i in truth[1:]:
    dic[i] = 1

parent = [i for i in range(n + 1)]
rank = [1] * (n + 1)

def find(x):
    while x != parent[x]:
        x = parent[x]
    return parent[x]

def union(x, y):
    if x != y:
        x = find(x)
        y = find(y)

        if rank[x] == rank[y]:
            if x <= y:
                parent[y] = parent[x]
                rank[x] += 1
            else:
                parent[x] = y
                rank[y] += 1
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y

if len(truth) > 1:
    party_lst = []
    for _ in range(m):
        party_lst.append(list(map(int, sys.stdin.readline().rstrip().split())))
        if party_lst[-1][0] > 1:
            for i in party_lst[-1][2:]:
                union(party_lst[-1][1], i)

    for i in range(1, n + 1):
        parent[i] = find(i)

    for i in truth[1:]:
        for j in range(1, n + 1):
            if parent[j] == parent[i]:
                dic[j] = 1

    for party in party_lst:
        check = dic[party[1]]
        if not check:
            cnt += 1
    print(cnt)
else:
    print(m)

