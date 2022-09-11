n, k = map(int, input().split())

what = 1

for i in range(k + 1, n + 1):
    what *= i
for i in range(1, n - k + 1):
    what //= i

print(what)