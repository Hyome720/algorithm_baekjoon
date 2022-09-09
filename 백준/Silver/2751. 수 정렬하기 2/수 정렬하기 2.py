import sys

lst = []

n = int(input())
lst = []

for _ in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()

for i in lst:
    print(i)