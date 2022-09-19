import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = [[0] * (n + 1)] + list([0] + list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))

lst_dp = list([0] * (n + 1) for _ in range(n + 1))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1:
            lst_dp[i][j] = lst_dp[i][j - 1] + lst[i][j]
        elif j == 1:
            lst_dp[i][j] = lst_dp[i - 1][j] + lst[i][j]
        else:
            lst_dp[i][j] = lst[i][j] + lst_dp[i - 1][j] + lst_dp[i][j - 1] - lst_dp[i - 1][j - 1]

for _ in range(m):
    x_s, y_s, x_e, y_e = map(int, sys.stdin.readline().rstrip().split())
    if x_s == x_e and y_s == y_e:
        res = lst[x_s][y_s]
        print(res)
    else:
        res = lst_dp[x_e][y_e] - lst_dp[x_e][y_s - 1] - lst_dp[x_s - 1][y_e] + lst_dp[x_s - 1][y_s - 1]
        print(res)
