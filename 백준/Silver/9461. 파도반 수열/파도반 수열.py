import sys

t = int(sys.stdin.readline().rstrip())

lst = [0, 1, 1, 1, 2, 2]
for i in range(6, 101):
    lst.append(lst[i - 1] + lst[i - 5])

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(lst[n])
