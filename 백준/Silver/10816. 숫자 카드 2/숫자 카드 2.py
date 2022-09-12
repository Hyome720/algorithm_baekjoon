import sys

n = int(input())
dic_a = dict()
lst_a = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0

m = int(input())
lst_b = list(map(int, sys.stdin.readline().rstrip().split()))

for i in lst_a:
    if i not in dic_a:
        dic_a[i] = 1
    else:
        dic_a[i] += 1

for i in lst_b:
    if i in dic_a:
        print(dic_a.get(i), end=" ")
    else:
        print(0, end=" ")