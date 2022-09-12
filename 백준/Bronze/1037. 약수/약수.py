import sys

n = int(input())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst.sort()

print(lst[0] * lst[-1])
