import sys


n = int(input())
lst_a = list(map(int, sys.stdin.readline().split()))
dic_a = dict()
for idx, value in enumerate(lst_a):
    dic_a[value] = value

m = int(input())
lst_b = list(map(int, sys.stdin.readline().split()))

for i in lst_b:
    if dic_a.get(i):
        print(1)
    else:
        print(0)