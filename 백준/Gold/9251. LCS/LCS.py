import sys

word_a = list(sys.stdin.readline().rstrip())
word_b = list(sys.stdin.readline().rstrip())

n = len(word_a)
m = len(word_b)

dp = [0] * m

for i in range(n):
    cnt = 0
    for j in range(m):
        if cnt < dp[j]:
            cnt = dp[j]
        elif word_a[i] == word_b[j]:
            dp[j] = cnt + 1

print(max(dp))