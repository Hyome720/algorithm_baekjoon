import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[1] * n for _ in range(2)]
res = 0

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[0][i] = max(dp[0][i], dp[0][j] + 1)

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i - 1, -1):
        if lst[i] > lst[j]:
            dp[1][i] = max(dp[1][i], dp[1][j] + 1)

for i in range(n):
    res = max(res, dp[0][i] + dp[1][i])

print(res - 1)