import sys

n, k = map(int, input().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
dic = dict()
for i in range(n):
    dic[i] = lst[i]

dic_sort = sorted(dic.items(), key=lambda x:x[1])

print(dic_sort[-k][1])
