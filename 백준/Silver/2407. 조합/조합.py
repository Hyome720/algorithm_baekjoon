import sys

factorial = [0, 1]

for i in range(2, 101):
    factorial.append(factorial[-1] * i)

n, m = map(int, sys.stdin.readline().rstrip().split())
res = factorial[n] // factorial[m] // factorial[n - m]

print(res)

