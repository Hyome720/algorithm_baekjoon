import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0, lst[1]]
dp_last = dp[-1]

for i in range(2, n + 1):
    dp_last += lst[i]
    dp.append(dp_last)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    res = dp[b] - dp[a - 1]
    print(res)