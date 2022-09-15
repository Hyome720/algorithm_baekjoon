import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

lst_a = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))
lst_b = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))

res = list([0] * m for _ in range(n))

for i in range(n):
    for j in range(m):
        res[i][j] = lst_a[i][j] + lst_b[i][j]

for i in res:
    print(*i)
