import sys

tc = int(sys.stdin.readline().rstrip())

for _ in range(tc):
    n = int(sys.stdin.readline().rstrip())
    lst = []

    for _ in range(2):
        lst.append(list(map(int, sys.stdin.readline().rstrip().split())))

    dp = [[0] * n for _ in range(2)]
    if n > 1:
        dp[0][0] = lst[0][0]
        dp[1][0] = lst[1][0]
        dp[0][1] = dp[1][0] + lst[0][1]
        dp[1][1] = dp[0][0] + lst[1][1]

        for i in range(2, n):
            dp[0][i] = max(dp[1][i - 1] + lst[0][i], dp[1][i - 2] + lst[0][i])
            dp[1][i] = max(dp[0][i - 1] + lst[1][i], dp[0][i - 2] + lst[1][i])

        print(max(dp[0][n - 1], dp[1][n - 1]))
    else:
        print(max(lst[0][0], lst[1][0]))
