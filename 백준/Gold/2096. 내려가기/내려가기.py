import sys

n = int(sys.stdin.readline().rstrip())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    for i in range(3):
        max_tmp[0] = max(max_dp[0], max_dp[1]) + a
        max_tmp[1] = max(max_dp[0], max_dp[1], max_dp[2]) + b
        max_tmp[2] = max(max_dp[1], max_dp[2]) + c

        min_tmp[0] = min(min_dp[0], min_dp[1]) + a
        min_tmp[1] = min(min_dp[0], min_dp[1], min_dp[2]) + b
        min_tmp[2] = min(min_dp[1], min_dp[2]) + c

    for i in range(3):
        max_dp[i] = max_tmp[i]
        min_dp[i] = min_tmp[i]

print(max(max_dp), min(min_dp))