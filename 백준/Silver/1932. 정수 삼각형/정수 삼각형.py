import sys

n = int(input())
lst = []
dp = []
for i in range(1, n + 1):
    dp.append([0] * i)

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp[0] = lst[0]

for i in range(1, n):
    for j in range(i + 1):
        if not j:
            dp[i][j] = dp[i - 1][j] + lst[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + lst[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + lst[i][j]

print(max(dp[-1]))