import sys

n = int(sys.stdin.readline().rstrip())
lst = []
for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1, n):
    lst[i][0] = min(lst[i - 1][1], lst[i - 1][2]) + lst[i][0]
    lst[i][1] = min(lst[i - 1][0], lst[i - 1][2]) + lst[i][1]
    lst[i][2] = min(lst[i - 1][0], lst[i - 1][1]) + lst[i][2]

print(min(lst[n - 1][0], lst[n - 1][1], lst[n - 1][2]))