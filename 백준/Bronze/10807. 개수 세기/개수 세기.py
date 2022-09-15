import sys

n = int(input())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
v = int(input())
print(lst.count(v))