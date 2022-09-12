import sys

n = int(input())
lst_a = set(map(int, input().split()))
m = int(input())
lst_b = list(map(int, input().split()))

res = [0] * m

for i in range(m):
    if lst_b[i] in lst_a:
        res[i] = 1

print(*res)



